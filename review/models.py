# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from member import models as m1


class Review(models.Model):
    memberid = models.ForeignKey(m1.Member, models.DO_NOTHING, db_column='MemberID')  # Field name made lowercase.
    typeplace = models.CharField(db_column='TypePlace', max_length=45, blank=True, null=True)  # Field name made lowercase.
    placeid = models.CharField(db_column='PlaceID', max_length=45, blank=True, null=True)  # Field name made lowercase.
    rating = models.CharField(db_column='Rating', max_length=45, blank=True, null=True)  # Field name made lowercase.
    datereview = models.CharField(db_column='DateReview', max_length=45, blank=True, null=True)  # Field name made lowercase.
    contentofreview = models.CharField(db_column='ContentofReview', max_length=500, blank=True, null=True)  # Field name made lowercase.
    idreview = models.IntegerField(db_column='idReview', primary_key=True)  # Field name made lowercase.
    hastable = models.CharField(db_column='HasTable', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'review'


class Restaurant(models.Model):
    resid = models.IntegerField(db_column='Resid', primary_key=True)  # Field name made lowercase.
    country_id = models.CharField(max_length=200, blank=True, null=True)
    region_id = models.CharField(max_length=200, blank=True, null=True)
    type = models.CharField(max_length=200, blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    time = models.CharField(max_length=500, blank=True, null=True)
    tel = models.CharField(max_length=200, blank=True, null=True)
    remainingseats = models.IntegerField(db_column='RemainingSeats', blank=True, null=True)  # Field name made lowercase.
    addr = models.CharField(max_length=200, blank=True, null=True)
    imgsrc = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'restaurant'


class Hotel(models.Model):
    id_hotel = models.IntegerField(primary_key=True)
    country_id = models.CharField(max_length=20, blank=True, null=True)
    reigien_id = models.CharField(max_length=45, blank=True, null=True)
    title = models.CharField(max_length=45, blank=True, null=True)
    h_price = models.CharField(max_length=45, blank=True, null=True)
    type = models.CharField(max_length=45, blank=True, null=True)
    addr = models.CharField(max_length=45, blank=True, null=True)
    imgsrc = models.CharField(max_length=200, blank=True, null=True)
    offical_url = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hotel'


class Attraction(models.Model):
    idattraction = models.IntegerField(db_column='idAttraction', primary_key=True)  # Field name made lowercase.
    title = models.CharField(max_length=100, blank=True, null=True)
    time = models.CharField(max_length=500, blank=True, null=True)
    addr = models.CharField(max_length=1000, blank=True, null=True)
    imgsrc = models.CharField(max_length=1000, blank=True, null=True)
    officailurl = models.CharField(max_length=1000, blank=True, null=True)
    country_id = models.IntegerField(blank=True, null=True)
    region_id = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'attraction'
