#  ##   ###
#  Import LIBRARIES
import flet as ft
from flet import Column, ElevatedButton, Icons, Image, MainAxisAlignment, Row, Text, Container, Colors

#  Import FILES
#  ##   ###

 #  ===========================
# TODO:  YOUMANITY
 #  ===========================

def VolunteeringView(page):
    page.title = "Volunteering"



    #  PICTURES
    _chesterfield_image = Image(
        src="chesterfield.jpg",  
        width=350,
        height=300,
        fit=ft.ImageFit.CONTAIN,
    )
    _centralaid_image = Image(
        src="centralaid.jpeg",  
        width=220,
        height=200,
        fit=ft.ImageFit.CONTAIN,
    )
    _youmanity_image = Image(
        src="yougroup.jpg",  
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
    _intro_text = Text(
        value="Volunteering has always been a big part of my life. I started young. I was 9 when i realised most of my friends could not afford music lessons. Therefore, i lost no time in starting a charity to address this problem.",
        width=650,
        size=20,
    )
    _busy_life = Text(
        value="I soon learned what a pair of sparly eyes, a good accent and a lot of drive can do for fundraising. In a couple of months I was able to get 5 pianos and 5 volunteers that could teach basic lessons to children from deprived background. It was a great and fulfilling experience and i never looked back.", 
        width=650,
        size=16, 
        color=ft.Colors.BLUE_600,
    )
    _fulfilling_life = Text(
        value="More recently, one deeply rewarding experience that has helped me grow has been working with Pranav, a non verbal autistic child, and other disabled children, adapting my communication to their needs i could nurture their innate curiosity whilst ensure they feel supported.\nAdditionally, I have helped underachieving primary school children improve their reading skills, which has strengthened my patience and ability to teach effectively. Recently, I was honored to receive the Best Volunteer award at this primary school, recognizing my dedication to supporting young learners. These experiences have shaped my ability to mentor others, adapt to challenges, and make a meaningful impact in my community.",
        width=650,
        size=20,
    )
#One deeply rewarding experience that has helped me grow.
    _youmanity_text = Text(
        value="Now I am the young Ambassador for Youmanity, a charity that celebrates equality, support social inclusion and promote human rights by delivering cultural project.",
        width=650,
        size=20,
    )

    _centralaid_text = Text(
        width=650,
        size=20,
        value="Last year, with other representative of my school charity, we collected the King’s Award for Voluntary Service. This is the highest award a voluntary group can receive in the UK and equivalent to an MBE.",
                spans=[
                ft.TextSpan(
                    " The charity was established in 1906 by Dame Frances Dove, Wycombe Abbey’s founding headmistress, whose aim was to alleviate poverty. Her mission has been carried through to the present day.",
                    ft.TextStyle(italic=True, size=16, color=ft.Colors.GREEN_600),
                    ),     
        ],    
    )

    _outro_text = Text(
        value="Outro - Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet, adipiscing 1  et, ultrices sed, augue.",
        width=1500,
        size=20,
    )    


 
    #  Page content rendering
    page_content = Column(
        alignment="center",   #MainAxisAlignment.CENTER,
        expand=True,
        controls=[ 
            Row(
                alignment=MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    Column(
                       controls=[
                           _intro_text,
                           _busy_life,
                           _fulfilling_life,
                           _youmanity_text,
                   ]),
                    Column(
                       controls=[
                           Row(controls=[
                                _youmanity_image,
                                _chesterfield_image,
                           ]),
                           _centralaid_text,
                           _centralaid_image,
                   ]),
                ], 
            ),
            _outro_text,
            Container(height=18),
        ],

    )
    
    return page_content


        # "The charity was established in 1906 by Dame Frances Dove, Wycombe Abbey’s founding headmistress, whose aim was to alleviate poverty. Her mission has been carried through to the present day with the success of the charity and the large number of people it helps",

        # 