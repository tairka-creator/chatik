from django.contrib.auth.models import User
from django.db import models
from django.db.models import DO_NOTHING


class Room(models.Model):
    name = models.CharField(max_length=1000)

    def __str__(self):
        return self.name


class Message(models.Model):
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=DO_NOTHING)
    room = models.ForeignKey(Room, on_delete=DO_NOTHING)

    def __str__(self):
        return self.value


def files_path(instance, filename):
    return "files/" + filename
class File_table(models.Model):
    message_id = models.ForeignKey(Message, on_delete=DO_NOTHING)
    files = models.FileField(upload_to=files_path, verbose_name="files")
    title = models.CharField(max_length=200, default="")

    def __str__(self):
        return self.title
