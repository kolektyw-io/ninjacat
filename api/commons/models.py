from django.db import models

# Create your models here.

class ServicingGroup(models.Model):
    """
        Preserves data
    """
    pass


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

