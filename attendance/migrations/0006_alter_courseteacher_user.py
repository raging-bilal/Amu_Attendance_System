# Generated by Django 5.1.2 on 2025-03-24 11:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0005_student_session_alter_student_roll_no_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseteacher',
            name='user',
            field=models.ForeignKey(limit_choices_to={'role': 'faculty'}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
