from django.shortcuts import render,redirect
from Myapp.models import categorydb,productdb,Contactdatab
from Myapp.views import shoppage
from webapp.models import  CustomerDetails

# Create your views here.
def newindex(request):
    data = categorydb.objects.all()
    products=productdb.objects.all()
    return render(request,'newwebindex.html',{'data':data,'products':products})

def aboutpage(request):
    data = categorydb.objects.all()
    return render(request,'About.html',{'data':data})

def contactpage(request):
    data=categorydb.objects.all()
    return render(request,'Contact.html',{'data':data})

def contactdatabase(request):
    if request.method=='POST':
        na = request.POST.get('name')
        em = request.POST.get('email')
        sb = request.POST.get('subject')
        mg = request.POST.get('msg')
        obj = Contactdatab(Name=na,EmailID=em,Subject=sb,Message=mg)
        obj.save()
        return redirect(contactpage)

def productfront(request):
    data = productdb.objects.all()
    return render(request,'produtcweb.html',{'data':data})

def discategory(request,itemCatg):
    data=categorydb.objects.all()
    print("===itemCatg===",itemCatg)
    catg=itemCatg.upper()
    products=productdb.objects.filter(CategoryName=itemCatg)
    context = {
        'products':products,
        'catg':catg,
        'data':data

    }
    return render(request,'categorypage.html',context)

def productshow(request,dataid):
    data = productdb.objects.get(id=dataid)
    return render(request, 'productdetails.html', {'data': data})

def loginpage(request):
    return render(request,'login.html')

def customersave(request):
    if request.method=="POST":
        un=request.POST.get('username')
        em=request.POST.get('email')
        pw=request.POST.get('password')
        cp=request.POST.get('confirmpassword')
        if pw==cp:
            obj = CustomerDetails(username=un,email=em,password=pw,confirmpassword=cp)
            obj.save()
            return redirect(loginpage)
        else:
            return render(request, 'login.html', {'msg':"sorry.... password not matched"})

def customerlogin(request):
    if request.method=='POST':
        username_r = request.POST.get("username")
        password_r = request.POST.get("password")
        if CustomerDetails.objects.filter(username=username_r,password=password_r).exists():
            request.session['username'] = username_r
            request.session['password'] = password_r

            return redirect(newindex)
        else:
            return render(request, 'login.html',{'msg':"sorry.... invalid username or password"})

def customerlogout(request):
    del request.session['username']
    del request.session['password']
    return redirect(newindex)