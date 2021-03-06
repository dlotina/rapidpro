# Generated by Django 1.10.6 on 2017-04-06 17:33

from django.db import migrations, models

from temba.utils import chunk_list


def do_populate_send_all(Broadcast):
    broadcast_ids = Broadcast.objects.all().values_list("id", flat=True)

    broadcast_count = len(broadcast_ids)
    if broadcast_count:
        print("Starting to update %d broadcasts send all field..." % broadcast_count)

    updated = 0
    for chunk in chunk_list(broadcast_ids, 5000):
        Broadcast.objects.filter(pk__in=chunk).update(send_all=False)
        print("Updated %d of %d broadcasts" % (updated + len(chunk), broadcast_count))


def apply_as_migration(apps, schema_editor):
    Broadcast = apps.get_model("msgs", "Broadcast")
    do_populate_send_all(Broadcast)


def apply_manual():
    from temba.msgs.models import Broadcast

    do_populate_send_all(Broadcast)


class Migration(migrations.Migration):

    dependencies = [("msgs", "0088_broadcast_send_all")]

    operations = [
        migrations.AlterField(
            model_name="broadcast",
            name="send_all",
            field=models.NullBooleanField(
                default=False, help_text="Whether this broadcast should send to all URNs for each contact"
            ),
        ),
        migrations.RunPython(apply_as_migration),
    ]
