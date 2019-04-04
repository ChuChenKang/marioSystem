from django.db import models

# Create your models here.

class IntentCategory (models.Model):
    intentCategoryName = models.CharField(max_length=100)
    accountId = models.IntegerField()
    campaignId = models.IntegerField()
    language = models.CharField(max_length=100)
    parentIntentCategoryId = models.IntegerField()

class Intent(models.Model):
    intentName = models.CharField(max_length=100)
    intentCategoryId = models.ForeignKey(IntentCategory, on_delete=models.CASCADE)
    agentId = models.IntegerField(null=True)

class IntentAnswer(models.Model):
    intentId = models.ForeignKey(Intent, on_delete=models.CASCADE)
    agentId = models.IntegerField(null=True)
    answerType = models.CharField(max_length=20)
    answer = models.TextField()

class TrainingData(models.Model):
    intentId = models.ForeignKey(Intent, on_delete=models.CASCADE)
    sentence = models.TextField()
    splitSentence = models.TextField()

    def __str__(self):
        return self.name