# Generated by Django 4.2.3 on 2023-08-19 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('final', '0003_alter_final_user_num11_alter_final_user_num12_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='final_user',
            name='total',
            field=models.IntegerField(blank=True, default=0, verbose_name='مجموع'),
        ),
    ]
