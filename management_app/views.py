from django.views.generic import ListView, DetailView
from .models import Company
import logging

logger = logging.getLogger('my_logger')
logger.setLevel(logging.INFO)


class CompanyDetailView(DetailView):
    model = Company
    template_name = 'management_app/company_detail.html'
    context_object_name = 'company'


class CompanyListView(ListView):
    model = Company
    template_name = 'management_app/company_list.html'
    context_object_name = 'company_list'

    def get_queryset(self):
        return Company.objects.order_by('name')
