# Generated by Django 5.1.2 on 2025-05-14 16:34

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0018_attendancechangerequest_requester_type_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendancechangerequest',
            name='requester_type',
        ),
        migrations.AddField(
            model_name='attendancechangerequest',
            name='decision',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='attendancechangerequest',
            name='student_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='student_attendance_change_requests', to=settings.AUTH_USER_MODEL),
        ),
    ]
