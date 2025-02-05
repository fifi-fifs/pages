#  ##   ###
#  Import LIBRARIES
import flet as ft
from flet import Text, TextField, ElevatedButton,Column,Row ,Colors,Icons,Container

#  Import FILES
#  ##   ###


def ContactsView(page: ft.Page):
    page.title = "Contact Me"
    # page.horizontal_alignment = "center"

    contacts_content = Column(
        width=650,
        alignment="centre",
        controls=[
            Text("Contact Me", style=ft.TextStyle(size=30)),
            Container(height=20),
            TextField(label="Name", icon=Icons.PERSON, border_color=Colors.AMBER),
            Container(height=20),
            TextField(label="Email", icon=Icons.EMAIL, border_color=Colors.AMBER), 
            Container(height=20),
            TextField(label="Message", multiline=True, icon=Icons.MESSAGE, border_color=Colors.AMBER),
            Container(height=30),
            Row(
                alignment="end",
                controls=[
                    ElevatedButton(content=Text("Submit", size=22, color=Colors.AMBER_500),),
                ],
            ),
        ],
        expand=True,
    )
    
    
    return contacts_content