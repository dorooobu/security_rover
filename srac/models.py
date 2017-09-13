from django.contrib.auth.models import User
from django.db import models
from django.forms import ModelForm, RadioSelect


class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    event = models.TextField()
    event_date = models.DateTimeField()
    emp_id = models.CharField(max_length=45)


class Classification(models.Model):
    classification_name = models.CharField(primary_key=True, max_length=45)
    classification_description = models.TextField()

    def __str__(self):
        return self.classification_name


class Checklist(models.Model):
    checklist_id = models.AutoField(primary_key=True)
    classification = models.ForeignKey(Classification)
    date_registered = models.DateTimeField()
    checklist_name = models.CharField(max_length=45)
    checklist_desc = models.TextField()
    registered_by = models.ForeignKey(User, related_name="registered_by")
    edited_by = models.ForeignKey(User, related_name="edited_by")
    last_edit = models.DateTimeField()

    def __str__(self):
        return self.checklist_name


class Location(models.Model):
    building = models.CharField(max_length=45)
    floor = models.CharField(max_length=45)
    area = models.CharField(max_length=45)
    location_hash = models.CharField(primary_key=True, max_length=45)

    def __str__(self):
        return "{} {} {}".format(self.building, self.floor, self.area)


class Location_Checklist(models.Model):
    location = models.ForeignKey(Location)
    checklist = models.ForeignKey(Checklist)
    priority_number = models.IntegerField(default=1)

    def __str__(self):
        return "{} {}".format(self.location, self.checklist.checklist_name)


class Session(models.Model):
    session_id = models.AutoField(primary_key=True)
    check_date = models.DateTimeField()
    check_remarks = models.TextField()
    checker = models.ForeignKey(User)
    is_session_submitted = models.IntegerField(default=0)


class Session_Checklist(models.Model):
    CONFIRMATION_VAL = (
        ('Y', 'Yes'),
        ('N', 'No'),
        ('NA', 'Not Applicable')
    )
    session_checklist_id = models.AutoField(primary_key=True)
    session = models.ForeignKey(Session)
    location_checklist = models.ForeignKey(Location_Checklist)
    confirmation = models.CharField(max_length=45, choices=CONFIRMATION_VAL, default=CONFIRMATION_VAL[2][0])
    remarks = models.TextField()
