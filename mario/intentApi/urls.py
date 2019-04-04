from django.conf.urls import url, include
from rest_framework import routers
from mario.intentApi import views
# from MarioSystem.api.views import CustomObtainAuthToken

router = routers.DefaultRouter()
router.register(r'intentCategory', views.IntentCategoryViewSet)
router.register(r'intent', views.IntentViewSet)
router.register(r'intentAnswer', views.IntentAnswerViewSet)
router.register(r'trainingData', views.TrainingDataViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'create_intentCategory', views.create_intentCategory, name='create_intentCategory'),
    url(r'get_allIntentCategory', views.get_allIntentCategory, name='get_allIntentCategory')
]