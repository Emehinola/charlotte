# Generated by Django 3.1.5 on 2021-04-12 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210411_2355'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.CharField(choices=[('entertainment', 'Entertainment')], default='Others', max_length=100),
        ),
    ]
