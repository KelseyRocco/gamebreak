# Generated by Django 3.1.7 on 2021-06-26 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='System',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('date', models.IntegerField()),
                ('platform', models.CharField(max_length=250)),
                ('people', models.IntegerField(choices=[('1', 'One'), ('2', 'Two'), ('3', 'Three'), ('4+', 'Four')], default='1')),
            ],
        ),
    ]