# Generated by Django 3.2.8 on 2021-11-02 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_alter_post_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.CharField(max_length=200, null=True),
        ),
    ]