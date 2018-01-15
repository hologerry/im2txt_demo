from django.conf.urls import url, include
from rest_framework import routers
from api.viewsets import UploadImageViewSet

router = routers.DefaultRouter()
router.register('images', UploadImageViewSet, 'images')

urlpatterns = [
    url(r'^', include(router.urls))
]
