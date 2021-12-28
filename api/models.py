from django.db import models
from django.conf import settings
from django.utils import timezone


User = settings.AUTH_USER_MODEL


class Post(models.Model):
    title_post = models.CharField(max_length=255)
    autor_post = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    abstract_post = models.TextField()
    content_post = models.TextField()
    image_post = models.ImageField(upload_to='media/%Y/%m/%d %H:%m:%s', blank=False, null=False)
    publicated = models.BooleanField(default=False)
    created_at = models.DateTimeField(timezone.now)
    updated_at = models.DateTimeField(timezone.now)

class Category(models.Model):
    category = models.CharField(max_length=50)
    post = models.ManyToManyField('Post', blank=False)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['category']

    def __str__(self):
        return self.category


