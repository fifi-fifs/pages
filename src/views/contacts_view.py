#  ##   ###
#  Import LIBRARIES
import flet as ft
from flet import Text, TextField, ElevatedButton,Column,Row ,Colors,Icons

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
            TextField(label="Name", icon=Icons.PERSON),
            TextField(label="Email", icon=Icons.EMAIL), 
            TextField(label="Message", multiline=True, icon=Icons.MESSAGE, border=Colors.AMBER),
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