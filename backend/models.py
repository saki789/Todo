# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Lkptbldisciplinarytypes(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    disciplinary_name = models.CharField(db_column='disciplinary name', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'lkptbldisciplinarytypes'


class Lkptblgender(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'lkptblgender'


class Lkptbljobtitle(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    job_title = models.CharField(db_column='Job Title', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'lkptbljobtitle'


class Lkptblleavetypes(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    txtleavetypes = models.CharField(db_column='txtLeaveTypes', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'lkptblleavetypes'


class Lkptblmaritalstatus(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'lkptblmaritalstatus'


class PoliceClearance(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'police clearance'


class Qualification(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    qualification = models.CharField(db_column='Qualification', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'qualification'


class Relevantexperiencedetails(models.Model):
    id = models.IntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    fkcid = models.IntegerField(db_column='fkcID', blank=True, null=True)  # Field name made lowercase.
    fkcgridno = models.CharField(db_column='fkcGridNo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dtmstartdate = models.DateTimeField(db_column='dtmStartDate', blank=True, null=True)  # Field name made lowercase.
    dtmenddate = models.DateTimeField(db_column='dtmEndDate', blank=True, null=True)  # Field name made lowercase.
    lkpemployer = models.IntegerField(db_column='lkpEmployer', blank=True, null=True)  # Field name made lowercase.
    txtreason = models.CharField(db_column='txtReason', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'relevantexperiencedetails'


class Relevantindustryexperience(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    industry = models.CharField(db_column='Industry', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'relevantindustryexperience'


class SecurityLicence(models.Model):
    pkid = models.AutoField(db_column='pkID', primary_key=True)  # Field name made lowercase.
    fkcid = models.IntegerField(db_column='fkcID', blank=True, null=True)  # Field name made lowercase.
    fkcgridno = models.CharField(db_column='fkcGridNo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    txtlicno = models.CharField(db_column='txtLicNo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    txttype = models.CharField(db_column='txtType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    txtsubclass = models.CharField(db_column='txtSubClass', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dtmexpiry = models.CharField(db_column='dtmExpiry', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'security licence'


class Startend(models.Model):
    pkid = models.AutoField(db_column='pkID', primary_key=True)  # Field name made lowercase.
    fkcid = models.IntegerField(db_column='fkcID', blank=True, null=True)  # Field name made lowercase.
    fkcgridno = models.CharField(db_column='fkcGridNo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dtmappointment = models.DateTimeField(db_column='dtmAppointment', blank=True, null=True)  # Field name made lowercase.
    lkpposition = models.IntegerField(db_column='lkpPosition', blank=True, null=True)  # Field name made lowercase.
    memcomments = models.TextField(db_column='memComments', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'startend'


class Status(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'status'


class Tblannualleave(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    fkcid = models.CharField(db_column='fkcID', max_length=10, blank=True, null=True)  # Field name made lowercase.
    fkcgridno = models.CharField(db_column='fkcGridNo', max_length=6, blank=True, null=True)  # Field name made lowercase.
    dtmleavestart = models.CharField(db_column='dtmLeaveStart', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dtmleaveresume = models.CharField(db_column='dtmleaveResume', max_length=10, blank=True, null=True)  # Field name made lowercase.
    intdays = models.CharField(db_column='intDays', max_length=2, blank=True, null=True)  # Field name made lowercase.
    lkpleavetype = models.CharField(db_column='lkpLeaveType', max_length=1, blank=True, null=True)  # Field name made lowercase.
    memcomment = models.CharField(db_column='memComment', max_length=105, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblannualleave'


class Tblarea(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    area = models.CharField(db_column='Area', max_length=255, blank=True, null=True)  # Field name made lowercase.
    town_city = models.ForeignKey('TownCity', models.DO_NOTHING, db_column='Town_City', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblarea'


class Tblbankdetails(models.Model):
    pkid = models.AutoField(db_column='pkID', primary_key=True)  # Field name made lowercase.
    fkcgridno = models.CharField(db_column='fkcGridNo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    fkcid = models.CharField(db_column='fkcID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dtmdateactive = models.DateTimeField(db_column='dtmDateActive', blank=True, null=True)  # Field name made lowercase.
    txtaccountnumber = models.CharField(db_column='txtAccountNumber', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lkpbank = models.ForeignKey('Tblbanks', models.DO_NOTHING, db_column='lkpBank', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblbankdetails'


class Tblbanks(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    bankname = models.CharField(db_column='BankName', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblbanks'


class Tblchildren(models.Model):
    pkid = models.AutoField(db_column='pkID', primary_key=True)  # Field name made lowercase.
    fkcid = models.CharField(db_column='fkcID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    fkcgridno = models.CharField(db_column='fkcGridNo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    txtchildname = models.CharField(db_column='txtChildName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dtmdob = models.DateTimeField(db_column='dtmDoB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblchildren'


class Tbldisciplinary(models.Model):
    intid = models.AutoField(db_column='intID', primary_key=True)  # Field name made lowercase.
    dtmdisciplinarydate = models.DateTimeField(db_column='dtmDisciplinaryDate', blank=True, null=True)  # Field name made lowercase.
    fkcgridno = models.CharField(db_column='fkcGridNo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    fkcid = models.IntegerField(db_column='fkcID', blank=True, null=True)  # Field name made lowercase.
    lkpdisciplinarytype = models.ForeignKey(Lkptbldisciplinarytypes, models.DO_NOTHING, db_column='lkpDisciplinaryType', blank=True, null=True)  # Field name made lowercase.
    memcomments = models.TextField(db_column='memComments', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbldisciplinary'


class Tbldriverslicence(models.Model):
    pkid = models.AutoField(db_column='pkID', primary_key=True)  # Field name made lowercase.
    fkcid = models.IntegerField(db_column='fkcID', blank=True, null=True)  # Field name made lowercase.
    fkcgridno = models.CharField(db_column='fkcGridNo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    txtlicno = models.CharField(db_column='txtLicNo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    txtlicclass = models.CharField(db_column='txtLicClass', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dtmlicexpiry = models.DateTimeField(db_column='dtmLicExpiry', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbldriverslicence'


class Tbleducation(models.Model):
    pkid = models.AutoField(db_column='pkID', primary_key=True)  # Field name made lowercase.
    fkcid = models.ForeignKey('Tbleducationlevel', models.DO_NOTHING, db_column='fkcID', blank=True, null=True)  # Field name made lowercase.
    fkcgridno = models.CharField(db_column='fkcGridNo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lkplevel = models.IntegerField(db_column='lkpLevel', blank=True, null=True)  # Field name made lowercase.
    txtschool = models.CharField(db_column='txtSchool', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dtmstart = models.DateTimeField(db_column='dtmStart', blank=True, null=True)  # Field name made lowercase.
    dtmend = models.DateTimeField(db_column='dtmEnd', blank=True, null=True)  # Field name made lowercase.
    qualification = models.ForeignKey(Qualification, models.DO_NOTHING, db_column='Qualification', blank=True, null=True)  # Field name made lowercase.
    comments = models.TextField(db_column='Comments', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbleducation'


class Tbleducationlevel(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    level = models.CharField(db_column='Level', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbleducationlevel'


class Tblemployeeprofile1(models.Model):
    id = models.IntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    gridno = models.IntegerField(db_column='GridNo', blank=True, null=True)  # Field name made lowercase.
    txtmiddlename = models.CharField(db_column='txtMiddleName', max_length=27, blank=True, null=True)  # Field name made lowercase.
    txtsurname = models.CharField(db_column='txtSurname', max_length=29, blank=True, null=True)  # Field name made lowercase.
    dtmdob = models.CharField(db_column='dtmDOB', max_length=15, blank=True, null=True)  # Field name made lowercase.
    lkpgender = models.CharField(db_column='lkpGender', max_length=1, blank=True, null=True)  # Field name made lowercase.
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


class Tblemploymenthistory(models.Model):
    pkid = models.IntegerField(db_column='pkID', primary_key=True)  # Field name made lowercase.
    fkcid = models.IntegerField(db_column='fkcID', blank=True, null=True)  # Field name made lowercase.
    fkcgridno = models.CharField(db_column='fkcGridNo', max_length=6, blank=True, null=True)  # Field name made lowercase.
    txtemployer = models.CharField(db_column='txtEmployer', max_length=57, blank=True, null=True)  # Field name made lowercase.
    txtjobtitle = models.CharField(db_column='txtJobTitle', max_length=47, blank=True, null=True)  # Field name made lowercase.
    dtmstartdate = models.CharField(db_column='dtmStartDate', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dtmenddate = models.CharField(db_column='dtmEndDate', max_length=255, blank=True, null=True)  # Field name made lowercase.
    txtreason = models.CharField(db_column='txtReason', max_length=117, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblemploymenthistory'


class TownCity(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    town_city = models.CharField(db_column='Town/City', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    zone = models.ForeignKey('Zones', models.DO_NOTHING, db_column='Zone', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'town_city'


class Training(models.Model):
    pkid = models.AutoField(db_column='pkID', primary_key=True)  # Field name made lowercase.
    fkcid = models.IntegerField(db_column='fkcID', blank=True, null=True)  # Field name made lowercase.
    fkcgridno = models.CharField(db_column='fkcGridNo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dtmstartdate = models.DateTimeField(db_column='dtmStartDate', blank=True, null=True)  # Field name made lowercase.
    dtmenddate = models.DateTimeField(db_column='dtmEndDate', blank=True, null=True)  # Field name made lowercase.
    dtmtrainingname = models.CharField(db_column='dtmTrainingName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    txttrainingvenue = models.CharField(db_column='txtTrainingVenue', max_length=255, blank=True, null=True)  # Field name made lowercase.
    memcomments = models.TextField(db_column='memComments', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'training'


class Users(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    field1 = models.CharField(db_column='Field1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    field2 = models.CharField(db_column='Field2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    field3 = models.CharField(db_column='Field3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    field4 = models.CharField(db_column='Field4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    field5 = models.CharField(db_column='Field5', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'users'


class Zones(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    zone = models.CharField(db_column='Zone', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'zones'
