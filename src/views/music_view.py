#  ##   ###
#  Import LIBRARIES
import flet as ft
from flet import Column, ElevatedButton, Icons, Image, Row, Text

#  Import FILES
#  ##   ###


def MusicView(page):
    page.title = "Music - My love of music"

    #  Image on the righthandside
    image = Image(
        src="https://images.unsplash.com/photo-1597656370793-12900b6d9a28?q=80&w=1364&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D        ",
        width=300,
        height=300,
        fit=ft.ImageFit.CONTAIN,
    )

    # Text for the left handside
    text_one = Text(
        "I play two instruments at a semi-professional level and have performed in many concerts, including a solo of the Mozart Clarinet Concerto.",
        width=300,
    )
    text_two = Text(
        "        As the first clarinet in my school’s symphony orchestra, I enjoy leading and shaping the ensemble’s sound. ",
        width=300,
    )
    text_three = Text(
        "Recently, I have learned challenging pieces like the Weber Clarinet Concerto and Brahms Op. 120 No. 1, which have deepened my musical expression. ",
        width=300,
    )
    text_four = Text(
        "Performing as a soloist has taught me to communicate through music, making each performance a rewarding experience. ",
        width=300,
    )
    text_five = Text(
        "Music remains a significant part of my life, allowing me to express myself beyond words.",
        width=300,
    )

    #  A clickable icon button to display ther PDF articles
    pdf_button = ElevatedButton(
        icon=Icons.PICTURE_AS_PDF,
        text="Articles",
        on_click=lambda e: print("PDF icon clicked"),
    )

    #  Page content rendering
    content = Column(
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment="center",
        controls=[
            Row(
                controls=[
                    Column(
                        alignment="center",
                        horizontal_alignment="center",
                        spacing=15,
                        controls=[
                            text_one,
                            text_two,
                            text_three,
                            text_four,
                            text_five,
                        ],
                    ),
                    image,
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
        ],
    )

    return content
