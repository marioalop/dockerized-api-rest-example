"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from anniversaries.drf_urls import urlpatterns as rest_urls
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView
from django.conf.urls import handler404
from anniversaries.views import error404


handler404 = error404
descrip = "API de consulta de efemérides del día y del mes especificados como parámetros.<br><br>" \
          "Puede utilizar el query param day (formato YYYY-MM-DD) para elegir un dia en /efemerides/"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('openapi', get_schema_view(title="Efemerides Docs", description=descrip),
         name='openapi-schema'),
    path('docs/', TemplateView.as_view(template_name='swagger.html',
                                       extra_context={'schema_url':'openapi-schema'}), name='docs'),
] + rest_urls


