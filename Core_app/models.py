from django.db import models
from django.urls import reverse

# Create your models here.


class Blog(models.Model):
    blog_title = models.CharField(max_length=250)
    slug = models.SlugField(unique=True, max_length=200)
    description = models.TextField(blank=True, max_length=500)
    blog_image = models.ImageField(upload_to='media/blogs', blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.blog_title

    def get_url(self):
        return reverse('app_core:blog_details', args=[self.slug])


class Contact_Us(models.Model):
    message = models.TextField(max_length=500)
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    send_at = models.DateTimeField(auto_now_add=True)
    updated_send = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Contact Us From Contact Page'
        verbose_name_plural = 'Contact Us From Contact Page'
