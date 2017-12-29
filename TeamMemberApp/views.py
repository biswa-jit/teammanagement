# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from django.views import View
from django.http import HttpResponse
from django.core.exceptions import ValidationError
import utils as utils

class TeamMemberView(View):
    """
    This class handles all crud operations related to a team member
    """

    def __init__(self):
        self.response = {
            "success":True,
            "data":None,
            "msg":""
        }

    def post(self,request):
        """
        Add a member to database.
        """
        member_data = json.loads(request.body)
        try:
            member = utils.add_member(member_data)
            self.response["data"] = member
        except ValidationError as e:
            self.response["status"] = False
            self.response["msg"] = e.message_dict
        except Exception as ex:
            self.response["status"] = False
            self.response["msg"] = str(ex)
        return HttpResponse(json.dumps(self.response))
        

    def get(self,request):
        """
        Fetch all members.
        """
        members = utils.fetch_members()
        self.response["data"] = members
        return HttpResponse(json.dumps(self.response))

    def put(self,request):
        """
        Update details of a member.
        """
        member_data = json.loads(request.body)
        try:
            member = utils.update_member(member_data)
            self.response["data"] = member
        except ValidationError as e:
            self.response["status"] = False
            self.response["msg"] = e.message_dict
        except Exception as ex:
            self.response["status"] = False
            self.response["msg"] = str(ex)
        return HttpResponse(json.dumps(self.response))
    
    def delete(self,request):
        """
        Delete a member.
        """
        member_id = json.loads(request.body)["id"]
        try:
            utils.delete_member(member_id)
        except Exception as ex:
            self.response["status"] = False
            self.response["msg"] = str(ex)
        return HttpResponse(json.dumps(self.response))
