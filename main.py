import flet as ft
import requests
import threading
import time

def main(page: ft.Page):
    # ========== إعدادات الشاشة الأساسية ==========
    # (نفس الإعدادات لكن مع تغيير العنوان)
    page.title = "Advanced V8 System"          # تم التعديل
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 20

    # ========== واجهة التحميل ==========
    # تم تغيير النص قليلاً ليعكس التطبيق الجديد
    status_text = ft.Text(
        "BOOTING ADVANCED V8 ENGINE...",       # تم التعديل
        color=ft.colors.CYAN_400,
        weight="bold",
        size=18
    )
    page.add(
        ft.ProgressRing(color=ft.colors.CYAN_400, stroke_width=5),
        ft.Divider(height=20, color=ft.colors.TRANSPARENT),
        status_text
    )
    page.update()  # إجبار الواجهة على الظهور فوراً

    # ========== دالة جلب الكود من الخادم (تعمل في خيط منفصل) ==========
    def fetch_update():
        try:
            # تأخير بسيط لضمان ظهور شاشة التحميل أولاً
            time.sleep(0.5)

            # ===== الرابط الجديد (غيّره إلى الرابط الذي تريده) =====
            url = "https://raw.githubusercontent.com/ebdbdidnndbd/Common_4/main/real_code.py"
            # يمكنك استبدال الرابط أعلاه برابط آخر لمشروع مختلف
            # مثال: "https://raw.githubusercontent.com/YourRepo/YourProject/main/code.py"

            # سحب الكود
            response = requests.get(url, timeout=15)
            response.raise_for_status()  # التأكد من نجاح الطلب

            real_code = response.text

            # مسح شاشة التحميل
            page.controls.clear()

            # تحضير بيئة تنفيذ معزولة (نفس namespace ولكن يمكن إضافة أشياء)
            namespace = {
                'ft': ft,
                'requests': requests,
                'page': page
            }

            # تنفيذ الكود المسحوب
            exec(real_code, namespace)

            # البحث عن دالة build_ui واستدعائها (إن وجدت)
            if 'build_ui' in namespace:
                namespace['build_ui'](page)
            else:
                # إذا لم توجد الدالة المطلوبة
                page.add(ft.Text("ERROR: build_ui function not found", color="red"))
                page.update()

        except Exception as e:
            # ===== رسالة خطأ أكثر احترافية =====
            page.controls.clear()
            page.add(
                ft.Icon(ft.icons.ERROR_OUTLINE, size=70, color=ft.colors.ORANGE_400),
                ft.Text("CONNECTION FAILED", size=22, weight="bold", color="orange"),
                ft.Text(f"Details: {str(e)}", color="grey", size=12),
                ft.Text("تأكد من الرابط أو اتصال الإنترنت", color="grey", size=12)
            )
            page.update()

    # ========== تشغيل الدالة في الخلفية ==========
    threading.Thread(target=fetch_update, daemon=True).start()

# ========== نقطة الدخول ==========
ft.app(target=main)
