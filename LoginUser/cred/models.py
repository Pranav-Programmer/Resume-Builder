from django.db import models

# Create your models here.
class intro(models.Model):
    rollno=models.CharField(primary_key=True,max_length=122)
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    number=models.CharField(max_length=122)
    linkd=models.CharField(max_length=122)
    github=models.CharField(max_length=122)
    university=models.CharField(max_length=122)
    degree=models.CharField(max_length=122)
    #year=models.DecimalField(max_digits=4,decimal_places=0)
    branch=models.CharField(max_length=122)
    cg=models.DecimalField(max_digits=3,decimal_places=2)
    school=models.CharField(max_length=122)
    percentage=models.DecimalField(max_digits=5,decimal_places=2)
    
    def __str__(self):
        return self.rollno
    