from django.urls import path
from stud import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('log',views.login1,name="login"),

    path('studreg',views.studreg,name="studreg"),
    path('studview',views.studview,name="studview"),

    path('teachreg',views.teachreg,name="teachreg"),
    path('teachview',views.teachview,name="teachview"),

   




]
