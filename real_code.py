import flet as ft

def build_ui(page):
    # تنظيف الشاشة بالكامل من أي بقايا
    page.clean()
    
    # إعدادات شاشة واضحة
    page.bgcolor = "#ffffff" # أبيض حتى نميزه فوراً
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # إضافة عناصر كبيرة وواضحة
    page.add(
        ft.Icon(ft.icons.VERIFIED_USER, size=120, color=ft.colors.GREEN_700),
        ft.Text("تم الاختراق بنجاح!", size=35, weight=ft.FontWeight.BOLD, color=ft.colors.BLUE_900),
        ft.Text("نظام V8 الهوائي يعمل 100%", size=18, color=ft.colors.BLACK87),
        ft.Divider(height=30, color=ft.colors.TRANSPARENT),
        ft.ElevatedButton(
            "فحص النظام", 
            icon=ft.icons.ROCKET_LAUNCH,
            bgcolor=ft.colors.RED_700,
            color=ft.colors.WHITE,
            width=200,
            height=50
        )
    )
    page.update()
