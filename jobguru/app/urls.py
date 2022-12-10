from pathlib import Path
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.IndexPage , name='index'),
    
    path('candindex/', views.CandidateIndexPAge ,name="candindex"),
    
    path('signup/',views.SignupPage , name='signup'),
    
    path('register/',views.RegisterUser , name='register'),
    
    path('otppage/',views.OTPPage,name='otppage'),
    
    path("otp/",views.OtpVerify,name='otp'),
    
    path("login/",views.Loginpage,name="loginpage"),
    
    path("loginuser/",views.loginUser,name="login"),
    
    path("profile/<int:pk>",views.profilePage,name='profile'),
    
    path('updateprofile/<int:pk>',views.UpdateProfile,name='updateprofile'),
    
    path('candidatejoblist/',views.CandidateJobPostList,name='candidatejoblist'),
    
    path('applypage/<int:pk>',views.ApplyPage,name="applypage"),
    
    path('applyjob/<int:pk>',views.ApplyJob,name="applyjob"),
    
    path('candidatelogout/',views.CandidateLogout,name='candidatelogout'),
    
    path('candidateprofile/',views.CandidateProfile,name="candidateprofile"),
    
    path('companylist/',views.CompanyListingPage,name="companylist"),


    ########compay side ############
    
    path('companyindex/',views.CompanyIndexPage,name="comindex"),
    
    path('companyprofile/<int:pk>',views.CompanyProfilePage,name="companyprofile"),
    
    path('companyprofiledetail/<int:pk>',views.CompanyProfileDetail,name="companyprofiledetail"),
    
    path('updatecompanyprofile/<int:pk>',views.UpdateCompanyProfile,name="updatecompanyprofile"),
    
    path('jobpostpage/<int:pk>',views.JobPostPage,name="jobpostpage"),
    
    path('jobpost/',views.JobDetailSubmit,name="jobpost"),

    path('joblist/',views.JobPostList,name='joblist'),
        
    path('companylogout/',views.CompanyLogout,name='companylogout'),
    
    path('jobapplylist/',views.JobApplicantsList,name='jobapplylist'),
    
    path('candidatelist/',views.CandidateListing,name="candidatelist"),
    
    path('jobdetailspage/<int:pk>',views.JobDetailsPage, name='jobdetailspage'),

    ######### Admin side ############
    
     
    path('adminloginpage/',views.AdminLoginPage,name='adminloginpage'),
    
    path('adminlogin/',views.AdminLogin,name='adminlogin'),
    
    path('adminlogout',views.AdminLogout,name='adminlogout'),
    
    path('admincandlist/',views.AdminCandidateList,name='admincandlist'),
   
    path('admincomplist/',views.AdminCompanyList,name='admincomplist'),
    
    path('deleteuser/<int:pk>',views.UserDelete,name='deleteuser'),
    
    path('verifyuserpage<int:pk>',views.VerifyUserPage,name='verifyuserpage'),
    
    path('verifyuser<int:pk>',views.VerifyUser,name='verifyuser'),
    
    path('deletecompany/<int:pk>',views.CompanyDelete,name='deletecompany'),
    
    path('verifycompanypage/<int:pk>',views.VerifyCompanyPage,name='verifycompanypage'),
    
    path('verifycompany/<int:pk>',views.VerifyCompany,name='verifycompany'),

   ##############websie side##########################
   
    path('aboutus/',views.AboutUs,name='aboutus') ,
    
]   