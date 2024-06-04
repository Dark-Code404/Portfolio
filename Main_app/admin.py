from django.contrib import admin

from Main_app.models import *

# Register your models here.


class about(admin.ModelAdmin):
    search_fields=('Name','Title',)


admin.site.register(About,about)
admin.site.register(Othercontact,about)
admin.site.register(Mycontact,about)
admin.site.register(ResumeAbout,about)
admin.site.register(ResumeTechnical,about)
admin.site.register(ResumeSoft,about)
admin.site.register(ResumeEducation,about)
admin.site.register(ResumeCerti,about)
admin.site.register(Language,about)
admin.site.register(Skills,about)


