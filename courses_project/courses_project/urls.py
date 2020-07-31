from django.contrib import admin
from django.urls import path,include
from django.conf import settings #
from django.conf.urls.static import static # Both hash tag comment are used to see the images through the link.

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('courses.urls')),
    path('courses/', include('courses.urls')),
]
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
