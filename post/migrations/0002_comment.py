# Generated by Django 4.1.7 on 2023-10-16 11:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import post.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=140, validators=[post.models.validate_no_bad_words])),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='post.post')),
            ],
        ),
    ]
