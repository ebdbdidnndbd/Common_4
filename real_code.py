import flet as ft

def build_ui(page):
    # تنظيف الشاشة وضبط الإعدادات
    page.clean()
    page.title = "Common V8 Global"
    page.bgcolor = "#0a0a0a" # لون أسود سيبراني خفيف
    page.padding = 20
    page.theme_mode = ft.ThemeMode.DARK

    # تصميم الواجهة بدون صور خارجية ثقيلة (لضمان السرعة)
    content = ft.Column(
        controls=[
            ft.Icon(ft.icons.SECURITY, size=110, color=ft.colors.CYAN_400),
            ft.Text("COMMON V8 GLOBAL", size=28, weight="bold", color=ft.colors.CYAN_400, font_family="Consolas"),
            ft.Text("SYSTEM ONLINE - SECURE", size=14, color=ft.colors.GREEN_400, letter_spacing=2),
            ft.Divider(height=40, color=ft.colors.TRANSPARENT),
            
            # زر تفعيل النظام
            ft.ElevatedButton(
                content=ft.Row([ft.Icon(ft.icons.SHIELD_OUTLINED), ft.Text("تفعيل نظام الحماية", size=18)], alignment=ft.MainAxisAlignment.CENTER),
                bgcolor=ft.colors.BLUE_900,
                color=ft.colors.WHITE,
                width=280,
                height=60,
                style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10))
            ),
            ft.SizedBox(height=15),
            
            # زر سحب البيانات
            ft.ElevatedButton(
                content=ft.Row([ft.Icon(ft.icons.DATA_USAGE), ft.Text("سحب البيانات", size=18)], alignment=ft.MainAxisAlignment.CENTER),
                bgcolor=ft.colors.RED_900,
                color=ft.colors.WHITE,
                width=280,
                height=60,
                style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10))
            ),
            
            ft.Divider(height=50, color=ft.colors.TRANSPARENT),
            ft.Text("Developed by Hussein - Iraq", size=12, color=ft.colors.WHITE54)
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        expand=True
    )

    page.add(
        ft.Container(
            content=content,
            alignment=ft.alignment.center,
            expand=True
        )
    )
    page.update()
