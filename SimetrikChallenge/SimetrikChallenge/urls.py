from django.urls import path
from simetrikApi import views

urlpatterns = [
    path('tables', views.get_tables, name = 'tables'),
    path('tables/<str:name>', views.get_table, name = 'tables-name'),
    path('tables/create/', views.create_table, name = 'tables-create'),
]
