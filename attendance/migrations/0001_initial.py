# Generated by Django 5.1.2 on 2025-02-20 11:01

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('role', models.CharField(choices=[('admin', 'Admin'), ('faculty', 'Faculty'), ('student', 'Student')], default='student', max_length=10)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('duration', models.IntegerField()),
                ('num_semesters', models.IntegerField()),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attendance.department')),
            ],
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='semesters', to='attendance.program')),
            ],
            options={
                'ordering': ['name'],
                'unique_together': {('program', 'name')},
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('credit', models.IntegerField()),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attendance.department')),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attendance.program')),
                ('semester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attendance.semester')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enrollment_no', models.CharField(max_length=20, unique=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attendance.department')),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attendance.program')),
                ('semester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attendance.semester')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_code', models.CharField(max_length=50, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attendance.department')),
            ],
        ),
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enrolled_students', to='attendance.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enrollments', to='attendance.student')),
            ],
            options={
                'ordering': ['course'],
                'unique_together': {('student', 'course')},
            },
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Present', 'Present'), ('Absent', 'Absent')], max_length=10)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attendance_records', to='attendance.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attendance_records', to='attendance.student')),
            ],
            options={
                'ordering': ['-date'],
                'unique_together': {('course', 'student', 'date')},
            },
        ),
    ]
