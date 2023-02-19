from django.views.generic import ListView, TemplateView
from django.http import HttpResponseRedirect, HttpResponse, HttpRequest
from django.conf import settings

from raptorWeb.gameservers.models import ServerManager, ServerStatistic, Server, Player

GAMESERVERS_TEMPLATE_DIR: str = getattr(settings, 'GAMESERVERS_TEMPLATE_DIR')
SCRAPE_SERVER_ANNOUNCEMENT: bool = getattr(settings, 'SCRAPE_SERVER_ANNOUNCEMENT')
SERVER_PAGINATION_COUNT: int = getattr(settings, 'SERVER_PAGINATION_COUNT')


class Server_List_Base(ListView):
    """
    Base ListView for Server information
    """
    model: Server = Server

    def get_queryset(self) -> ServerManager:
        return Server.objects.filter(archived=False).order_by('-pk')

    def get(self, request: HttpRequest, *args: tuple, **kwargs: dict) -> HttpResponse:
        if request.headers.get('HX-Request') == "true":
            return super().get(request, *args, **kwargs)

        else:
            return HttpResponseRedirect('/')


class Server_Buttons(Server_List_Base):
    """
    Returns Bootstrap buttons for each server
    Buttons used to open Server Modals
    """
    paginate_by: int = SERVER_PAGINATION_COUNT


class Player_List(ListView):
    """
    Returns button showing total player count
    and Bootstrap Modal containing names of online players

    This view will also call the update_servers() method of
    the Server Manager.
    """
    model: Player = Player

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["stat_object"] = ServerStatistic.objects.get_or_create(name='gameservers-stat')[0]
        context["server_list"] = Server.objects.filter(archived=False)
        return context

    def get(self, request, *args, **kwargs):
        if request.headers.get('HX-Request') == "true":
            Server.objects.update_servers()
            return super().get(request, *args, **kwargs)

        else:
            return HttpResponseRedirect('/')


class Import_Servers(TemplateView):
    """
    Import servers
    """
    def get(self, request: HttpRequest, *args: tuple, **kwargs: dict) -> HttpResponse:
        return HttpResponseRedirect('/')

    def post(self, request: HttpRequest, *args: tuple, **kwargs: dict) -> HttpResponse:
        if not request.user.is_staff:
            return HttpResponseRedirect('/')
        
        if Server.objects.import_server_data() == False:
            return HttpResponse('<div class= "alert alert-danger">You attempted to import servers, but you did not place server_data_full.json '
                                'in the root directory of the application.</div>')

        return HttpResponse('<div class= "alert alert-success">Servers from server_data_full.json have successfully been imported.</div>')


class Export_Servers(TemplateView):
    """
    Export servers
    """
    def get(self, request: HttpRequest, *args: tuple, **kwargs: dict) -> HttpResponse:
        return HttpResponseRedirect('/')

    def post(self, request: HttpRequest, *args: tuple, **kwargs: dict) -> HttpResponse:
        if not request.user.is_staff:
            return HttpResponseRedirect('/')
        
        Server.objects.export_server_data()
        return HttpResponse('<div class= "alert alert-success">All Servers have successfully been exported to server_data_full.json.</div>')
