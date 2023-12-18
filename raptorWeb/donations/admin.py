from django.contrib import admin
from django.forms import ModelForm

from tinymce.widgets import TinyMCE

from raptorWeb.donations.models import DonationPackage, DonationServerCommand, DonationDiscordRole, CompletedDonation

class DonationPackageAdminForm(ModelForm):
    class Meta:
        model = DonationPackage
        widgets = {
            'package_description': TinyMCE
        }
        fields = '__all__'
        
        
class CompletedDonationAdmin(admin.ModelAdmin):
    """
    Object defining behavior and display of 
    Completed Donations in the Django admin interface.
    """
    fieldsets: tuple[tuple[str, dict[str, tuple[str]]]] = (
        ('Donation Information', {
            'fields': (
                'donation_datetime',
                'donating_user',
                'minecraft_username',
                'discord_username',
                'bought_package',
                'spent',
                'session_id',
                'checkout_id',
                'completed',
                'sent_commands_count',
                'gave_roles_count')
        }),
    )

    search_fields: list[str] = [
        'minecraft_username',
        'discord_username',
        'donating_user',
        'bought_package'
    ]

    list_display: list[str] = [
        'minecraft_username',
        'discord_username',
        'spent',
        'bought_package',
        'sent_commands_count',
        'gave_roles_count',
        'completed'  
    ]
    
    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False


class DonationPackageAdmin(admin.ModelAdmin):
    """
    Object defining behavior and display of 
    Donation Packages in the Django admin interface.
    """
    form = DonationPackageAdminForm
    
    fieldsets: tuple[tuple[str, dict[str, tuple[str]]]] = (
        ('Package Information', {
            'fields': (
                'name',
                'price',
                'variable_price',
                'allow_repeat',
                'package_picture',
                'package_description')
        }),
        ('Benefits', {
            'fields': (
                'servers',
                'commands',
                'discord_roles',)
        }),
    )

    search_fields: list[str] = [
        'name',
    ]

    list_display: list[str] = ['name', 'allow_repeat', 'variable_price', 'price']
    
    
class DonationServerCommandAdmin(admin.ModelAdmin):
    """
    Object defining behavior and display of Donation
    Server Commands in the Django admin interface.
    """
    fieldsets: tuple[tuple[str, dict[str, tuple[str]]]] = (
        ('Donation Command', {
            'fields': (
                'command',)
        }),
    )

    search_fields: list[str] = [
        'command',
    ]

    list_display: list[str] = ['command']
    
    
class DonationDiscordroleAdmin(admin.ModelAdmin):
    """
    Object defining behavior and display of Donation
    Discord Roles in the Django admin interface.
    """
    fieldsets: tuple[tuple[str, dict[str, tuple[str]]]] = (
        ('Discord Role', {
            'fields': (
                'name',
                'role_id')
        }),
    )

    search_fields: list[str] = [
        'name',
        'role_id,'
    ]

    list_display: list[str] = ['name', 'role_id']
    
admin.site.register(DonationPackage, DonationPackageAdmin)
admin.site.register(DonationServerCommand, DonationServerCommandAdmin)
admin.site.register(DonationDiscordRole, DonationDiscordroleAdmin)
admin.site.register(CompletedDonation, CompletedDonationAdmin)