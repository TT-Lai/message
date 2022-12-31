# Generated by Django 3.2.3 on 2021-06-01 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsUnit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catego', models.CharField(max_length=10)),
                ('nickname', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=50)),
                ('message', models.TextField()),
                ('pubtime', models.DateTimeField(auto_now=True)),
                ('enabled', models.BooleanField(default=False)),
                ('press', models.IntegerField(default=0)),
            ],
        ),
    ]
