from django.contrib import admin
from .models import Truck, Trailer

# Register your models here.

class TrucksAdmin(admin.ModelAdmin):
    pass
admin.site.register(Truck, TrucksAdmin)

class TrailersAdmin(admin.ModelAdmin):
    pass
admin.site.register(Trailer, TrailersAdmin)
