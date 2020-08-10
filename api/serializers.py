from rest_framework import serializers
from .models import UserMasterModel, childModel

from rest_framework.exceptions import ValidationError
from drf_writable_nested.serializers import WritableNestedModelSerializer
from drf_writable_nested.mixins import UniqueFieldsMixin


class UserMaster_Serializer(serializers.ModelSerializer):
    class Meta:
        model = UserMasterModel
        fields = ['pk','user_id','first_name','last_name', 'gender','dob','email', 'phone', 'website', 'address','status']


class Child_Serializer(serializers.ModelSerializer):
    class Meta:
        model = childModel
        fields = ['pk','self_link','edit_link','avatar_link']