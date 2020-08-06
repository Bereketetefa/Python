from django.db import models

class dojos(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __unicode__(self):
        return "id : " + str(self.id) + ", name : " + self.name + ", city : " + self.city + ", state : " + self.state



class ninja(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    dojos = models.ForeignKey(dojos, related_name = "dojos", on_delete=models.CASCADE, null = True)
    desc = models.TextField( null = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    
    def __unicode__(self):
        return "id : " + str(self.id) + ", first_name : " + self.first_name + ", last_name : " + self.last_name + ", dojo : " + str(self.dojo.name)