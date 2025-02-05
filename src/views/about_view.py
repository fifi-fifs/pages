#  ##   ###
#  Import LIBRARIES
import flet as ft
from flet import Column, ElevatedButton, Icons, Image, MainAxisAlignment, Row, Text, Container, Colors

#  Import FILES
#  ##   ###


def AboutView(page):
    page.title = "This page is all about ME!"

    #  PICTURES
    _mun_image = Image(
        src="mun.png",  # Replace with your image URL
        width=350,
        height=300,
        fit=ft.ImageFit.CONTAIN,
    )
    _scout_image = Image(
        src="scout.jpg",  # Replace with your image URL
        width=220,
        height=200,
        fit=ft.ImageFit.CONTAIN,
    )
    _youmanity_image = Image(
        src="youmanity.jpg",  # Replace with your image URL
        width=220,
        height=200,
        fit=ft.ImageFit.CONTAIN,
    )

    # _solo_image = Image(
    #     src="solo.jpg",
    #     width=250,
    #     height=250,
    #     fit=ft.ImageFit.CONTAIN,
    # )



    # TEXT
    _intro = Text(
        value="Only few knows that my full name is Sofia Caterina. I am preparing for my A-Level: Math, Physics, Chemistry and Psychology + EPQ in Neuroscience. My GCSE were Math, English, English Literature, Physics, Chemistry, Biology, Computer Science, History, Latin, Geography, Spanish, Italian.",
        width=650,
        size=20,
    )
    _busy_life = Text(
        value="Being a student ad Wycombe Abbey is not for the faint of heart. Academic schedule is incredibly busy, timing is tight and on top of all one has all the music, clubs, sport and chariteable activities.",
        width=650,
        size=20,
    )
    _mun_text = Text(
        width=600,
        size=20,
        value="The actvities i enjoyed the most in the past few years:\n    - Funding the Neuroscience Society. ",
        spans=[
                ft.TextSpan(
                    "\n            Press the button to see my effort in Neuroscience",
                    ft.TextStyle(italic=True, size=16, color=ft.Colors.INDIGO_400),
                    ),
                    ft.TextSpan(
                        spans=[ft.TextSpan("\n    - Taking part to the Model United Nations.",),],
                    )        
        ],    
    )
    _past_life = Text(
        width=480,
        size=20,
        value="In my past life i enjoyed many activities:",
        spans=[
            ft.TextSpan("\n   - Scouting", ft.TextStyle(italic=True, size=18, color=ft.Colors.GREEN_600),),
            ft.TextSpan("\n   - Music", ft.TextStyle(italic=True, size=18, color=ft.Colors.INDIGO_600),),        
            ft.TextSpan("\n   - Coding", ft.TextStyle(italic=True, size=18, color=ft.Colors.ORANGE_600),),        
            ft.TextSpan("\n   - Cycling and swimming", ft.TextStyle(italic=True, size=18, color=ft.Colors.CYAN_600),),        
            ft.TextSpan("\n   - Volunteering and chariteable work", ft.TextStyle(italic=True, size=18, color=ft.Colors.RED_600),),        
        ],    
    )


    _outro_text = Text(
        value="Outro - Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet, adipiscing 1  et, ultrices sed, augue.",
        width=1500,
        size=20,
    )    
    # _____text = Text(
    #     "Throughout the years, I have performed in many concerts. I started big, at the Royal Albert Hall while more recently I plyed a solo of the Mozart Clarinet Concerto.",
    #     width=600,
    #     size=20,
    # )


    #  A clickable icon button to move to Neuroscience
    _neuroscience_button = ElevatedButton(
        width=140, 
        height=25,
        bgcolor=Colors.GREY_800,
        content=Text(value="Neuroscience", size=18, color=Colors.ORANGE_500),
        # text="Contacts",
        # icon=Icons.CONTACT_PAGE,
        on_click=lambda e: page.go("/neuroscience"),  # Replace with your contact page route
        # on_click=lambda e: print("Contacts"),
    )
    _music_button = ElevatedButton(
        width=80, 
        height=25,
        bgcolor=Colors.GREY_800,
        content=Text(value="Music", size=18, color=Colors.ORANGE_500),
        on_click=lambda e: page.go("/music"),  # Replace with your music page route
        # on_click=lambda e: print("Music"),
    )
    _volunteering_button = ElevatedButton(
        width=130, 
        height=25,
        bgcolor=Colors.GREY_800,
        content=Text(value="Volunteering", size=18, color=Colors.ORANGE_500),
        # text="Contacts",
        # icon=Icons.CONTACT_PAGE,
        on_click=lambda e: page.go("/volunteering"),  # Replace with your contact page route
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
                    _intro,
                    _busy_life,
                ]
            ),
            Container(height=18),
            Row(
                alignment=MainAxisAlignment.SPACE_AROUND ,
                controls=[
                    _mun_image,
                    _mun_text,
                    _neuroscience_button,
                ]
            ),
            Row(
                alignment=MainAxisAlignment.SPACE_AROUND,
                controls=[
                    _past_life,
                    _scout_image,
                    _music_button,
                    _youmanity_image,
                    _volunteering_button,
                ],

            ),
            
            Container(height=18),
            _outro_text,
            Container(height=18),
        ],

    )
    
    return page_content

