from django.urls import path
from . import views

urlpatterns=[
    path('',views.index),
    path('nosotros/',views.nosotros),
    path('catalogo/',views.catalogo),
    path('privacidad/',views.privacidad),
    path('copyright/',views.copyright),
    path('expofunsa/', views.expofunsa),
    path('registrarse/',views.registrarse),
    path('hospedaje/', views.hospedaje),
    path('contacto/',views.contacto),
    path('ubicacion/',views.ubicacion),
    path('navidad/',views.navidad),
    path('fiestasPatrias/',views.fiestasPatrias),
    path('otrasFiestas/',views.otrasFiestas)
]
