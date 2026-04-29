from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phonenumber=models.CharField(max_length=12)
    description=models.TextField()

    def __str__(self):
        return self.email            

class Enrollment(models.Model):
   fullname = models.CharField(max_length=50)
   email = models.EmailField()
   gender=models.CharField(max_length=10)
   phonenumber=models.CharField(max_length=12)
   dob=models.DateField()
   selected_plan=models.CharField(max_length=100)
   selected_trainer=models.CharField(max_length=50)
   address=models.TextField()
   paymentStatus=models.CharField(max_length=20, blank=True, null=True)
   amount_paid=models.IntegerField(blank=True,null=True)
   duedate=models.DateField(blank=True, null=True)  
   timestamp=models.DateTimeField(auto_now_add=True)

   def __str__(self):   
       return self.fullname
   
class Trainer(models.Model):
    name = models.CharField(max_length=30)
    gender=models.CharField(max_length=10)
    phone=models.CharField(max_length=12)
    salary=models.IntegerField(max_length=20)
    timestamp=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    
class Membership(models.Model):
    plan = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return self.plan
    
class Gallery(models.Model):
    title= models.CharField(max_length=100)
    image = models.ImageField(upload_to='gallery')
    timestamp=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title  # Return the title of the gallery item
    
class Attendence(models.Model):
    selectdate=models.DateField(auto_now_add=True)
    phonenumber=models.CharField(max_length=12)
    login=models.CharField(max_length=200)
    logout=models.CharField(max_length=200)
    selectworkout=models.CharField(max_length=100)
    trainedby=models.CharField(max_length=50)

    def __str__(self):
        return self.phonenumber