from django.db import models

class Poll(models.Model):
    text = models.CharField(max_length=250)
    pub_date = models.DateField()

    def __str__(self):
        return self.text

class Choice(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length = 144)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text