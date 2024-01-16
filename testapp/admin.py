from django.contrib import admin
from .models import entropy
from .models import siteuser,photopost,newcomentss

# admin.site.register(entropy)
admin.site.register(siteuser)
admin.site.register(photopost)
admin.site.register(newcomentss)