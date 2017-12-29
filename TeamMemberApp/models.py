# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class TeamMember(models.Model):
	choices = (
		('a','admin'),
		('r','regular')
	)

	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	phone_no = models.CharField(max_length=13,unique=True)
	email_id = models.EmailField(max_length=30,unique=True)
	role = models.CharField(max_length=1,choices=choices)
