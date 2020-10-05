from django.contrib import admin
from .models import Reviews


class ReviewsAdmin(admin.ModelAdmin):
    date_hierarchy = ('pub_date')
    list_display = ('title', 'content', 'state', 'grade',
    )
    search_fields = ('title', 'pub_date')

    def krotki_opis(self, obj):
        return (
            f'{obj.content[:50]}...'
            if len(obj.content) > 50
            else obj.content
        )


admin.site.register(Reviews, ReviewsAdmin)



