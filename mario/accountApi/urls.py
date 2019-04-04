from django.conf.urls import url, include
from rest_framework import routers
from mario.accountApi import views
# from MarioSystem.api.views import CustomObtainAuthToken

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]