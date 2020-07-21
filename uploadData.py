import json
from tutor.models import TutorProfile

with open('dummyProfileData.json') as f:
    data = json.load(f)

for p in data:
    # queryset = TutorProfile.objects.filter(user_id=p['user_id'])
    # if not queryset:
        tp = TutorProfile(bio=p['bio'], zipcode=p['zipcode'], method=p['method'], fee=p['fee'], user_id=p['user_id'])
        tp.save()
