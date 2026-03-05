import flet as ft
import urllib.request # مكتبة بايثون الأساسية (لا تحتاج requirements)

def main(page: ft.Page):
    # 1. إعدادات الشاشة
    page.title = "V8 Global System"
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    # 2. إظهار واجهة التحميل فوراً
    page.add(
        ft.ProgressRing(color="cyan", stroke_width=5),
        ft.Text("INITIALIZING V8 CORE...", color="cyan", weight="bold")
    )
    page.update()

    try:
        # 3. جلب الكود من جيثب
        url = "https://raw.githubusercontent.com/ebdbdidnndbd/Common_4/main/real_code.py"
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req, timeout=15) as response:
            real_code = response.read().decode('utf-8')
        
        # 4. مسح شاشة التحميل وتشغيل الواجهة المرفوعة
        page.controls.clear()
        namespace = {'ft': ft, 'page': page}
        exec(real_code, namespace)
        
        if 'build_ui' in namespace:
            namespace['build_ui'](page)
        else:
            page.add(ft.Text("ERROR: build_ui not found", color="red"))
            
    except Exception as e:
        # إذا انقطع النت أو صار خطأ
        page.controls.clear()
        page.add(
            ft.Icon(ft.icons.GPP_BAD, size=70, color="red"),
            ft.Text("SYSTEM ERROR", color="red", weight="bold"),
            ft.Text(str(e), color="grey")
        )
        
    page.update()

ft.app(target=main)
