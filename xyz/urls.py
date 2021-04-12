from django.contrib import admin
from django.urls import path, include
import persons.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', persons.views.home, name="home"),
    path('ohLocal/', include('persons.urls') ),
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
