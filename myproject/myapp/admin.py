from msilib.schema import AdminExecuteSequence
from django.contrib import admin
from .models import DETAIL 
from .models import Cart
from .models import about

admin.site.register(DETAIL)
admin.site.register(Cart)
admin.site.register(about)


# Register your models here.
