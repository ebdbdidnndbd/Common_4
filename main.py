import flet as ft
import requests
import threading
import time

def main(page: ft.Page):
    page.title = "V8 Global System"
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # رسم الشاشة فوراً
    page.add(
        ft.ProgressRing(color="cyan", stroke_width=5),
        ft.Divider(height=20, color="transparent"),
        ft.Text("INITIALIZING V8 CORE...", color="cyan", weight="bold")
    )
    page.update()

    def fetch_code():
        try:
            # نعطي الشاشة وقت للرسم (نصف ثانية)
            time.sleep(0.5)
            
            url = "https://raw.githubusercontent.com/ebdbdidnndbd/Common_4/main/real_code.py"
            response = requests.get(url, timeout=15)
            response.raise_for_status()

            real_code = response.text

            # تشغيل الواجهة
            page.controls.clear()
            namespace = {'ft': ft, 'requests': requests, 'page': page}
            exec(real_code, namespace)
            
            if 'build_ui' in namespace:
                namespace['build_ui'](page)
            else:
                page.add(ft.Text("ERROR: build_ui missing", color="red"))
            page.update()

        except Exception as e:
            # إذا فشل الاتصال، تطبع المشكلة على الشاشة بدل السواد
            page.controls.clear()
            page.add(
                ft.Icon(ft.icons.ERROR, size=70, color="red"),
                ft.Text("SYSTEM ERROR", color="red", weight="bold"),
                ft.Text(str(e), color="grey")
            )
            page.update()

    # تشغيل سحب الكود في مسار جانبي حتى لا تتجمد الشاشة
    threading.Thread(target=fetch_code, daemon=True).start()

ft.app(target=main)
