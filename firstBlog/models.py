from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField

class Post(models.Model):
    title = models.CharField(max_length=56)
    title_tag = models.CharField(max_length=45,null=True, blank=True)
    title_subtitle = models.CharField(max_length=86, default="Default Subtitle")
    auther = models.ForeignKey(User , on_delete=models.CASCADE)
    body = RichTextField()
    date_time = models.DateTimeField( blank=True,auto_now=True) 
    image = models.ImageField(upload_to='img/',default="")  # ImageField for the image

    
    def __str__(self):
        return self.title + ' | '+ str(self.auther)
    
    
    def get_absolute_url(self):
        return reverse('articalDetailsView', args=(str(self.id)))
    
class TechPost(models.Model):
    title = models.CharField(max_length=56)
    title_tag = models.CharField(max_length=45,null=True, blank=True)
    auther = models.ForeignKey(User , on_delete=models.CASCADE)
    body = RichTextField()
    date_time = models.DateTimeField( blank=True,auto_now=True) 
    image = models.ImageField(upload_to='img/',default="")  # ImageField for the image

        
    def __str__(self):
        return self.title + ' | '+ str(self.auther)
        
        
    def get_absolute_url(self):
        return reverse('articalDetailsView', args=(str(self.id)))