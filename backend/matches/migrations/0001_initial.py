# Generated by Django 5.2.3 on 2025-07-16 19:16

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teams', '0003_alter_teammember_role_alter_teams_team_name'),
        ('venue', '0004_alter_venueslots_slot_time_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invitation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_slot', models.TimeField()),
                ('date', models.DateField(default=datetime.date.today)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(default='pending', max_length=50, verbose_name='status')),
                ('message', models.CharField(max_length=200)),
                ('receiver_team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiver_invitations', to='teams.teams')),
                ('sender_team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender_invitations', to='teams.teams')),
                ('venue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invitations', to='venue.venues')),
            ],
        ),
        migrations.CreateModel(
            name='Matches',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_played', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('away_team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='away_matches', to='teams.teams')),
                ('home_team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='home_matches', to='teams.teams')),
                ('time_slot', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='match', to='venue.venueslots')),
                ('venue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matches', to='venue.venues')),
            ],
        ),
    ]
