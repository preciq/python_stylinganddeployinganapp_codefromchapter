from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Topic, Entry
from .forms import TopicForm, EntryForm
from django.http import Http404

# Create your views here.
def index(request):
    """The home page for Learning Log."""
    return render(request, 'learning_logs/index.html')
    # creating an index view here 
    # when a user tries to access the index path (defined in urls.py in learning logs), they will be shown an HTML page
    # defined in index.html, which needs to be made
        # note that the path should be /<app_folder>/templates/learning_logs/index.html
        # so "learning_logs/templates/learning_logs/index.html" in this case

@login_required
# this annotation forces users to be logged in before they see topics rendered
def topics(request):
    """Topics page (view)"""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    # this line ensures only currently logged in users topics will be displayed 
    
    context = {'topics': topics}
    # adding information needed to properly render the Topics page
    
    return render(request, 'learning_logs/topics.html', context)

@login_required
def topic(request, topic_id):
    """Show a single topic and all its entries."""
    topic = Topic.objects.get(id=topic_id)
    # Make sure the topic belongs to the current user.
    
    if topic.owner != request.user:
        raise Http404
    # a user trying to accesss data that is not owned by them will receive a 404
    
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)
    # adding information needed to properly render an individual Topic page

@login_required
def new_topic(request):
    """Add a new topic."""
    if request.method != 'POST': # we've been making API calls this whole time! This project primarily uses GET (when we get a page or some data) and POST (when we save some data)
        # No data submitted; create a blank form.
        form = TopicForm()
    else:
        # POST data submitted; process data.
        form = TopicForm(data=request.POST)
        if form.is_valid():
            # if all form information was input successfully
            
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            # this ensures that the form is saved under the current user; the previous ownership logic implemented ensures that other users cannot access this
            
            form.save()
            return redirect('learning_logs:topics')
            # redirects back to the topics page (see above) if form was successfully submitted
        # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)


@login_required
def new_entry(request, topic_id):
    """Add a new entry for a particular topic."""
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = EntryForm()
    else:
        # POST data submitted; process data.
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id=topic_id)
    # Display a blank or invalid form.
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)


@login_required
def edit_entry(request, entry_id):
    """Edit an existing entry."""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    
    if topic.owner != request.user:
        raise Http404
    # same thing as above one, stops user from changing entries that are not theirs
    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry.
        form = EntryForm(instance=entry)
    else:
        # POST data submitted; process data.
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id=topic.id)
        
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)