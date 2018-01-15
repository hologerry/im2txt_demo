import uuid
from django.db import models


def scramble_uploaded_filename(instance, filename):
    extension = filename.split('.')[-1]
    random_name = uuid.uuid4()
    return "{}.{}".format(random_name, extension)


class UploadImage(models.Model):
    image = models.ImageField("Upload image", upload_to=scramble_uploaded_filename)
