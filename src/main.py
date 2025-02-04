import flet as ft
from flet import Page, Container, Text, AppBar

def main(page:Page):
	page.appbar = AppBar(title=Text("New app!!!"))
	page.add(
		Container(
			bgcolor="red",
			padding=10,
			alignment=ft.alignment.center,
			content=Text("hello",size=30,weight="bold"),
			),
		Container(
			bgcolor="blue",
			padding=10,
			alignment=ft.alignment.center,
			content=Text("mum!",size=50,weight="bold"),
			),
		),
	

if __name__ == "__main__":
	ft.app(main)