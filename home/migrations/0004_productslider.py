# Generated by Django 4.0.3 on 2022-03-23 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_slider'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductSlider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='product-slider')),
            ],
        ),
    ]
