# Generated by Django 4.2.2 on 2023-09-14 13:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Bank', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=50)),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(max_length=10)),
                ('phone_number', models.IntegerField(max_length=15)),
                ('mail_id', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=250)),
                ('account_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Bank.accounttype')),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Bank.branch')),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Bank.district')),
            ],
        ),
        migrations.DeleteModel(
            name='login',
        ),
        migrations.DeleteModel(
            name='register',
        ),
        migrations.AddField(
            model_name='branch',
            name='district',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Bank.district'),
        ),
    ]
