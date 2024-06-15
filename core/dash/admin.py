from django.contrib import admin
from .models import Member,Transaction,Guest,Idme,Bank,Contact_us



admin.site.register(Member)
admin.site.register(Guest)
admin.site.register(Transaction)
admin.site.register(Idme)
admin.site.register(Bank)
admin.site.register(Contact_us)
# Register your models here.
