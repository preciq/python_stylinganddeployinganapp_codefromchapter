"""Defines URL patterns for learning_logs."""
from django.urls import path # allows us to create/use URLS
from . import views # imports the views.py module (to link views with the URLs below)

app_name = 'learning_logs'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # the empty string represents the base url (http://127.0.0.1:8000/), which django ignores
    # so essentially, we are defining the view that will be displayed if a user arrives at the home page
    # we also name this home page "index", which lets us refer to this later elsewhere
    
    path('topics/', views.topics, name='topics'),
    # adding a topics url in the path <base_url>/topics/
    # view for this is defined in learning_logs/views.py module, just like index
    
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # adds a dynamic url created for every topic page <int:topic_id>
    
    path('new_topic/', views.new_topic, name='new_topic'),
    # Page for adding a new topic.
    
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # Page for adding a new entry
    
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
    # Page for editing an entry.
    
]