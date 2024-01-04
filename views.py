from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import authenticate,login
from managestudent.models import student,teacher
from django.utils.datastructures import MultiValueDictKeyError



# Create your views here.
def login1(request):
    if request.method=="POST":
        u=request.POST['uname']
        p=request.POST['pass']
        user=authenticate(request,username=u,password=p)
        if user is not None and user.is_superuser==1:
            login(request,user)
            # return HttpResponse("ok")
            return render(request,"adminhome.html")
        
        elif student.objects.filter(username=u,password=p):
            sts=student.objects.filter(username=u,password=p)
            for i in sts:
                if i.value==1:
                    request.session['stud_id']=i.id
                    return render(request,"studenthome.html")
                else:
                    return redirect("login")
                
        elif teacher.objects.filter(username=u,password=p):
            teach=teacher.objects.filter(username=u,password=p)
            for i in teach:
                request.session['teach_id']=i.id
                return render(request,"teacherhome.html")
        return HttpResponse("invalid username or password")
    else:
        return render(request,'login.html')
    # return HttpResponse("success")
        
        
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
        return render(request,"studreg.html")

def studview(request):
    a=student.objects.all()
    return render(request,"viewstudent.html",{"a1":a})

def delstudent(request,did):
    a=student.objects.filter(id=did)
    a.delete()
    return redirect(studview)

def update_student(request,eid):
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
        try:
            g=request.POST['gender']
        except MultiValueDictKeyError:
            g='female'
        c=request.POST['co']
        x=teacher.objects.filter(id=eid).update(FirstName=f,LastName=l,age=a,email=e,phone=ph,place=pl,address=ad,username=u,password=p,gender=g,course=c)
        return redirect(studview)
    else:
        a=student.objects.get(id=eid)
        return render(request,"edit_student.html",{"a1":a})

def studentprofile(request):
        a= request.session['stud_id']
        profile=student.objects.filter(id=a)
        return render(request,"studentprofile.html",{"a1":profile})

def studviewteacher(request):
    a=teacher.objects.all()
    return render(request,"studviewteacher.html",{"a1":a})

def approve(request):
    a=student.objects.filter(value=0)
    return render(request,"approve.html",{"a1":a})
def one(request,sid):
    a=student.objects.filter(id=sid).update(value=1)
    return redirect(approve)

def edit_studprofile(request,eid):
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
        try:
            g=request.POST['gender']
        except MultiValueDictKeyError:
            g='female'
        c=request.POST['co']
        
        x=student.objects.filter(id=eid).update(FirstName=f,LastName=l,age=a,email=e,phone=ph,place=pl,address=ad,username=u,password=p,gender=g,course=c)
        return redirect(studentprofile)
    else:
        a=student.objects.get(id=eid)
        return render(request,"edit_studprofile.html",{"a1":a})



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
        return render(request,"teachreg.html")
    
def teachview(request):
    a=teacher.objects.all()
    return render(request,"viewteacher.html",{"a1":a})

def delteacher(request,did):
    a=teacher.objects.filter(id=did)
    a.delete()
    return redirect(teachview)

def teachviewstudent(request):
    a=student.objects.all()
    return render(request,"teachviewstudent.html",{"a1":a})
   
def update_teacher(request,eid):
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
        try:
            g=request.POST['gender']
        except MultiValueDictKeyError:
            g='female'
        d=request.POST['dept']
        x=teacher.objects.filter(id=eid).update(FirstName=f,LastName=l,age=a,email=e,phone=ph,place=pl,address=ad,username=u,password=p,gender=g,department=d)
        return redirect(teachview)
   else:
        a=teacher.objects.get(id=eid)
        return render(request,"edit_teacher.html",{"a1":a})


def teachprofile(request):
    a= request.session['teach_id']
    profile=teacher.objects.filter(id=a)
    return render(request,"teacherprofile.html",{"a1":profile})


def edit_teachprofile(request,eid):
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
        try:
            g=request.POST['gender']
        except MultiValueDictKeyError:
            g='female'
        d=request.POST['dept']
        x=teacher.objects.filter(id=eid).update(FirstName=f,LastName=l,age=a,email=e,phone=ph,place=pl,address=ad,username=u,password=p,gender=g,department=d)
        return redirect(teachprofile)
    else:
        a=teacher.objects.get(id=eid)
        return render(request,"edit_teachprofile.html",{"a1":a})
    
def logout(request):
    return render(request,"login.html")
    
def index(request):
    return render(request,"index.html")