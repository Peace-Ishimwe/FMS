# Generated by Django 4.2.16 on 2024-11-15 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='province',
            field=models.CharField(choices=[('kigali', 'Kigali'), ('northern', 'Northern'), ('southern', 'Southern'), ('eastern', 'Eastern'), ('western', 'Western')], max_length=100),
        ),
    ]
