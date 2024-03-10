from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin, BaseUserManager



# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self,email,password):
        if not email:
            raise ValueError("Please insert user email")
        email = self.normalize_email(email)
        user = self.model(email=email)
        user.set_password(password)
        user.save(using=self.db)
        return user
    

    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self.db)
        return user

class User(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(max_length = 100, unique = True)
    is_staff = models.BooleanField(default = False)
    is_active = models.BooleanField(default = True)
    is_superuser = models.BooleanField(default = False)
    objects = UserManager()
    USERNAME_FIELD = "email"


    def __str__(self):
        return self.email
    


class Ingredient(models.Model):
    salad = models.IntegerField(default = 0)
    chesse = models.IntegerField(default = 0)  
    meat = models.IntegerField(default = 0)

    def __str__(self):
        return f" salad: {self.salad}, chesse: {self.chesse}, meat:{self.meat}"

class CustomerDetail(models.Model):
    deliveryAdress = models.TextField(blank = True)
    phone = models.CharField(max_length = 11, blank= True)
    paymentType = models.CharField(max_length =50, blank = True)

    def __str__(self):
        return f"Customer Details: {self.deliveryAdress} , Phone:{self.phone}"    
    
class Order(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    ingredients = models.OneToOneField(Ingredient, on_delete = models.CASCADE)
    customer = models.OneToOneField(CustomerDetail, on_delete = models.CASCADE)
    price = models.CharField(max_length=10,default= "0")
    orderTime = models.CharField(max_length=40,blank= True)

    def __str__(self):
        return f" Order: {self.user.email}"
    