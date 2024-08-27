
from django.urls import path
#from django.contrib.auth.views import LogoutView
from .views import UsersListView,ClosedUser,RegisterView

urlpatterns = [
   path('',UsersListView.as_view(),name="login"),
   path('logout/',ClosedUser.as_view(),name="logout"),
   path('register/',RegisterView.as_view(),name="register"),
]
