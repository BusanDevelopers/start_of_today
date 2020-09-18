# Generated by Django 3.1 on 2020-09-05 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.CharField(max_length=10)),
                ('title', models.TextField()),
                ('views', models.TextField()),
                ('video_length', models.TextField()),
                ('url', models.TextField()),
            ],
            options={
                'verbose_name': '오늘의 영상',
                'verbose_name_plural': '오늘의 영상',
                'db_table': 'DB_Video',
            },
        ),
    ]