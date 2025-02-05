# Generated by Django 5.1.2 on 2024-11-02 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rate', '0013_alter_deposit_currency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alert',
            name='alert',
            field=models.CharField(choices=[('sweetAlert', 'click on to show'), ('paid', 'mark as paid')], default='sweetAlert', max_length=24),
        ),
        migrations.AlterField(
            model_name='alert1',
            name='alert',
            field=models.CharField(choices=[('sweetAlert', 'click on to show'), ('paid', 'mark as paid')], default='sweetAlert', max_length=24),
        ),
        migrations.AlterField(
            model_name='alert2',
            name='alert',
            field=models.CharField(choices=[('sweetAlert', 'click on to show'), ('paid', 'mark as paid')], default='sweetAlert', max_length=24),
        ),
    ]
