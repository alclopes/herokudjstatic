from __future__ import absolute_import, unicode_literals
from django.contrib import admin
from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static

urlpatterns = [
    path('', include('mypage.urls', namespace='mypage')),
    path('admin/', admin.site.urls),
]

# ##########################Media/Static
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
