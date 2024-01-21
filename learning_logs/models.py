from django.db import models
from django.contrib.auth.models import User

# Create your models here.

"""
What is a model? 
A model is a class
It tells django how to work with data we have stored in our database
As with other classes, it will have its own fields/methods
"""

# example model: 
"""A topic the user is learning about."""
class Topic(models.Model): # model class "Topic"; inheritance happens here, Topic inherits from the class "Model", which is built in and we import it above
# allows this class to use all the methods in "Model", as if they were "Topic"s own methods

    text = models.CharField(max_length=200) # note that we are specifying the text max size, must be 200 chars or less
    date_added = models.DateTimeField(auto_now_add=True)
    # these two lines add a text field and a date time field to our application
    # the basic building blocks of this is already defined in Models
    # Note these are not UI elements but rather columns in a SQL database (text is one, date_added is another)
    # we are simply defining what can go inside these two columns here
    
    # other addable columns exist, they can be seen here: https://docs.djangoproject.com/en/4.1/ref/models/fields (replace 4.1 with latest django version)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    # this only displays the currently logged in User's topics, rather than everything on the database
    
"""Return a string representation of the model."""
def __str__(self):
    return self.text
# the python equivalent of a toString() method in other languages
# whenever we need to convert a Topic object to a string (i.e. to make it human readable), this __str__ method will be called by default

"""Something specific learned about a topic."""
class Entry(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    # ForeignKey is a database concept
    # Every table created in a database has a key
    # To link one table to another, we use these keys
    # meaning if we wanted to link an "Entry" object to a "Topic" object, we would use the Topic's key here (this would be the Entry's foreign key) 
    
    # on_delete=models.CASCADE means that if a Topic gets deleted, all associated Entrys with that topic will also be deleted
    
    text = models.TextField() # no size limit this time
    date_added = models.DateTimeField(auto_now_add=True)
    # adding a text column and date_added column for each Entry, just as we did with Topics
    
    class Meta:
        verbose_name_plural = 'entries'
        # tells django to rever to multiple Entry objects as "entries", not "Entrys", which is the default if we had not added this line
        # this is more for user readability than anything

    """Return a simple string representing the entry."""
    def __str__(self):
        return f"{self.text[:50]}..."
    # If we needed to convert an Entry object to a String, this is how we would do it
    # we additionally specify that we want only the first 50 characters of the text of the Entry object when converting to a string