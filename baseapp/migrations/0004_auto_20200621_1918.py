# Generated by Django 3.0.3 on 2020-06-21 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseapp', '0003_query_subject_of_query'),
    ]

    operations = [
        migrations.AddField(
            model_name='career',
            name='Experience',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='career',
            name='Gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=200, null=True),
        ),
    ]
