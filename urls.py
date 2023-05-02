"""itn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1 import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',views.index),
    path ('update_data/',views.update_data),
   
    path('jail/',views.jail),
    path('jail_insertion/',views.jail_insertion),
    path('jail_remove/',views.jail_remove),
    path('jail_remove1/<int:id>',views.jail_remove1),

    
    path('cell/',views.cell),        
    path('cell_insertion/',views.cell_insertion),
    path('cell_remove/',views.cell_remove),
    path('cell_remove1/<int:id>',views.cell_remove1),


    path('duty/',views.duty),
    path('duty_insertion/',views.duty_insertion),
    path('duty_remove/',views.duty_remove),
    path('duty_remove1/<int:id>',views.duty_remove1),

    
    path('account/',views.account),
    path('account_insertion/',views.account_insertion),
    path('account_remove/',views.account_remove),
    path('account_remove1/<int:id>',views.account_remove1),

    path('search_jail/',views.search_jail),
    path('visitors_request/<int:id>',views.visitors_request),
    path('public_header/',views.public_header),
    path('request1/',views.request1),
    path('jailer_header/',views.jailer_header),

    path('allot_prisoner/',views.allot_prisoner),
    path('allot_prisoner1/<int:id>',views.allot_prisoner1),
    path('allot1/',views.allot1),

    path('release_prisoner/',views.release_prisoner),
    path('release_prisoner1/<int:id>',views.release_prisoner1),

    path('allot_warden/',views.allot_warden),
    path('allot_warden1/<int:id>',views.allot_warden1),
    path('allot_warden2/<int:id>',views.allot_warden2),
    path('view_visit_request/',views.view_visit_request),
    path('login/',views.login),
    path('logins/',views.logins),
    path('admin1/',views.admin1),
    path('jailer1/',views.jailer1),
    path('warden1/',views.warden1),
    path('prisoner1/',views.prisoner1),
    path('logout/',views.logout),
    path('view_account/',views.view_account),
    path('view_cell/',views.view_cell),
    path('view_jail/',views.view_jail),
    path('update_account/',views.update_account),
    path('update_account1/<int:id>',views.update_account1),
    path('update_account2/<int:id>',views.update_account2),
    path('view_prisoner/',views.view_prisoner),
    path('view_warden/',views.view_warden),
    path('view_prisoner1/',views.view_prisoner1),
    path('allot_duty/<str:id>',views.allot_duty),
    path('allot_duty1/<int:id>',views.allot_duty1),
    path('allot_duty3/',views.allot_duty3),
    path('allot_duty2/',views.allot_duty2),
    path('give_complaint/',views.give_complaint),
    path('view_duty/',views.view_duty),
    path('give_complaint1/',views.give_complaint1),
    path('view_complaint/',views.view_complaint),
    path('report/',views.report),
    path('report1/<str:id>',views.report1),
    path('report2/<str:id>',views.report2),
    path('changepassword/',views.changepassword),
    path('changepassword1/',views.changepassword1),
    
    
  
  
  
  



    




]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


