from rest_framework import serializers
from image_upload.models import UploadedImage


class UploadImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadedImage
        fields = ('pk', 'image', 'thumbnail', 'title', 'captions',)
        read_only_fields = ('thumbnail',)

