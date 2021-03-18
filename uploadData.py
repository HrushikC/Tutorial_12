import json
from django.contrib.auth.models import User
from tutor.models import TutorProfile, Subject

# go to manage.py shell and run exec(open('uploadData.py').read())

# Sample Users:

with open('dummyUserData.json') as f:
    data = json.load(f)

keys = []
for i in data:
    keys += i.keys()
keys = set(keys)

for i in data:
    for j in keys:
        try:
            i[j]
        except:
            i[j] = ""

for p in data:
    user = User(**dict(zip(keys, [p[i] for i in keys])))
    user.save()


# TutorProfiles:

with open('dummyTutorProfileData.json') as f:
    data = json.load(f)

keys = []
for i in data:
    keys += i.keys()
keys = set(keys)

for i in data:
    for j in keys:
        try:
            i[j]
        except:
            i[j] = "ok"

for p in data:
    tp = TutorProfile(**dict(zip(keys, [p[i] for i in keys])))
    tp.save()


# Subjects:

with open('subjects.json') as f:
    data = json.load(f)

keys = []
for i in data:
    keys += i.keys()
keys = set(keys)

for i in data:
    for j in keys:
        try:
            i[j]
        except:
            i[j] = ""

for p in data:
    subject = Subject(**dict(zip(keys, [p[i] for i in keys])))
    subject.save()
