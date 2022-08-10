from django.urls import path, include
from .views import CustomLoginView, EventList
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page = 'login'), name='logout'),
    # path('register/', RegisterPage.as_view(), name = 'register'),
    path('',EventList.as_view(), name='events_home'),
    path('events/',views.eventsList,name='events'),
    path('users/',views.userList,name='users'),
    path('addEvents/',views.addEvents,name='addevents'),
    path('edit/<str:id>/',views.editEvent,name='edit'),
    path('delete/<str:id>/',views.deleteEvent,name='delete'),
    path('countimage/',views.countform,name='countimage'),
    path('countimages/',views.countimages,name='countimages'),
    # path('delete/',views.,name='users/'),
 
]