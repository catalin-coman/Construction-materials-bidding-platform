# Generated by Django 3.2.4 on 2021-06-17 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Concrete',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Type', models.CharField(max_length=100)),
                ('Diameter', models.IntegerField()),
                ('Consistency', models.IntegerField()),
            ],
        ),
    ]
