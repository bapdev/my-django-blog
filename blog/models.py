from django.db import models
from django.utils import timezone

''' Define Post Model it is an Object.
    models.Model means Post is a Django Model
    so Django knows that it should be saved in
    the database.
'''

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

''' Define the publish method. '''

def publish(self):
        self.published_date = timezone.now()
        self.save()

''' Return a text(string) with a Post title. '''

def __str__(self):
        return self.title
