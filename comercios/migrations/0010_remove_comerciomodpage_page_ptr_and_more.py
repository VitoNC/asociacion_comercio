# Generated by Django 4.0.4 on 2022-06-02 18:53

from django.db import migrations
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('comercios', '0009_rename_comercioalipage_comerciopage_and_more'),
    ]

    operations = [

        migrations.AlterField(
            model_name='comercio',
            name='description',
            field=wagtail.fields.RichTextField(blank=True),
        ),

    ]
