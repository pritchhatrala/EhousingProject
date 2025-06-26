from django.db import models

class signup(models.Model):
    Yourname = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    mobile = models.CharField(max_length=15)


class login(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=20)
    
   
class contect(models.Model):
    name = models.CharField(max_length=20)     
    email = models.EmailField()
    message = models.CharField(max_length=100)



class add_sellhouse(models.Model):
    name = models.CharField(max_length=255, default='Untitled') 
    address = models.CharField(max_length=255, default='Not provided')  # Set default value
    price = models.BigIntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='houses/', blank=True, null=True)

    def __str__(self):
        return self.name

class add_renthouse(models.Model):
    housename = models.CharField(max_length=20)     
    adress = models.CharField(max_length=50)
    Monthly_rent = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to="rent_images/")



class complaint(models.Model):
    name = models.CharField(max_length=20)     
    House_number = models.CharField(max_length=10)
    mobile = models.BigIntegerField()
    complain_detail = models.TextField()
    image = models.ImageField(blank=True, null=True, upload_to="complaints_image/")




