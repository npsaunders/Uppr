# Generated by Django 4.1.2 on 2022-10-25 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main_app", "0013_profile_delete_category_alter_question_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="email",
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
