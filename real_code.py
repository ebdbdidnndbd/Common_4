import flet as ft

def build_ui(page):
    # تنظيف الشاشة وضبط الإعدادات
    page.clean()
    page.title = "Common V8 Global"
    page.padding = 0
    page.theme_mode = ft.ThemeMode.DARK

    # روابط الصور (تقدر تغيرها بروابط صورك الخاصة بعدين)
    # خلفية سيبرانية متحركة (GIF)
    bg_url = "https://i.pinimg.com/originals/2b/30/4e/2b304e2eb275218d89e52e507ee8f0de.gif" 
    # شعار احترافي
    logo_url = "https://cdn-icons-png.flaticon.com/512/3208/3208726.png"

    # تصميم الواجهة والأزرار
    content = ft.Container(
        content=ft.Column(
            [
                ft.Image(src=logo_url, width=130, height=130, fit=ft.ImageFit.CONTAIN),
                ft.Text("COMMON V8 GLOBAL", size=32, weight=ft.FontWeight.BOLD, color=ft.colors.CYAN_400),
                ft.Text("SYSTEM ONLINE - SECURE CONNECTION", size=12, color=ft.colors.GREEN_400, letter_spacing=2),
                ft.Divider(height=40, color=ft.colors.TRANSPARENT),
                
                # زر تفعيل النظام
                ft.ElevatedButton(
                    content=ft.Row([ft.Icon(ft.icons.SHIELD_OUTLINED), ft.Text("تفعيل نظام الحماية", size=18)], alignment=ft.MainAxisAlignment.CENTER),
                    bgcolor=ft.colors.BLUE_900,
                    color=ft.colors.WHITE,
                    width=260,
                    height=55,
                    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=8))
                ),
                ft.SizedBox(height=15),
                
                # زر سحب البيانات
                ft.ElevatedButton(
                    content=ft.Row([ft.Icon(ft.icons.DATA_USAGE), ft.Text("سحب البيانات", size=18)], alignment=ft.MainAxisAlignment.CENTER),
                    bgcolor=ft.colors.RED_900,
                    color=ft.colors.WHITE,
                    width=260,
                    height=55,
                    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=8))
                ),
                
                ft.Divider(height=50, color=ft.colors.TRANSPARENT),
                ft.Text("Developed by Hussein - Iraq", size=12, color=ft.colors.WHITE54)
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        alignment=ft.alignment.center,
        expand=True,
        # طبقة تظليل خفيفة حتى الأزرار والنصوص تبين واضحة فوق الخلفية المتحركة
        bgcolor=ft.colors.with_opacity(0.6, ft.colors.BLACK) 
    )

    # دمج الخلفية المتحركة مع الواجهة
    page.add(
        ft.Stack(
            [
                # الصورة المتحركة في الخلف
                ft.Image(src=bg_url, fit=ft.ImageFit.COVER, expand=True, width=page.width, height=page.height),
                # الواجهة فوقها
                content
            ],
            expand=True
        )
    )
    page.update()
