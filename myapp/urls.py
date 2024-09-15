from django.urls import path, re_path
from .views import *
urlpatterns = [
    path('', MyAppListView.as_view(), name='list_view'),
    path('<int:pk>/', MyAppDetailView.as_view(), name='detail_view'),
]