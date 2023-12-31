from django.conf import settings
from django.http import HttpResponse

from raptorWeb.raptormc.models import SiteInformation
from raptorWeb.gameservers.models import Server

BASE_USER_URL: str = getattr(settings, 'BASE_USER_URL')
BASE_DIR: str = getattr(settings, 'BASE_DIR')


def server_settings_to_context(request: HttpResponse) -> dict:
    site_info: SiteInformation.objects = SiteInformation.objects.get_or_create(pk=1)[0]
    current_servers = Server.objects.filter(archived=False)
    
    return {"server_query_enabled": site_info.enable_server_query,
            "server_pagination_count": site_info.server_pagination_count,
            "total_server_count": current_servers.count(),
            "current_enabled_servers": current_servers}
    