from rest_framework import viewsets
from .serializers import UploadImageSerializer
from image_upload.models import UploadImage


class UploadImageViewSet(viewsets.ModelViewSet):
    queryset = UploadImage.objects.all()
    serializer_class = UploadImageSerializer
