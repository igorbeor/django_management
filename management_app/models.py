from django.db import models
import datetime


# Contants for status field
NEW = 1
APPROVED = 2
CANCELLED = 3
FINISHED = 4


class Company(models.Model):
    name = models.CharField(max_length=64, unique=True)
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


class WorkPlace(models.Model):
    employee = models.OneToOneField(
        Employee,
        null=True,
        on_delete=models.CASCADE
    )
    job = models.ForeignKey(
        Job,
        on_delete=models.CASCADE
    )
    status = models.IntegerField(choices=(
        (NEW, 'New'),
        (APPROVED, 'Approved'),
        (CANCELLED, 'Canceled'),
        (FINISHED, 'Finished')
    ), blank=True, null=True)

    hours_per_week = models.IntegerField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        unique_together = [['employee', 'job']]


class WorkTime(models.Model):
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()
    status = models.IntegerField(choices=(
        (NEW, 'New'),
        (APPROVED, 'Approved'),
        (CANCELLED, 'Canceled')
    ), default=NEW)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE,
                                 related_name='worktimes')
    workplace = models.ForeignKey(WorkPlace, on_delete=models.CASCADE,
                                  related_name='worktimes')


class Statistics(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE,
                                 related_name='statistics')
    workplace = models.ForeignKey(WorkPlace, on_delete=models.CASCADE,
                                  related_name='statistics')
    hours_total = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)