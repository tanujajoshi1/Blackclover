from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
      
      path("",views.index,name="index"),
      path("login",views.login_view,name='login'),
      path('register',views.register,name="register"),
      path("logout",views.logout_view,name="logout"),
      path("getstarted/<str:username>/",views.getstarted,name="getstarted"),
      path("learn",views.learn,name='learn'),
      path("photo_list/",views.photo_list,name="photo_list")

]

if settings.DEBUG:
	urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

