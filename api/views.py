import requests
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import IntegrityError
from django.shortcuts import render
from rest_framework import generics
from .models import UserMasterModel, childModel
from .serializers import UserMaster_Serializer, Child_Serializer
import csv
from rest_framework.settings import api_settings
from rest_framework_csv import renderers as r
from rest_framework.decorators import api_view

from django.views.generic import View
from django.http import HttpResponse

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.settings import api_settings
from rest_framework_csv.parsers import CSVParser
from rest_framework_csv.renderers import CSVRenderer


class SomeModelCSVExportView(View):

    serializer_class = UserMaster_Serializer

    def get_serializer(self, queryset, many=True):
        return self.serializer_class(
            queryset,
            many=many,
        )

    def get(self, request, *args, **kwargs):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="export.csv"'

        serializer = self.get_serializer(UserMasterModel.objects.all(),
                                         many=True)
        header = UserMaster_Serializer.Meta.fields

        writer = csv.DictWriter(response, fieldnames=header)
        writer.writeheader()
        for row in serializer.data:
            writer.writerow(row)
        return response


class fetchAPi(APIView):
    def get(self, request, format=None):
        url = "https://gorest.co.in/public-api/users?_format=json&access-token=YUvH3F0gk3TABlo4-QYhvImhbtsKmTse_ZFt"
        headers = {
            'Cookie':
            '_csrf=24486f8342630836e6af50b31a9a1b94fdfa3d57bd2bfd0af73460131dda79d7a%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22rz8YZbh94vPkncZyJcIZkryCfuts3c4d%22%3B%7D'
        }
        response = requests.request("GET", url, headers=headers)
        json = response.json()
        resultData = json["result"]
        for line in resultData:
            user_id = line['id']
            first_name = line['first_name']
            last_name = line['last_name']
            gender = line['gender']
            dob = line['dob']
            email = line['email']
            phone = line['phone']
            website = line['website']
            address = line['address']
            status = line['status']

            Links_Data = line['_links']
            self_data = Links_Data['self']
            edit_data = Links_Data['edit']
            avatar_data = Links_Data['avatar']

            self_link = self_data['href']
            edit_link = edit_data['href']
            avatar_link = avatar_data['href']

            UserMasterModel.objects.create(user_id=user_id,
                                           first_name=first_name,
                                           last_name=last_name,
                                           gender=gender,
                                           dob=dob,
                                           email=email,
                                           phone=phone,
                                           website=website,
                                           address=address,
                                           status=status)

            childModel.objects.create(self_link=self_link,
                                      edit_link=edit_link,
                                      avatar_link=avatar_link)
        return Response({"status": "data saved"})


class ListUserMasterView(generics.ListAPIView):
    queryset = UserMasterModel.objects.all()
    serializer_class = UserMaster_Serializer


class UpdateUserMasterView(generics.RetrieveUpdateAPIView):
    queryset = UserMasterModel.objects.all()
    serializer_class = UserMaster_Serializer


class ListChildView(generics.ListAPIView):
    queryset = childModel.objects.all()
    serializer_class = Child_Serializer


class UpdateChildView(generics.RetrieveUpdateAPIView):
    queryset = childModel.objects.all()
    serializer_class = Child_Serializer


# ++++++++++++++++++++++


def export(request):
    pass


#     response = HttpResponse(content_type='text/csv')
#     writer = csv.writer(response)
#     writer.writerow([
#         'User Id', 'First Name', 'Last Name', 'Gender', 'DOB', 'Email',
#         'Phone', 'Website', 'Address', 'Status'
#     ])

#     for member in UserMasterModel.objects.all().values_list(
#             'user_id', 'first_name', 'last_name', 'gender', 'dob', 'email',
#             'phone', 'website', 'address', 'status'):
#         writer.writerow(member)

#     response['Content-Disposition'] = 'attachment; filename="members.csv"'

#     return response
