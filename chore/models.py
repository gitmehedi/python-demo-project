from django.db import models

class Chorelist(models.Model):
    name= models.CharField(max_length=100)
    due_date= models.DateTimeField()

    def __str__(self):
        return self.name;

class Chore(models.Model):
    chore_list = models.ForeignKey(Chorelist)
    name= models.CharField(max_length=100)
    due_date= models.DateTimeField()
    
    def __str__(self):
        return self.name;

class Category(models.Model):
    title = models.CharField(max_length=100)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.name;