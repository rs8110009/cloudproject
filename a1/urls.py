from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name='home'),
    path('register',views.register,name='register'),
    path('login/',views.userlogin,name='login'),
    path('logout/',views.userlogout,name='logout'),
    path('showpost/',views.showpost,name='showpost'),
    path('addpost/',views.addpost,name='addpost'),
    path('mypost/',views.mypost,name='mypost'),
    path('profile/',views.userprofile,name='profile'),
    path('deletepost/<int:id>',views.deletepost,name='delpost'),
    path('likepost/<int:id> <int:isliked>',views.likepost,name='likepost'),

]