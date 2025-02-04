from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from config import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('rest_authtoken.urls')),
    path('users/', include('app_users.urls')),
    path('posts/', include('app_posts.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
