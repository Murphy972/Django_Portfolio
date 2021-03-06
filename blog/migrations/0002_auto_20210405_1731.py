# Generated by Django 2.2.19 on 2021-04-05 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('title', models.CharField(max_length=20)),
                ('pub_date', models.DateTimeField()),
                ('body', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
