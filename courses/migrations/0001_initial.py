# Generated by Django 3.2 on 2023-02-02 05:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('subtitle', models.CharField(max_length=90, verbose_name='Sub-Title')),
                ('image', models.ImageField(upload_to='courses/photos/', verbose_name='Image')),
                ('price', models.FloatField(verbose_name='price')),
                ('preview_video', models.FileField(upload_to='courses/videos/preview/', verbose_name='Preview Video')),
                ('description', tinymce.models.HTMLField(verbose_name='Desc')),
                ('language', models.CharField(max_length=50, verbose_name='Language')),
                ('what_you_learn', tinymce.models.HTMLField(verbose_name='What Will You Learn')),
                ('requirements', tinymce.models.HTMLField()),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='Date Added')),
                ('date_modified', models.DateTimeField(auto_now=True, verbose_name='Date Modified')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.category', verbose_name='Category')),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_section', to='courses.course', verbose_name='Course')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(verbose_name='')),
                ('content', models.TextField(verbose_name='Content')),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='Date Added')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_review', to='courses.course', verbose_name='Course')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_review', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
        migrations.CreateModel(
            name='Lucture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('subtitle', models.CharField(max_length=90, verbose_name='Sub-Title')),
                ('video', models.FileField(upload_to='courses/videos/luctures', verbose_name='Video')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_lucture', to='courses.course', verbose_name='Course')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='section_lucture', to='courses.section', verbose_name='Section')),
            ],
        ),
    ]