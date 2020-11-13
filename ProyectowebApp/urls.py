from django.contrib.auth import views as auth_views
from django.urls import path, reverse_lazy

from ProyectowebApp import views
from django.conf import settings
from django.conf.urls.static import static


from django.contrib import admin



urlpatterns = [
    path('', views.index, name="Index"),
    path('arsenal', views.arsenal, name="Arsenal"),
    path('acerca', views.acerca, name="Acerca"),
    path('formulario', views.formulario, name="Formulario"),
    path('equipos', views.equipos, name="Equipos"),
    path('nuevo_equipo', views.nuevo_team, name="Nuevo_team"),
    path('listar_equipos', views.listado_equipos, name="Listado_equipos"),
    path('equipos_modificar/<id>/',views.equipos_modificar, name="Equipo_Modificar"),
    path('equipos_eliminar/<id>/',views.equipos_eliminar, name="Equipo_Eliminar"),
    path('registro',views.registro_usuario, name="registro_usuario"),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), 
        name='password_change_done'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'), 
        name='password_change'),
    path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_done.html'),
     name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
     name='password_reset_complete'),

    
    ]







urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)