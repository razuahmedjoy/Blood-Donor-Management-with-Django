# Generated by Django 3.2.5 on 2022-03-26 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0010_auto_20220326_1143'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('designation', models.CharField(blank=True, max_length=60, null=True)),
                ('address', models.CharField(blank=True, max_length=250, null=True)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='volunteers/')),
                ('fb_link', models.CharField(blank=True, max_length=200, null=True)),
                ('contact_no', models.CharField(blank=True, max_length=13, null=True)),
                ('is_active', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='volunteers/'),
        ),
    ]
