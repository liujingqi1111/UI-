import flet as ft

def main(page: ft.Page):
    # 设置窗口大小和无边框
    page.window_width = 400
    page.window_height = 600
    page.window_frameless = True
    # 初始化内容
    content = ft.Column(
        [
            ft.Text("Body!", size=20),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    # 输入框和列表视图
    input_text = ft.TextField(label="输入商品名称")
    items_list = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)

    data_table = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("商品名称")),
            ft.DataColumn(ft.Text("是否勾选")),
        ],
        rows=[],
    )

    # 更新页面内容的函数
    def navigate(e):
        if page.navigation_bar.selected_index == 0:
            content.controls = [
                ft.Column([
                    input_text,
                    ft.Column(
                        [items_list],
                        height=page.window_height - 220,  # 减去导航栏和输入框的高度
                        scroll=ft.ScrollMode.AUTO
                    ),
                ], alignment=ft.MainAxisAlignment.START)
            ]
        elif page.navigation_bar.selected_index == 1:
            content.controls = [
                ft.Column(
                    [
                        ft.Text("购物清单", size=18, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                        ft.Container(
                            content=ft.Column(
                                [
                                    ft.Column(
                                        [data_table],
                                        height=page.window_height - 220,  # 减去导航栏和标题的高度
                                        scroll=ft.ScrollMode.AUTO
                                    ),
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER
                            ),
                            padding=20,
                            alignment=ft.alignment.center
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                )
            ]
        else:
            content.controls = [
                ft.Text("关于内容！", size=20),
                ft.Divider(),
                ft.Image(src="logo传奇开心果.png", width=100, height=100),
                ft.Column([
                    ft.Text("购物清单助手移动应用app1.0", size=14),
                ], alignment=ft.MainAxisAlignment.START),
            ]

        page.update()

    # 设置导航栏
    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(
                icon=ft.icons.HOME,
                selected_icon=ft.icons.HOME_ROUNDED,
                label="主页"
            ),
            ft.NavigationBarDestination(
                icon=ft.icons.LIST,
                selected_icon=ft.icons.LIST_ALT,
                label="清单"
            ),
            ft.NavigationBarDestination(
                icon=ft.icons.INFO,
                selected_icon=ft.icons.INFO_ROUNDED,
                label="关于"
            ),
        ],
        on_change=navigate
    )

    # 设置 AppBar
    def add_action(e):
        if input_text.value:
            item = ft.ListTile(
                leading=ft.Checkbox(),
                title=ft.Text(input_text.value),
                on_click=lambda e: toggle_checkbox(e.control),
            )
            items_list.controls.append(item)
            input_text.value = ""
            page.update()

    def delete_action(e):
        checked_items = [item for item in items_list.controls if item.leading.value]
        for item in checked_items:
            items_list.controls.remove(item)
        page.update()

    def save_action(e):
        saved_items = [item for item in items_list.controls if item.leading.value]
        update_data_table(saved_items)
        page.update()

    def exit_app(e):
        page.window_close()

    def toggle_checkbox(control):
        control.leading.value = not control.leading.value
        page.update()

    def update_data_table(items):
        data_table.rows.clear()
        for item in items:
            data_table.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(item.title.value)),
                        ft.DataCell(ft.Text("是" if item.leading.value else "否")),
                    ]
                )
            )
        page.update()

    page.appbar = ft.AppBar(
        leading=ft.Row(
            [
                ft.Container(
                    content=ft.Text("购物清单助手1.0", size=14, weight=ft.FontWeight.BOLD),
                    padding=ft.padding.only(left=20),  # 设置左边的 padding 为 20
                )
            ],
            alignment=ft.MainAxisAlignment.START
        ),
        center_title=False,
        bgcolor=ft.colors.SURFACE_VARIANT,
        actions=[
            ft.IconButton(ft.icons.ADD, on_click=add_action),
            ft.IconButton(ft.icons.DELETE, on_click=delete_action),
            ft.IconButton(ft.icons.SAVE, on_click=save_action),
            ft.IconButton(ft.icons.CLOSE, on_click=exit_app),
        ],
        toolbar_height=60  # 可以调整高度以适应更多的空间
    )

    # 包裹内容在 SafeArea 组件内
    safe_area_content = ft.SafeArea(content)

    # 添加内容到页面
    page.add(safe_area_content)

    # 初始化导航栏
    page.navigation_bar.selected_index = 0
    navigate(None)

# 启动应用
ft.app(target=main)
