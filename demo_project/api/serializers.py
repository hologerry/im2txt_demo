from rest_framework import serializers
from image_upload.models import UploadImage


class UploadImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadImage
        fields = ('pk', 'image')
