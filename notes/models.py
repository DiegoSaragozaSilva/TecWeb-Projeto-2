from django.db import models
from django.contrib.postgres.fields import ArrayField

class Tag(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 200, blank = True)
    notes_ids = ArrayField(models.IntegerField(default = -1), size = 256)

    def __str__(self):
        return f"{self.id}. {self.name}"

class Note(models.Model):
    id = models.AutoField(primary_key = True)
    title = models.CharField(max_length = 200, blank = False)
    content = models.CharField(max_length = 1000, blank = False)
    tag = models.CharField(max_length = 200, blank = False)

    def __str__(self):
        return f"{self.id}. {self.title}"