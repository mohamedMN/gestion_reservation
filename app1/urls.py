
from django.urls import path
from .views import *
from . import views
from django.contrib import admin

from django.conf.urls.static import static
from django.conf import settings

from django.contrib.auth import views as authViews
from django.conf.urls.static import static
from django.conf import settings

urlpatterns =[


    path('',views.home,name='home'),

    path('userLogin/',views.userLogin,name='userLogin'),

    path('login2/',views.login2,name='login2'),

    path('logout/',views.userlogout,name='userlogout'),

    path('table/',views.table,name='table'),


    #path('update/<str:pk>',views.update,name='update'),

    path('delete_res/<str:pk>',views.delete_res,name='delete_res'),

    path('table2/<str:pk>',views.table2,name='table2'),

    path('resform/',views.resform,name='resform'),

 


    path('userProfile/',views.userProfile,name='userProfile'),

#booking urls
    path('BookingView/',
    views.BookingView.as_view(),
    name="BookingView"),



#reset password urls
    path('reset_password/',
    authViews.PasswordResetView.as_view(template_name="password_reset.html"),
    name="resert_password"),

    path('reset_password_sent/',
    authViews.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"),
    name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
    authViews.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"),
    name="password_reset_confirm"),

    path('reset_password_complete/',
    authViews.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"),
    name="password_reset_complete"),

]

    
 



urlpatterns += static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)