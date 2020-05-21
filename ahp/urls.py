from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_crit_model, name='add_crit_model'),
    path('', views.welcome, name='welcome'),
    path('crit_model_details/<int:pk>/', views.crit_model_details, name='crit_model_details'),
    path('crit_model_details/<int:pk>/modify_criterias/', views.modify_criterias, name='modify_criterias'),
    path('crit_model_details/<int:pk>/modify_elements/', views.modify_elements, name='modify_elements'),
    path('crit_model_details/<int:pk>/solve/', views.solve, name='solve'),
]
