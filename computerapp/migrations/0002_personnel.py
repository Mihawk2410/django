# Generated by Django 4.0.3 on 2022-04-14 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('computerapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Personnel',
            fields=[
                ('id', models.AutoField(max_length=15, primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=10)),
                ('prenom', models.CharField(max_length=10)),
            ],
        ),
    ]
