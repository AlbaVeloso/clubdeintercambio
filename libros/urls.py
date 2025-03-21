from django.urls import path

from . import views

app_name = 'libros'
urlpatterns = [
    path("", views.index, name="index"),
    path("alta_libro", views.alta_libro, name="alta_libro"),
    path("ver/<int:libro_id>", views.ver, name="ver"),
    path("editar/<int:libro_id>", views.editar, name="editar"),
    path("borrar/<int:libro_id>", views.borrar, name="borrar"),

]
