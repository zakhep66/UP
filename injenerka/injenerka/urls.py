from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from mainPage import views

# from mainPage.views import customer_list, customer_detail

urlpatterns = [
    # path('baton/', include('baton.urls')),
    path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
    path('api/', include('mainPage.urls')),
    path('', views.index, name='home'),
    path('lending', views.lending, name='lending'),
    path('home', views.home, name='home'),

    # path('user-detail/<int:pk>', customer_detail),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
