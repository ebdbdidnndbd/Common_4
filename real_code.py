import traceback

def build_ui(page):
    try:
        # 1. تنظيف الشاشة
        page.controls.clear()
        
        # 2. إعدادات الشاشة السيبرانية المضمونة
        page.title = "Common V8 Hussein"
        page.bgcolor = "#050505" 
        page.padding = 20
        page.theme_mode = ft.ThemeMode.DARK
        
        # 3. تصميم واجهة V8 الاحترافية السريعة
        main_content = ft.Column(
            controls=[
                ft.Icon(ft.icons.SHIELD, size=110, color=ft.colors.CYAN_400),
                ft.Text("COMMON V8 GLOBAL", size=28, weight=ft.FontWeight.BOLD, color=ft.colors.CYAN_400, font_family="Consolas"),
                ft.Text("SYSTEM ONLINE - SECURE", size=14, color=ft.colors.GREEN_400, letter_spacing=2),
                ft.Divider(height=40, color=ft.colors.TRANSPARENT),
                
                ft.ElevatedButton(
                    content=ft.Row([ft.Icon(ft.icons.ROCKET_LAUNCH), ft.Text("تفعيل نظام V8", size=18)], alignment=ft.MainAxisAlignment.CENTER),
                    bgcolor=ft.colors.BLUE_900,
                    color=ft.colors.WHITE,
                    width=280,
                    height=60,
                    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10))
                ),
                ft.SizedBox(height=15),
                
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
        )

        # 4. تجميع الواجهة
        page.add(
            ft.Container(
                content=main_content,
                alignment=ft.alignment.center,
                expand=True
            )
        )
        page.update()

    except Exception as e:
        # 5. صائد الأخطاء: يمنع الشاشة السوداء ويظهر تفاصيل العطل
        page.controls.clear()
        page.bgcolor = ft.colors.BLACK
        page.add(
            ft.Icon(ft.icons.WARNING_AMBER_ROUNDED, size=80, color=ft.colors.RED_500),
            ft.Text("تم اكتشاف خطأ في الواجهة!", size=22, weight=ft.FontWeight.BOLD, color=ft.colors.RED_500),
            ft.Text(f"الخطأ: {str(e)}", color=ft.colors.WHITE),
            ft.Text(traceback.format_exc(), color=ft.colors.GREY_500, size=10, selectable=True)
        )
        page.update()
