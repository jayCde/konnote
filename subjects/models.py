# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Subject(models.Model):
    name = models.CharField(max_length=100, default='')
    description = models.CharField(max_length=250, default='')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, default='', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name
