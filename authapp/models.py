from django.db import models

# Create your models here.
#this file we create databse tables
class Contact(models.Model):
    name=models.CharField(max_length=25)
    email=models.EmailField()
    phonenumber=models.CharField(max_length=25)
    description=models.TextField()

    def __str__(self):
        return self.email
    
class Enrollment(models.Model):
    Fullname = models.CharField(max_length=25,null=False, default='Fullname')  # Provide a default for Fullname
    Email = models.EmailField()
    Gender = models.CharField(
        max_length=15,
        choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')],
        default='M'  # Default for Gender
    )
    Phone = models.CharField(max_length=12, default='0000000000')  # Default for Phone
    DOB = models.CharField(max_length=12)
    SelectMembershipplan = models.CharField(max_length=200)
    SelectTrainer = models.CharField(max_length=25)
    Reference = models.CharField(max_length=25)
    Address = models.CharField(max_length=25)
    PymentStatus=models.CharField(max_length=55,blank=True,null=True)
    price=models.IntegerField(max_length=55,blank=True, null=True)
    # Price = models.IntegerField()  # Remove max_length
    DueDate=models.DateTimeField(blank=True,null=True)
    timestamp = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.Fullname
    
class Trainer(models.Model):
    name = models.CharField(max_length=50)
    Gender = models.CharField(
        max_length=15,
        choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')],
        default='M'
    )
    Phone = models.CharField(max_length=50, default='0000000000')  # Add default value
    salary = models.IntegerField()
    timestamp = models.DateTimeField(auto_now=True, blank=True)
    def __str__(self):
        return self.name
     
class MembershipPlan(models.Model):
    plan=models.CharField(max_length=125) 
    price=models.IntegerField()  
    def __str__(self):
        return f"Plan {self.plan} - {self.price} USD"
    

class Gallery(models.Model):
    title=models.CharField(max_length=50)
    img=models.ImageField(upload_to='gallery')
    timestamp = models.DateTimeField(auto_now=True, blank=True)    
    def __int__(self):
        return self.id
    
 
     
class Attendance(models.Model):
    Selectdate=models.DateField(auto_now_add=True)
    phonenumber = models.CharField(max_length=15, null=False, default='0000000000')
    Login=models.CharField(max_length=200)
    Logout=models.CharField(max_length=200)
    SelectWorkout=models.CharField(max_length=200)
    TrainedBy=models.CharField(max_length=200)

    def __int__ (self):
        return self.id



     