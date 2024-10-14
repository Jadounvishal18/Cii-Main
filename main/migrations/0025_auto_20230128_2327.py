# Generated by Django 3.2.12 on 2023-01-28 17:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_alter_institutes_city_alter_institutes_country_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='institute',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.institutes'),
        ),
        migrations.AddField(
            model_name='application',
            name='profile',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.profile'),
        ),
        migrations.AlterField(
            model_name='stud_data_upload',
            name='insertion_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]