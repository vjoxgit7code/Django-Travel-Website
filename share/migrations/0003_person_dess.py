# Generated by Django 4.2.5 on 2023-10-04 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('share', '0002_person'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='dess',
            field=models.TextField(default='Your Default Value Here'),
        ),
    ]
