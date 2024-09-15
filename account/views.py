from django.shortcuts import render,redirect

# Create your views here.
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from .sendemail import ssendemail
from django.contrib import messages
from .models import otpcode
import random




        




    

class VerifyCode2(View):
    def get(self,request):
        return render(request,'verify.html')
    
    def post(self,request):
        code=request.POST.get('code')
        email=request.session['user-signin-data']['email']


     

       

        
        code2=otpcode.objects.get(email=email)
        if int(code) == int(code2.code):
            code2.delete()
             
            user=User.objects.get(email=email)
            
            login(request,user)
            messages.success(request,'وارد شدید')
            return redirect('home:home')
        else:
            code2.delete()
            return redirect('account:login')





class SignUpUser(View):
    def get(self,request):
        return render(request,'loginview.html')

    def post(self,request):
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        password2=request.POST.get('password2')
        codes=[]
        all=otpcode.objects.all()
        for i in all:
            codes.append(i.email)
        users = User.objects.all()
        emails=[]
        usernames=[]
        for i in users:
            emails.append(i.email)
            usernames.append(i.username)

        if username in usernames:
            messages.error(request,'نام کاربری تکراری است')
            return render (request,'loginview.html')
        

        if email in emails:
            messages.error(request,'ایمیل قبلا حساب ساخته است')
            return render(request,'loginview.html')
        


        if password != password2:
            messages.error(request,'باید رمز ها یکی باشد')
            return render(request,'loginview.html')
        

        if email in codes:
            
            last_code=otpcode.objects.get(email=email)

            last_code.delete()







             
            
            code=random.randint(10000,99999)

            objectt=otpcode(email=email,code=code)


            objectt.save()


            ssendemail(email=email,code=code)
            request.session['user-signin-data']={
            'username':username,
            'password':password,
            'email':email,

                }
            messages.success(request,'کد برای ایمیل شما ارسال شد')
            return redirect('account:verify')
        else:
                         
            
            code=random.randint(10000,99999)

            objectt=otpcode(email=email,code=code)


            objectt.save()


            ssendemail(email=email,code=code)
            request.session['user-signin-data']={
            'username':username,
            'password':password,
            'email':email,

                }
            messages.success(request,'کد برای ایمیل شما ارسال شد')
            return redirect('account:verify')


        

            

        








        




class LogoutUser(View):
    def get(self,request):
        logout(request)
        messages.success(request,'شما خارج شدید')
        return redirect('home:home')



    def post(self,request):
        pass


        



 








        
class VerifyCode(View):
    def get(self,request):
        return render(request,'verify.html')
    
    def post(self,request):
        code=request.POST.get('code')
        email=request.session['user-signin-data']['email']
        password=request.session['user-signin-data']['password']

        username=request.session['user-signin-data']['username']
        code2=otpcode.objects.get(email=email)
        if int(code) == int(code2.code):
            code2.delete()
            User.objects.create_user(username=username,email=email,password=password)
            user=User.objects.get(username=username,email=email)

            login(request,user)
            messages.success(request,'حساب کاربری ساخته شد')
            return redirect('home:home')
        else:
            code2.delete()
            messages.error(request,'کد وارد شده اشتباه است')
            return redirect('account:signupuser')



class LoginUser(View):
    def get(self,request):
        pass
    

    def post(self,request):
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(request,username=username,password=password)

      

        if user is not None:
            codes=[]
            all=otpcode.objects.all()
            for i in all:
                codes.append(i.email)


              

            if user.email in codes:



                last_code=otpcode.objects.get(email=user.email)

                last_code.delete()



             
            
                
            
                randomcode=random.randint(10000,99999)
            
                code=otpcode(email=user.email,code=randomcode)
                code.save()
                ssendemail(email=user.email,code=randomcode)
                request.session['user-signin-data']={
                   
                        'password':password,
                        'email':user.email,

                }
                messages.success(request,'کد برای ایمیل شما ارسال شد')
                return redirect('account:verify2')   
            else:
                            
                randomcode=random.randint(10000,99999)
            
                code=otpcode(email=user.email,code=randomcode)
                code.save()
                ssendemail(email=user.email,code=randomcode)
                request.session['user-signin-data']={
                   
                        'password':password,
                        'email':user.email,

                }
                messages.success(request,'کد برای ایمیل شما ارسال شد')
                return redirect('account:verify2')   

        else:
                    
            messages.error(request,'پیدا نشد')
            return redirect('account:loginview')
           


class LoginView(View):
    def get(self,request):
        return render(request,'loginview.html')
    

    def post(self,request):
        pass




class Card(View):
    def get(self,request):
        return render(request,'card.html')
    

    def post(self,request):
        pass