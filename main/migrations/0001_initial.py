# Generated by Django 3.2.5 on 2021-07-20 14:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TrainingList',
            fields=[
                ('title', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('kind', models.CharField(max_length=200)),
                ('body', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nickname', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='TrainingImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images')),
                ('title', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='main.traininglist')),
            ],
        ),
    ]
