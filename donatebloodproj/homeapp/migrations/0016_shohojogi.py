# Generated by Django 3.2.5 on 2022-03-26 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0015_blog_blog_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='shohojogi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=100)),
                ('contact_no', models.CharField(max_length=50)),
            ],
        ),
    ]
