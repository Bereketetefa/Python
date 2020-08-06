from django.db import models


class ShowManager(models.Manager):
    def fanValidator(self, postData):
        errors = {}
        if len(postData['name'])<2:
            errors['firstNameRequired'] = "Title is required."
        if len(postData['network'])<3:
            errors['networkNameRequired'] = "Network is required."
        if len(postData['release']) == 0:
            errors['releaseNameRequired'] = "Date is required."
        if len(postData['description'])<10:
            errors['descriptionNameRequired'] = "Description is required."
        return errors

    def editValidator(self, postData):
        errors = {}
        if len(postData['nombre'])<2:
            errors['firstNameRequired'] = "Title is required."
        if len(postData['net'])<3:
            errors['networkNameRequired'] = "Network is required so write it out bruvvvv."
        if len(postData['rel']) == 0:
            errors['releaseNameRequired'] = "Date is required."
        if len(postData['description'])<10:
            errors['descriptionNameRequired'] = "Description is required."
        return errors


class Show(models.Model):
    title = models.CharField(max_length=225)
    Network = models.CharField(max_length=225)
    Release = models.DateField(max_length=225)
    desc = models.TextField(max_length=225)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()
# class Author(models.Model):
#     first_name = models.CharField(max_length = 255)
#     last_name = models.CharField(max_length = 255)
#     update = models.ManyToManyField(Book, related_name="author")
#     notes = models.CharField(max_length = 255, null = True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)    