from django.urls import path
from managestudent import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('log',views.login1,name="login"),

    path('studreg',views.studreg,name="studreg"),
    path('studview',views.studview,name="studview"),
    path('approve/<int:sid>',views.one,name="one"),
    path('approve',views.approve,name="approve"),
    path('delete/<int:did>',views.delstudent,name="delstudent"),
    path('edit/<int:eid>',views.update_student,name="update_student"),
    path('studentprofile',views.studentprofile,name="studentprofile"),
    path('studviewteacher',views.studviewteacher,name="studviewteacher"),
    path('editstudprofile/<int:eid>',views.edit_studprofile,name="edit_studprofile"),

    path('teachreg',views.teachreg,name="teachreg"),
    path('teachview',views.teachview,name="teachview"),
    path('teachprofile',views.teachprofile,name="teachprofile"),
    path('del/<int:did>',views.delteacher,name="delteacher"),
    path('update/<int:eid>',views.update_teacher,name="update_teacher"),
    path('teachviewstudent',views.teachviewstudent,name="teachviewstudent"),
    path('editteachprofile/<int:eid>',views.edit_teachprofile,name="edit_teachprofile"),

    path('log',views.logout,name="logout"),
    path('',views.index,name="index"),






   




]