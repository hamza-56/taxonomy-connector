# Generated by Django 2.2.15 on 2020-09-03 04:39

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('external_id', models.CharField(help_text='The external identifier for the skill received from API.', max_length=255)),
                ('name', models.CharField(blank=True, help_text='The name of the skill.', max_length=255)),
                ('info_url', models.URLField(blank=True, help_text='The url with more info for the skill.', verbose_name='Skill Information URL')),
                ('type_id', models.CharField(blank=True, help_text='The external type id for the skill received from API.', max_length=255)),
                ('type_name', models.CharField(blank=True, help_text='The external type name for the skill received from API.', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='CourseSkills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('course_id', models.CharField(help_text='The ID of the course whose text was used for skills extraction.', max_length=255)),
                ('confidence', models.FloatField(help_text='The extraction confidence threshold used for the skills extraction.')),
                ('skill', models.ForeignKey(help_text='The ID of the skill extracted for the course.', on_delete=django.db.models.deletion.CASCADE, to='taxonomy.Skill')),
            ],
            options={
                'ordering': ['created'],
            },
        ),
    ]
