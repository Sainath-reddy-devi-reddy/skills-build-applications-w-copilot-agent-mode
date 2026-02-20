from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import date

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='Marvel', description='Marvel superheroes')
        dc = Team.objects.create(name='DC', description='DC superheroes')

        # Users
        tony = User.objects.create(name='Tony Stark', email='tony@marvel.com', team=marvel.name)
        steve = User.objects.create(name='Steve Rogers', email='steve@marvel.com', team=marvel.name)
        bruce = User.objects.create(name='Bruce Wayne', email='bruce@dc.com', team=dc.name)
        clark = User.objects.create(name='Clark Kent', email='clark@dc.com', team=dc.name)

        # Activities
        Activity.objects.create(user=tony.name, activity_type='Running', duration=30, date=date.today())
        Activity.objects.create(user=steve.name, activity_type='Cycling', duration=45, date=date.today())
        Activity.objects.create(user=bruce.name, activity_type='Swimming', duration=60, date=date.today())
        Activity.objects.create(user=clark.name, activity_type='Yoga', duration=20, date=date.today())

        # Leaderboard
        Leaderboard.objects.create(team=marvel.name, points=150)
        Leaderboard.objects.create(team=dc.name, points=120)

        # Workouts
        Workout.objects.create(name='HIIT', description='High Intensity Interval Training', difficulty='Hard')
        Workout.objects.create(name='Cardio', description='Cardio workout', difficulty='Medium')
        Workout.objects.create(name='Stretching', description='Full body stretching', difficulty='Easy')

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data.'))
