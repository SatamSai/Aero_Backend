from django.contrib import admin
from .models import Event,EventImage,Competition,CompetitionImage, Post,TeamMember
# Register your models here.

class ImageAdmin(admin.ModelAdmin):
    list_display = ('event','imgname','image_tag')


admin.site.register(Event)
admin.site.register(Competition)
admin.site.register(EventImage,ImageAdmin)
admin.site.register(CompetitionImage,ImageAdmin)
admin.site.register(TeamMember)
admin.site.register(Post)

