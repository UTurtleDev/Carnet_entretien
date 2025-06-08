from django.contrib import admin
from django.contrib.auth.admin import UserAdmin 
from .models import CustomUser

# Register your models here.
class CustomUserAdmin(UserAdmin):
    model = CustomUser

    # Permet l'affichage de l'instance utilisateur dans l'admin
    # fieldsets = UserAdmin.fieldsets + (('Informations complémentaires', 
    #                                     {'fields': ('zip_code',)}),
    # )

    add_fieldsets = UserAdmin.add_fieldsets + ((None, {
                                                'classes': ('wide',), 
                                                'fields': ('email', "username","password1", "password2", "is_active", "is_staff", "is_superuser", "groups", "user_permissions",)
                                                }),)


admin.site.register(CustomUser, CustomUserAdmin)