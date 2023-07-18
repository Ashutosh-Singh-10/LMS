
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',include("userLogin.urls")),
    path('profile/',include("userProfile.urls")), 
    path('exam/',include("exam.urls")), 
    path('course/',include("course.urls")), 
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT )
