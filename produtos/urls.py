from django.urls import path
from . import views

urlpatterns=[
    path('',views.listar_tabela,name='lista_produtos'),
    path('<int:id>/',views.detalhes_elementos,name='detalhe_produto'),

]