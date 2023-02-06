from django.urls import path
from Myapp import views

urlpatterns = [
    path('shoppage/', views.shoppage, name='shoppage'),
    path('shopvegpg/', views.shopvegpg, name='shopvegpg'),
    path('shopvegform/', views.shopvegform, name='shopvegform'),
    path('displayveg/', views.displayveg, name='displayveg'),
    path('editdata/<int:dataid>/',views.editdata,name='editdata'),
    path('fruitspage/',views.fruitspage,name='fruitspage'),
    path('shopfruitspage/',views.shopfruitspage,name='shopfruitspage'),
    path('dispfruit/',views.dispfruit,name='dispfruit'),
    path('editfru/<int:dataid>/',views.editfru,name='editfru'),
    path('updatedata/<int:dataid>/',views.updatedata,name='updatedata'),
    path('updatedatafruit/<int:dataid>/', views.updatedatafruit, name='updatedatafruit'),
    path('deletedata/<int:dataid>/',views.deletedata,name='deletedata'),
    path('delete2/<int:dataid>/',views.delete2,name='delete2'),
    path('adminpage/',views.adminpage,name='adminpage'),
    path('adminpagedb/',views.adminpagedb,name='adminpagedb'),
    path('displayadminpg/',views.displayadminpg,name='displayadminpg'),
    path('editadmin/<int:dataid>/',views.editadmin,name='editadmin'),
    path('updateadminpage/<int:dataid>/',views.updateadminpage,name='updateadminpage'),
    path('deleteadmin/<int:dataid>/',views.deleteadmin,name='deleteadmin'),
    path('categoryadd/',views.categoryadd,name='categoryadd'),
    path('categorypagedb/',views.categorypagedb,name='categorypagedb'),
    path('displaycategory/',views.displaycategory,name='displaycategory'),
    path('editcategorypage/<int:dataid>/',views.editcategorypage,name='editcategorypage'),
    path('updatecategory/<int:dataid>/',views.updatecategory,name='updatecategory'),
    path(' deletecategory/<int:dataid>/',views. deletecategory,name='deletecategory'),
    path('addproduct/',views.addproduct,name='addproduct'),
    path('productback/',views.productback,name='productback'),
    path('displayproduct/',views.displayproduct,name='displayproduct'),
    path('editproduct/<int:dataid>/',views.editproduct,name='editproduct'),
    path('updateproduct/<int:dataid>/',views.updateproduct,name='updateproduct'),
    path('deleteproduct/<int:dataid>/',views.deleteproduct,name='deleteproduct'),
    path('logindata/',views.logindata,name='logindata'),
    path('logindb_fun/',views.logindb_fun,name='logindb_fun')



]
