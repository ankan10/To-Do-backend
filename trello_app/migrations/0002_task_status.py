# Generated by Django 3.1.6 on 2021-02-26 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trello_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('P', 'PENDING'), ('C', 'COMPLETED'), ('IP', 'IN_PROGRESS'), ('D', 'DROPPED')], default=('IP', 'IN_PROGRESS'), max_length=2),
        ),
    ]
