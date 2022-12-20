from django.db import models
from django.contrib.auth.models import User
from PIL import Image
import os

COURSE = (
    ('1','1'),  
    ('2','2'),
    ('3','3'),
    ('4','4'),
    ('5','5'),
    ('6','6'),
)

#users
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    bio = models.TextField()

    def __str__(self):
        return self.user.username

    # resizing images
    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.avatar.path)

        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.avatar.path)

#book
def file_path(instance, filename):
    path = 'documents'
    format = 'uploaded-' + filename
    return os.path.join(path, format)

class AllBooksModel(models.Model):
    name_of_book = models.CharField(max_length=30)
    description_of_book = models.TextField()
    image_of_book = models.ImageField(upload_to='')
    author_of_book = models.CharField(max_length=50)
    short_description_of_book = models.TextField(max_length=100)
    course = models.CharField(choices=COURSE, max_length=100)
    download = models.FileField(upload_to=file_path ,blank=True, null=True, help_text='download only PDF')

    def __str__(self):
        return self.name_of_book


class Model_notes_of_user(models.Model):
    title_note = models.CharField(max_length=200)
    text_note = models.TextField()
    date_note = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title_note


class Model_footer(models.Model):
    locations = models.CharField(max_length=500)
    sponsors = models.CharField(max_length=500)
    friends = models.CharField(max_length=500)
    authors = models.CharField(max_length=500)
    
    
class PersonModal(models.Model):
    name = models.CharField(max_length=150)
    text = models.TextField()
    image = models.ImageField(upload_to='')
    