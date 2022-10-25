# Generated by Django 4.1.2 on 2022-10-25 00:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("main_app", "0010_remove_question_category"),
    ]

    operations = [
        migrations.AddField(
            model_name="question",
            name="category",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="main_app.category",
            ),
            preserve_default=False,
        ),
    ]
