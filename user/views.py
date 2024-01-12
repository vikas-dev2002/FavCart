import email
from sqlite3 import Cursor
from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from datetime import datetime
from django.db import connection
# Create your views here.

def index(request):
    user=request.session.get('userid')
    ct=""
    if user:
        ct=mcart.objects.all().filter(userid=user).count()
    x=category.objects.all().order_by('-id')
    pdata=myproduct.objects.all().order_by('-id')
    mydict={"data":x,"prodata":pdata,"cart":ct}
    return render(request,'user/index.html',context=mydict)
#########################################################
def about(request):
    user=request.session.get('userid')
    ct=""
    if user:
        ct=mcart.objects.all().filter(userid=user).count()
    return render(request,'user/aboutus.html',{"cart":ct})
###########################################################
def product(request):
    user=request.session.get('userid')
    ct=""
    if user:
        ct=mcart.objects.all().filter(userid=user).count()
    return render(request,'user/product.html',{"cart":ct})
#############################################################
def myorder(request):
    user=request.session.get('userid')
    ct=""
    if user:
        ct=mcart.objects.all().filter(userid=user).count()
    user=request.session.get('userid')
    oid=request.GET.get('oid')
    pdata=""
    ddata=""
    if user:
        if oid is not None:
           morder.objects.all().filter(id=oid).delete()
           return HttpResponse("<script>alert('Your order has been canceled..');location.href='/user/myorder/'</script>")
        cursor=connection.cursor()
        cursor.execute("select p.*,o.* from user_myproduct p,user_morder o where p.id=o.pid and o.userid='"+str(user)+"' and o.remarks='pending'")
        pdata=cursor.fetchall()
        cursor.execute("select p.*,o.* from user_myproduct p,user_morder o where p.id=o.pid and o.userid='"+str(user)+"' and o.remarks='Delivered'")
        ddata=cursor.fetchall()
    return render(request,'user/myorder.html',{"cart":ct,"pdata":pdata,"ddata":ddata})
############################################################
def enquiry(request):
    user=request.session.get('userid')
    ct=""
    if user:
        ct=mcart.objects.all().filter(userid=user).count()
    status=False
    if request.method=="POST":
        a=request.POST.get('name')
        b=request.POST.get('email')
        c=request.POST.get('mob')
        d=request.POST.get('msg')
        contactus(Name=a,Mobile=c,Email=b,Message=d).save()
        status=True
        #mdict={"Name":a,"Email":b,"Mobile":c,"Message":d}
    msg={"m":status,"cart":ct}
    return render(request,'user/enquiry.html',context=msg)
##############################################################
def signup(request):
    user=request.session.get('userid')
    ct=""
    if user:
        ct=mcart.objects.all().filter(userid=user).count()
    if request.method=="POST":
        Name=request.POST.get('name')
        Email=request.POST.get('email')
        Mobile=request.POST.get('mob')
        Password=request.POST.get('passwd')
        CPassword=request.POST.get('cpasswd')
        Picture=request.FILES.get('ig')
        Address=request.POST.get('msg')
        x=register.objects.all().filter(email=Email).count()
        if x==0:
            register(name=Name,email=Email,mobile=Mobile,ppic=Picture,passwd=Password,cpasswd=CPassword,address=Address).save()
            return HttpResponse("<script>alert('You are register successfully..');location.href='/user/signup/'</script>")
        else:
            return HttpResponse("<script>alert('You are already registered');location.href='/user/signup/'</script>")
    return render(request,'user/signup.html',{"cart":ct})        
        
##################################################################
def myprofile(request):
    user=request.session.get('userid')
    ct=""
    if user:
        ct=mcart.objects.all().filter(userid=user).count()
    x=""    
    if user:
        if request.method=="POST":
           Name=request.POST.get('name')
           Mobile=request.POST.get('mob')
           Password=request.POST.get('passwd')
           Picture=request.FILES.get('ig')
           Address=request.POST.get('msg')
           register(email=user,name=Name,mobile=Mobile,ppic=Picture,passwd=Password,address=Address).save()
           return HttpResponse("<script>alert('Your Profile Updated successfully');location.href='/user/profile/'</script>")
        x=register.objects.all().filter(email=user)    
    return render(request,'user/myprofile.html',{"cart":ct,"mdata":x})
########################################################################
def signin(request):
    user=request.session.get('userid')
    ct=""
    if user:
        ct=mcart.objects.all().filter(userid=user).count()
    if request.method=="POST":
        Email=request.POST.get('e')
        Password=request.POST.get('p')
        x=register.objects.all().filter(email=Email,passwd=Password).count()
        y=register.objects.all().filter(email=Email,passwd=Password)
        if x==1:
            request.session['userid']=Email
            request.session['userpic']=str(y[0].ppic)
            return HttpResponse("<script>alert('You Are Login Successfully..');location.href='/user/index/'</script>")
        else:
            return HttpResponse("<script>alert('Your userid or password is incorrect !!!');location.href='/user/signin/'</script>")
    return render(request,'user/signin.html',{"cart":ct})
