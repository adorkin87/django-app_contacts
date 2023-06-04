from django.contrib import admin

from . import models


class RequisitesInline(admin.TabularInline):
    model = models.Requisites
    extra = 0


class PhonesInline(admin.TabularInline):
    model = models.Phones
    extra = 0


class OtherContactsInline(admin.TabularInline):
    model = models.OtherContacts
    extra = 0


@admin.register(models.Companies)
class CompaniesAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = (RequisitesInline, PhonesInline, OtherContactsInline)
    save_on_top = True
