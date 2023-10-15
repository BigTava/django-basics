# Generated by Django 4.1.7 on 2023-10-15 17:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('profilepage', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profilepage',
            name='user_account',
        ),
        migrations.AddField(
            model_name='profilepage',
            name='content_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype'),
        ),
        migrations.AddField(
            model_name='profilepage',
            name='object_id',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
