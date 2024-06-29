from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('sucursales/', views.sucursales, name='sucursales'),
    path('comparar/', views.comparar, name='comparar'),
    path('registros/', views.registros, name='registros'),
    path('doctores/', views.doctores, name='doctores'),
    path('admin/', views.admin_tables, name='admin'),
    path('logout/', views.logout_view, name='logout'),
    path('agregar-registro/', views.agregar_registro, name='agregar_registro'),
    path('editar-registro/<str:folio>/',
         views.editar_registro, name='editar_registro'),
    path('eliminar-registro/<str:folio>/',
         views.eliminar_registro, name='eliminar_registro'),
    path('agregar-doctor/', views.agregar_doctor, name='agregar_doctor'),
    path('editar-doctor/<str:id>/', views.editar_doctor, name='editar_doctor'),
    path('eliminar-doctor/<str:id>/',
         views.eliminar_doctor, name='eliminar_doctor'),
]
