# Generated by Django 4.2.7 on 2024-11-16 04:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_user_dob'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='health_info_filled',
            new_name='healthInfoFilled',
        ),
    ]