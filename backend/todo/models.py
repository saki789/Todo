from tkinter import CASCADE
from django.db import models

# Create your models here.


class Lkptblgender(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True, null=False)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'lkptblgender'

class Tblemployeeprofile1(models.Model):
    id = models.IntegerField(db_column='ID', blank=True, null=False, primary_key=True)  # Field name made lowercase.
    gridno = models.IntegerField(db_column='GridNo', blank=True, null=True)  # Field name made lowercase.
    txtmiddlename = models.CharField(db_column='txtMiddleName', max_length=27, blank=True, null=True)  # Field name made lowercase.
    txtsurname = models.CharField(db_column='txtSurname', max_length=29, blank=True, null=True)  # Field name made lowercase.
    dtmdob = models.CharField(db_column='dtmDOB', max_length=15, blank=True, null=True)  # Field name made lowercase.
    lkpgender = models.ForeignKey(Lkptblgender,on_delete=models.CASCADE)  # Field name made lowercase.
    txtfnpfno = models.CharField(db_column='txtFNPFNo', max_length=36, blank=True, null=True)  # Field name made lowercase.
    txttinno = models.CharField(db_column='txtTinNo', max_length=18, blank=True, null=True)  # Field name made lowercase.
    intmobile = models.CharField(db_column='intMobile', max_length=23, blank=True, null=True)  # Field name made lowercase.
    txtmn = models.CharField(db_column='txtMN', max_length=51, blank=True, null=True)  # Field name made lowercase.
    txtfn = models.CharField(db_column='txtFN', max_length=45, blank=True, null=True)  # Field name made lowercase.
    txtstreetaddress = models.CharField(db_column='txtStreetAddress', max_length=57, blank=True, null=True)  # Field name made lowercase.
    lkparea = models.CharField(db_column='lkpArea', max_length=2, blank=True, null=True)  # Field name made lowercase.
    town_city = models.CharField(db_column='Town/City', max_length=2, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    lkpstatus = models.CharField(db_column='lkpStatus', max_length=1, blank=True, null=True)  # Field name made lowercase.
    dtmstartdate = models.CharField(db_column='dtmStartDate', max_length=15, blank=True, null=True)  # Field name made lowercase.
    lkpexittype = models.CharField(db_column='lkpExitType', max_length=11, blank=True, null=True)  # Field name made lowercase.
    dtmexitdate = models.CharField(db_column='dtmExitDate', max_length=15, blank=True, null=True)  # Field name made lowercase.
    lkppoliceclearence = models.CharField(db_column='lkpPoliceClearence', max_length=1, blank=True, null=True)  # Field name made lowercase.
    lkpcategory = models.CharField(db_column='lkpCategory', max_length=5, blank=True, null=True)  # Field name made lowercase.
    lkpmaritalstatus = models.CharField(db_column='lkpMaritalStatus', max_length=1, blank=True, null=True)  # Field name made lowercase.
    txtspousename = models.CharField(db_column='txtSpouseName', max_length=35, blank=True, null=True)  # Field name made lowercase.
    txtspousedob = models.CharField(db_column='txtSpouseDoB', max_length=10, blank=True, null=True)  # Field name made lowercase.
    intspousephone = models.CharField(db_column='intSpousePhone', max_length=35, blank=True, null=True)  # Field name made lowercase.
    lkpjobtitle = models.CharField(db_column='lkpJobTitle', max_length=2, blank=True, null=True)  # Field name made lowercase.
    attphoto = models.CharField(db_column='attPhoto', max_length=34, blank=True, null=True)  # Field name made lowercase.
    lkpfuneralassistance = models.CharField(db_column='lkpFuneralAssistance', max_length=7, blank=True, null=True)  # Field name made lowercase.
    lkpnuw = models.CharField(db_column='lkpNUW', max_length=3, blank=True, null=True)  # Field name made lowercase.
    txtnextofkin = models.CharField(db_column='txtNextOfKin', max_length=32, blank=True, null=True)  # Field name made lowercase.
    lkprelevantexperience = models.CharField(db_column='lkpRelevantExperience', max_length=1, blank=True, null=True)  # Field name made lowercase.
    intweight = models.CharField(db_column='intWeight', max_length=1, blank=True, null=True)  # Field name made lowercase.
    intheight = models.CharField(db_column='intHeight', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblemployeeprofile__1_'



