from django.contrib import admin
from django.urls import path
from Home import views
from django.conf.urls.static import static
from django.conf import settings
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name = "index"),
    path('login', views.login, name="login"),
    path('adminpage', views.adminpage, name="adminpage"),
    path('createEvent', views.createEvent, name='createEvent'),
    path("logout", views.logout, name="logout"),
    path("views", views.views, name="views")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)