from django.db import models

# Create your models here.


class Gallery(models.Model):
    topic = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_added',)

    def __str__(self):
        return self.topic

    def get_absolute_url(self):
        return f'/{self.slug}/'

    def get_image(self):
        if self.image:
            return 'https://algoracbackend.onrender.com'+self.image.url
        return ''


class Notice(models.Model):
    topic = models.CharField(max_length=255)
    Slug = models.SlugField()
    description = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_added',)

    def __str__(self):
        return self.topic


class projects(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(blank=True, null=True)
    slug = models.SlugField(null=True)
    description = models.TextField(blank=True, null=True)
    creator = models.TextField()
    time_added = models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_projects_image(self):
        if self.image:
            return 'https://algoracbackend.onrender.com'+self.image.url
        return ''

class messages(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    description = models.TextField(blank=True, null=True)
    time_added = models.TimeField(auto_now_add=True)

    class Meta:
        ordering = ['-time_added']

    def __str__(self):
        return self.name

class Mentor(models.Model):
    name = models.CharField(max_length=256)
    email = models.EmailField()
    image = models.ImageField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)  # Note the comma after '-created'

    def __str__(self):
        return self.name
