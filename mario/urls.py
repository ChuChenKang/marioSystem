from django.conf.urls import url
from django.contrib import admin
from rest_framework_swagger.views import get_swagger_view
from django.urls import path, include

schema_view = get_swagger_view(title='Mario Swagger API')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', schema_view),
    url(r'^account/', include('mario.accountApi.urls')),
    url(r'^bot/', include('mario.botApi.urls')),
    url(r'^intent/', include('mario.intentApi.urls')),
]
