from django.db import models

class books(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField( max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class authors(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    update = models.ManyToManyField(books, related_name="author")
    notes = models.CharField(max_length = 255, null = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    



