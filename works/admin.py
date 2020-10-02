from django.contrib import admin
from .models import Project, Category



class ProjectAdmin(admin.ModelAdmin):
    date_hierarchy = ('date_of_create')
    list_display = ('name', 'description', 'web_site',
                    'portfolio', 'categories')
    search_fields = ('title', 'date_of_create')

    def krotki_opis(self, obj):
        return (
            f'{obj.description[:50]}...'
            if len(obj.description) > 50
            else obj.description
        )


class CategoryAdmin(admin.ModelAdmin):

    list_display = ('name', 'description')
    search_fields = ('name', 'description')


admin.site.register(Project, ProjectAdmin)
admin.site.register(Category, CategoryAdmin)
