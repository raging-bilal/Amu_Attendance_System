# Generated by Django 5.1.2 on 2025-05-07 11:59

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0015_attendancechangerequest_notification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('admin', 'Admin'), ('faculty', 'Faculty'), ('student', 'Student'), ('chairperson', 'Chairperson'), ('dean', 'Dean')], default='student', max_length=15),
        ),
        migrations.CreateModel(
            name='Dean',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attendance.department')),
                ('teacher', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='attendance.teacher')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Dean',
                'verbose_name_plural': 'Deans',
            },
        ),
        migrations.CreateModel(
            name='ChairpersonRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_type', models.CharField(choices=[('add', 'Add'), ('remove', 'Remove'), ('edit', 'Edit')], max_length=10)),
                ('model_name', models.CharField(max_length=50)),
                ('object_id', models.IntegerField()),
                ('changes', models.JSONField()),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='pending', max_length=10)),
                ('reason', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('reviewed_at', models.DateTimeField(blank=True, null=True)),
                ('review_notes', models.TextField(blank=True)),
                ('chairperson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requests', to='attendance.chairperson')),
                ('reviewed_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reviewed_requests', to='attendance.dean')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
