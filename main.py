import flet as ft
import typer


def load_txt() -> str:
    with open("./static/sample.txt", "r", encoding="utf8") as txt_file:
        txt_content = txt_file.read()
    return txt_content


def main(page: ft.Page):
    page.title = "Flet counter example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = "dark"

    txt_number = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)

    txt_content = load_txt()

    def minus_click(e):
        txt_number.value = str(int(txt_number.value) - 1)
        page.update()

    def plus_click(e):
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()

    def size_click(e):
        print(page.width, page.height)

    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.REMOVE, on_click=minus_click),
                txt_number,
                ft.IconButton(ft.icons.ADD, on_click=plus_click),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        ft.IconButton(ft.icons.CHECK, on_click=size_click),
        ft.Text(value=txt_content),
    )


def flet_main():
    ft.app(target=main)


if __name__ == "__main__":
    typer.run(flet_main)
