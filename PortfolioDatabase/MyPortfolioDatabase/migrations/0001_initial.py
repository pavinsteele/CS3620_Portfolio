# Generated by Django 2.2 on 2023-06-13 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hobbies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hobbies_name', models.CharField(max_length=200)),
                ('hobbies_desc', models.CharField(max_length=200)),
            ],
        ),
    ]