from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from datetime import datetime
from cred.models import intro
from django.contrib import messages
from django.contrib.auth import logout,authenticate,login
import jinja2
import os
from jinja2 import Template
from django_tex.shortcuts import render_to_pdf

# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request,"index.html")
    
def loginUser(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
        # A backend authenticated the credentials
            login(request,user)
            return redirect('/')
        else:
        # No backend authenticated the credentials
            return render(request,'login.html')
    
    return render(request,"login.html")
    
def logoutUser(request):
    logout(request)
    return redirect("/login")

def template(request):
    return render(request,"exampletemp.html")

def sec1(request):
    if request.method=="POST":
            rollno=request.user
            name=request.POST.get('name')
            email=request.POST.get('email')
            number=request.POST.get('number')
            linkd=request.POST.get('linkdin')
            github=request.POST.get('Github')
            university=request.POST.get('University')
            degree=request.POST.get('degree')
            year=request.POST.get('year')
            branch=request.POST.get('Branch')
            cg=request.POST.get('CGPA')
            school=request.POST.get('HSC')
            percentage=request.POST.get('Percentage')
        
            alpha=intro(name=name,email=email,rollno=rollno,number=number,linkd=linkd,github=github,year=year,university=university,degree=degree,branch=branch,cg=cg,school=school,percentage=percentage)
            alpha.save()
            
            return redirect('/sec2')
    
    return render(request,"sec1.html")

def sec2(request):
    return render(request,"sec2.html")

def sec3(request):
    return render(request,"sec3.html")

def current(request):
    # latex_jinja_env = jinja2.Environment(
	# block_start_string = '\BLOCK{',
	# block_end_string = '}',
	# variable_start_string = '\VAR{',
	# variable_end_string = '}',
	# comment_start_string = '\#{',
	# comment_end_string = '}',
	# line_statement_prefix = '%%',
	# line_comment_prefix = '%#',
	# trim_blocks = True,
	# autoescape = False,
	# loader = jinja2.FileSystemLoader(os.path.abspath('.'))
    # )
    template_name = "tests/alpha.tex"
    context = {'foo': 'Bar'}
    return render_to_pdf(request, template_name, context, filename='test.pdf')
    
    
    #return render(request,"current.html")

