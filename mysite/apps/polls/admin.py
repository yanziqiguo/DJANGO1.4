from django.contrib import admin
from apps.polls.models import Poll,Choice

class PollAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question']

class ChoiceAdmin(admin.ModelAdmin):
    fields = ['poll', 'choice_text', 'votes']

admin.site.register(Poll, PollAdmin)
admin.site.register(Choice, ChoiceAdmin)