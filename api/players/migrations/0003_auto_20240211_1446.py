# Generated by Django 5.0.2 on 2024-02-11 17:46

from django.db import migrations
from django.contrib.auth.hashers import make_password

class Migration(migrations.Migration):

    def insert_admins(apps, schema_editor):
        # We can't import the Person model directly as it may be a newer
        # version than this migration expects. We use the historical version.
        User = apps.get_model("auth", "User")
        admin1 = User.objects.create(username="admin1", email="admin1@admin1.com",
                           password="admin1", is_staff=True)
        admin1.password = make_password('admin1')
        admin1.save()

        admin2 = User.objects.create(username="admin2", email="admin2@admin2.com",
                                password="admin2", is_staff=True)
        admin2.password = make_password('admin2')
        admin2.save()

    dependencies = [
        ('players', '0002_remove_partida_times_partida_times'),
    ]

    operations = [
        migrations.RunPython(insert_admins),
    ]