#  ##   ###
#  Import LIBRARIES
import flet as ft
from flet import Column, ElevatedButton, Icons, Image, Row, Text

#  Import FILES
#  ##   ###


def VolunteeringView(page):
    page.title = "Volunteering"

    #  Image on the righthandside
    image = Image(
        src="https://plus.unsplash.com/premium_photo-1664372145541-4556b409492e?q=80&w=2069&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        # src="https://via.placeholder.com/150",  # Replace with your image URL
        width=300,
        height=300,
        fit=ft.ImageFit.CONTAIN,
    )

    # Text for the left handside
    text_one = Text(
        "I am the head and founder of the Neuroscience Society, where I lead discussions on research, invite guest speakers, and connect neuroscience with other disciplines.",
        width=300,
    )
    text_two = Text(
        "To spread awareness, I have written various articles for the school magazine. To access my articles click the button below.",
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
                            pdf_button,
                        ],
                    ),
                    image,
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
        ],
    )

    return content
