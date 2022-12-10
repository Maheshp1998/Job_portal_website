from django.contrib import admin

# Register your models here.
from django.contrib import admin
from . models import *

# Register your models here.

class UserMasteradmin(admin.ModelAdmin):
    list_display = ('email', 'role','otp','password')#this fields will show on django admin interface
    
class Candidateadmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname' ,'profilepic',)
    
class Companyadmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname' ,'company_name','is_verified')
    
class Jobdatailsadmin(admin.ModelAdmin):
    list_display = ('jobname','companyname','doca','salarypackage',)
    
class Jobapplyadmin(admin.ModelAdmin):
    list_display = ('firstname','lastname','jobtitle','city','e_ctc')
    
class Adminloginadmin(admin.ModelAdmin):
    list_display = ('username',)
    
    
    
admin.site.register(UserMaster,UserMasteradmin)
admin.site.register(Candidate,Candidateadmin)
admin.site.register(Company,Companyadmin)
admin.site.register(Jobdetails,Jobdatailsadmin)
admin.site.register(Jobapply,Jobapplyadmin)
admin.site.register(Adminlogin,Adminloginadmin)