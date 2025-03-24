# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    enter = models.DateTimeField(blank=True, null=True, default=timezone.now)
    status = models.IntegerField(null=True, blank=True)
    role = models.IntegerField(null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Event(models.Model):

    #__Event_FIELDS__
    title = models.TextField(max_length=255, null=True, blank=True)
    group = models.ForeignKey(EventGroup, on_delete=models.CASCADE)

    #__Event_FIELDS__END

    class Meta:
        verbose_name        = _("Event")
        verbose_name_plural = _("Event")


class Eventgroup(models.Model):

    #__Eventgroup_FIELDS__
    order = models.IntegerField(null=True, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True)

    #__Eventgroup_FIELDS__END

    class Meta:
        verbose_name        = _("Eventgroup")
        verbose_name_plural = _("Eventgroup")


class Markinggroup(models.Model):

    #__Markinggroup_FIELDS__
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    event_member = models.ForeignKey(EventMember, on_delete=models.CASCADE)

    #__Markinggroup_FIELDS__END

    class Meta:
        verbose_name        = _("Markinggroup")
        verbose_name_plural = _("Markinggroup")


class Markingcommand(models.Model):

    #__Markingcommand_FIELDS__
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    event_member = models.ForeignKey(EventMember, on_delete=models.CASCADE)

    #__Markingcommand_FIELDS__END

    class Meta:
        verbose_name        = _("Markingcommand")
        verbose_name_plural = _("Markingcommand")


class Aspectvalue(models.Model):

    #__Aspectvalue_FIELDS__
    value = models.IntegerField(null=True, blank=True)
    command = models.ForeignKey(MarkingCommand, on_delete=models.CASCADE)
    group = models.ForeignKey(MarkingGroup, on_delete=models.CASCADE)
    competitor = models.ForeignKey(EventMember, on_delete=models.CASCADE)
    expert = models.ForeignKey(EventMember, on_delete=models.CASCADE)

    #__Aspectvalue_FIELDS__END

    class Meta:
        verbose_name        = _("Aspectvalue")
        verbose_name_plural = _("Aspectvalue")


class Eventmember(models.Model):

    #__Eventmember_FIELDS__
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    enter = models.DateTimeField(blank=True, null=True, default=timezone.now)
    status = models.IntegerField(null=True, blank=True)
    role = models.IntegerField(null=True, blank=True)

    #__Eventmember_FIELDS__END

    class Meta:
        verbose_name        = _("Eventmember")
        verbose_name_plural = _("Eventmember")



#__MODELS__END
