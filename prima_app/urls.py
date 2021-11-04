from django.urls import path
from prima_app. views import homepage
from prima_app.views import welocome
from prima_app.views import lista
from prima_app.views import chi_siamo
from prima_app.views import variabili

app_name="prima_app"
urlpatterns=[
path('', homepage, name='homepage'),
path('welcome', welocome, name='welcome'),
path('lista', lista, name='lista'),
path('chi_siamo', chi_siamo, name='chi_siamo'),
path('variabili', variabili, name='variabili'),
]
