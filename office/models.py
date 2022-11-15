from django.db import models

# Create your models here.




class company(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)

class Employee(models.Model):
    name= models.CharField(max_length=100)
    designation = models.CharField(max_length=200,null=True,blank=True)
    company =models.ForeignKey(company,on_delete=models.CASCADE,null=True,blank=True)
    

    def __str__(self):
        return self.name

class OfficeResource(models.Model):

    name = models.CharField(max_length=100)
    employee = models.ManyToManyField(Employee)
    office = models.ManyToManyField(company)
    reasontobuy =  models.CharField(max_length=200,null=True,blank=True)
    issuedate = models.DateField(auto_now_add=True,null=True,blank=True)
    returndate = models.CharField(max_length=200,null=True,blank=True)
    
    def __str__(self):
        return self.name