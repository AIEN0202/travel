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
    contentofreview = models.CharField(db_column='ContentofReview', max_length=45, blank=True, null=True)  # Field name made lowercase.
    idreview = models.IntegerField(db_column='idReview', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'review'
