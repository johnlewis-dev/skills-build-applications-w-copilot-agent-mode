from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelSmokeTests(TestCase):
    def test_user_creation(self):
        user = User.objects.create(name='Test', email='test@example.com', team='Marvel')
        self.assertEqual(user.email, 'test@example.com')

    def test_team_creation(self):
        team = Team.objects.create(name='TestTeam', members=[])
        self.assertEqual(team.name, 'TestTeam')

    def test_activity_creation(self):
        activity = Activity.objects.create(user='test@example.com', activity='Run', duration=10)
        self.assertEqual(activity.activity, 'Run')

    def test_workout_creation(self):
        workout = Workout.objects.create(name='TestWorkout', suggested_for='Marvel')
        self.assertEqual(workout.name, 'TestWorkout')

    def test_leaderboard_creation(self):
        lb = Leaderboard.objects.create(team='Marvel', points=100)
        self.assertEqual(lb.points, 100)
