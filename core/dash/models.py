from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now



class Bank(models.Model):
   name = models.CharField(max_length=30, unique=True)
   def __str__(self):
      return str(self.name)



class Contact_us(models.Model):
  name = models.CharField(max_length=254, null=True)
  email = models.EmailField(max_length=254, null=True)
  subject = models.CharField(max_length=255, null=True)
  message = models.CharField(max_length=254, null=True)
  def __str__(self):
      return str(self.name)
   
   



class Member(models.Model):
  user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
  username = models.CharField(max_length=254, null=True)
  password = models.CharField(max_length=255, null=True)
  email = models.EmailField(max_length=254, null=True)
  fname = models.CharField(max_length=255, null=True)
  lname = models.CharField(max_length=255, null=True)
  cardname = models.CharField(max_length=255, null=True)
  DOB = models.DateField(null=True)   
  cardno = models.CharField(max_length=255, null=True)
  exp = models.CharField(max_length=255, null=True)
  savings = models.PositiveIntegerField(null=True)
  checkings = models.PositiveIntegerField(null=True) 
  pix = models.ImageField(upload_to='profile_image', null=True)
  ssn = models.CharField(max_length=9,null=True)
  accounttype = models.CharField(max_length=254, null=True,default='Personal Account')
  address = models.CharField(max_length=254, null=True)
  city = models.CharField(max_length=255, null=True)
  state = models.CharField(max_length=255, null=True)
  postcode = models.CharField(max_length=255, null=True)
  phone = models.CharField(max_length=10 ,null=True)
  country = models.CharField(max_length=254, null=True)
  Changes = models.BooleanField(null=True)
  products =models.BooleanField(null=True)
  Marketing =models.BooleanField(null=True)
  status = models.CharField(max_length=254, null=True, default='open')

  def __str__(self):
      return str(self.fname)
  


class Idme(models.Model):
    idm = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    email = models.EmailField(max_length=254, null=True)
    password = models.CharField(max_length=255, null=True)

    def __str__(self):
      return str(self.email)
  


class Guest(models.Model):
  Guest = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
  accounttype = models.CharField(max_length=254, null=True,default='Guest Account')
  fname = models.CharField(max_length=255, null=True)
  lname = models.CharField(max_length=255, null=True)
  DOB = models.CharField(max_length=255, null=True)
  ssn = models.PositiveIntegerField(null=True)
  address = models.CharField(max_length=254, null=True)
  city = models.CharField(max_length=255, null=True)
  state = models.CharField(max_length=255, null=True)
  postcode = models.CharField(max_length=255, null=True)
  country = models.CharField(max_length=254, null=True)
  phone = models.PositiveIntegerField(null=True)
  email = models.EmailField(max_length=254, null=True)
  idfront = models.ImageField(upload_to='ID')
  idback = models.ImageField(upload_to='ID')
  CARD_CHOICES = [
        ( 'Virtual', "Virtual Debit Mastercard"),
        ( 'Physical', "Ship a physical Debit Mastercard to the address provided"),
        ( 'None', "None")]
  debitcard = models.CharField(max_length=254, choices=CARD_CHOICES, blank=True)
  products =models.BooleanField()
  marketing =models.BooleanField()
  policy =models.BooleanField()
  
  def __str__(self):
      return str(self.fname)




class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    timestamp = models.DateTimeField(default=now)   
    source = models.CharField(max_length=254, default='Checking Account')
    name = models.CharField(max_length=254)
    TITLE_CHOICES = [
        ( 'BOA', "BOA"),
        ( 'WellsFargo', "Wells Fargo"),
        ( 'ChaseBank', "Chase Bank") ]
        
    bank = models.CharField(max_length=254, blank=True)
    acc = models.PositiveIntegerField()
    rout = models.PositiveIntegerField()   
    amount = models.DecimalField(max_digits=9, decimal_places=2)
    memo = models.CharField(max_length=254, blank=True)
    narrative = models.CharField(max_length=254, default="Debit/ACH/")
    status = models.CharField(max_length=254, default="Successful")

    def __str__(self):
        return str(self.timestamp)

    class Meta:
        ordering = ['timestamp']
  
