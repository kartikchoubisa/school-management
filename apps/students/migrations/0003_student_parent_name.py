# Generated by Django 3.2.17 on 2024-04-15 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_auto_20201124_0614'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='parent_name',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]