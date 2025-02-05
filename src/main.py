#  ##   ###
#  Import LIBRARIES
import flet as ft
from flet import Page

#  Import FILES
from user_controls.app_bar import NavBar
from views.FletRouter import Router

#  ##   ###



def main(page: Page):
    page.title = "Sofia Responsive Website using Python's Flet"

    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.padding = 40


    page.theme_mode = "dark"

    page.appbar = NavBar(page)
    myRouter = Router(page)

    page.on_route_change = myRouter.route_change

    page.add(myRouter.body)

    page.go("/")


if __name__ == "__main__":
    ft.app(target=main, assets_dir="assets")