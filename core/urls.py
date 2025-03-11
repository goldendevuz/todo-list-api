from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import (
    SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
)

from apps.shared.views import test

urlpatterns = [
    path('admin/', admin.site.urls),
]

spectacular_urls = [
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), 
        name='swagger-ui'
    ),
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]

api_urls = [
    path('todos/', include('apps.todo.urls')),
    path('test-login', test, name='test'),
    path('api-auth/', include('rest_framework.urls')),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
]

urlpatterns += api_urls
urlpatterns += spectacular_urls