import flet as ft 
from db import main_db 

def main(page: ft.Page):
    page.title = "Список покупок"
    page.theme_mode = ft.ThemeMode.LIGHT

    buy_list = ft.Column(spacing=15)
    filter_type = "all"

    def load_buy():
        buy_list.controls.clear()
        for buy_id, buy_text, completed  in main_db.get_buys(filter_type):
            buy_list.controls.append(create_buy_row(buy_id, buy_text, completed))
        
        page.update()

    def create_buy_row(buy_id, buy_text, completed_buy):
        buy_field = ft.TextField(value=buy_text, read_only=True, expand=True )

        buy_chekbox = ft.Checkbox(
            value=bool(completed_buy),
            on_change=lambda e: toggle_buy(buy_id, e.control.value)
        )

        def delete_buy(buy_id):
            main_db.delete_buy(buy_id)
            load_buy()

        delete_button = ft.IconButton(icon=ft.Icons.DELETE, on_click=lambda e: delete_buy(buy_id), icon_color=ft.Colors.RED)
        return ft.Row([
            buy_chekbox,
            buy_field,
            delete_button
        ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)

    def add_buy(_):
        if buy_input.value:
            buy_id = main_db.add_buy(buy_input.value)
            buy_list.controls.append(create_buy_row(buy_id, buy_input.value, 0 ))
            buy_input.value = ""
            page.update() 

    def toggle_buy(buy_id, is_completed_buy):
        main_db.update_buy(buy_id, completed_buy=int(is_completed_buy))
        load_buy()

    def set_filter(filter_value):
        nonlocal filter_type
        filter_type = filter_value
        load_buy()

    
    

    filter_buttons = ft.Row(controls=[
        ft.ElevatedButton('Все', on_click=lambda e: set_filter("all")),
        ft.ElevatedButton('Куплено', on_click=lambda e: set_filter("completed_buy")),
        ft.ElevatedButton('Нужно купить', on_click=lambda e: set_filter('uncompleted_buy'))
    ], alignment=ft.MainAxisAlignment.SPACE_AROUND)

   
    buy_input = ft.TextField(label="Мне нужно купить : ", expand=True)
    add_button = ft.ElevatedButton("Добавить", on_click=add_buy )

    page.add(ft.Column([
        ft.Row([buy_input, add_button], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
        filter_buttons,
        buy_list
    ]))
    load_buy()

if __name__ == "__main__":
    main_db.init_db()
    ft.app(target=main)