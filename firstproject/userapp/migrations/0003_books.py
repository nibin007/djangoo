# Generated by Django 4.0.3 on 2022-04-01 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0002_teacher_students_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='book name')),
                ('price', models.IntegerField()),
                ('author', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'Book',
            },
        ),
    ]
