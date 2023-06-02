from django.contrib import admin
from django.urls import path
from myapp_cookie import views

urlpatterns =[
    path('admin/',admin.site.urls),
    path('scookie/',views.setcookie),
    path('gcookie/',views.getcookie),
]