from django.contrib import admin
import models

admin.site.register(models.User, models.UserAdmin)
admin.site.register(models.Order, models.OrderAdmin)
admin.site.register(models.House, models.HouseAdmin)
admin.site.register(models.Payment, models.PaymentAdmin)
