from ast import Return
import email
from email import message
import pkgutil
from django.shortcuts import redirect, render
from . models import *
from random import randint

# Create your views here.
def IndexPage(request):
    return render(request,'app/index.html')

def CandidateIndexPAge(request):
    return render(request,"app/candindex.html")

def SignupPage(request):
   return render(request,'app/signup.html')



def RegisterUser(request):
    if request.method == 'POST':
        if request.POST['Role'] == 'Candidate':
            role = request.POST['Role']
            fname = request.POST['firstname']
            lname = request.POST['lastname']
            email = request.POST['email']
            password = request.POST['password']
            cpassword = request.POST['cpassword']
            
            user = UserMaster.objects.filter(email=email)
        
            if user:
                message = "user already Exist!!!"
                return render(request,"app/signup.html",{'msg':message})
            else:
                if password == cpassword:
                    otp = randint(100000,999999)
                    newuser = UserMaster.objects.create(role=role,otp=otp,email=email,password=password)
                    newcand = Candidate.objects.create(user_id=newuser,firstname=fname,lastname=lname)
                    return render(request,"app/otpverify.html",{'email': email})
                else:
                    message = "password and confirm password are not matched!!! "
                    return render(request,"app/signup.html",{'msg':message})

        else:
            if request.POST['Role'] =='Company':
                role = request.POST['Role']
                fname = request.POST['firstname']
                lname = request.POST['lastname']
                email = request.POST['email']
                password = request.POST['password']
                cpassword = request.POST['cpassword']
        
                user = UserMaster.objects.filter(email=email)
        
                if user:
                    message = "user already Exist!"
                    return render(request,"app/signup.html",{'msg':message})
                else:
                    if password == cpassword:
                        otp = randint(100000,999999)
                        newuserr = UserMaster.objects.create(role=role,otp=otp,email=email,password=password)
                        newcompany = Company.objects.create(user_id=newuserr,firstname=fname,lastname=lname)
                        return render(request,"app/otpverify.html",{'email':email})
        
                
def OTPPage(request):
    return render(request,'app/otpverify.html')

def OtpVerify(request):
    email = request.POST['email']
    otp = int(request.POST['otp'])
    
    user = UserMaster.objects.get(email=email)
    if user:
        if user.otp == otp:
            messages = "OTP Verify Succesfully !"
            return render (request,"app/login.html",{'msgs':messages})
        else:
            message = "Entered OTP is invalid, Try again! "
            return render(request,"app/otpverify.html",{'msg':message})
    else:
        return render(request,"app/signup.html")
    

def Loginpage (request):
    return render (request,"app/login.html")


def loginUser(request):
    if request.method == "POST":
        if request.POST['Role']=='Candidate':
            email = request.POST['email']
            password = request.POST['password']
            
            user = UserMaster.objects.filter(email=email).first()
            
            if (user):     
                if user.password == password and user.role == "Candidate":  
                    candi = Candidate.objects.get(user_id = user)
                    request.session["id"] = user.id
                    request.session['role'] = user.role
                    request.session['firstname'] = candi.firstname
                    request.session['lastname'] = candi.lastname
                    request.session['email'] = user.email
                    request.session['password']=user.password
                    return redirect('candindex')
                else:
                    message = "Entered Password is Invalid!"
                    return render(request,"app/login.html",{'msg':message})
                
            else:
                message = "User not exist, Enter correct Email!"   
                return render (request,"app/login.html",{'msg':message})                 

            
        else:            
            if request.POST['Role']=='Company':
                email = request.POST['email']
                password = request.POST['password']
                
                user = UserMaster.objects.filter(email=email).first()
            
                if (user):                            
                    if user.password == password and user.role == "Company":  
                        compa = Company.objects.get(user_id = user)
                        request.session["id"] = user.id
                        request.session['role'] = user.role
                        request.session['firstname'] = compa.firstname
                        request.session['lastname'] = compa.lastname
                        request.session['email'] = user.email
                        request.session['password'] = user.password
                        request.session['company_name'] = compa.company_name
                        return redirect('comindex')
                    else:
                        message = "Entered Password is Invalid!"
                        return render(request,"app/login.html",{'msg':message})
                    
                else:
                    message="User Not exist! Enter correct Email"
                    return render (request,"app/login.html",{'msg':message})  
                
                
