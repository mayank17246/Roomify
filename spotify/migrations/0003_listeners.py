# Generated by Django 3.2.5 on 2021-07-22 11:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_room_current_song'),
        ('spotify', '0002_vote'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listeners',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, null=True)),
                ('user', models.CharField(max_length=50, unique=True)),
                ('is_host', models.BooleanField(default=False)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.room')),
            ],
        ),
    ]