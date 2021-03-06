# Generated by Django 3.1.5 on 2021-04-13 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20210412_0039'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='must_read',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.CharField(choices=[('education', 'Education'), ('giveaway', 'Giveaway'), ('entertainment', 'Entertainment'), ('telecommunication', 'Telecommunication'), ('medical', 'Medical'), ('religion', 'Religion'), ('fitness', 'Fitness'), ('gossip', 'Gossip'), ('computer science', 'Computer Science'), ('business', 'Business'), ('fitness', 'Fitness'), ('marriage', 'Marriage'), ('movie', 'Movie'), ('health', 'Health'), ('books', 'Books and Novels'), ('fashion', ' Fashion and Beauty'), ('skin-care', 'Skin Care'), ('politics', 'Politics'), ('engineering', 'Engineering'), ('food', 'Foods and Nutrition'), ('graphics', 'Grpahics design'), ('fashion', 'Fashion'), ('media', 'Media'), ('tricks_and_hacks', 'Tricks and Hacks'), ('psychology', 'Psychology'), ('sports', 'Sports'), ('strike', 'Strkie'), ('scarcity', 'Scarcity'), ('fuel_subsidy', 'Fuel Subsidy'), ('food', 'Foods'), ('technology', 'Technology'), ('religion', 'Religion'), ('others', 'Others')], default='Others', max_length=100),
        ),
    ]