def profilePage(request,id):
    user = UserMaster.objects.get(id=id)
    can = Candidate.objects.get(user_id=user)
    return render(request,"app/profile.html",{'user':user,'can':can} ) 


def UpdateProfile(request,pk): 
    user = UserMaster.objects.get(pk=pk)
    if user.role  == "Candidate":
        cand=Candidate.objects.get(user_id = user)
        cand.title = request.POST["title"]
        cand.middlename = request.POST['middlename']
        cand.linkden =  request.POST['linkden']
        cand.pincode =  request.POST['pincode']
        cand.qualification1 =  request.POST['qualification1']
        cand.degree1 =  request.POST['degree1']
        cand.college1 =  request.POST['college1']
        cand.CGPA1 =  request.POST['cgpa1']
        cand.datefrom1 =  request.POST['datefrom1']
        cand.dateto1 =  request.POST['dateto1']
        cand.qualification2 =  request.POST['qualification2']
        cand.degree2 =  request.POST['degree2']
        cand.college2 =  request.POST['college2']
        cand.CGPA2 =  request.POST['cgpa2']
        cand.datefrom2 =  request.POST['datefrom2']
        cand.dateto2 =  request.POST['dateto2']
        cand.qualification3 =  request.POST['qualification3']
        cand.degree3 =  request.POST['degree3']
        cand.college3 =  request.POST['college3']
        cand.CGPA3 =  request.POST['cgpa3']
        cand.datefrom3 =  request.POST['datefrom3']
        cand.dateto3 =  request.POST['dateto3']
        cand.companyname1 =  request.POST['companyname1']
        cand.jobposition1 =  request.POST['jobposition1']
        cand.c_city1 =  request.POST['c_city1']
        cand.cwh1 =  request.POST['cwh1']
        cand.date_from1 =  request.POST['date_from1']
        cand.date_to1 =  request.POST['date_to1']
        cand.addinfo1 =  request.POST['addinfo1']
        cand.companyname2 =  request.POST['companyname2']
        cand.jobposition2 =  request.POST['jobposition2']
        cand.c_city2 =  request.POST['c_city2']
        cand.cwh2 =  request.POST['cwh2']
        cand.date_from2 =  request.POST['date_from2']
        cand.date_to2 =  request.POST['date_to2']
        cand.addinfo2 =  request.POST['addinfo2']
        cand.companyname3 =  request.POST['companyname3']
        cand.jobposition3 =  request.POST['jobposition3']
        cand.c_city3 =  request.POST['c_city3']
        cand.cwh3 =  request.POST['cwh3']
        cand.date_from3 =  request.POST['date_from3']
        cand.date_to3 =  request.POST['date_to3']
        cand.addinfo3 =  request.POST['addinfo3']
        cand.skills =  request.POST['skills']
        cand.designation =  request.POST['designation']
        cand.dob =  request.POST['dob']
        cand.marital_status =  request.POST['marital_status']
        cand.city = request.POST["city"]
        cand.state = request.POST['state'] #First country variable is from database field and sec from html form
        cand.country = request.POST["country"]
        cand.experience = request.POST["experience"]
        cand.address = request.POST["address"]
        cand.contact = request.POST["contact"]
        cand.website = request.POST["website"]
        cand.current_ctc = request.POST["c_ctc"]
        cand.expected_ctc = request.POST["e_ctc"]
        cand.dob= request.POST["dob"]
        cand.gender = request.POST["gender"]
        cand.objective = request.POST["objective"]
        cand.profilepic = request.FILES["profilepic"]
        cand.upload_resume = request.FILES["upload_resume"]
        cand.save()
        url = f'/profile/{pk}'#formatting url -(profile- url name)
        return redirect(url)
    
def CandidateJobPostList(request):
    if 'email' in request.session and 'password' in request.session:
        all_job =  Jobdetails.objects.all
        return render(request,"app/job-list.html",{'all_job':all_job})
    else:
        return redirect('loginpage')

def ApplyPage(request,pk):
    user = request.session['id']
    if user:
        cand = Candidate.objects.get(user_id=user)
        job= Jobdetails.objects.get(id=pk)
        return render(request,'app/applypage.html',{'user':user,'cand':cand,'job':job})
    
    
