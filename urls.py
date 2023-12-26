from django.urls import path
from stud import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('log',views.login1,name="login"),
    path('studreg',views.studreg,name="login"),
    path('teachreg',views.teachreg,name="teachreg")



]
