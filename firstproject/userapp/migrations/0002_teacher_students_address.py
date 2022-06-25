# Generated by Django 4.0.3 on 2022-03-30 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Student_name')),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='students',
            name='address',
            field=models.CharField(default=0, max_length=28),
        ),
    ]
