from management_app.models import Company
from django.urls import reverse


class TestCompaniesPage(TestCase):
    def setUp(self):
        self.company = Company.objects.create(
            name='Facebook',
            info='Facebook is an American online social media and ' \
                'social networking service based in Menlo Park, ' \
                'California and a flagship service of the namesake ' \
                'company Facebook, Inc.'
        )
  
    def test_companies_page(self):
        response = self.client.get(reverse('companies'))
        self.assertIsNotNone(response.context['company_list'])

    def test_company_detail_page(self):
        response = self.client.get(reverse('companies', kwargs={
            'pk': self.company.id
        }))
        self.assertIsNotNone(response.context['company'])