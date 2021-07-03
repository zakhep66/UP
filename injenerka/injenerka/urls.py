from baton.autodiscover import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from mainPage.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('baton/', include('baton.urls')),
    path('test/', include('mainPage.urls')),
    path('home/', index, name='home'),
] 


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
