# Generated by Django 1.10.5 on 2017-01-13 07:25

from django.db import migrations


class Migration(migrations.Migration):

    INDEX_SQL = """
CREATE INDEX values_value_contact_field_location_not_null
ON values_value(contact_field_id, location_value_id)
WHERE contact_field_id IS NOT NULL AND location_value_id IS NOT NULL;
    """

    dependencies = [("values", "0008_reset_1")]

    operations = [migrations.RunSQL(INDEX_SQL)]
