from django.urls import path
from . import views

urlpatterns = [
    path('', views.FamiliaListView.as_view(), name='familia_list'),
    path('nova/', views.FamiliaCreateView.as_view(), name='familia_create'),
    path('<int:pk>/', views.FamiliaDetailView.as_view(), name='familia_detail'),
    path('<int:pk>/editar/', views.FamiliaUpdateView.as_view(), name='familia_update'),
    path('<int:pk>/excluir/', views.FamiliaDeleteView.as_view(), name='familia_delete'),
    path('exportar/csv/', views.exportar_familias_csv, name='familia_export_csv'),

]
