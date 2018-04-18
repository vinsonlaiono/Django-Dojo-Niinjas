from django.db import models

# Create your models here.
class Dojo(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    desc = models.CharField(max_length=600)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    # def __repr__(self):
        # return "<Blog object: {} {} {}>".format(self.name, self.city, self.state)

class Ninja(models.Model):
    dojo = models.ForeignKey(Dojo, related_name = "ninjas")
    first_name = models.CharField(max_length=255)
    last_name = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    # def __repr__(self):
        # return "<Blog object: {} {} {}>".format(self.first_name, self.last_name)