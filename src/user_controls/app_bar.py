# ##   ###
#  Import LIBRARIES
import flet as ft
from flet import (
    AppBar,
    Colors,
    Container,
    CrossAxisAlignment,
    ElevatedButton,
    Icon,
    Icons,
    MainAxisAlignment,
    Row,
    Text,
)


#  Import FILES
#  ##   ###
def NavBar(page):
    NavBar = ft.AppBar(
        leading=Row(
            alignment=MainAxisAlignment.SPACE_AROUND,
            controls=[
                Icon(Icons.TAG_FACES_ROUNDED),
                Text("  Sof", weight="bold", size=22),
                Text("IA", weight="italics", size=22, color=Colors.ORANGE_500),
            ],
        ),
        leading_width=40,
        # title=ft.Text(""),center_title=False,
        bgcolor=ft.colors.SURFACE_CONTAINER_HIGHEST,
        actions=[
            ElevatedButton("Home", on_click=lambda _: page.go("/")),
            ElevatedButton("About", on_click=lambda _: page.go("/about")),
            ElevatedButton("Music", on_click=lambda _: page.go("/music")),
            ElevatedButton("Neuroscience", on_click=lambda _: page.go("/neuroscience")),
            ElevatedButton("Coding", on_click=lambda _: page.go("/coding")),
            ElevatedButton("Contacts"),
        ],
    )

    return NavBar