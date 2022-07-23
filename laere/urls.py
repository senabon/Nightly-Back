from django.urls import path
from . import views 



urlpatterns = [

    path('', views.view_name, name="view_name"),
    #path("", views.homepage, name="homepage")
    path('event_list', views.event_list),

    path('login', views.login),  #fix this line possibly with a serializer 
    #path('signup', views.CreateUser.as_view()),
    path('signup', views.signup),

    path('events/', views.EventList.as_view()),
    path('events/<int:pk>', views.EventDetail.as_view()),
    path('Events_protected/', views.EventListProtected.as_view()),

   # path('register', views.register_request, name="register"),
   # path('login', views.login_request, name="login")



]