# Generated by Django 4.0.6 on 2022-07-29 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Message",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=64)),
                ("email", models.EmailField(max_length=64)),
                ("phone_number", models.IntegerField(blank=True, max_length=15, null=True)),
                ("message", models.TextField(max_length=800)),
            ],
        ),
    ]
