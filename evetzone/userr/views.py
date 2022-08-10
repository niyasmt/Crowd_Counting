from asyncio import events
from multiprocessing import Event
from pyexpat import model
from urllib import request
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from admn.models import Events, RegisterdEvents
from .forms import RegisterEventsForms
from django.urls import reverse_lazy
from django.shortcuts import redirect
from .forms import UserRegisterForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView

class CustomLoginView(LoginView,LoginRequiredMixin):
    template_name = 'admn/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')

class UserHome(ListView):
    model = Events
    template_name = 'userr/index.html'
    context_object_name = 'events'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['user_events'] = RegisterdEvents.objects.filter(user = self.request.user)
        except:
            pass
        return context

class SignUpView(SuccessMessageMixin, CreateView):
  template_name = 'userr/register.html'
  success_url = reverse_lazy('login')
  form_class = UserRegisterForm
  success_message = "Your profile was created successfully"


class EventList(ListView):
    model = Events
    template_name = 'userr\shop.html'
    context_object_name = 'events'

# class RegisterEvents(CreateView):
#     model = RegisterdEvents
#     form_class =RegisterEventsForms
#     template_name = 'userr\Reg_events.html'
#     success_url = reverse_lazy('home')
    

#     def post(self, request, *args, **kwargs):
#         print(self.kwargs)
#         form = self.get_form()

#         print(form,'*********************************8')
def register_event_view(request,pk):
    event = Events.objects.get(id=pk)
    form = RegisterEventsForms(request.POST or None)


    if request.method== 'POST':
        if form.is_valid():
            
            form = form.save( commit=False)
            form.user = request.user
            form.event_id = event
            form.save()
            
    context = {
        'forms': form,
        'events':event,
        }
    
    return render(request, 'userr/Reg_events.html',context)
# Create your views here.
