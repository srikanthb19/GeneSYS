from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import loader
from django.middleware.csrf import get_token
from django.core.urlresolvers import resolve


def index(request):
    return render_to_response('index.html')

def signin(request):
    if request.method == 'GET':
        login_status=""
        csrf_token = get_token(request)
        template = loader.get_template('site-templates/signin.html')
        context={'csrf_token':csrf_token , 'login_status':login_status}
        return HttpResponse(template.render(context,request))
    else:
        from django.contrib.auth import authenticate, login
        username = request.POST.get("inputEmail")
        password = request.POST.get("inputPassword")
        uname = username.split("@")
        user = authenticate(username=uname[0], password=password)
        if user is not None:
            login(request,user)
            template = loader.get_template('home.html')
            logged_user = user
            context = {'logged_user':logged_user}
            return HttpResponse(template.render(context, request))
        else:
            login_status = "Usernme or Password is incorrect , Retry."
            csrf_token = get_token(request)
            template = loader.get_template('site-templates/signin.html')
            context = {'csrf_token': csrf_token, 'login_status': login_status}
            return HttpResponse(template.render(context, request))
