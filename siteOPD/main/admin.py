from django.contrib import admin
from .models import Recommendation, UserInfo, Interests, Activity, Friends


admin.site.register(Friends)
admin.site.register(Activity)
admin.site.register(Recommendation)
admin.site.register(Interests)
admin.site.register(UserInfo)
