"""api_tramite URL Configuration

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
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
# from django.conf.urls import include, url # For django versions before 2.0

from rest_framework import permissions
from rest_framework.schemas import get_schema_view
from rest_framework.renderers import CoreJSONRenderer
from rest_framework.documentation import include_docs_urls
from rest_framework_swagger.views import get_swagger_view
from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer

from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from procedure_resource import urls as procedure_urls

swagger_view = get_swagger_view(title='Cobranza Api')
# schema_view = get_schema_view(title='Cobranza Api', renderer_classes=[OpenAPIRenderer, SwaggerUIRenderer])
schema_view = get_schema_view(title='Cobranza Api', renderer_classes=[CoreJSONRenderer])

from drf_yasg.views import get_schema_view as yags_get_schema_view
from drf_yasg import openapi

yags_schema_view = yags_get_schema_view(
    openapi.Info(
        title='Concordia Api',
        default_version='v1',
        description='',
        terms_of_service='www.google.com/policies/terms',
        contact=openapi.Contact(email='rodriguezmador90@gmail.com'),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    url(r'api/v1/json', schema_view, name="docs"),
    url(r'api/v1/doc', swagger_view),
    # url(r'api-doc', include('rest_framework_swagger.urls')),
    url(r'^swagger(?P<format>\.json|.yaml)$', yags_schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger$', yags_schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc$', yags_schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-rest-auth/', include('rest_auth.urls'), name='rest_auth'),
    path(r'api-token-auth/', obtain_jwt_token),
    path(r'api-token-refresh/', refresh_jwt_token),
    path('', include(procedure_urls)),
]

from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_jwt.views import verify_jwt_token

urlpatterns += [
    url(r'^auth-jwt/', obtain_jwt_token),
    url(r'^auth-jwt-refresh/', refresh_jwt_token),
    url(r'^auth-jwt-verify/', verify_jwt_token),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
                      path('__debug__/', include(debug_toolbar.urls)),
                      # For django versions before 2.0:
                      # url(r'^__debug__/', include(debug_toolbar.urls)),
                  ] + urlpatterns
