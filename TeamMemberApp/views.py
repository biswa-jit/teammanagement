# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views import View

class TeamMemberView(View):
	'''
	This class handles all crud operations related to a team member
	'''

	def __init__(self):
		self.response = {
			"success":True,
			"data":[],
			"msg":""
		}

	def get(self,request):
		print 'here'
