from django.urls import path

from news.models import Giornalista
from .views import GiornalistaDetailViewCB, home, ArticoloDetailViewCB, ArticoloListView, GiornalistaListView

app_name="news"

urlpatterns = [
    path('', home, name="homeview"),
    #path('articoli/<int:pk>', articoloDetailView, name="articolo_detail")
    path('articoli/<int:pk>', ArticoloDetailViewCB.as_view(), name="articolo_detail"),
    path('lista_articoli/', ArticoloListView.as_view(), name="Lista_articoli"),
    path('giornalisti/<int:pk>', GiornalistaDetailViewCB.as_view(), name="giornalista_detail"),
    path('lista_giornalisti/', GiornalistaListView.as_view(), name="Lista_giornalisti"),
]
