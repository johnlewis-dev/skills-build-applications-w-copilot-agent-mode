from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models

from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Connect to MongoDB
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']

        # Drop collections if they exist
        db.users.drop()
        db.teams.drop()
        db.activities.drop()
        db.leaderboard.drop()
        db.workouts.drop()

        # Create teams
        teams = [
            {'name': 'Marvel', 'members': []},
            {'name': 'DC', 'members': []},
        ]
        team_ids = db.teams.insert_many(teams).inserted_ids

        # Create users (superheroes)
        users = [
            {'name': 'Spider-Man', 'email': 'spiderman@marvel.com', 'team': 'Marvel'},
            {'name': 'Iron Man', 'email': 'ironman@marvel.com', 'team': 'Marvel'},
            {'name': 'Wonder Woman', 'email': 'wonderwoman@dc.com', 'team': 'DC'},
            {'name': 'Batman', 'email': 'batman@dc.com', 'team': 'DC'},
        ]
        db.users.insert_many(users)
        db.users.create_index([('email', 1)], unique=True)

        # Create activities
        activities = [
            {'user': 'spiderman@marvel.com', 'activity': 'Running', 'duration': 30},
            {'user': 'ironman@marvel.com', 'activity': 'Cycling', 'duration': 45},
            {'user': 'wonderwoman@dc.com', 'activity': 'Swimming', 'duration': 60},
            {'user': 'batman@dc.com', 'activity': 'Yoga', 'duration': 20},
        ]
        db.activities.insert_many(activities)

        # Create workouts
        workouts = [
            {'name': 'Morning Cardio', 'suggested_for': 'Marvel'},
            {'name': 'Strength Training', 'suggested_for': 'DC'},
        ]
        db.workouts.insert_many(workouts)

        # Create leaderboard
        leaderboard = [
            {'team': 'Marvel', 'points': 75},
            {'team': 'DC', 'points': 80},
        ]
        db.leaderboard.insert_many(leaderboard)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
