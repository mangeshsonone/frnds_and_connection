from django.db import models
from django.contrib.auth.models import User


class siteuser(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile=models.ImageField(default='default.jpg',upload_to='myprofile')
    newname=models.CharField(max_length=100)
    follow=models.ManyToManyField(User,related_name='follow')
    following=models.ManyToManyField(User,related_name='following')
    

class photopost(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    photo=models.ImageField(default='default.jpg',upload_to='myphotos')
    # video=models.FileField(default='default.mp4',upload_to='video/%y')
    # anewname=models.CharField(max_length=100)
    def __str__(self):
        return str(self.photo)
    
# class follows(models.Model):
#     follow=models.ManyToManyField(User)
#     helmet=models.OneToOneField(User,on_delete=models.CASCADE)
    # pass

class newcomentss(models.Model):
    myuser=models.ForeignKey(photopost, on_delete=models.CASCADE)
    coment=models.TextField()

class getcoment(models.Model):
    name=models.CharField(max_length=100)




    


# class entropy(models.Model):
#     rmssd=models.FloatField()
#     sd1=models.FloatField()
#     sd2=models.FloatField()
#     s=models.FloatField()
#     sd1sd2=models.FloatField()
