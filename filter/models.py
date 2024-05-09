from django.db import models

class Filter(models.Model):

    CATEGORIES_CHOICES = {
        "Pornography": "Pornography",
        "Politics":"Politics",
        "Entertainment" : "Entertainment"
    }

    ACTION_CHOICES = {
        "Block":"Block",
        "Alert":"Alert",
        "Log":"Log",
        "Redirect":"Redirect",
        "Sanitize":"Sanitize"
    }

    category = models.CharField(max_length=50, choices = CATEGORIES_CHOICES)
    action = models.CharField(max_length=50, choices = ACTION_CHOICES, default = ACTION_CHOICES["Block"])
    domain = models.CharField(max_length=50)
    active = models.BooleanField(default = True)

    def __str__(self):
        return self.domain
