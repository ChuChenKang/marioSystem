from rest_framework import serializers
from mario.intentApi.models import Intent, IntentCategory,IntentAnswer,TrainingData


class IntentCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = IntentCategory
        fields = ('intentCategoryName', 'accountId', 'campaignId', 'language', 'parentIntentCategoryId')


class IntentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Intent
        fields = ('intentName', 'intentCategoryId', 'agentId')


class IntentAnswerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = IntentAnswer
        fields = ('intentId', 'agentId', 'answerType', 'answer')


class TrainingDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TrainingData
        fields = ('intentId', 'sentence', 'splitSentence')


