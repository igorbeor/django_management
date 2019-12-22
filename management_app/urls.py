from django.urls import path
from .views import CompanyListView, CompanyDetailView


urlpatterns = [
    path('companies', CompanyListView.as_view(), name='company-list'),
    path(
        'companies/<int:pk>',
        CompanyDetailView.as_view(),
        name='company-details'
    )
]
