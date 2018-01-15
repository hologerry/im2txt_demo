from rest_framework import viewsets
from .serializers import UploadImageSerializer
from image_upload.models import UploadedImage


class UploadImageViewSet(viewsets.ModelViewSet):
    queryset = UploadedImage.objects.all()
    serializer_class = UploadImageSerializer
