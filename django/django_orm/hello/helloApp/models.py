from django.db import models

class User(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __repr__(self):
        return f"<User object: {self.firstname} {self.lastname}({self.id})>"






class Post(models.Model):
    content = models.TextField()
    # uploader = models.CharField(user, related_name="posts_uploaded", on_delete=models.CASCADE)
    # likes =
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        