from django.contrib import admin
from authapp.models import Contact, Enrollment, Trainer, Membership, Gallery
# Register your models here.
admin.site.register(Contact)
admin.site.register(Enrollment)
admin.site.register(Trainer)
admin.site.register(Membership)
admin.site.register(Gallery)