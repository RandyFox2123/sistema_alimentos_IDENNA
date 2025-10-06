
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    #General
    path('', views.index, name="index"),
    path('panel_principal/', views.panel_principal, name='panel_principal'),
    
    #Alimento
    path('registrar_alimento/', views.registrar_alimento, name='registrar_alimento'),
    path('edicion_alimento/<int:id_alimento>', views.editar_alimento, name='edicion_alimento'),
    path('borrar_alimento/<int:id_alimento>', views.borrar_alimento, name='borrar_alimento'),
    path('sumar_alimento/<int:id_alimento>', views.sumar_cantidad_alimento, name="sumar_alimento"),
    path('restar_alimento/<int:id_alimento>', views.restar_cantidad_alimento, name="restar_alimento"),
    
    #Otros
    path('generar_excel/', views.generar_excel, name='generar_excel')
    
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)#Servir los archivos de media