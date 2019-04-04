from django.conf.urls import url, include
from rest_framework import routers
from mario.botApi import views
# from MarioSystem.api.views import CustomObtainAuthToken

router = routers.DefaultRouter()
router.register(r'bots', views.BotViewSet),

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'get_bot', views.get_bot, name='get_bot'),
    url(r'create_bot', views.create_bot, name='create_bot')
]
