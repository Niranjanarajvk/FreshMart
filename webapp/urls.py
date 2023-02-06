from django.urls import path
from webapp import views

urlpatterns=[
    path('',views.newindex,name='newindex'),
    path('aboutpage/',views.aboutpage,name='aboutpage'),
    path('contactpage/',views.contactpage,name='contactpage'),
    path('productfront/',views.productfront,name='productfront'),
    path('discategory/<itemCatg>/',views.discategory,name='discategory'),
    path('productshow/<int:dataid>/',views.productshow,name='productshow'),
    path('loginpage/',views.loginpage,name='loginpage'),
    path('customersave/',views.customersave,name='customersave'),
    path('customerlogin/',views.customerlogin,name='customerlogin'),
    path('customerlogout/', views.customerlogout, name='customerlogout'),
    path('contactdatabase/', views.contactdatabase, name='contactdatabase')


]