from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import authenticate,login
# from sms.models import Student1,Teacher1
from sms.models import Student,Teacher


# Create your views here.
def login(request):
    if request.method=="POST":
        u=request.POST['uname']
        p=request.POST['pass']
        user=authenticate(request,username=u,password=p)
        if user is not None and user.is_superuser==1:
            login(request,user)
            return HttpResponse("ok")
     
            # return render(request,"adminhome.html")
        elif Student.objects.filter(username=u,password=p).exit():
            sts=Student.objects.filter(username=u,password=p)
            for i in sts:
                if i.value==1:
                    request.session['stud_id']=i.id
                    return redirect("studenthome")
                else:
                    return redirect("logins")
        elif Teacher.objects.filter(username=u,password=p):
            for i in teach:
                request.session['teach_id']=i.id
                return redirect("Teacherhome")
        return HttpResponse("success")
    else:
        return render(request,'login.html')
        
        
def stud(request):
    if request.method=='POST':
        f=request.POST['fn']
        l=request.POST['ln']
        # a=request.POST['ag']
        e=request.POST['em']
        ph=request.POST['ph']
        # ad=request.POST['add']
        pl=request.POST['pl']
        # c=request.POST['co']
        # u=request.POST['user']
        # p=request.POST['pass']
        x=Student.objects.create(FirstName=f,LastName=l,email=e,phone=ph,place=pl)
        x.save()
        return HttpResponse("registerd")
    else:      
        return render(request,"student.html")


def teach(request):
        return render(request,"teacher.html")