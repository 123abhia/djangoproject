
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import View,TemplateView,CreateView,FormView
from django.contrib.auth import authenticate,login 
from .forms import sigupform,signinform

from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.



# template view cheyaan

# class Homeview(TemplateView):
#     template_name='home.html'






class Signin(FormView):
    template_name='signin.html'
    form_class=signinform
    def post(self,request,*args,**kwargs):
        formdata=signinform(data=request.POST)
        if formdata.is_valid():
            usn=formdata.cleaned_data.get('username')
            pas=formdata.cleaned_data.get('password')
            user=authenticate(request,username=usn,password=pas)
            if user:
                login(request,user)  #session creation
               
                return redirect("p")
            else:
               
                return render(request,"signin.html",{'form':formdata})
        else:
            return render(request,"signin.html",{'form':formdata})
        



class Register(CreateView):
    template_name='reg.html'
    form_class=sigupform
    model=User
    success_url=reverse_lazy("sign")
    def form_valid(self, form ) :
        messages.success(self.request,'registration successfull')
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.error(self.request,"registratrion invalid")
        return super().form_invalid(form)


class Lgout(View):
    def get(self,request):
        logout(request)
        return redirect('sign')