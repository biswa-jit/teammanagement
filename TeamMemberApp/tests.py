# -*- coding: utf-8 -*-
from django.test import TestCase, RequestFactory
import json
from views import TeamMemberView
from models import TeamMember

class SimpleTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.data = {
                "first_name":"Biswajit",
                "last_name":"Sahu",
                "phone_no":"8892398240",
                "email_id":"biswajit.iiitbh@gmail.com",
                "role":"r",
                }

    def test_add_member(self):
        request = self.factory.post('/member/',json.dumps(self.data),content_type="application/json")
        response = TeamMemberView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_fetch_members(self):
        request = self.factory.get('/member/')
        response = TeamMemberView.as_view()(request)
        self.assertEqual(response.status_code, 200)
