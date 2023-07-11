from typing import Any, Dict
from django.db.models.query import QuerySet
from django.shortcuts import redirect, render
from django .views.generic import TemplateView,ListView,View,DetailView,CreateView,FormView
from owner.models import *
from  cust.models import *
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
# Create your views here.

def signin_required(fn):
    def inner(request,*args,**kwargs):
        if request.user.is_authenticated:
            return fn(request,*args,**kwargs)
        else:
           
            return redirect('signit')
    return inner
dec=[signin_required,never_cache]



class userhome(TemplateView):
    template_name='index.html'

@method_decorator(dec,name='dispatch')
class Produlist(ListView):
    template_name="detail.html"
    model=Detailm
    context_object_name='product'

    def get_context_data(self, **kwargs):
     context = super(Produlist, self).get_context_data(**kwargs)
     context['prod']=Keraladm.objects.all()
     return context
   
@method_decorator(dec,name='dispatch')
class Detailist(DetailView):
    template_name="productdetail.html"
    model=Keraladm
    context_object_name='produ'
    pk_url_kwarg='id'

@method_decorator(dec,name='dispatch')
class CheckoutView(TemplateView):
    template_name='checkout.html'

    def post(self,request,*args,**kwargs):
    #     cid=kwargs.get("cid")
        pid=kwargs.get("pid")
    #     cart=Cart.objects.get(id=cid)
        prod=Keraladm.objects.get(id=pid)
        user=request.user
        # quantity=.quantity
        address=request.POST.get("address")
        phone=request.POST.get("phone")
        Orders.objects.create(product=prod,user=user,address=address,phone=phone)
    #     cart.status=" Order Placed"
    #     cart.save()
        
        return redirect("p") 
@method_decorator(dec,name='dispatch')
class OrderListv(ListView):
    template_name='orderlist.html'
    model=Orders
    context_object_name='orders'
    

    def get_queryset(self) :
        return Orders.objects.filter(user=self.request.user)
    


   


# class KProdulist(ListView):
    # template_name="detail.html"
    # model=Keraladm
    # context_object_name='prod'

def Delete(request,id):
    id=id 
    Orders.objects.filter(id=id).delete()
    return redirect('p')
