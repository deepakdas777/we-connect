from django.contrib.auth.models import Permission, User
from django.db import models
from django.utils import timezone


class Item(models.Model):
    user = models.ForeignKey('auth.User', blank=True, null=True)
    post = models.CharField(max_length=1000)
    image = models.FileField(blank=True, null=True)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approved_comments(self):
    	return self.comments.filter(approved_comment=True)
    def __str__(self):
        return self.item_name
class Comment(models.Model):
    item = models.ForeignKey('app.Item', related_name='comments')
    user = models.CharField(max_length=200, blank=True, null=True)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
class Likes(models.Model):
    item = models.ForeignKey('app.Item', related_name='likes')
    user = models.CharField(max_length=200, blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.user
class Unlike(models.Model):
    item = models.ForeignKey('app.Item', related_name='unlike')
    user = models.CharField(max_length=200, blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.user
