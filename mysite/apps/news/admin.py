__author__ = 'Rajesh'

import models
from apps.news.models import Article,Reporter
from django.contrib import admin

admin.site.register(Article)
admin.site.register(Reporter)