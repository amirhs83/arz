from django.shortcuts import render

from django.views import View


from .models import Weblog,Video,Webhook,PompDump

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

class Home(View):
    def get(self,request):
        return render(request,'index.html')
    
    def post(self,request):
        pass

# Create your views here.


class About(View):
    def get(self,request):
        return render(request,'about.html')
    
    def post(self,request):
        pass

class Servise(View):
    def get(self,request):
        return render(request,'servise.html')
    
    def post(self,request):
        pass

class Why(View):
    def get(self,request):
        return render(request,'why.html')
    
    def post(self,request):
        pass

class Panel(View):
    def get(self,request):
        return render(request,'panel.html')
    
    def post(self,request):
        pass



class CapitanTrade(View):
    def get(self,request):
        return render(request,'capitantrade.html')
    

    def post(self,request):
        pass


class Weblogg(View):
    def get(self,request,on):




        weblogs=Weblog.objects.filter(on=on)
        
        return render(request,'weblog.html',{'weblogs':weblogs})



    def post(self,request,on):
        pass


class Amozesh(View):
    def get(self,request):
        videos=Video.objects.all()


        
        return render(request,'amozesh.html',{'videos':videos})


    def post(self,request):
        pass


@csrf_exempt
def webhook(request):
    if request.method == 'POST':
        print("Data received from Webhook is: ", request.body)
        name=''
        timeframe=''
        content=''
        webhoook=Webhook(name=name,timeframe=timeframe,content=content)
        webhook.save()

        return HttpResponse("Webhook received!")
    


class WallReader(View):
    def get(self,request):
        return render(request,'wallreader.html')
    



    def post(self,request):
        pass


class Alerts(View):
    def get(self,request,name):
        alerts=Webhook.objects.filter(name=name)
        

        return render(request,'alerts.html',{'alerts':alerts,'name':name})
        



    def post(self,request,name):
        pass

class Pomp(View):
    def get(self,request):
        return render(request,'pomp.html')
    



    def post(self,request):
        pass




class Alertp(View):
    def get(self,request,name):

        alerts=PompDump.objects.filter(name=name)
        return render(request,'alertp.html',{'alerts':alerts})
    



    def post(self,request,name):
        pass
