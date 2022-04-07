from django.urls import path
from prova_pratica_1.views import view_b,view_c,view_e


app_name="prova_pratica_1"
urlpatterns=[
    path('view_b/', view_b, name='view_b'),
    path('view_c/', view_c, name='view_c'),
    path('view_e/', view_e, name='view_e'),
]