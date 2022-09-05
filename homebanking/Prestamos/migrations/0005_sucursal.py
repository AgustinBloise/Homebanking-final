# Generated by Django 4.1 on 2022-08-27 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Prestamos', '0004_alter_prestamo_loan_total'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('branch_id', models.AutoField(primary_key=True, serialize=False)),
                ('branch_number', models.BinaryField()),
                ('branch_name', models.TextField()),
                ('branch_address_id', models.IntegerField()),
                ('employee_amnt_per_client', models.FloatField()),
                ('given_credit_cards', models.IntegerField()),
                ('given_dedit_cards', models.IntegerField()),
                ('average_given_loans', models.TextField()),
            ],
            options={
                'db_table': 'sucursal',
            },
        ),
    ]
