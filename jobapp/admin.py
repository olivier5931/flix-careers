from django.contrib import admin

from jobapp.models import Author, JobPost, Location, Skills

class JobAdmin(admin.ModelAdmin):
  list_display= ('__str__', 'title', 'date', 'salary')
  list_filter = ('date', 'salary', 'expiry')
  search_fields = ('title', 'description')
  search_help_text = "Write in your query and hit enter"
  #fields = (('title', 'description'), 'expiry')
  #exclude = ('title',)
  fieldsets = (
    ('Basic information', {
    'fields': ('title', 'description')
    }),
    ('More information', {
    'classes':('collapse', 'wide'),
    'fields': ('expiry', 'salary', 'slug')
    }),
  )

admin.site.register(JobPost)
admin.site.register(Location)
admin.site.register(Author)
admin.site.register(Skills)
