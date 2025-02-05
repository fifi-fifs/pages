#  ##   ###
#  Import LIBRARIES
import flet as ft
from flet import Page

#  Import FILES
from views.about_view import AboutView
from views.coding_view import CodingView
from views.index_view import IndexView
from views.music_view import MusicView
from views.neuro_view import NeuroView
from views.volunteering_view import VolunteeringView
from views.contacts_view import ContactsView
# from views.contacts_view import SettingsView


#  ##   ###


class Router:
    def __init__(self, page):
        self.page = page
        self.ft = ft
        self.routes = {
            "/": IndexView(page),
            "/about": AboutView(page),
            "/music": MusicView(page),
            "/neuroscience": NeuroView(page),
            "/coding": CodingView(page),
            "/volunteering": VolunteeringView(page),
            "/contacts": ContactsView(page),
            
        }
        self.body = ft.Container(content=self.routes["/"])

    def route_change(self, route):
        self.body.content = self.routes[route.route]
        self.body.update()
