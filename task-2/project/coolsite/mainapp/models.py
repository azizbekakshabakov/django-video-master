from django.db import models
from django.core.validators import FileExtensionValidator

# class Women(models.Model):
#     title = models.CharField(max_length=255)
#     content = models.TextField(blank=True)
#     photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
#     time_create = models.DateTimeField(auto_now_add=True)
#     time_update = models.DateTimeField(auto_now=True)
#     is_published = models.BooleanField(default=True)

#     def __str__(self):
#         return self.title

class User(models.Model):
    login = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    icon = models.ImageField(upload_to='icons/')

class Video(models.Model):
    index = models.CharField(max_length=255)
    video = models.FileField(upload_to='videos/', null=True, validators=[FileExtensionValidator(allowed_extensions=['mov','avi','mp4','webm','mkv'])])
    preview = models.ImageField(upload_to='previews/')
    user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)

class Comment(models.Model):
    content = models.TextField()
    user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    video_id = models.ForeignKey(Video, on_delete=models.DO_NOTHING)

class Playlist(models.Model):
    name = models.CharField(max_length=255)
    user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)

class PlaylistContent(models.Model):
    url = models.CharField(max_length=255)
    playlist_id = models.ForeignKey(Playlist, on_delete=models.DO_NOTHING)