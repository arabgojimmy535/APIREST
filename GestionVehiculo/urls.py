
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from Vehiculos.api import RegisterAPI,LoginAPI
from knox import views as knox_views




schema_view = get_schema_view(
   openapi.Info(
      title="Gestion vehiculos API",
      default_version='v1',
      description="Gestion Vehiculos",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="arangojimmy535@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Vehiculos.urls'), name= 'api'),
    path('api/registrar/', RegisterAPI.as_view(),name= 'registrar'),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('', include('rest_framework.urls')),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redocs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
if settings.DEBUG :
    urlpatterns+=static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT )
    urlpatterns+=static(settings.STATIC_URL , document_root = settings.STATIC_ROOT )