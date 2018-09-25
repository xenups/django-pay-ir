# Generated by Django 2.1.1 on 2018-09-25 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Full name')),
                ('amount', models.BigIntegerField(verbose_name='Amount')),
                ('mobile', models.CharField(blank=True, max_length=11, null=True, verbose_name='Mobile number')),
                ('description', models.CharField(blank=True, max_length=255, null=True, verbose_name='Description')),
                ('transid', models.IntegerField(verbose_name='Trans ID')),
                ('status', models.BooleanField(default=False, verbose_name='Status')),
                ('card_number', models.BigIntegerField(blank=True, null=True, verbose_name='Card number')),
                ('trace_number', models.BigIntegerField(blank=True, null=True, verbose_name='Trace number')),
                ('message', models.TextField(blank=True, null=True, verbose_name='Message')),
            ],
        ),
    ]
