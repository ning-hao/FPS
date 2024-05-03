# Generated by Django 5.0.4 on 2024-05-03 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Room', max_length=100)),
                ('port', models.IntegerField(default=7777)),
            ],
        ),
    ]