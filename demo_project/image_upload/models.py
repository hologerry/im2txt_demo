import uuid
import os
from django.db import models

from PIL import Image
from django.conf import settings

from im2txt.generate_captions import generate_captions


def scramble_uploaded_filename(instance, filename):
    extension = filename.split('.')[-1]
    random_name = filename.split('.')[0]
    return "{}.{}".format(random_name, extension)


# creates a thumbnail of an existing image
def create_thumbnail(input_image, thumbnail_size=(256, 256)):
    # make sure an image has been set
    if not input_image or input_image == "":
        return

    # open image
    image = Image.open(input_image)

    # use PILs thumbnail method; use anti aliasing to make the scaled picture look good
    image.thumbnail(thumbnail_size, Image.ANTIALIAS)

    # parse the filename and scramble it
    filename = scramble_uploaded_filename(None, os.path.basename(input_image.name))
    arrdata = filename.split(".")
    # extension is in the last element, pop it
    extension = arrdata.pop()
    basename = "".join(arrdata)
    # add _thumb to the filename
    new_filename = basename + "_thumb." + extension

    # save the image in MEDIA_ROOT and return the filename
    image.save(os.path.join(settings.MEDIA_ROOT, new_filename))

    return new_filename


class UploadedImage(models.Model):
    title = models.CharField("Title of the uploaded image", max_length=255, default="Picture")
    image = models.ImageField("Upload image", upload_to=scramble_uploaded_filename)
    thumbnail = models.ImageField("Thumbnail of uploaded image", blank=True)
    caption1 = models.CharField("Caption 0:", default="", max_length=512)
    caption2 = models.CharField("Caption 1:", default="", max_length=512)
    caption3 = models.CharField("Caption 2:", default="", max_length=512)

    def __str__(self):
        return self.title

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        # generate and set thumbnail or none
        self.thumbnail = create_thumbnail(self.image)
        super(UploadedImage, self).save(force_update=force_update)
        
        captions = generate_captions(self.image.name)

        self.caption1, self.caption2, self.caption3 = captions

        print(self.caption1)

        super(UploadedImage, self).save(force_update=force_update)