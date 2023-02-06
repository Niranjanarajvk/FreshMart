from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from Myapp.models import shopvegdb,fruitsdb,admindb,categorydb,productdb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError



# Create your views here.
def shoppage(request):
    return render(request,'index.html')


def shopvegpg(request):
    return render(request,'shopvegiform.html')



def shopvegform(request):
    if request.method=="POST":
        na =request.POST.get('name')
        pr = request.POST.get('price')
        de = request.POST.get('desc')
        img = request.FILES['image']
        obj = shopvegdb(VegitableName=na,Price=pr,Description=de,Image=img)
        obj.save()
        return redirect(shopvegpg)

def displayveg(request):
    data = shopvegdb.objects.all()
    return render(request,'displayshopveg.html', {'data':data})


def editdata(request,dataid):
    data = shopvegdb.objects.get(id=dataid)
    print(data)
    return render(request,'editpage.html',{'data':data})


def fruitspage(request):
    return render(request,'fruits.html')

def shopfruitspage(request):
    if request.method=="POST":
        na =request.POST.get('name')
        pr = request.POST.get('price')
        de = request.POST.get('desc')
        img = request.FILES['image']
        obj = fruitsdb(FruitsName=na,Price=pr,Description=de,Image=img)
        obj.save()
        return redirect(fruitspage)

def dispfruit(request):
    data = fruitsdb.objects.all()
    return render(request,'displayfruits.html',{'data':data})

def editfru(request,dataid):
    data = fruitsdb.objects.get(id=dataid)
    print(data)
    return render(request,'editfruit.html',{'data':data})

def updatedata(request,dataid):
    if request.method=="POST":
        na = request.POST.get('name')
        pr = request.POST.get('price')
        de = request.POST.get('desc')
        try:
            img =request.FILES['image']
            fs =FileSystemStorage()
            file=fs.save(img.name, img)
        except MultiValueDictKeyError:
            file=shopvegdb.objects.get(id=dataid).Image
        shopvegdb.objects.filter(id=dataid).update(VegitableName=na,Price=pr,Description=de,Image=file)
        return redirect(displayveg)


def updatedatafruit(request,dataid):
    if request.method=="POST":
        na = request.POST.get('name')
        pr = request.POST.get('price')
        de = request.POST.get('desc')
        try:
            img =request.FILES['image']
            fs =FileSystemStorage()
            file=fs.save(img.name, img)
        except MultiValueDictKeyError:
            file=fruitsdb.objects.get(id=dataid).Image
        fruitsdb.objects.filter(id=dataid).update(FruitsName=na,Price=pr,Description=de,Image=file)
        return redirect(dispfruit)

def deletedata(request,dataid):
    data =shopvegdb.objects.filter(id=dataid)
    data.delete()
    return redirect(displayveg)

def delete2(request,dataid):
    data =fruitsdb.objects.filter(id=dataid)
    data.delete()
    return redirect(dispfruit)

def adminpage(request):
    return render(request,'admin.html')

def adminpagedb(request):
    if request.method == "POST":
        na = request.POST.get('name')
        mb = request.POST.get('mob')
        em = request.POST.get('mail')
        img = request.FILES['image']
        un = request.POST.get('username')
        pd = request.POST.get('pwd')
        cp = request.POST.get('confpwd')
        obj =admindb(Name=na,MobileNumber=mb,EmailID=em,Image=img,UserName=un,Password=pd,ConfirmPassword=cp)
        obj.save()
        return redirect(adminpage)

def displayadminpg(requset):
    data = admindb.objects.all()
    return render(requset,'displayadmin.html',{'data':data})

def editadmin(request,dataid):
    data = admindb.objects.get(id=dataid)
    print(data)
    return render(request, 'editadmin.html', {'data': data})

def updateadminpage(request,dataid):
    if request.method == "POST":
        na = request.POST.get('name')
        mb = request.POST.get('mob')
        em = request.POST.get('mail')
        un = request.POST.get('username')
        pd = request.POST.get('pwd')
        cp = request.POST.get('confpwd')
        try:
            img = request.FILES['image']
            fs = FileSystemStorage()
            File=fs.save(img.name,img)
        except MultiValueDictKeyError:
            file = admindb.objects.get(id=dataid).Image
            admindb.objects.filter(id=dataid).update(Name=na,MobileNumber=mb,EmailID=em, Image=file,UserName=un,Password=pd,ConfirmPassword=cp)
            return redirect(displayadminpg)

def deleteadmin(request,dataid):
    data = admindb.objects.filter(id=dataid)
    data.delete()
    return redirect(displayadminpg)

def categoryadd(request):
    return render(request,'category.html')
def categorypagedb(request):
    if request.method == "POST":
        na =request.POST.get('name')
        de =request.POST.get('desc')
        img =request.FILES['image']
        obj = categorydb(CategoryName=na,Description=de,Image=img)
        obj.save()
        return redirect(categoryadd)
def displaycategory(request):
    data = categorydb.objects.all()

    return render(request,'displaycategory.html',{'data':data})
def editcategorypage(request,dataid):
    data =categorydb.objects.get(id=dataid)
    print(data)
    return render(request,'editcategory.html',{'data':data})

def updatecategory(request,dataid):
    if request.method == "POST":
        na= request.POST.get('name')
        de = request.POST.get('desc')
        try:
            img =request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
             file = categorydb.objects.get(id=dataid).Image
        categorydb.objects.filter(id=dataid).update(CategoryName=na,Description=de,Image=file)
        return redirect(displaycategory)

def deletecategory(request,dataid):
    data =categorydb.objects.filter(id=dataid)
    data.delete()
    return redirect(displaycategory)

def addproduct(request):
    data =categorydb.objects.all()
    return render(request,'product.html', {'data':data})

def productback(request):
    if request.method=='POST':
        cn = request.POST.get('category')
        pn = request.POST.get('name')
        pr = request.POST.get('price')
        de = request.POST.get('desc')
        img = request.FILES['image']
        obj = productdb(CategoryName=cn,ProductName=pn,Price=pr,Description=de,Image=img)
        obj.save()
        return redirect(addproduct)

def displayproduct(request):
    data =productdb.objects.all()
    return render(request,'displayproduct.html',{'data':data})

def editproduct(request,dataid):
    data = productdb.objects.get(id=dataid)
    da = categorydb.objects.all()
    print(data)
    return render(request,'editproduct.html' ,{'data':data,'da':da})




def updateproduct(request, dataid):
    if request.method == "POST":
        cn = request.POST.get('category')
        pn = request.POST.get('name')
        pr = request.POST.get('price')
        de = request.POST.get('desc')

        try:
            img = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = productdb.objects.get(id=dataid).Image
        productdb.objects.filter(id=dataid).update(CategoryName=cn, ProductName=pn, Price=pr, Description=de, Image=file)
        return redirect(displayproduct)

def deleteproduct(request,dataid):
    data =productdb.objects.filter(id=dataid)
    data.delete()
    return redirect(displayproduct)

def logindata(request):
    return render(request,'log.html')

def logindb_fun(request):
    if request.method == "POST":
        un=request.POST.get('username')
        pwd=request.POST.get('password')
        if User.objects.filter(username__contains=un).exists():
            user = authenticate(username=un,password=pwd)
            if user is not None:
                login(request, user)
                request.session['username'] = un
                request.session['password'] = pwd
                return redirect(shoppage)

            else:
                return redirect(logindata)
        else:
            return redirect(logindata)

