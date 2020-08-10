from django.contrib import admin
from .models import UserMasterModel,childModel

admin.site.register(UserMasterModel)
admin.site.register(childModel)
