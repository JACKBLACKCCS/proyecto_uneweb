"""
URL configuration for marketplace project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# marketplace/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.urls import re_path



urlpatterns = [
    path('admin/', admin.site.urls),
    # URLs DE CORE
    path('', include('item.urls')),
    path('cart/', include('cart.urls')),
    path('accounts/', include('accounts.urls')),
    # path('conversation/', include('conversation.urls')),  # Comentado temporalmente
]


# ✅ SERVIR ARCHIVOS MEDIA EN PRODUCCIÓN
urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT,
    }),
]

# IMPORTANTE: Servir archivos media en AMBOS entornos (desarrollo y producción)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Servir archivos static en desarrollo (en producción los sirve WhiteNoise)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



