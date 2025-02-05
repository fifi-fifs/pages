#  ##   ###
#  Import LIBRARIES
import flet as ft
from flet import Column, ElevatedButton, Icons, Image, Row, Text

#  Import FILES
#  ##   ###


def AboutView(page):
    page.title = "Neuroscience Society"

    #  Image on the righthandside
    image = Image(
        src="mun.png",  # Replace with your image URL
        width=300,
        height=300,
        fit=ft.ImageFit.CONTAIN,
    )

    # Text for the left handside
    text_one = Text(
        "In my free time, I enjoy coding and even built this website myself.",
        width=300,
    )
    text_two = Text(
        "Recently, I completed the 100 Days of Python challenge, avery hard coding course which strengthened my problem-solving skills and deepened my understanding of programming.",
        width=300,
    )

    text_three = Text(
        "This website is a direct result of the above course. In addition this course inspired me to write articles and my EPQ.",
        width=300,
    )
    text_four = Text(
        "Learning about data science has been particularly valuable, as it has helped me analyze neuroscience data more effectively. By applying coding to neuroscience, I can explore complex patterns in brain activity and behavior.",
        width=300,
    )

    #  A clickable icon button to move to contacts
    contact_button = ElevatedButton(
        icon=Icons.CONTACT_PAGE,
        text="Contacts",
        on_click=lambda e: print("Contacts"),
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
                        ],
                    ),
                    image,
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
        ],
    )

    return content
