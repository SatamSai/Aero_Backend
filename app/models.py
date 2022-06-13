from django.utils.safestring import mark_safe
from django.db import models
# Create your models here.
class Event(models.Model):
    eventname=models.CharField(max_length=150)
    venue=models.CharField(max_length=150)
    speaker=models.CharField(max_length=200,default="")
    eventdate=models.DateField()
    eventdesc=models.TextField(max_length=1000,default="No Description")
    poster_img=models.ImageField(null=False,upload_to="")
    def __str__(self):
        return self.eventname

class EventImage(models.Model):
    event=models.ForeignKey(Event,on_delete=models.CASCADE,default=1)
    imgname=models.CharField(max_length=50,default="no name")
    img=models.ImageField(null=False,upload_to="")
    def __str__(self):
        return self.imgname
    def image_tag(self):
        if self.img:
            img_path="http://127.0.0.1:8000/images/"+str(self.img)
            return mark_safe('<img src="%s" style="height:45px;" />' % img_path)
        else:
            return 'No Image Found'
    image_tag.short_description = 'Image'

class Competition(models.Model):
    competitionName=models.CharField(max_length=150)
    competitionDesc=models.TextField(max_length=1000)
    achievements=models.CharField(max_length=150,blank=True)
    year=models.CharField(max_length=5,default="20")
    poster_img=models.ImageField(null=False,upload_to="")
    def __str__(self):
        return self.competitionName

class CompetitionImage(models.Model):
    event=models.ForeignKey(Competition,on_delete=models.CASCADE,default=1)
    imgname=models.CharField(max_length=50,default="no name")
    img=models.ImageField(null=False,upload_to="")
    def __str__(self):
        return self.imgname
    def image_tag(self):
        if self.img:
            img_path="http://127.0.0.1:8000/images/"+str(self.img)
            return mark_safe('<img src="%s" style="height:45px;" />' % img_path)
        else:
            return 'No Image Found'
    image_tag.short_description = 'Image'

class TeamMember(models.Model):
    membername=models.CharField(max_length=150)
    profileImg=models.ImageField(null=False,upload_to="")
    year=models.CharField(max_length=10)
    role=models.CharField(max_length=50)
    def __str__(self):
        return self.membername

class Post(models.Model):
    posturl=models.CharField(max_length=150)
    def __str__(self):
        return self.posturl