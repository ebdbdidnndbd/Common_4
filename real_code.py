# هذا الكود سيتم سحبه وتشغيله داخل التطبيق مباشرة
# المتغيرات ft و requests و page جاهزة للاستخدام تلقائياً

def build_ui(page):
    # إعدادات الواجهة
    page.title = "V8 Control Panel"
    page.padding = 30
    page.bgcolor = "#0a0a0a" # أسود سيبراني
    
    # محتويات التطبيق
    header = ft.Text("SYSTEM ONLINE", size=28, weight="bold", color=ft.colors.GREEN_400)
    sub_header = ft.Text("Welcome to Common V8 Global Interface", color=ft.colors.GREY_500)
    
    # زر تجريبي تفاعلي
    def on_click_test(e):
        e.control.text = "تم تنفيذ الأمر بنجاح!"
        e.control.bgcolor = ft.colors.GREEN_700
        e.control.icon = ft.icons.CHECK_CIRCLE
        page.update()

    action_btn = ft.ElevatedButton(
        text="تنفيذ أمر الاختبار",
        icon=ft.icons.TERMINAL,
        bgcolor=ft.colors.BLUE_700,
        color=ft.colors.WHITE,
        on_click=on_click_test,
        width=250,
        height=50
    )

    # ترتيب العناصر في المنتصف
    content = ft.Column(
        [
            ft.Icon(ft.icons.SHIELD_OUTLINED, size=100, color=ft.colors.CYAN_500),
            header,
            sub_header,
            ft.Divider(height=40, color=ft.colors.TRANSPARENT),
            action_btn,
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        alignment=ft.MainAxisAlignment.CENTER,
    )
    
    page.add(
        ft.Container(
            content=content,
            alignment=ft.alignment.center,
            expand=True
        )
    )
    page.update()