def ApplyJob(request,pk):
    user = request.session['id']
    if user:
        can = Candidate.objects.get(user_id=user)
        job = Jobdetails.objects.get(id=pk)
        country = request.POST['country']
        jobname = request.POST['jobname']
        firstname = request.POST['firstname']
        middlename = request.POST['middlename']
        lastname = request.POST['lastname']
        marital_status = request.POST['marital_status']
        dob = request.POST['dob']    
        gender = request.POST['gender'] 
        city = request.POST['city'] 
        state = request.POST['state'] 
        phone = request.POST['contact'] 
        website = request.POST['website'] 
        address = request.POST['address'] 
        c_ctc = request.POST['c_ctc'] 
        e_ctc = request.POST['e_ctc'] 
        linkden = request.POST['linkden']
        qualification1 = request.POST['qualification1']
        degree1 = request.POST['degree1']
        college1 = request.POST['college1']
        cgpa1 = request.POST['cgpa1']
        datefrom1 = request.POST['datefrom1']
        dateto1 = request.POST['dateto1']
        qualification2 = request.POST['qualification1']
        degree2 = request.POST['degree1']
        college2 = request.POST['college1']
        cgpa2 = request.POST['cgpa1']
        datefrom2 = request.POST['datefrom1']
        dateto2 = request.POST['dateto2']
        qualification3 = request.POST['qualification1']
        degree3 = request.POST['degree1']
        college3 = request.POST['college1']
        cgpa3 = request.POST['cgpa1']
        datefrom3 = request.POST['datefrom1']
        dateto3 = request.POST['dateto3']
        experience = request.POST['experience']
        companyname1 = request.POST['companyname1']
        jobposition1 = request.POST['jobposition1']
        c_city1 = request.POST['c_city1']
        cwh1 = request.POST['cwh1']
        date_from1 = request.POST['date_from1']
        date_to1 = request.POST['date_to1']
        addinfo1 = request.POST['addinfo1']
        companyname2 = request.POST['companyname2']
        jobposition2 = request.POST['jobposition2']
        c_city2 = request.POST['c_city2']
        cwh2 = request.POST['cwh2']
        date_from2 = request.POST['date_from2']
        date_to2 = request.POST['date_to2']
        addinfo2 = request.POST['addinfo2']
        companyname3 = request.POST['companyname3']
        jobposition3 = request.POST['jobposition3']
        c_city3 = request.POST['c_city3']
        cwh3 = request.POST['cwh3']
        date_from3 = request.POST['date_from3']
        date_to3 = request.POST['date_to3']
        addinfo3 = request.POST['addinfo3']
        skills = request.POST['skills']
        resume = request.FILES['resume']
        
        #first candidate id mpodel field and second is form view.
        newjobapply = Jobapply.objects.create(candidate=can,job=job,firstname=firstname,lastname=lastname,dob=dob,city=city,
                                              state=state,phone=phone,website=website,address=address,c_ctc=c_ctc,e_ctc=e_ctc,
                                              country=country,jobtitle=jobname,middlename=middlename,marital_status=marital_status,linkden=linkden,
                                              qualification1=qualification1,degree1=degree1,college1=college1,CGPA1=cgpa1,gender=gender,
                                              datefrom1=datefrom1,dateto1=dateto1,qualification2=qualification2,
                                              degree2=degree2,college2=college2,CGPA2=cgpa2,datefrom2=datefrom2,dateto2=dateto2,
                                              qualification3=qualification3,degree3=degree3,college3=college3,CGPA3=cgpa3,
                                              datefrom3=datefrom3,dateto3=dateto3,experience=experience,
                                              companyname1=companyname1,jobposiion1=jobposition1,c_city1=c_city1,cwh1=cwh1,date_from1=date_from1,
                                              date_to1=date_to1,addinfo1=addinfo1,companyname2=companyname2,
                                              jobposiion2=jobposition2,c_city2=c_city2,cwh2=cwh2,date_from2=date_from2,
                                              date_to2=date_to2,addinfo2=addinfo2,companyname3=companyname3,jobposiion3=jobposition3,
                                              c_city3=c_city3,cwh3=cwh3,date_from3=date_from3,
                                              date_to3=date_to3,addinfo3=addinfo3,skills=skills,resume=resume)
        
        
        message = "Job applied Successfully !!!"
        
        return render(request,("app/applypage.html"),{'msg':message})


