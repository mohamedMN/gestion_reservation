from email import message
from multiprocessing import context
from pyexpat.errors import messages
from telnetlib import STATUS
from unittest import result
from django.shortcuts import render,redirect,HttpResponse
from pkg_resources import require
from .models import *
from .forms import *
from django.forms import inlineformset_factory
from django.forms import *
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import requests 
from django.conf import settings
from django.views.generic import *
from django.db.models.functions import Now

from django.utils.decorators import method_decorator


# Create your views here.
@login_required(login_url='login2')
def home(request):
    return render(request,'index.html')

"""if request.Utilisateur.is_authentificated:
        return redirect('home')
    else:
"""
# Create your views here.
def login2(request):
    return render(request,'login2.html')


@login_required(login_url='login2')
def resform(request):
    return render(request,'resForm.html')




#update informations
"""  
def update(request,pk):

    utiRES =Reservation.objects.get(id=pk)
    form = AvaForm(instance=utiRES)
    if request.method == 'POST':
        #savegarde data in database      
        form = ReservationForm(request.POST,instance=utiRES)
        if form.is_valid():
            form.save()
            return redirect('table')

    context ={
        'form':form
    }
    return render(request,'resForm.html',context)

"""
def delete_res(request,pk):
    utiRES =Reservation.objects.get(id=pk)
    utiRES.delete()
    return redirect('table')

#user login 
def userLogin(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == "POST":
                username = request.POST['username']
                password = request.POST['password']
                user=authenticate(request, username=username,password=password)
                if user is not None:
                    recaptcha_response=request.POST.get('g-recaptcha-response')
                    data={
                        'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                        'response': recaptcha_response
                    }
                    r=requests.post('https://www.google.com/recaptcha/api/siteverify',data=data)
                    result=r.json()
                    if result['success']:
                        login(request,user)
                        return redirect('home')
                    else:
                        messages.success(request, 'ReCaptcher failed, try again !')
                else:
                     messages.error(request, 'login failed, try again !')
    return render(request,'login2.html')
    



def userlogout(request):
    logout(request)
    return redirect('userLogin')



"""@login_required(login_url='login2')
def NewReservation(request):
    utilID =Reservation.objects.filter(
    check_in__gte=Now()
    ).delete()
    return redirect('table')



    stackoverflow site to make :How to delete a record after a certain time of it's creation in Django?
    https://stackoverflow.com/questions/65718886/how-to-delete-a-record-after-a-certain-time-of-its-creation-in-django
"""



@login_required(login_url='login2')
def table(request):
    pk= request.user.pk
    utilID =Reservation.objects.filter(utilisateurID=pk)
    id_res=utilID.count()
    context={
        'pk':pk,
        'utilID':utilID,
        'id_res':id_res,
            }
    return render(request,'table.html',context )

#the function table2 take single id and show all he's attribut if isn't go to url i got the same error 
#https://stackoverflow.com/questions/54972280/django-typeerror-objects-is-not-iterable
#if you wile to return multiple row you should use like that
#https://stackoverflow.com/questions/22063748/django-get-returned-more-than-one-topic


@login_required(login_url='login2')
def table2(request,pk):
    utilID =Reservation.objects.filter(utilisateurID=pk)
    id_res=utilID.count()
    acc=utilID.filter(etat='accepter').count()
    rej=utilID.filter(etat='reject').count()

    context={
        'utilID':utilID,
        'id_res':id_res,
        'acc':acc,
        'rej':rej
            }
    return render(request,'table2.html',context)



"""
@login_required(login_url='login2')
def userProfile(request):
    user=request.user.Utilisateur
    form= UserForm(instance=user)
    if request.method=="POST":
        form=UserForm(request.POST , request.FILES , instance=Utilisateur)
        if form.is_valid():
            form.save()

    context={
            'form':form
            }
    return render(request,'profile.html',context)

"""

@login_required(login_url='login2')
def userProfile(request):
    user=request.user.utilisateur
    form=UserForm(instance=user)
    if request.method == "POST":
        form=UserForm(request.POST , request.FILES , instance=user)
        if form.is_valid():
            form.save()

    context={
        'form':form,
        'user':user
            }
    return render(request,'profile.html',context)

#https://www.youtube.com/watch?v=m7uVhLxT1AA&list=PL_6Ho1hjJirn8WbY4xfVUAlcn51E4cSbY&index=3   hada for other things
#reservation form and validation
#@login_required(login_url='login2')    in class function @login_required desn't work
#this function create reservation and teste if place/time are available on database
#https://stackoverflow.com/questions/57545684/hotel-reservation-system-in-django-how-to-make-a-room-unavailable-to-other-user
#solution to that probléme
@method_decorator(login_required, name='dispatch')
class BookingView(FormView):
    form_class= AvailabilityForm
    template_name = 'reservation.html'

    def form_valid(self, form):
        data= form.cleaned_data
        place=Place.objects.all()
        available=False
        i =0
        for disp in place:    # disp represent evry place that has to be free
            i = i+1
            case_1 = Reservation.objects.filter(place=i, check_in__lte=data['check_in'], check_out__gte=data['check_out']).exists()

            case_2 = Reservation.objects.filter(place=i, check_in__lte=data['check_out'], check_out__gte=data['check_out']).exists()

            case_3 = Reservation.objects.filter(place=i, check_in__gte=data['check_in'], check_out__lte=data['check_out']).exists()

            if not (case_1 or case_2 or case_3):
                    my_p = Utilisateur.objects.get(user=self.request.user.id)
                    plc=Place.objects.get(id=i)
                    booking=Reservation.objects.create(
                        utilisateurID=my_p,
                        place=plc,
                        check_in=data['check_in'],
                        check_out=data['check_out']
                    )
                    booking.save()
                    pk= self.request.user.id
                    utilID =Reservation.objects.filter(utilisateurID=pk)
                    id_res=utilID.count()
                    context={
                        "id_res":id_res,
                        'booking':booking,
                        'utilID':utilID,
                            }
                    return render(self.request,'table.html',context)            
        else: 
            messages.error(self.request, 'this schedure is already has been booked try again !')
            return render(self.request,'reservation.html')