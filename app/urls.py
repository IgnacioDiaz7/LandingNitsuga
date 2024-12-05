from django.urls import path
from .views import home, contacto, nosotros

app_name = 'app'

urlpatterns = [
    path('', home, name="home"),
    path('contacto/', contacto, name="contacto"),
    path('nosotros/', nosotros, name="nosotros"),
    
    
]