def CandidateProfile(request):
    if 'email' in request.session and 'password' in request.session:    
        user = request.session['id']
        if user:
            candi = Candidate.objects.get(user_id=user)
            return render (request,"app/candidates-profile.html",{'user':user ,'candi':candi})
        
    else:
        return redirect('loginpage')
    
    

def CandidateLogout(request):
    del request.session['email']
    del request.session['password']    
    return redirect('index')

def CompanyListingPage(request):
    if 'email' in request.session and 'password' in request.session:   
        all_comp  = Company.objects.all
        return render (request,'app/employers-list.html',{'all_comp':all_comp})
    else:
        return redirect('loginpage')

    
    ############################ Company Side ####################################

    
def CompanyIndexPage(request):
    if 'email' in request.session and 'password' in request.session:   
        return render(request,"app/company/index.html")
    else:
        return redirect('loginpage')


def CompanyProfilePage(request,pk):
    user = UserMaster.objects.get(pk=pk)
    comp = Company.objects.get(user_id = user)
    return render(request,"app/company/companyprofile.html",{'user':user,'comp':comp})


def CompanyProfileDetail(request,pk):
    user = UserMaster.objects.get(pk=pk)
    comp = Company.objects.get(user_id = user)
    message = "Profile Updated Successfully!"
    return render(request,"app/company-detail.html",{'user':user,'comp':comp,'msg':message})

def UpdateCompanyProfile(request,pk): 
    user = UserMaster.objects.get(pk=pk)
    if user.role  == "Company":
        compa = Company.objects.get(user_id=user)
        compa.company_name = request.POST["company_name"]
        compa.company_email = request.POST["company_email"]
        compa.employee = request.POST["employee"]
        compa.established_on = request.POST["established_on"]
        compa.average_ctc = request.POST["average_ctc"]
        compa.services = request.POST["services"]
        compa.city = request.POST["city"]
        compa.state = request.POST['state'] #First  variable is from database field and sec from html form
        compa.country = request.POST["country"]
        compa.address = request.POST["address"]
        compa.contact = request.POST["contact"]
        compa.website = request.POST["website"]
        # compa.linkden = request.POST["linkden"]
        compa.description = request.POST["description"]
        compa.logo_pic = request.FILES["logo_pic"]
        compa.save()
        url = f'/companyprofile/{pk}'#formatting url -(profile- url name)
        return redirect(url)


def JobPostPage(request,pk):
    user = UserMaster.objects.get(pk=pk)
    comp = Company.objects.get(user_id=user)
    return render(request,"app/company/jobdetails.html",{'user':user,'comp':comp})


def JobDetailSubmit(request):
    user = UserMaster.objects.get(id=request.session['id'])
    if user.role == "Company":
        comp = Company.objects.get(user_id = user)
        jobname = request.POST['jobname']
        companyname = request.POST['companyname']
        companyaddress= request.POST['companyaddress']
        companyemail= request.POST['companyemail']
        companycontact= request.POST['companycontact']
        companywebsite= request.POST['companywebsite']
        companydescription = request.POST['description']
        jobtype= request.POST['jobtype']
        jobcategory= request.POST['jobcategory']
        location= request.POST['location']
        jobdescription= request.POST['description']
        responsibilities= request.POST['responsibilities']
        skills = request.POST['skills']
        doca= request.POST['doca']
        qualification= request.POST['qualification']
        salarypackage= request.POST['salarypackage']
        experience= request.POST['experience']
        shift= request.POST['shift']
        gender= request.POST['gender']
        pics = request.FILES['imag']
        
        newjobpost = Jobdetails.objects.create(company_id=comp,jobname=jobname,companyaddress=companyaddress,companydescription=companydescription,companyname=companyname,companycontact=companycontact,
                                           companyemail=companyemail, skills=skills,companywebsite=companywebsite,jobtype=jobtype,jobcategory=jobcategory,location=location,
                                           jobdescription=jobdescription,responsibilities=responsibilities,doca=doca,qualification=qualification,salarypackage=salarypackage,
                                           experience=experience,shift=shift,gender=gender,Image=pics)   
         
        message = "Job Posted successfully!"  
        return render(request,"app/company/jobdetails.html",{'msgs':message})  
        
        
