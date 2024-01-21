from django.contrib import admin

# Register your models here.
from .models import Topic, Entry
# we import the Topic model created previously (using .models, the '.' means that the 'models' module is in the same directory as this one)

admin.site.register(Topic)
# we make the Topic model available for admin (super) users

admin.site.register(Entry)
# addding Entry model as well for admin users
