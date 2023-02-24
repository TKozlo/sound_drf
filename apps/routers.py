from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Audio library",
        default_version='v1',
        description="Пример аудио библиотеки на DRF. Можно сделать платформу для изучения иностранного языка",
        contact=openapi.Contact(url="https://www.twitter.com/"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('auth/', include('apps.oauth.urls')),
    path('audio/', include('apps.audio_lib.urls'))
]