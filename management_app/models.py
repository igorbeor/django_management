from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=64)
    info = models.TextField(max_length=1024, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Companies'


class Manager(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)


class Employee(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)


class Job(models.Model):
    name = models.CharField(max_length=64)
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name


class Workplace(models.Model):
    name = models.CharField(max_length=64)
    employee = models.OneToOneField(
        Employee,
        null=True,
        on_delete=models.CASCADE
    )
    job = models.ForeignKey(
        Job,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name
