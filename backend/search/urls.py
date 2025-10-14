from django.urls import path
from search import views

urlpatterns = [
    path('', views.searchListView.as_view(), name='search')
]