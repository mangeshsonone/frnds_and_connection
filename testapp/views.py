from django.shortcuts import render
from .forms import usercreation,entropyform
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.models import User
from .models import entropy,siteuser,photopost
from .forms import profileform,photoform
from django.db.models import Q


def userregister(request):
    if request.method=='POST':
        print('hi')
        fm=usercreation(request.POST)
        print('hi2')
        if fm.is_valid():
           
            fm.save()
            id=fm.cleaned_data['username']
            obj=User.objects.get(username=id)
            print(obj)
            obj2=siteuser.objects.create(user=obj)
            print(obj2)
            messages.success(request,'user created')
            return HttpResponseRedirect('/getlogin/')
    else:
        fm=usercreation()
    return render(request,'usercreate.html',{'form':fm})


def getlogin(request):
    if request.method=='POST':
        fm=AuthenticationForm(request=request,data=request.POST)
        if fm.is_valid():
            uname=fm.cleaned_data['username']
            passw=fm.cleaned_data['password']
            obj=authenticate(username=uname,password=passw)
            if obj is not None:
                login(request,obj)
                # messages.success(request,'user created')
                return HttpResponseRedirect('/entropypredict/')
    fm=AuthenticationForm()
    return render(request,'userlogin.html',{'form':fm})


def page(request):
    # print(type(request.user))
    # print('usertype1',type(request.user.siteuser.user))
    # print(request.user.siteuser.user)
    obj=siteuser.objects.get(user=request.user.siteuser.user)
    # print(type(obj))
    # print(obj)
    abj=siteuser.objects.get(user=request.user)
    # print(abj)
    # print('siteuseris',siteuser)
    # print(obj,abj)
    # s=request.user.siteuser.profile
    # print(s)
    # print(request.user.siteuser)
    # obj=followme.objects.all()
    # print(obj)

    post=photopost.objects.filter(user=request.user)
    print('user is',request.user.id)
    # request.user.siteuser.user=request.user
    
    return render(request,'profile.html',{'user':request.user,'post':post})


def searchu(request):
    print('user is',request.user.id)
    susername=request.GET.get('susername')
    abj=User.objects.get(username=susername)
    print(abj.id)
    obj=siteuser.objects.get(user__username=susername)
    # print(type(obj.user))
    # print(type(obj.user.username))
    # print(siteuser.user)
    # print('wel')
    # print('susername',susername)
    abj=User.objects.get(username=susername)
    # print(User)
    # print('usertype2',type(abj))
    # print(abj)
    # print(abj.siteuser)
    print(type(abj))
    post=photopost.objects.filter(user=abj)
    for i in post:
        print(i.user.id)
    # sub=followme.objects.filter(followers=abj)
    # print((sub))
    # for i in sub:
    #     print((i.followers.get(username=susername)))
    #     print(i.followers.all())
        # for j in i.followers.all():
        #     print(type(j))
    # print(sub)
    

    # return render(request,'searchuser.html',{'user':abj,'post':post})
    return render(request,'searchuser.html',{'user':obj,'post':post})
    return HttpResponseRedirect('/page/')


def profilepic(request,id=None):
    obj=siteuser.objects.get(user=request.user.siteuser.user)
    if request.method=='POST':
        fm=profileform(request.POST,request.FILES,instance=obj)
        if fm.is_valid():
            fm.save()
        return HttpResponseRedirect('/page/')
    print('welcome',obj.profile)
    fm=profileform(instance=obj)
    return render(request,'profilepic.html',{'form':fm})

def photoupload(request):
    if request.method=='POST':
        fm=photoform(request.POST,request.FILES)
        if fm.is_valid():
            photo=fm.cleaned_data['photo']
            obj=photopost.objects.create(user=request.user,photo=photo)
            print(obj.user,obj.photo)
            return HttpResponseRedirect('/page/')

    fm=photoform()
    return render(request,'photo.html',{'form':fm})

def home(request):
    print(request.user)
    l=[]
    sbj=User.objects.all()
    # for i in sbj:
    #     l.append(i)
    #     print(i)
    obj=photopost.objects.filter(Q(user=request.user) | Q(user__username='jayesh')).order_by('-id')
    obj=photopost.objects.filter(user__in=sbj).order_by('-id')
    print(obj)
    return render(request,'home.html',{'obj':obj})

# def followme(request,user):
#     print('hi')
#     print(user)
#     print(type(user))
#     obj=User.objects.get(username=user)
#     print(type(obj))
#     request.user.siteuser.follow.add(obj)
#     abj=siteuser.objects.get(user=obj)
#     print(abj.user)
#     abj.following.add(request.user)
#     print(type(abj))
#     # return redirect('homepage/?username=jayesh')
#     return HttpResponseRedirect('/homepage/?username='+user)

    

def entropypredict(request):
    fm=entropyform()
    return render(request,'entropy.html',{'form':fm})
