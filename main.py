import flet as ft
import requests

def main(page: ft.Page):
    # إعدادات شاشة التحميل
    page.title = "V8 Loader"
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    loading_text = ft.Text("جاري الاتصال بالسيرفر...", size=20, color="blue")
    page.add(ft.ProgressRing(), loading_text)

    try:
        # هنا تضع رابط الكود الحقيقي (الرابط الخام Raw من جيثب)
        # هذا مجرد رابط وهمي هسه، بعدين نغيره للرابط مالتك
        url = "https://raw.githubusercontent.com/Hussein/V8-App/main/real_code.py"
        
        response = requests.get(url, timeout=10)
        
        if response.status_code == 200:
            page.controls.clear() # نمسح شاشة التحميل
            real_code = response.text
            
            # تشغيل الكود المسحوب بداخل التطبيق!
            namespace = {'ft': ft, 'requests': requests}
            exec(real_code, namespace)
            namespace['build_ui'](page) # استدعاء واجهة التطبيق الحقيقية
            
        else:
            page.controls.clear()
            page.add(ft.Text("التطبيق قيد التحديث... يرجى المحاولة لاحقاً", color="red"))
            page.update()
            
    except Exception as e:
        page.controls.clear()
        page.add(ft.Text("لا يوجد اتصال بالإنترنت", color="red"))
        page.update()

ft.app(target=main)
