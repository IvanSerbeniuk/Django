
from django.contrib import admin
from django.urls import path, include
from django.conf import settings #var media and..
#it helps to make url path
from django.conf.urls.static import static #connection between base root and static files especially medias

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls')), #here we connect urls from store to project
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)      #MEDIA_URL this is why we imported settings we can connect to var we imported