def JobPostList(request):
    if 'email' in request.session and 'password' in request.session:   
        all_job =  Jobdetails.objects.all
        return render(request,"app/company/jobpostlist.html",{'all_job':all_job})
    else:
        return redirect('loginpage')

def JobDetailsPage(request,pk):
    user = request.session['id']
    if user:
        cand = Candidate.objects.get(user_id=user)
        job= Jobdetails.objects.get(id=pk)
        
        return render (request,'app/job-details.html',{'user':user,'cand':cand ,'job':job} )

def CompanyLogout(request):
    del request.session['email']
    del request.session['password'] 
    return redirect('index')

def CandidateListing(request):
    if 'email' in request.session and 'password' in request.session:   
        all_candi = Candidate.objects.all
        return render(request,"app/candidates-listing.html",{'all_candi':all_candi})
    else:
        return redirect('loginpage')
        

def JobApplicantsList(request):
    if 'email' in request.session and 'password' in request.session:   
        all_jobapply = Jobapply.objects.all 
        return render(request,"app/company/jobapplylist.html",{'all_jobapply':all_jobapply})
    else:
        return redirect('loginpage')

# def CompanyIndexPage(request):
#     all_company = Company.objects.all
#     all_job = Jobapply.objects.all
#     return render (request,'app/company/index.html',{'all_company':all_company,'all_job':all_job})


######################################   Admin Side ######################################


def AdminLoginPage(request):
    return render (request,"app/admin/adminlogin.html")

def AdminLogin(request):
    if request.method == "POST":

        username = request.POST['username']
        password = request.POST['password']
        
        admin =Adminlogin.objects.get(username=username)
        
        if(admin):
            if admin.username == username and admin.password == password:
                request.session['username']= username
                request.session['password']= password
                return render (request,"app/admin/index.html")
            
        else:
            message="username or password is incorrect!"
            return render(request,"app/admin/login.html",{'msg':message})
    
        
        
def AdminLogout(request):
    del request.session['username']
    del request.session['password']
    return render (request,"app/admin/index.html")

def AdminCandidateList(request):
    if 'username' in request.session and 'password' in request.session:
        all_candidate = UserMaster.objects.filter(role='Candidate')
        return render(request,"app/admin/candidatelist.html",{'all_candidate':all_candidate,})
    else:
        return redirect('adminloginpage')

def AdminCompanyList(request):
    if 'username' in request.session and 'password' in request.session:
        all_company = UserMaster.objects.filter(role='Company')
        return render(request,"app/admin/companylist.html",{'all_company':all_company})
    else:
        return redirect('adminloginpage')

def UserDelete(request,pk):
    if 'username' in request.session and 'password' in request.session:
        user = UserMaster.objects.get(pk=pk)
        user.delete()
        return redirect('admincandlist')
    else:
        return redirect('adminloginpage')

def VerifyUserPage(request,pk):
    if 'username' in request.session and 'password' in request.session:
        user = UserMaster.objects.get(pk=pk)
        if user:
            return render (request,"app/admin/verify.html",{'candidate':user})
    else:
        return redirect('adminloginpage')
    
def VerifyUser(request,pk):
    user =UserMaster.objects.get(pk=pk)
    if user:
        user.is_verified = request.POST['ver']
        user.save()
        return redirect('admincandlist')
    
def CompanyDelete(request,pk):
    company = UserMaster.objects.get(pk=pk)
    company.delete()
    return redirect('admincomplist')

def VerifyCompanyPage(request,pk):
    company = UserMaster.objects.get(pk=pk)
    if company:
        return render (request,"app/admin/verify2.html",{'company':company})
    
def VerifyCompany(request,pk):
    company = UserMaster.objects.get(pk=pk)
    if company:
        company.is_verified = request.POST['verify']
        company.save()
        return redirect('admincomplist')
    

    ###### email subscription  ########
    
def EmailSubscription(request):
    s_email = request.POST['email']
    
    subscribe = Subscribtion.objects.create(s_email=s_email)


def AboutUs(request):
    return render (request,"app/about.html")   

    
    
