from django.db import models
from csvImporter import fields
from csvImporter.model import CsvModel


class UserProfile(models.Model):
    fb_user_id = models.CharField(primary_key=True, max_length=200, null=False)
    name = models.CharField(max_length=200, null=True)
    branch = models.CharField(max_length=200, null=True)
    rank = models.CharField(max_length=200, null=True)
    unit = models.CharField(max_length=200, null=True)

class MilitaryBase(models.Model):
    name = models.CharField(max_length=200, null=False)
    state = models.CharField(max_length=200, null=False)
    state_abbr = models.CharField(max_length=5, null=False)
    branch = models.CharField(max_length=200, null=False)
    latitude = models.FloatField(null=False)
    longitude = models.FloatField(null=False)

class PastLocation(models.Model):
    fb_user_id = models.CharField(max_length=200, null=False)
    base = models.ForeignKey(MilitaryBase)

class CurrentLocation(models.Model):
    fb_user_id = models.CharField(primary_key=True, max_length=200, null=False)
    base = models.ForeignKey(MilitaryBase)

class Base(models.Model):
    name = models.CharField(max_length=200, null=False)
    state = models.CharField(max_length=200, null=False)
    state_abbr = models.CharField(max_length=200, null=False)
    fac_type = models.CharField(max_length=200, null=False)
    closure = models.CharField(max_length=200, null=False)
    realign = models.CharField(max_length=200, null=False)
    brac = models.CharField(max_length=200, null=False)
    branch = models.CharField(max_length=200, null=False)
    stfips = models.CharField(max_length=200, null=False)
    version = models.CharField(max_length=200, null=False)
    wkt = models.CharField(max_length=2000, null=False)

class CSVBase(CsvModel):
    name = fields.CharField()
    state = fields.CharField()
    state_abbr = fields.CharField()
    fac_type = fields.CharField()
    closure = fields.CharField()
    realign = fields.CharField()
    brac = fields.CharField()
    branch = fields.CharField()
    stfips = fields.CharField()
    version = fields.CharField()
    wkt = fields.CharField()
    class Meta:
        delimiter = ","
        dbModel = Base