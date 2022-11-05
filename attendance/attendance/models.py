from distutils.command.upload import upload
from email.policy import default
from django.db import models


# Create your models here.
class college(models.Model):
    username  = models.CharField( max_length=50)
    password = models.CharField( max_length=20)
    name=models.TextField()
    logo = models.ImageField( upload_to="pics")
    


class cse1(models.Model):
    name = models.TextField()
    reg = models.TextField()
    s_mobile = models.IntegerField(20)
    p_mobile = models.IntegerField(20)
    attendance = models.BooleanField(default=False)

class cse2(models.Model):
    name = models.TextField()
    reg = models.TextField()
    s_mobile = models.IntegerField(20)
    p_mobile = models.IntegerField(20)
    attendance = models.BooleanField(default=False)

class cse3(models.Model):
    name = models.TextField()
    reg = models.TextField()
    s_mobile = models.IntegerField(20)
    p_mobile = models.IntegerField(20)
    attendance = models.BooleanField(default=False)
    

class cse4(models.Model):
    name = models.TextField()
    reg = models.TextField()
    s_mobile = models.IntegerField(20)
    p_mobile = models.IntegerField(20)
    attendance = models.BooleanField(default=False)

class it1(models.Model):
    name = models.TextField()
    reg = models.TextField()
    s_mobile = models.IntegerField(20)
    p_mobile = models.IntegerField(20)
    attendance = models.BooleanField(default=False)

class it2(models.Model):
    name = models.TextField()
    reg = models.TextField()
    s_mobile = models.IntegerField(20)
    p_mobile = models.IntegerField(20)
    attendance = models.BooleanField(default=False)

class it3(models.Model):
    name = models.TextField()
    reg = models.TextField()
    s_mobile = models.IntegerField(20)
    p_mobile = models.IntegerField(20)
    attendance = models.BooleanField(default=False)

class it4(models.Model):
    name = models.TextField()
    reg = models.TextField()
    s_mobile = models.IntegerField(20)
    p_mobile = models.IntegerField(20)
    attendance = models.BooleanField(default=False)

class ece1(models.Model):
    name = models.TextField()
    reg = models.TextField()
    s_mobile = models.IntegerField(20)
    p_mobile = models.IntegerField(20)
    attendance = models.BooleanField(default=False)

class ece2(models.Model):
    name = models.TextField()
    reg = models.TextField()
    s_mobile = models.IntegerField(20)
    p_mobile = models.IntegerField(20)
    attendance = models.BooleanField(default=False)

class ece3(models.Model):
    name = models.TextField()
    reg = models.TextField()
    s_mobile = models.IntegerField(20)
    p_mobile = models.IntegerField(20)
    attendance = models.BooleanField(default=False)

class ece4(models.Model):
    name = models.TextField()
    reg = models.TextField()
    s_mobile = models.IntegerField(20)
    p_mobile = models.IntegerField(20)
    attendance = models.BooleanField(default=False)

class eee1(models.Model):
    name = models.TextField()
    reg = models.TextField()
    s_mobile = models.IntegerField(20)
    p_mobile = models.IntegerField(20)
    attendance = models.BooleanField(default=False)

class eee2(models.Model):
    name = models.TextField()
    reg = models.TextField()
    s_mobile = models.IntegerField(20)
    p_mobile = models.IntegerField(20)
    attendance = models.BooleanField(default=False)

class eee3(models.Model):
    name = models.TextField()
    reg = models.TextField()
    s_mobile = models.IntegerField(20)
    p_mobile = models.IntegerField(20)
    attendance = models.BooleanField(default=False)

class eee4(models.Model):
    name = models.TextField()
    reg = models.TextField()
    s_mobile = models.IntegerField(20)
    p_mobile = models.IntegerField(20)
    attendance = models.BooleanField(default=False)

class civil1(models.Model):
    name = models.TextField()
    reg = models.TextField()
    s_mobile = models.IntegerField(20)
    p_mobile = models.IntegerField(20)
    attendance = models.BooleanField(default=False)

class civil2(models.Model):
    name = models.TextField()
    reg = models.TextField()
    s_mobile = models.IntegerField(20)
    p_mobile = models.IntegerField(20)
    attendance = models.BooleanField(default=False)

class civil3(models.Model):
    name = models.TextField()
    reg = models.TextField()
    s_mobile = models.IntegerField(20)
    p_mobile = models.IntegerField(20)
    attendance = models.BooleanField(default=False)

class civil4(models.Model):
    name = models.TextField()
    reg = models.TextField()
    s_mobile = models.IntegerField(20)
    p_mobile = models.IntegerField(20)
    attendance = models.BooleanField(default=False)

class mech1(models.Model):
    name = models.TextField()
    reg = models.TextField()
    s_mobile = models.IntegerField(20)
    p_mobile = models.IntegerField(20)
    attendance = models.BooleanField(default=False)

class mech2(models.Model):
    name = models.TextField()
    reg = models.TextField()
    s_mobile = models.IntegerField(20)
    p_mobile = models.IntegerField(20)
    attendance = models.BooleanField(default=False)

class mech3(models.Model):
    name = models.TextField()
    reg = models.TextField()
    s_mobile = models.IntegerField(20)
    p_mobile = models.IntegerField(20)
    attendance = models.BooleanField(default=False)

class mech4(models.Model):
    name = models.TextField()
    reg = models.TextField()
    s_mobile = models.IntegerField(20)
    p_mobile = models.IntegerField(20)
    attendance = models.BooleanField(default=False)

class Staff(models.Model):
    staffName=models.TextField(max_length=50)
    staffDep=models.TextField(max_length=40)
    staffCollege = models.TextField()
    staffPosition=models.TextField(max_length=20)
    staffUsername=models.TextField(max_length=20)
    staffPassword=models.TextField(max_length=20)

