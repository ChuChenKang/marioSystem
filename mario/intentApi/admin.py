from django.contrib import admin
from .models import Intent, IntentAnswer, IntentCategory, TrainingData

# Register your models here.
admin.site.register(Intent),
admin.site.register(IntentAnswer),
admin.site.register(IntentCategory),
admin.site.register(TrainingData),
