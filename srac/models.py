from django.contrib.auth.models import User
from django.db import models


class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    event = models.TextField()
    event_date = models.DateTimeField()
    emp_id = models.CharField(max_length=45)


class Check_Session_Log(models.Model):
    check_session_id = models.AutoField(primary_key=True)
    check_date = models.DateTimeField()
    check_remarks = models.TextField()
    checker = models.ForeignKey(User)
    is_session_submitted = models.IntegerField(default=0)


class Location(models.Model):
    building = models.CharField(max_length=45)
    floor = models.CharField(max_length=45)
    area = models.CharField(max_length=45)
    location_hash = models.CharField(primary_key=True, max_length=45)

    def __str__(self):
        return "{} {} {}".format(self.building, self.floor, self.area)


class Classification(models.Model):
    classification_name = models.CharField(primary_key=True, max_length=45)
    classification_description = models.TextField()

    def __str__(self):
        return self.classification_name


class Checklist(models.Model):
    checklist_id = models.AutoField(primary_key=True)
    location_hash = models.ForeignKey(Location)
    classification_name = models.ForeignKey(Classification)
    date_registered = models.DateTimeField()
    checklist_name = models.CharField(max_length=45)
    checklist_desc = models.TextField()
    registered_by = models.ForeignKey(User, related_name="registered_by")
    edited_by = models.ForeignKey(User, related_name="edited_by")
    last_edit = models.DateTimeField()
    priority_number = models.IntegerField()

    def __str__(self):
        return self.checklist_name


class Check_Item_Log(models.Model):
    CONFIRMATION_VAL = (
        ('Y', 'Yes'),
        ('N', 'No'),
        ('NA', 'Not Applicable')
    )
    check_item_log_id = models.AutoField(primary_key=True)
    check_session_id = models.ForeignKey(Check_Session_Log)
    checklist_id = models.ForeignKey(Checklist)
    confirmation = models.CharField(max_length=45, choices=CONFIRMATION_VAL)
    remarks = models.TextField()
