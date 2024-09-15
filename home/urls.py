from django.urls import path

from .views import Home, About, Servise, Why, Panel,CapitanTrade,Weblogg,Amozesh,webhook,WallReader,Alerts,Pomp,Alertp
app_name='home'
urlpatterns=[
    path('',Home.as_view(),name='home'),
    path('about/',About.as_view(), name='about' ),
    path('servise/',Servise.as_view(), name='servise' ),
    path('why/',Why.as_view(), name='why' ),
path('panel/',Panel.as_view(), name='panel' ),
   path('capitantrade/',CapitanTrade.as_view(),name='capitantrade'),
   path('weblog/<str:on>/',Weblogg.as_view(),name='weblog'),
     path('amozesh/',Amozesh.as_view(),name='amozesh'),
     path('webhook',webhook),
     path('wallreader/',WallReader.as_view(),name='wallreader'),
     path('alerts/<str:name>/',Alerts.as_view(),name='alerts'),
      path('pompdump/',Pomp.as_view(),name='pomps'),
 path('alertp/<str:name>/',Alertp.as_view(),name='alertp'),
    
 
]