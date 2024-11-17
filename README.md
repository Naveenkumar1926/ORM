# Ex02 Django ORM Web Application
## Date: 14/11/2024

## AIM
To develop a Django application to store and retrieve data from a bank loan database using Object Relational Mapping(ORM).

## ENTITY RELATIONSHIP DIAGRAM
![WhatsApp Image 2024-11-16 at 14 51 50_9dde0791](https://github.com/user-attachments/assets/c16436e4-8162-47c2-a74b-459cf969db22)



## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
models.py



from django.db import models
from django.contrib import admin
class Bank_loan (models.Model):
    customer_id=models.IntegerField(primary_key=True)
    customer_name=models.CharField(max_length=100)
    loan_amount=models.IntegerField()
    customer_age=models.IntegerField()
    email=models.EmailField()

class Bank_loanAdmin(admin.ModelAdmin):
    list_display=('customer_id','customer_name','loan_amount','customer_age','email')



    admin.py



    
from django.contrib import admin
from .models import Bank_loan,Bank_loanAdmin
admin.site.register(Bank_loan,Bank_loanAdmin)

## OUTPUT

![WhatsApp Image 2024-11-17 at 22 27 44_903c38f6](https://github.com/user-attachments/assets/aaf5cda7-21f7-41d2-9d34-3baf1d3a74b9)
![WhatsApp Image 2024-11-17 at 22 27 44_e0d268d4](https://github.com/user-attachments/assets/4337517b-879b-4369-b0ea-107f6c1a84b3)


## RESULT
Thus the program for creating a database using ORM hass been executed successfully
