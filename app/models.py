# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
import time

class ThinkAdv(models.Model):
    text = models.CharField(max_length=20, blank=True, null=True)
    web = models.CharField(max_length=127, blank=True, null=True)
    js = models.CharField(max_length=127, blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'think_adv'


class ThinkArticle(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    img = models.CharField(max_length=200, blank=True, null=True)
    author = models.CharField(max_length=20, blank=True, null=True)
    time = models.CharField(max_length=11, blank=True, null=True)
    times_read = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=20, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    istop = models.IntegerField(db_column='isTop', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'think_article'


class ThinkCollections(models.Model):
    phone = models.CharField(primary_key=True, max_length=11)
    tx_id = models.IntegerField()
    tx_type = models.CharField(max_length=2)
    tx_offset = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'think_collections'
        unique_together = (('phone', 'tx_id'),)


class ThinkExam(models.Model):
    name = models.TextField()
    list = models.TextField(blank=True, null=True)
    time = models.CharField(max_length=10,default=time.time())
    timelong = models.IntegerField(default=9000)
    class Meta:
        managed = False
        db_table = 'think_exam'


class ThinkExamlist(models.Model):
    type = models.CharField(max_length=1)
    id = models.IntegerField(primary_key=True)
    offset = models.IntegerField()
    subject = models.IntegerField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    a = models.TextField(blank=True, null=True)
    b = models.TextField(blank=True, null=True)
    c = models.TextField(blank=True, null=True)
    d = models.TextField(blank=True, null=True)
    e = models.TextField()
    right = models.CharField(max_length=2)
    anaylze = models.TextField()
    other = models.TextField(blank=True, null=True)
    year = models.CharField(max_length=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'think_examlist'
        unique_together = (('id', 'offset'),)


class ThinkExamrecord(models.Model):
    id = models.IntegerField(primary_key=True)
    phone = models.CharField(max_length=11)
    examid = models.IntegerField(blank=True, null=True)
    record = models.TextField(blank=True, null=True)
    uptime = models.TextField(blank=True, null=True)
    titlenum = models.IntegerField()
    grade1 = models.DecimalField(max_digits=10,decimal_places=2)
    grade2 = models.DecimalField(max_digits=10,decimal_places=2)
    grade = models.DecimalField(max_digits=10,decimal_places=2)

    class Meta:
        managed = False
        db_table = 'think_examrecord'


class ThinkExercises(models.Model):
    sx_id = models.IntegerField(blank=True, null=True)
    sx_type = models.CharField(max_length=2, blank=True, null=True)
    sx_title = models.CharField(max_length=20, blank=True, null=True)
    sx_subject = models.TextField(blank=True, null=True)
    sx_answera = models.CharField(max_length=40, blank=True, null=True)
    sx_answerb = models.CharField(max_length=40, blank=True, null=True)
    sx_answerc = models.CharField(max_length=40, blank=True, null=True)
    sx_answerd = models.CharField(max_length=40, blank=True, null=True)
    sx_answere = models.CharField(max_length=40, blank=True, null=True)
    sx_answer = models.CharField(max_length=1, blank=True, null=True)
    sx_analyze = models.TextField(blank=True, null=True)
    sx_all = models.IntegerField(blank=True, null=True)
    sx_wrong = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'think_exercises'


class ThinkFeedback(models.Model):
    phone = models.CharField(max_length=11)
    contact = models.CharField(max_length=20, blank=True, null=True)
    content = models.CharField(max_length=500, blank=True, null=True)
    time = models.CharField(max_length=10, blank=True, null=True)
    device = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'think_feedback'


class ThinkLesson(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    img = models.CharField(max_length=255, blank=True, null=True)
    time = models.CharField(max_length=255, blank=True, null=True)
    detail = models.CharField(max_length=255, blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'think_lesson'


class ThinkLogin(models.Model):
    phone = models.CharField(max_length=11)
    mobiledevice_last = models.CharField(max_length=80, blank=True, null=True)
    time_last = models.IntegerField(blank=True, null=True)
    ip_last = models.CharField(max_length=20, blank=True, null=True)
    pcdevice_last = models.CharField(max_length=100, blank=True, null=True)
    isfirst = models.IntegerField(db_column='isFirst', blank=True, null=True)  # Field name made lowercase.
    loginretime = models.CharField(db_column='loginReTime', max_length=20, blank=True, null=True)  # Field name made lowercase.
    todaysignin = models.CharField(db_column='todaySignIn', max_length=1, blank=True, null=True)  # Field name made lowercase.
    version = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'think_login'
        unique_together = (('id', 'phone'),)


class ThinkOthers(models.Model):
    name = models.CharField(max_length=20)
    data = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'think_others'


class ThinkUsers(models.Model):
    phone = models.CharField(max_length=11)
    secret = models.CharField(max_length=50)
    deviceid = models.CharField(max_length=50, blank=True, null=True)
    nickname = models.CharField(max_length=30, blank=True, null=True)
    addr = models.CharField(max_length=200, blank=True, null=True)
    email = models.CharField(max_length=40, blank=True, null=True)
    headurl = models.CharField(max_length=100, blank=True, null=True)
    vip = models.IntegerField(blank=True, null=True)
    ip = models.CharField(max_length=20, blank=True, null=True)
    registrytime = models.CharField(db_column='registryTime', max_length=10, blank=True, null=True)  # Field name made lowercase.
    level = models.CharField(max_length=20, blank=True, null=True)
    topics_last = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'think_users'


class ThinkWrongtopic(models.Model):
    phone = models.CharField(primary_key=True, max_length=11)
    tx_id = models.IntegerField()
    tx_type = models.IntegerField(blank=True, null=True)
    tx_offset = models.IntegerField(blank=True, null=True)
    wrong_num = models.IntegerField(blank=True, null=True)
    all_sum = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'think_wrongtopic'
        unique_together = (('phone', 'tx_id'),)
