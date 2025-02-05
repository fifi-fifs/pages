#  ##   ###
#  Import LIBRARIES
import flet as ft
from flet import Column, ElevatedButton, Icons, Image, MainAxisAlignment, Row, Text, Container, Colors

#  Import FILES
#  ##   ###




def IndexView(page):
    page.title = "Home Page"

    #  TEXT - Left hand-side
    #  Citation + Author text
    citation_text = Text(
        "\"Imagination is more important than knowledge. For knowledge is limited, whereas imagination embraces the entire world, stimulating progress, giving birth to evolution.\"",
        size=35,
        width=650,  # Adjust width as needed
        text_align="center",
    )

    author_text = Text(
        "Albert Einstein",
        width=650,  # Same width as citation
        size=20,
        text_align="right",
          # Add space above
    )

    #  A clickable icon button to move to contacts
    contact_button = ElevatedButton(
        width=155, 
        height=28,
        content=Text(value="Contact Me", size=22, color=Colors.AMBER_500,bgcolor=Colors.GREY_800),
        # text="Contacts",
        # icon=Icons.CONTACT_PAGE,
        on_click=lambda e: page.go("/contacts"),  # Replace with your contact page route
        # on_click=lambda e: print("Contacts"),
    )

    #  IMAGE -  Righthandside
    home_image = Image(
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
                        spacing=35,
                        controls=[
                            citation_text, 
                            author_text,
                            Container(height=30),
                            Row(
                                alignment=MainAxisAlignment.CENTER,
                                controls=[
                                    contact_button,
                                ],
                            ),
                        ],
                        
                    ),
                
                # Text("Hello Mum!"),
                home_image


                ], 
        
            ),
        ],

        
       
       
        # alignment="center",
        # bgcolor=Colors.BLACK,
    )
    

    return page_content
