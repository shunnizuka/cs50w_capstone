# Generated by Django 3.1 on 2021-01-01 14:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SwapNGameOn', '0002_auto_20201229_2243'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='swap',
            name='hasRequestedGame',
        ),
        migrations.RemoveField(
            model_name='swap',
            name='meetup',
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hasRequestedGame', models.BooleanField(default=False)),
                ('meetup', models.BooleanField(default=False)),
                ('altMeetup', models.CharField(max_length=255)),
                ('isAccepted', models.BooleanField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('offeredGame', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='request_game', to='SwapNGameOn.game')),
                ('requester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='request_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='swap',
            name='request',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='swap_request', to='SwapNGameOn.request'),
        ),
    ]
