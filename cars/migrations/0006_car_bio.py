# Generated by Django 5.0 on 2024-01-25 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0005_carinventory'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
    ]
