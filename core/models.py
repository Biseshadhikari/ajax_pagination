from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    



class Items(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null = True,blank = True,related_name="category")
    title = models.CharField(max_length=400)
    description = models.CharField(max_length=400)

    def __str__(self):
        return self.title