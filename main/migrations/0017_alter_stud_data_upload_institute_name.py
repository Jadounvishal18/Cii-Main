# Generated by Django 4.1.5 on 2023-01-21 17:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("main", "0016_stud_data_upload"),
    ]

    operations = [
        migrations.AlterField(
            model_name="stud_data_upload",
            name="institute_name",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]