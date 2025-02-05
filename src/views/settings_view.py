#  ##   ###
#  Import LIBRARIES
import flet as ft
from flet import Column, TextButton, Row, Text, IconButton, Icons

#  Import FILES
#  ##   ###



def SettingsView(page):
    page.title = "Settings"

    def toggle_dark_mode(e):
        if page.theme_mode == "dark":
            page.theme_mode = "light"
            page.update()
        else: 
            page.theme_mode = "dark"
            page.update()

    def exit_app(e):
        page.window_destroy()
    
    
    content = Column(
        controls=[
            Row(
                controls=[
                    Text("My Settings", size=30), 
                    IconButton(icon=Icons.SETTINGS_ROUNDED, icon_size=30),
                ], 
                alignment=ft.MainAxisAlignment.CENTER
            ),
            Row(
                controls=[
                    TextButton("Light/Dark Mode", icon=Icons.WB_SUNNY_OUTLINED, on_click=toggle_dark_mode)
                ],
            ),
            Row(
                controls=[
                    TextButton("Exit Application", icon=Icons.CLOSE, on_click=exit_app, icon_color="red")
                ]
            ),
        ]
    )
    
    
    return content