#######################################################################

def mens(request):
    user=request.session.get('userid')
    ct=""
    if user:
        ct=mcart.objects.all().filter(userid=user).count()
    cid=request.GET.get('msg')
    cat=category.objects.all().order_by('-id')
    d=myproduct.objects.all().order_by('-id').filter(mcategory=3)
    if cid is not None:
        d=myproduct.objects.all().filter(mcategory=3,pcategory=cid)
    mydict={"cats":cat,"data":d,"cart":ct}
    return render(request,'user/mens.html',mydict)
#############################################################################
def womens(request):
    user=request.session.get('userid')
    ct=""
    if user:
        ct=mcart.objects.all().filter(userid=user).count()
    cid=request.GET.get('msg')
    cat=category.objects.all().order_by('-id')
    d=myproduct.objects.all().filter(mcategory=4)
    if cid is not None:
        d=myproduct.objects.all().filter(mcategory=4,pcategory=cid)
    mydict={"cats":cat,"data":d,"cart":ct}
    return render(request,'user/womens.html',mydict)
##################################################################################
def kids(request):
    user=request.session.get('userid')
    ct=""
    if user:
        ct=mcart.objects.all().filter(userid=user).count()
    cid=request.GET.get('msg')
    cat=category.objects.all().order_by('-id')
    d=myproduct.objects.all().filter(mcategory=5)
    if cid is not None:
        d=myproduct.objects.all().filter(mcategory=5,pcategory=cid)
    mydict={"cats":cat,"data":d,"cart":ct}
    return render(request,'user/kids.html',mydict)
################################################################################
def viewproduct(request):
    user=request.session.get('userid')
    ct=""
    if user:
        ct=mcart.objects.all().filter(userid=user).count()
    a=request.GET.get('abc')
    x=myproduct.objects.all().filter(id=a)

    return render(request,'user/viewproduct.html',{"pdata":x,"cart":ct})
#################################################################################
def signout(request):
    user=request.session.get('userid')
    ct=""
    if user:
        ct=mcart.objects.all().filter(userid=user).count()
    if request.session.get('userid'):
        del request.session['userid']
    return HttpResponse("<script>alert('You are singout');location.href='/user/index/'</script>")    
#################################################################################################
def myordr(request):
    user=request.session.get('userid')
    ct=""
    if user:
        ct=mcart.objects.all().filter(userid=user).count()
    user=request.session.get('userid')
    ppid=request.GET.get('msg')
    if user:
        if ppid is not None:
            morder(userid=user,pid=ppid,remarks='pending',odate=datetime.now().date(),status=True).save()
            return HttpResponse("<script>alert('Your Order Confirm...');location.href='/user/index/'</script>")

    else:
        return HttpResponse("<script>alert('You are login first ..');location.href='/user/signin/'</script>")
    return render(request,'user/myordr.html')
################################################################################################################    
def mycart(request):
    user=request.session.get('userid')
    ct=""
    if user:
        ct=mcart.objects.all().filter(userid=user).count()
    p=request.GET.get('pid')
    user=request.session.get('userid')
    if user:
        if p is not None:
            mcart(userid=user,pid=p,cdate=datetime.now().date(),status=True).save()
            return HttpResponse("<script>alert('Your item added...');location.href='/user/index/'</script>")
    else:
        return HttpResponse("<script>alert('You have login first!!!!');location.href='/user/signin/'</script>")
    return render(request,'user/mcart.html',{"cart":ct}) 
##################################################################################################################################    
def showcart(request):
    user=request.session.get('userid')
    a=request.GET.get('msg')
    cid=request.GET.get('cid')
    pid=request.GET.get('pid')
    if user:
        if a is not None:
            mcart.objects.all().filter(id=a).delete()
            return HttpResponse("<script>alert('Your item deleted from cart');location.href='/user/showcart/'</script>")
        elif pid is not None:
            mcart.objects.all().filter(id=cid).delete()
            morder(userid=user,pid=pid,remarks="pending",status=True,odate=datetime.now().date()).save()
            return HttpResponse("<script>alert('Your order has been place successfully');location.href='/user/showcart/'</script>")
        cursor=connection.cursor()
        cursor.execute("select p.*,c.* from user_myproduct p, user_mcart c where p.id=c.pid and c.userid='"+str(user)+"'")
        cdata=cursor.fetchall()
        md={"cdata":cdata}
    return render(request,'user/showcart.html',md)
##############################################################################################################################    
def cpdetail(request):
    c=request.GET.get('cid')
    p=myproduct.objects.all().order_by('-id').filter(pcategory=c)
    return render(request,'user/cpdetail.html',{"pdata":p}) 
#################################################################################################                    