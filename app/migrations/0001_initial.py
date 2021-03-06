# Generated by Django 4.0.2 on 2022-03-21 15:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Competition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('competitionName', models.CharField(max_length=150)),
                ('competitionDesc', models.TextField(max_length=1000)),
                ('achievements', models.CharField(blank=True, max_length=150)),
                ('year', models.CharField(default='20', max_length=5)),
                ('poster_img', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eventname', models.CharField(max_length=150)),
                ('venue', models.CharField(max_length=150)),
                ('speaker', models.CharField(default='', max_length=200)),
                ('eventdate', models.DateField()),
                ('eventdesc', models.TextField(default='No Description', max_length=1000)),
                ('poster_img', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('membername', models.CharField(max_length=150)),
                ('profileImg', models.ImageField(upload_to='')),
                ('year', models.CharField(max_length=10)),
                ('role', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='EventImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imgname', models.CharField(default='no name', max_length=50)),
                ('img', models.ImageField(upload_to='')),
                ('event', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.event')),
            ],
        ),
        migrations.CreateModel(
            name='CompetitionImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imgname', models.CharField(default='no name', max_length=50)),
                ('img', models.ImageField(upload_to='')),
                ('event', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.competition')),
            ],
        ),
    ]
