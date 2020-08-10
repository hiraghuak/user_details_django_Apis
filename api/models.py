from django.db import models


class UserMasterModel(models.Model):
    user_id = models.CharField(max_length=500,
                               blank=True,
                               default='',
                               unique=True)
    first_name = models.CharField(max_length=500, blank=True, default='')
    last_name = models.CharField(max_length=500, blank=True, default='')
    gender = models.CharField(max_length=500, blank=True, default='')
    dob = models.CharField(max_length=500, blank=True, default='')
    email = models.CharField(max_length=500, blank=True, default='')
    phone = models.CharField(max_length=500, blank=True, default='')
    website = models.CharField(max_length=500, blank=True, default='')
    address = models.CharField(max_length=500, blank=True, default='')
    status = models.CharField(max_length=500, blank=True, default='')

    def __str__(self):
        return self.user_id


class childModel(models.Model):
    self_link = models.CharField(max_length=1000, blank=True, default='',unique=True)
    edit_link = models.CharField(max_length=1000, blank=True, default='')
    avatar_link = models.CharField(max_length=1000, blank=True, default='')

    def __str__(self):
        return self.self_link