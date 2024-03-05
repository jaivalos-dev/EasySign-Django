from django.urls import path
from . import views

urlpatterns = [
    path('', views.getDocument, name="index"),
    path('signed_documents/', views.showDocument, name="signed_documents"),
]