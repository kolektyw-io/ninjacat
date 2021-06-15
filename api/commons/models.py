from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_agent = models.BooleanField(default=False)


class ServicingGroup(models.Model):
    """
        Preserves data
    """
    pass


class Group(models.Model):
    name = models.CharField(max_length=500, null=False, blank=False)
    mnemonic = models.CharField(max_length=50, null=False, blank=False, default="")
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.SET_NULL)


class UserGroup(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)


class Permission(models.Model):
    pass


class PermissionSet(models.Model):
    pass


class CustomField(models.Model):
    pass


class SystemProperty(models.Model):
    """
        Contains various system properties for use i.e. for in-place upgrade.
    """
    key = models.CharField(max_length=500, null=False, blank=False)
    value = models.CharField(max_length=5000, null=True, blank=True)
