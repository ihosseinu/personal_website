# Generated by Django 3.2.7 on 2021-12-06 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_article_metatags'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField(max_length=3000)),
            ],
        ),
    ]