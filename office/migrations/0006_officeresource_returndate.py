# Generated by Django 4.1.3 on 2022-11-14 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('office', '0005_officeresource_issuedate_officeresource_reasontobuy'),
    ]

    operations = [
        migrations.AddField(
            model_name='officeresource',
            name='returndate',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]