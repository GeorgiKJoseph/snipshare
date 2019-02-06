# Generated by Django 2.0.10 on 2019-02-06 15:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0012_friend_current_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vote',
            name='acc_pk',
        ),
        migrations.RemoveField(
            model_name='vote',
            name='pastebin_pk',
        ),
        migrations.AddField(
            model_name='vote',
            name='current_pastebin',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='current_bin', to='webapp.Pastebin'),
        ),
        migrations.AddField(
            model_name='vote',
            name='pastebin',
            field=models.ManyToManyField(blank=True, null=True, to='webapp.Pastebin'),
        ),
    ]