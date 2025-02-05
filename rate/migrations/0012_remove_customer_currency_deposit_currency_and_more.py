# Generated by Django 5.1.2 on 2024-11-02 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rate', '0011_alter_alert_status_alert1_alert2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='currency',
        ),
        migrations.AddField(
            model_name='deposit',
            name='currency',
            field=models.CharField(choices=[('$', 'US Dollar $'), ('£ ', 'Pound Sterling £'), ('€', 'Euro €')], default='$', max_length=24),
        ),
        migrations.AlterField(
            model_name='alert',
            name='alert',
            field=models.CharField(choices=[('click on to show', 'sweetAlert'), ('mark as paid', 'paid')], default='sweetAlert', max_length=24),
        ),
        migrations.AlterField(
            model_name='alert1',
            name='alert',
            field=models.CharField(choices=[('click on to show', 'sweetAlert'), ('mark as paid', 'paid')], default='sweetAlert', max_length=24),
        ),
        migrations.AlterField(
            model_name='alert2',
            name='alert',
            field=models.CharField(choices=[('click on to show', 'sweetAlert'), ('mark as paid', 'paid')], default='sweetAlert', max_length=24),
        ),
        migrations.AlterField(
            model_name='pin',
            name='pin',
            field=models.CharField(default='1991', max_length=200, null=True),
        ),
    ]
