Team Management module.

Setup:
1. Create a virtual environment instawork.
   mkvirtulenv instwork

2. Install the dependencies.
   pip install -r requirement.txt

3. Setup the database.
   Modify DATABASES field in settings.py. Change username and password as per host environment.


Testing the end points:
1. Add a member
   curl -H "Content-Type:application/json" -X POST -d '{"first_name": "David","last_name": "Jones", "phone_no": "+15101234567", "email_id":"test@test.com","role": "r"}' http://127.0.0.1:8000/member/

2. Fetch all members
   curl -X GET http://127.0.0.1:8000/member/

3. Update a member(whose id is 3)
   curl -H "Content-Type:application/json" -X PUT -d '{"id":3, "phone_no": "1234567890"}' http://127.0.0.1:8000/member/

4. Delete a member(whose id is 3)
   curl -H "Content-Type:application/json" -X DELETE -d '{"id":3}' http://127.0.0.1:8000/member/
