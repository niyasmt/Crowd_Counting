

from django.shortcuts import redirect, render #first line
from django.contrib.auth.views import LoginView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from . models import Events, RegisterdEvents, CountImage
from django.contrib.auth.models import User
from .forms import EventsForms, CountForm
from .inference.model_inference import Count
from django.conf import settings

class CustomLoginView(LoginView,LoginRequiredMixin):
    template_name = 'admn/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('events_home')

class EventList(LoginRequiredMixin, ListView):
    model = Events
    context_object_name = 'events'

    # def get_context_data(self, **kwargs):
    #     # context = super().get_context_data(**kwargs)
    #     # context['events'] = context['events'].filter(user = self.request.user)
    #     # context['count'] = context['events'].filter(complete = False).count()
    #     search_input = self.request.GET.get('search-area') or ''
    #     if search_input:
    #         context['events'] = context['events'].filter(title__icontains = search_input)

    #     context['search_input'] = search_input
    #     return context

# Create your views here.

def eventsList(request):

    events = Events.objects.all()
    context = {
        'events': events,
    }
    return render(request,'admn/events.html',context)

def userList(request):

    users = User.objects.all()
    context = {
        'users': users,
    }
    return render(request,'admn/user.html',context)

def addEvents(request):
    form = EventsForms(request.POST or None)


    context = {
        'forms':form,
    }
    if request.method == "POST":
        form = EventsForms(request.POST, request.FILES)
        if form.is_valid():
            form.save() 
            return redirect('events')

    return render(request,'admn/addevents.html',context)


def editEvent(request,id):
    event = Events.objects.get(id=id)

    form = EventsForms(instance=event)


    if request.method== 'POST':
        form = EventsForms(request.POST,instance=event)
        if form.is_valid():
            form.save()
            return redirect('events')
    context = {
        'forms': form,
        }
    
    return render(request, 'admn/edit_event.html',context)


def deleteEvent(request,id):

    events= Events.objects.get(id=id)
    events.delete()
        
    return redirect('events')

def countform(request):
    form  = CountForm(request.POST or None, request.FILES)
    result = None
    if form.is_valid():
        image_field = form.cleaned_data['image']
        form = form.save(commit=False)
        
        result = Count(settings.MEDIA_ROOT, image_field.name)
        form.count = result
        form.save()
        return redirect('countimages')
    context = {
        'forms': form,
    }

    return render(request, 'admn/countimage.html', context)

def countimages(request):
    counts = CountImage.objects.all()
    context = {
        'counts': counts,
    }
    return render(request,'admn/countimages.html',context)