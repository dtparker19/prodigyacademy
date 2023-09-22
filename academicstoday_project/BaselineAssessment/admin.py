from django.contrib import admin
from .models import CertificationTrack, BaselineQuestion, BaselineAssessment, UserBaselineResponse

admin.site.register(CertificationTrack)
admin.site.register(BaselineQuestion)
admin.site.register(BaselineAssessment)
admin.site.register(UserBaselineResponse)
