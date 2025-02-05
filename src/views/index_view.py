#  ##   ###
#  Import LIBRARIES
import flet as ft
from flet import Column, ElevatedButton, Icons, Image, MainAxisAlignment, Row, Text, Container, Colors

#  Import FILES
#  ##   ###




def IndexView(page):
    page.title = "Home Page"

    #  TEXT - Left hand-side
    #  Salutation + name
    _salutation_text = Text(
        "Hi, I am",
        size=50,
        weight="bold",
        text_align="center",
    )
    _name_text = Text(
        "Sofia ...",
        size=50,
        color=Colors.ORANGE_500,
        weight="bold",
        text_align="center",
    )

    #  Citation + Author text
    _citation_text = Text(
        "\"Imagination is more important than knowledge. For knowledge is limited, whereas imagination embraces the entire world, stimulating progress, giving birth to evolution.\"",
        size=35,
        width=650,  # Adjust width 
        text_align="center",
    )

    _author_text = Text(
        "Albert Einstein",
        width=650,  # Same width as citation
        size=20,
        text_align="right",
          # Add space above
    )

    #  A clickable icon button to move to contacts
    _contact_button = ElevatedButton(
        width=155, 
        height=30,
        bgcolor=Colors.GREY_800,
        content=Text(value="Contact Me", size=22, color=Colors.ORANGE_500),
        # text="Contacts",
        # icon=Icons.CONTACT_PAGE,
        on_click=lambda e: page.go("/contacts"),  # Replace with your contact page route
        # on_click=lambda e: print("Contacts"),
    )

    #  IMAGE -  Righthandside
    _home_image = Image(
        src="harvard_library.jpg",
        width=600,  # Adjust width as needed
        height=500,  # Adjust height as needed
        fit=ft.ImageFit.CONTAIN,
    )



    #  Page content rendering
    page_content = Column(
        alignment="center",   #MainAxisAlignment.CENTER,
        expand=True,
        controls=[    
            Row(
                alignment=MainAxisAlignment.SPACE_EVENLY ,
                expand=True,
                # vertical_alignment="center",
                controls=[
                    Column(
                        alignment="center",  #MainAxisAlignment.CENTER,
                        expand=True,
                        spacing=30,
                        controls=[
                            Row(
                                alignment=MainAxisAlignment.START,
                                controls=[ 
                                    _salutation_text,
                                    _name_text,]
                                ),
                            Container(height=30,),
                            _citation_text, 
                            _author_text,
                            Row(
                                alignment="center",   # alignment=MainAxisAlignment.CENTER,
                                controls=[
                                    _contact_button,
                                ],
                            ),
                        ],
                        
                    ),
                
                # Text("Hello Mum!"),
                _home_image


                ], 
        
            ),
        ],

    )
    

    return page_content
