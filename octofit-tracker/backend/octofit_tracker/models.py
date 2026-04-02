from djongo import models

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    members = models.JSONField(default=list)

    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    team = models.CharField(max_length=100)

    def __str__(self):
        return self.email

class Activity(models.Model):
    user = models.CharField(max_length=100)
    activity = models.CharField(max_length=100)
    duration = models.IntegerField()

class Workout(models.Model):
    name = models.CharField(max_length=100)
    suggested_for = models.CharField(max_length=100)

class Leaderboard(models.Model):
    team = models.CharField(max_length=100)
    points = models.IntegerField()
