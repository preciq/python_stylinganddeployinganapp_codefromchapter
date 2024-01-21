from django import forms
from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}
# creating a new type of topic, called a "Form"
# something that user fills out. This particular form will allow the user to add more topics
# this will also need a URL so the user can access it successfully; this will be made in urls.py

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
# same as above but creates an EntryForm, something the user can use to add a new entry