from django.db import models
from uuid import uuid4
from pymongo.server_api import ServerApi
import os


class User(models.Model):
    id = models.UUIDField(primary_key=True,default = uuid4,editable = False)
    name  = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)
    gender = models.CharField(max_length = 10)
    

