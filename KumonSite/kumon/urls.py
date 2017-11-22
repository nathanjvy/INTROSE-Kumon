from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^login/$', views.login, name='login'),
    url(r'^home/$', views.home, name='home'), 
    url(r'^students/$', views.studentPage, name='students'), 
    url(r'^teachers/$', views.teacherPage, name='teacher'), 
    url(r'^attendance/$', views.attendancePage, name='attendance'), 
    url(r'^schedule/$', views.schedulePage, name='schedule'),
    url(r'^salaries/$', views.salaryPage, name='salary'),
    url(r'^payments/$', views.paymentPage, name='payments'),   
    url(r'^expenses/$', views.expensesPage, name='expenses'),
    url(r'^inventory/$', views.inventoryPage, name='inventory'),  
]