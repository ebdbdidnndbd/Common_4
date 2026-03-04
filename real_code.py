# لا تحتاج تسوي import flet هنا لأن الهيكل راح يجهزها إلك

def build_ui(page):
    # هذا الكود راح يشتغل بجهاز المستخدم
    page.title = "Hussein V8 Control"
    page.bgcolor = "#0f111a"
    
    page.add(
        ft.Icon(ft.icons.ROCKET_LAUNCH, size=80, color="green"),
        ft.Text("مرحباً بك في نظام V8", size=30, weight="bold", color="white"),
        ft.Text("تم سحب التحديث الهوائي بنجاح وبدون تحميل!", color="grey"),
        ft.ElevatedButton("تحديث الصفحة", on_click=lambda _: page.update())
    )
    page.update()
