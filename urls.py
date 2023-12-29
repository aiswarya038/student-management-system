from django.urls import path
from stud import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('log',views.login1,name="login"),

    path('studreg',views.studreg,name="studreg"),
    path('studview',views.studview,name="studview"),
    path('approve/<int:sid>',views.one,name="one"),
    path('approve',views.approve,name="approve"),
    path('delete/<int:did>',views.delstudent,name="delstudent"),
    path('studentprofile',views.studentprofile,name="studentprofile"),



    path('teachreg',views.teachreg,name="teachreg"),
    path('teachview',views.teachview,name="teachview"),
    path('teachprofile',views.teachprofile,name="teachprofile"),
    path('del/<int:did>',views.delteacher,name="delteacher"),
    path('update/<int:eid>',views.update_teacher,name="update_teacher"),
    path('teachviewstudent',views.teachviewstudent,name="teachviewstudent"),






   




]
