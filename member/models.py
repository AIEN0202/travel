# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Country(models.Model):
    idcountry = models.IntegerField(db_column='idCountry', primary_key=True)  # Field name made lowercase.
    countryname = models.CharField(db_column='Countryname', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'country'


class Member(models.Model):
    idmember = models.IntegerField(db_column='idMember', primary_key=True)  # Field name made lowercase.
    membername = models.CharField(db_column='Membername', max_length=45)  # Field name made lowercase.
    memberemail = models.CharField(db_column='MemberEmail', max_length=45)  # Field name made lowercase.
    memberpassword = models.CharField(db_column='MemberPassword', max_length=45)  # Field name made lowercase.
    memberbday = models.DateField(db_column='MemberBday')  # Field name made lowercase.
    membergender = models.CharField(db_column='MemberGender', max_length=2)  # Field name made lowercase.
    memberidcountry = models.ForeignKey(Country, models.DO_NOTHING, db_column='MemberidCountry')  # Field name made lowercase.
    memberhobby = models.CharField(db_column='MemberHobby', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'member'


class Region(models.Model):
    idregion = models.IntegerField(db_column='idRegion', primary_key=True)  # Field name made lowercase.
    regionname = models.CharField(db_column='Regionname', max_length=45)  # Field name made lowercase.
    idcountry = models.ForeignKey(Country, models.DO_NOTHING, db_column='idCountry')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'region'
