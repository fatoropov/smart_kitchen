from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/',
         admin.site.urls),
    path('account/',
         include('account.urls')),
    path('products/',
         include('products.urls', namespace='products')),
    path('cooking/',
         include('cooking.urls')),
    path('social-auth/',
         include('social_django.urls', namespace='social')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
