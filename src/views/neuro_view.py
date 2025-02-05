#  ##   ###
#  Import LIBRARIES
import flet as ft
from flet import Column, ElevatedButton, Icons, Image, MainAxisAlignment, Row, Text, Container, Colors

#  Import FILES
#  ##   ###



def NeuroView(page):
    page.title = "Neuroscience"


    #  PICTURES
    
    _nplasty_image = Image(
        src="neuroplasticity.jpg",  
        width=220,
        height=200,
        fit=ft.ImageFit.CONTAIN,
    )
    _professional_image = Image(
        src="professional.jpg",  
        width=220,
        height=200,
        fit=ft.ImageFit.CONTAIN,
    )



    # TEXT
    _intro_text = Text(
        value="I blame my pshychology teacher for introducing and making fall in love with Neuroscience. I will be forever indebted to her!", 
        width=650,
        size=20,
    )
    _headof_text = Text(
        value="Now, I am the head and founder of the Neuroscience Society at WA, where I lead discussions on research, invite guest speakers, and connect neuroscience with other disciplines.",
        width=650,
        size=20,
    )    
    _busy_life = Text(
        value="To share my enthusiasm and spread awareness, I have written various articles for the school magazine. To access my articles click the button above.",
        width=650,
        size=20,
    )

    _outro_text = Text(
        value="Outro - Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet et, ultrices sed, augue.",
        width=1500,
        size=20,
    )    


    #  A clickable icon button to download the Neuroscience articles
    _articles_button = ElevatedButton(
        width=140, 
        height=25,
        bgcolor=Colors.GREY_800,
        content=Text(value="Articles", size=18, color=Colors.ORANGE_500),
        # text="Contacts",
        # icon=Icons.CONTACT_PAGE,
        on_click=lambda e: page.go("/neuroscience"),  # Replace with your contact page route
        # on_click=lambda e: print("Contacts"),
    )

 
    #  Page content rendering
    page_content = Column(
        alignment="center",   #MainAxisAlignment.CENTER,
        expand=True,
        controls=[ 
            Row(
                alignment=MainAxisAlignment.SPACE_AROUND,
                controls=[
                   Column(
                        alignment=MainAxisAlignment.CENTER,
                        spacing=30,
                        controls=[
                            _intro_text,
                            _headof_text,
                            _articles_button,
                            _busy_life,
                            
                       ], 
                   ),
                   Column(
                        # alignment=MainAxisAlignment.SPACE_AROUND,
                        spacing=20,
                        controls=[
                            _professional_image,
                            _nplasty_image
                       ], 
                   ),

                ]
            ),
            _outro_text,
            
            
        ],

    )
    
    return page_content



