from django.shortcuts import render
from django.http import HttpResponseRedirect 
from .forms import RegisterForm,LoginForm,BlogForm
from django.contrib.auth import authenticate,login,logout
from .models import Blog,Likemodel
from django.contrib.auth.models import User
import datetime as dt
# Create your views here.
def home(request):
    return render(request,"a1/home.html")
def register(request):
    if request.method=="POST":
        rform=RegisterForm(request.POST)
        if rform.is_valid():
            rform.save()
    else:        
        rform=RegisterForm()
    return render(request,'a1/register.html',{"form":rform})

def userlogin(request):
    if request.method=="POST":
        rform=LoginForm(data=request.POST)
        if rform.is_valid():
            uname=request.POST["username"]
            upass=request.POST["password"]
            user=authenticate(username=uname,password=upass)
            if user:
                login(request,user)
                return HttpResponseRedirect("/profile")
    else:        
        rform=LoginForm()
    return render(request,'a1/login.html',{"form":rform})
def userlogout(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect("/login/")
    else:
        return HttpResponseRedirect("/login/")

def userprofile(request):
    if request.user.is_authenticated:
        return render(request,'a1/profile.html',{"user":request.user})
    else:
        return HttpResponseRedirect("login")
def addpost(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            fm=BlogForm(data=request.POST)
            if fm.is_valid():
                ob=Blog()
                ob.title=request.POST["title"]
                ob.description=request.POST["description"]
                ob.postby=request.user
                ob.postedat=dt.date.today()
                ob.likecount=0
                ob.save()
                lob=Likemodel()
                lob.likepostid=ob.id
                lob.likedbyid=""
                lob.save()
        else:
            fm=BlogForm()
        return render(request,"a1/addpost.html",{"user":request.user,"form":fm})
    else:
        return HttpResponseRedirect("/login/")
def showpost(request):
    if request.user.is_authenticated:

        allpost=Blog.objects.all()
        alllikes=Likemodel.objects.all()
        likebuttonlist=[]
        for i in alllikes:
            print(i," ",i.likedbyid)
            if str(request.user) in i.likedbyid:
                likebuttonlist.append("already liked")
            else:
                likebuttonlist.append("like")
            
        print(likebuttonlist)

        return render(request,"a1/showpost.html",{"posts":zip(allpost,likebuttonlist)})
    return HttpResponseRedirect("/login/")

def mypost(request):
    if request.user.is_authenticated:
        allpost=Blog.objects.filter(postby=request.user)
        return render(request,"a1/mypost.html",{"posts":allpost})
    return HttpResponseRedirect("/login/")

def deletepost(request,id):
    if request.user.is_authenticated:
        allpost=Blog.objects.filter(pk=id)
        allpost.delete()
        return HttpResponseRedirect("/mypost/")    
    return HttpResponseRedirect("/login/")
def likepost(request,id,isliked):
    print("like on post id",id,'by user',request.user,'liked or not',isliked)    
    likepost=Blog.objects.get(id=id)
    if int(isliked)==1:
        likepost.likecount=likepost.likecount-1
        likepost.save()
    else:
        likepost.likecount=likepost.likecount+1
        likepost.save()

    likeid=Likemodel.objects.filter(likepostid=id)
    if int(isliked)==1:
        obj=Likemodel.objects.get(likepostid=id)
        likedata=obj.likedbyid
        likedata=likedata.replace(str(request.user)+",","")
        obj.likedbyid=likedata
        obj.save()
    else:
        if len(likeid)>=1:
            obj=Likemodel.objects.get(likepostid=id)
            obj.likedbyid+=str(request.user)+","
            obj.save()
        else:
            ob=Likemodel()
            ob.likepostid=id
            ob.likedbyid+=str(request.user)+","
            ob.save()
    return HttpResponseRedirect("/showpost/")