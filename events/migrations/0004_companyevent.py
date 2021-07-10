# Generated by Django 3.2.5 on 2021-07-10 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_sloganevent'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.URLField(max_length=500)),
                ('title', models.TextField()),
                ('description', models.TextField()),
                ('is_main', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'company_events',
            },
        ),
    ]
