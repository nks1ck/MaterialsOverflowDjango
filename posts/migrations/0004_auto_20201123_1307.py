# Generated by Django 3.1.3 on 2020-11-23 10:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_course_draft'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseshots',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.course', verbose_name='Курс'),
        ),
    ]