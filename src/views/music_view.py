#  ##   ###
#  Import LIBRARIES
import flet as ft
from flet import Column, ElevatedButton, Icons, Image, MainAxisAlignment, Row, Text, Container, Colors

#  Import FILES
#  ##   ###


# TODO: Harry Styles


def MusicView(page):
    page.title = "Music - My love of music"

    #  PICTURES
    _solo_image = Image(
        src="solo.jpg",
        width=250,
        height=250,
        fit=ft.ImageFit.CONTAIN,
    )

        #  Royal Albert Hall
    _rah_image = Image(
        src="rah.jpg",
        width=300,
        height=300,
        fit=ft.ImageFit.CONTAIN,
    )

    # TEXT
    _intro = Text(
        value="I started playing the clarinet at the age of 5 and piano at 8. Now, I play at a semi-professional level. Next week I will be taking the ABRSM Music Diploma",
        width=680,
        size=20,
    )
    _first_clarinet = Text(
        value="As the first clarinet in my school\’s symphony orchestra, I enjoy leading and shaping the ensemble’s sound.",
        width=680,
        size=20,
    )

    _solo_text = Text(
        width=480,
        size=20,
        value="Throughout the years, I have performed in many concerts. I started big, at the Royal Albert Hall ",
        spans=[
                ft.TextSpan(
                    "(if you sqeeze your eyes you can see me on the big screen in the picture on the left!)",
                    ft.TextStyle(italic=True, size=18, color=ft.Colors.INDIGO_600),
                    ),
                    ft.TextSpan(
                        spans=[ft.TextSpan(" while more recently I played a solo of the Mozart Clarinet Concerto. Performing as a soloist has taught me to communicate through music, making each performance a rewarding experience.",),],
                    )        
        ],    
    )
    _challenge_text = Text(
         value="Recently, I have learned challenging pieces like the Weber Clarinet Concerto and Brahms Op. 120 No. 1, which have deepened my musical expression. ",
        width=600,
        size=20,
    )
    _outro_text = Text(
        value="Music remains a significant part of my life, allowing me to express myself beyond words.",
        width=600,
        size=20,
    )    
    # _____text = Text(
    #     "Throughout the years, I have performed in many concerts. I started big, at the Royal Albert Hall while more recently I plyed a solo of the Mozart Clarinet Concerto.",
    #     width=600,
    #     size=20,
    # )



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
            _intro,
            Container(height=18),
            _first_clarinet,
            Container(height=18),
            Row(
                alignment=MainAxisAlignment.SPACE_EVENLY ,
                expand=True,
                # vertical_alignment="center",
                controls=[
                _rah_image,
                _solo_text,
                # Text("Hello Mum!"),
                _solo_image,
                ], 
            ),
            Container(height=18),
            _challenge_text,
            Container(height=18),
            _outro_text
        ],

    )
    

    return page_content
