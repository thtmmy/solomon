# Generated by Django 5.0.6 on 2024-05-16 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rate', '0008_transaction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='status',
            field=models.CharField(choices=[('You need to have a Withdrawal Pin in order to facilitate your withdrawal request. Please contact an agent for help on how to get one.', 'You need to have a Withdrawal Pin in order to facilitate your withdrawal request. Please contact an agent for help on how to get one.'), ('Please upgrade your account, your current investment plan does not support this action, the company will email you shortly or contact customer care for more info', 'Please upgrade your account, your current investment plan does not support this action, the company will email you shortly or contact customer care for more info'), ('KYC has not been uploaded kindly fill in your details on your kyc data table', 'KYC has not been uploaded kindly fill in your details on your kyc data table')], default='Pending', max_length=200, null=True),
        ),
    ]
