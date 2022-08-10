from django.urls import path
from . views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page = 'home'), name='logout'),
    path('register/', SignUpView.as_view(), name = 'register'),
    path('', UserHome.as_view(), name = 'home'),
    path('uevents/', EventList.as_view(), name='uevents'),
    path('register_eve/<int:pk>/',register_event_view,name='register_events')

]