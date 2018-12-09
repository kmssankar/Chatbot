# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .forms import Fleetform
from .forms import LoginForm
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from .chatbot import chatbot
import time

# Create your views here.
def Claimadd(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/fleet/login/?next=%s' % request.path)
    else:
        form = Fleetform()
        UserName = request.user.username
        return render(request, "claimserv/Addclaim.html", {'form': form ,'User':UserName}) 


def Login(request):
    form = LoginForm()
    return render(request, "claimserv/login.html", {'form': form}) 
    
def Logout(request):
    if  request.user.is_authenticated():
        auth.logout(request)
        return HttpResponseRedirect('/fleet/login/?next=/fleet/addorder/')
    else:
        return HttpResponseRedirect('/fleet/login/?next=/fleet/addorder/')

# Create your views here.
def Chat(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/fleet/login/?next=%s' % request.path)
    else:
        UserName = request.user.username
        return render(request, "claimserv/chat.html", {'User':UserName}) 
# Handle response request 
def Reply(request): 
    if request.method == 'GET':
        start = time.clock()
        print request.body
        print request.session.session_key
        received=(str(request.GET['Input'])).upper()
        ReceivedActual=str(request.GET['Input'])
        print received
        servreturn = chatbot().replychat(ReceivedActual,request.session.session_key)
        resp_data = {'ResponseRply':servreturn,}
        end = time.clock() - start
        print JsonResponse(resp_data)
        print(" Response received in %.2f Seconds"% (end))
        return JsonResponse(resp_data) 
#Handle Trainbot Request     
#def Trainbot(request):     
 #   if not request.user.is_authenticated():
  #      return HttpResponseRedirect('/fleet/login/?next=%s' % request.path)
   # else:
    #    UserName = request.user.username
     #   Adddictform = 
      #  return render(request, "claimserv/trainbot.html", {'Add_Dict_form': Adddictform ,'User':UserName}) 
    
