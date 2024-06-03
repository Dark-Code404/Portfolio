from django.contrib import admin

from Main_app.models import *

# Register your models here.


class about(admin.ModelAdmin):
    search_fields=('Name','Title',)


admin.site.register(About,about)
admin.site.register(Othercontact,about)
admin.site.register(Mycontact,)
admin.site.register(Resume,)
admin.site.register(ResumeAbout,)
admin.site.register(ResumeTechnical,)
admin.site.register(ResumeSoft,)
admin.site.register(ResumeEducation,)
admin.site.register(ResumeCerti,)
admin.site.register(Language,)
admin.site.register(Skills,)


