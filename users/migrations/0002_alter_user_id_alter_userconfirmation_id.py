# Generated by Django 5.0.6 on 2024-06-30 18:50

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.UUIDField(default=uuid.UUID('6c3798b0-064c-4b6c-b0cb-7432ab3a9061'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='userconfirmation',
            name='id',
            field=models.UUIDField(default=uuid.UUID('6c3798b0-064c-4b6c-b0cb-7432ab3a9061'), editable=False, primary_key=True, serialize=False),
        ),
    ]
