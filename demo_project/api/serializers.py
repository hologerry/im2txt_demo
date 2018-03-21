from rest_framework import serializers
from image_upload.models import UploadedImage


class UploadImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadedImage
        fields = ('pk', 'image', 'thumbnail', 'title', 'caption1', 'caption2', 'caption3',)
        read_only_fields = ('thumbnail', 'caption1', 'caption2', 'caption3',)

