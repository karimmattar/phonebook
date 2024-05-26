# Generated by Django 5.0.6 on 2024-05-26 16:52

import django.db.models.deletion
import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ContactNumber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(choices=[('home', 'Home'), ('work', 'Work'), ('mobile', 'Mobile'), ('other', 'Other')], default='other', max_length=16)),
                ('number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contact_numbers', to='contact.contact')),
            ],
        ),
    ]