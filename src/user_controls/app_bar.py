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
    Container,TextButton,Page
)


#  Import FILES
#  ##   ###



def toggle_dark_mode(e):
    if page.theme_mode == "dark":
        page.theme_mode = "light"
        page.update()
    else: 
        page.theme_mode = "dark"
        page.update()


def NavBar(page: Page):
    NavBar = ft.AppBar(
        leading=Row(
            alignment=MainAxisAlignment.SPACE_AROUND,
            controls=[
                Container(width=30),
                Icon(Icons.TAG_FACES_ROUNDED),
                Text("  Sof", weight="bold", size=22),
                Text("IA", weight="italics", size=22, color=Colors.ORANGE_500),
            ],
        ),
        leading_width=40,
        # title=ft.Text(""),center_title=False,
        bgcolor=ft.colors.SURFACE_CONTAINER_HIGHEST,
        actions=[
            Row(
                alignment=MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    ElevatedButton("Home", on_click=lambda _: page.go("/")),
                    ElevatedButton("About", on_click=lambda _: page.go("/about")),
                    ElevatedButton("Music", on_click=lambda _: page.go("/music")),
                    ElevatedButton("Neuroscience", on_click=lambda _: page.go("/neuroscience")),
                    ElevatedButton("Coding", on_click=lambda _: page.go("/coding")),
                    ElevatedButton("Volunteering", on_click=lambda _: page.go("/volunteering")),
                    ElevatedButton("Contacts", on_click=lambda _: page.go("/contacts")),
                    # TextButton("Light/Dark Mode", icon=Icons.WB_SUNNY_OUTLINED, on_click=toggle_dark_mode),
                    TextButton(icon=Icons.WB_SUNNY_OUTLINED, on_click=toggle_dark_mode),
                ],
            
            ),
            Container(width=50),
        ],
    )

    return NavBar


            # ElevatedButton("Home", on_click=lambda _: page.go("/")),
            # Container(width=10),
            # ElevatedButton("About", on_click=lambda _: page.go("/about")),
            # Container(width=10),
            # ElevatedButton("Music", on_click=lambda _: page.go("/music")),
            # Container(width=10),
            # ElevatedButton("Neuroscience", on_click=lambda _: page.go("/neuroscience")),
            # Container(width=10),
            # ElevatedButton("Coding", on_click=lambda _: page.go("/coding")),
            # Container(width=10),
            # ElevatedButton("Volunteering", on_click=lambda _: page.go("/volunteering")),
            # Container(width=10),
            # ElevatedButton("Contacts"),
            # Container(width=10),