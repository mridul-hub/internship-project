# Generated by Django 3.2.3 on 2021-09-05 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_alter_itemmodel_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemmodel',
            name='name',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
