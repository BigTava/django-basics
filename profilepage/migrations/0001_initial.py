# Generated by Django 4.1.7 on 2023-10-14 16:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('useraccount', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfilePage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_account', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='useraccount.useraccount')),
            ],
        ),
    ]
