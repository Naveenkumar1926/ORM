# Generated by Django 5.1.2 on 2024-11-13 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bank_loan',
            fields=[
                ('customer_id', models.IntegerField(primary_key=True, serialize=False)),
                ('customer_name', models.CharField(max_length=100)),
                ('loan_amount', models.IntegerField()),
                ('customer_age', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
