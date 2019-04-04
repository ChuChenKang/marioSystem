from django.contrib.auth.models import User
from rest_framework import serializers
from mario.botApi.models import Bot


class BotSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bot
        ## fields = ('name', 'language', 'pub_date', 'icon', 'createBy')
        fields = ('__all__')


