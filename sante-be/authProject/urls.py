from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from rest_framework.urlpatterns import format_suffix_patterns
from authApp import views


urlpatterns = [
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('signosvitales/', views.SignosVitalesList.as_view()),
    path('signosvitales/<int:pk>/', views.SignosVitalesDetail.as_view()),
    path('personalsalud/', views.PersonalSaludList.as_view()),
    path('personalsalud/<int:pk>/', views.PersonalSaludDetail.as_view()),
    path('pacientes/', views.PacienteList.as_view()),
    path('pacientes/<int:pk>/', views.PacienteDetail.as_view()),
    path('historiasclinicas/', views.HistoriaClinicaList.as_view()),
    path('historiasclinicas/<int:pk>/', views.HistoriaClinicaDetail.as_view()),
    path('familiares/', views.FamiliarList.as_view()),
    path('familiares/<int:pk>/', views.FamiliarDetail.as_view()),
    path('especialidades/', views.EspecialidadList.as_view()),
    path('especialidades/<int:pk>/', views.EspecialidadDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

'''
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]

'''