from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import authenticate,login
from stud.models import student,teacher


# Create your views here.
def login1(request):
    if request.method=="POST":
        u=request.POST['uname']
        p=request.POST['pass']
        user=authenticate(request,username=u,password=p)
    #     user=authenticate(
    #     username=request.POST['uname'],
    #     password=request.POST['pass']
        
    #     if user is not None:
    #         login(request,user)
        if user is not None and user.is_superuser==1:
            login(request,user)
            # return HttpResponse("ok")
            return render(request,"adminhome.html")
        
        elif student.objects.filter(username=u,password=p).exit():
            sts=student.objects.filter(username=u,password=p)
            for i in sts:
                if i.value==1:
                    request.session['stud_id']=i.id
                    return render("studenthome.html")
                else:
                    return redirect("logins")
        elif teacher.objects.filter(username=u,password=p):
            teach=teacher.objects.filter(username=u,password=p)
            for i in teach:
                request.session['teach_id']=i.id
                return render("teacherhome.html")
        return HttpResponse("success")
    else:
        return render(request,'login.html')
        
        
def studreg(request):
    if request.method=='POST':
        f=request.POST['fn']
        l=request.POST['ln']
        a=request.POST['ag']
        e=request.POST['em']
        ph=request.POST['ph']
        ad=request.POST['add']
        g=request.POST['gender']
        pl=request.POST['pl']
        c=request.POST['co']
        u=request.POST['user']
        p=request.POST['pass']
        x=student.objects.create(FirstName=f,LastName=l,email=e,phone=ph,place=pl,age=a,address=ad,gender=g,course=c,username=u,password=p,value=0,usertype='student')
        x.save()
        return HttpResponse("registerd")
    else:      
        return render(request,"student.html")


def teachreg(request):
    if request.method=='POST':
        f=request.POST['fn']
        l=request.POST['ln']
        a=request.POST['ag']
        e=request.POST['em']
        ad=request.POST['add']
        ph=request.POST['ph']
        pl=request.POST['pl']
        u=request.POST['user']
        p=request.POST['pass']
        g=request.POST['gender']
        d=request.POST['dept']
        x=teacher.objects.create(FirstName=f,LastName=l,age=a,email=e,phone=ph,place=pl,address=ad,username=u,password=p,gender=g,department=d,value=1,usertype="teacher")
        x.save()
        return HttpResponse("success")
    else:
        return render(request,"teacher.html")