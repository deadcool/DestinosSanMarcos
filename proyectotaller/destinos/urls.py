from django.conf.urls import url
from destinos import views


urlpatterns = [
    url(r'^$/', views.administrador),
]
