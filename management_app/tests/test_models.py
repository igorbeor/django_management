from django.test import TestCase
from management_app.models import Company, Manager, Employee, Job, WorkPlace
from django.db import IntegrityError


class CompanyTestCase(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.company = Company.objects.create(
            name='Facebook',
            info='Facebook is an American online social media and ' \
                'social networking service based in Menlo Park, ' \
                'California and a flagship service of the namesake ' \
                'company Facebook, Inc.'
        )
    
    def test_company(self):
        with self.assertRaises(IntegrityError):
            Company.objects.create(
                name='Boston Dynamics',
                weekly_hours_limit=40,
            )

class ManagerTestCase(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.company = Company.objects.create(
            name='Facebook',
            info='Facebook is an American online social media and ' \
                'social networking service based in Menlo Park, ' \
                'California and a flagship service of the namesake ' \
                'company Facebook, Inc.'
        )
        cls.manager = Manager.objects.create(
            first_name='John',
            last_name='Smith',
            company=cls.company
        )
    
    def test_manager(self):
        self.assertEqual(self.manager.company, self.company)

class EmployeeTestCase(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.employee = Employee.objects.create(
            first_name='John',
            last_name='Smith'
        )

    def test_employee(self):
        self.assertIsNotNone(self.employee.id)


class JobTestCase(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.company = Company.objects.create(
            name='Facebook',
            info='Facebook is an American online social media and ' \
                'social networking service based in Menlo Park, ' \
                'California and a flagship service of the namesake ' \
                'company Facebook, Inc.'
        )
        cls.job = Job.objects.create(
            name='Designer',
            company=cls.company
        )

    def test_job(self):
        self.assertIsNotNone(self.job.id)
        self.assertIsNotNone(self.job.company)

class WorkPlaceTestCase(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.company = Company.objects.create(
            name='Facebook',
            info='Facebook is an American online social media and ' \
                'social networking service based in Menlo Park, ' \
                'California and a flagship service of the namesake ' \
                'company Facebook, Inc.'
        )
        cls.job = Job.objects.create(
            name='Designer',
            company=cls.company
        )
        cls.employee = Employee.objects.create(
            first_name='John',
            last_name='Smith'
        )
        cls.workplace = WorkPlace.objects.create(
            employee=cls.employee,
            job=cls.job
        )

    def test_unique_employee_and_job(self):
        with self.assertRaises(IntegrityError):
            WorkPlace.objects.create(
                employee=self.employee,
                job=self.job
            )