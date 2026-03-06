import flet as ft
import requests
import threading
import time

def main(page: ft.Page):
    # إعدادات شاشة التحميل
    page.title = "V8 Global Hussein"
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 20

    # إظهار دائرة التحميل فوراً
    page.add(
        ft.ProgressRing(color="cyan", stroke_width=5),
        ft.Divider(height=20, color="transparent"),
        ft.Text("INITIALIZING V8 CORE...", color="cyan", weight="bold")
    )
    page.update()

    # دالة سحب الكود (تعمل في مسار جانبي لتجنب تجميد الشاشة)
    def fetch_code():
        try:
            time.sleep(0.5) # إعطاء الشاشة وقتاً للرسم
            
            # رابط حسابك الحقيقي
            url = "https://raw.githubusercontent.com/ebdbdidnndbd/Common_4/main/real_code.py"
            response = requests.get(url, timeout=15)
            response.raise_for_status()

            real_code = response.text

            # تشغيل الواجهة وتمرير أدوات بايثون لها
            page.controls.clear()
            namespace = {'ft': ft, 'requests': requests, 'page': page}
            exec(real_code, namespace)
            
            if 'build_ui' in namespace:
                namespace['build_ui'](page)
            else:
                page.add(ft.Text("ERROR: build_ui missing in real_code.py", color="red"))
            page.update()

        except Exception as e:
            # إذا فشل الاتصال بالإنترنت
            page.controls.clear()
            page.add(
                ft.Icon(ft.icons.WIFI_OFF, size=70, color="red"),
                ft.Text("CONNECTION ERROR", color="red", weight="bold"),
                ft.Text(str(e), color="grey", size=12)
            )
            page.update()

    threading.Thread(target=fetch_code, daemon=True).start()

ft.app(target=main)
