import models as TeamModel

def add_member(member_data):
    """
    Store member details in database.
    Returns the member data with id.
    """
    member = TeamModel.TeamMember()
    member.first_name = member_data["first_name"]
    member.last_name = member_data["last_name"]
    member.phone_no = member_data["phone_no"]
    member.email_id = member_data["email_id"]
    member.role = member_data["role"]
    member.full_clean()
    member.save()
    member_data["id"] = member.id
    return member_data

def fetch_members():
    """
    Returns array of members.
    """
    member_qs = TeamModel.TeamMember.objects.all()
    members = []
    for member in member_qs:
        members.append(serialize(member))
    return members

def update_member(member_data):
    """
    Updates details of a member.
    Args:
        member_data: dictionary containing member data
    """
    if "id" in member_data:
        member = TeamModel.TeamMember.objects.get(id=member_data["id"])
    else:
        raise Exception("Please supply member id.")
    if "first_name" in member_data:
        member.first_name = member_data["first_name"]
    if "last_name" in member_data:
        member.last_name = member_data["last_name"]
    if "email_id" in member_data:
        member.email_id = member_data["email_id"]
    if "phone_no" in member_data:
        member.phone_no = member_data["phone_no"]
    if "role" in member_data:
        member.role = member_data["role"]
    member.full_clean()
    member.save()
    return serialize(member)

def delete_member(member_id):
    """
    Deletes a member.
    Args:
        member_id: id of the member.
    """
    member = TeamModel.TeamMember.objects.get(id=member_id)
    member.delete()

def serialize(obj):
    """
    Converts object to dictionary.
    Args:
        obj: object
    Returns:
        data_dict: dictionary
    """
    data_dict = {}
    for key in obj.__dict__:
        if key != '_state':
            data_dict[key] = obj.__dict__[key]
    return data_dict
