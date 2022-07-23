from multiprocessing import Event
from django.shortcuts import render, redirect
from django.http import JsonResponse,HttpResponse
from rest_framework import generics, permissions
from .forms import NewUserForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm


from .models import User, Event#, Ratings 
from .serializers import UserSerializer, EventSerializer #, RatingsSerializer


from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET', 'POST'])

# Create your views here.
def view_name(request):
    return HttpResponse('ok!')


def event_list(request):
    events = Event.objects.all().values()
    ev_list = list(events)
    return JsonResponse(ev_list, safe=False )

@api_view(['POST'])
def eventCreate(request):
        serializer = EventSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

@api_view(['DELETE'])
def eventDelete(request, pk):
    events = Event.objects.get(id=pk)
    events.delete()

class EventList(generics.ListCreateAPIView):
    serializer_class = EventSerializer
    queryset = Event.objects.all()
    permission_classes= [permissions.IsAuthenticatedOrReadOnly]

    def post(self, request, *args, **kwargs):
        print(request.user.username)     
        request.data['user_string'] = request.user.username
        return super().post(request, *args, **kwargs)

class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EventSerializer
    queryset = Event.objects.all()

class EventListProtected(generics.ListCreateAPIView):
    serializer_class = EventSerializer
    queryset = Event.objects.all()

    permission_classes = [permissions.IsAuthenticated]

class CreateUser(generics.CreateAPIView): 
    model = User
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer

class UserLogin(generics.RetrieveAPIView):     
    model = User 
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer

#put ratings serializer here (stretch goal)


def login(request):
    return JsonResponse({'loggedIn':True , 'username': 'mock'})

def signup(request):
    return JsonResponse({'loggedIn':True , 'username': 'mock'})


# def register_request(request):
#     if request.method == 'POST':
#         form = NewUserForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request,user)
#             messages.success(request,"Registration success! ")
#             return redirect("/")
#         messages.error(request, "Try again!")
#     form = NewUserForm()
#     return render (
#         request=request,
#         template_name='register.html', context={"register_form":form}
#     )

# def login_request(request):
# 	if request.method == 'POST':
# 		form = AuthenticationForm(request, data=request.POST)
# 		if form.is_valid():
# 			username = form.cleaned_data.get('username')
# 			password = form.cleaned_data.get('password')
# 			user = authenticate(username=username, password=password)
# 			if user is not None:
# 				login(request, user)
# 				messages.info(request, f"You are now logged in as {username}.")
# 				return redirect("/")
# 			else:
# 				messages.error(request,"Invalid username or password.")
# 		else:
# 			messages.error(request,"Invalid username or password.")
# 	form = AuthenticationForm()
# 	return render(request=request, template_name="login.html", context={"login_form":form})