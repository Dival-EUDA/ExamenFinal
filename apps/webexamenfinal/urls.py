from django.urls import path
from .views import examenfinal


urlpatterns = {
    path('', examenfinal, name='examenfinal'),
}