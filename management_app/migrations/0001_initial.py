# Generated by Django 2.2.7 on 2019-11-25 20:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('info', models.TextField(blank=True, max_length=1024)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=64)),
                ('last_name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management_app.Company')),
            ],
        ),
        migrations.CreateModel(
            name='WorkPlace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='management_app.Employee')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job', to='management_app.Job')),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=64)),
                ('last_name', models.CharField(max_length=64)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management_app.Company')),
            ],
        ),
    ]
