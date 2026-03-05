import flet as ft
import requests

def main(page: ft.Page):
    # إعدادات شاشة التحميل الأساسية (V8 Core)
    page.title = "Common V8 Global"
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    # واجهة تحميل احترافية
    status_text = ft.Text("INITIALIZING V8 CORE...", color=ft.colors.CYAN_400, weight="bold", size=18)
    page.add(
        ft.ProgressRing(color=ft.colors.CYAN_400, stroke_width=5), 
        ft.Divider(height=20, color=ft.colors.TRANSPARENT),
        status_text
    )
    page.update()

    try:
        # رابطك النهائي المباشر (Raw) من مستودعك
        url = "https://raw.githubusercontent.com/ebdbdidnndbd/Common_4/main/real_code.py"
        
        # سحب الكود مع مهلة 15 ثانية لتجنب التعليق
        response = requests.get(url, timeout=15)
        response.raise_for_status() # التأكد من أن الرابط يعمل 100%
        
        real_code = response.text
        page.controls.clear()
        
        # بيئة التشغيل المعزولة (نمرر المكتبات حتى لا يحدث خطأ ModuleNotFoundError)
        namespace = {'ft': ft, 'requests': requests, 'page': page}
        exec(real_code, namespace)
        
        # تشغيل واجهتك المرفوعة على جيثب
        if 'build_ui' in namespace:
            namespace['build_ui'](page)
        else:
            page.add(ft.Text("SYSTEM ERROR: build_ui function missing in real_code.py", color="red"))
            
    except requests.exceptions.RequestException:
        # إذا لم يكن هناك إنترنت
        page.controls.clear()
        page.add(
            ft.Icon(ft.icons.WIFI_OFF, size=70, color=ft.colors.RED_500),
            ft.Text("CONNECTION FAILED", size=22, weight="bold", color="red"),
            ft.Text("يرجى التحقق من الاتصال بالإنترنت وإعادة تشغيل التطبيق.", color="grey")
        )
    except Exception as e:
        # حماية ضد أي خطأ برمجي مستقبلي
        page.controls.clear()
        page.add(
            ft.Icon(ft.icons.GPP_BAD, size=70, color=ft.colors.AMBER_500),
            ft.Text("CRITICAL ERROR", size=22, weight="bold", color="amber"),
            ft.Text(f"Error Details: {str(e)}", color="grey", size=12)
        )
    
    page.update()

ft.app(target=main)
