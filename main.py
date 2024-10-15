# from flet import *
# import speech_recognition as sr
# import sqlite3
# import functools as fc
# from urllib import request

# # حالة تتبع التسجيل
# is_recording = False


# tab1 = True
# tab2 = False
# language_name = "ar-SA"

# def main(page: Page):
#     page.window.height = 720
#     page.window.width = 390
#     page.window.title_bar_hidden = False
    
#     # page.theme_mode = ThemeMode.DARK
#     # page.bgcolor=colors.DEEP_PURPLE_50
    
# # دالة الرسالة التعرفية
#     def show_help(e):
#         def close_dialog(e):
#             page.dialog.open = False
#             page.update()

#         page.dialog = AlertDialog(
#             title=Text("معلومات عن المطورين علي التطبيق "),
#             content=Text("1.عمر بركات\n2.علي عبدالعال\n3.عبدالله عايش\n4.ادم احمد (مطور الشركه)"),
#             actions=[TextButton("حسنا", on_click=close_dialog)]
#         )
#         page.dialog.open = True
#         page.update()
# ##دالة لتعريف من نحن
#     def am(e):
#         def close_dialog(e):
#             page.dialog.open = False
#             page.update()

#         page.dialog = AlertDialog(
#             title=Text("من نحن ؟؟"),
#             content=Text(" am نحن شركة  \n نقدم احدث التطبيقات الاندرويد والويب والوندوذ \n يمكنك صناعة تطبيقات عن طريق خدمة الشركة بسعر مناسب للجميع\n !! معلومات عن خدمة الشركة \n خدمه صناعة تطبيقات اندرويد ويب ووندوذ عن طريق مهندسين محترفين "),
#             actions=[TextButton("حسنا", on_click=close_dialog)]
#         )
#         page.dialog.open = True
#         page.update()
#     def ll(e):
#         def close_dialog(e):
#             page.dialog.open = False
#             page.update()
# ###دالة لتواصل مع المطورين
#         page.dialog = AlertDialog(
#             title=Text("تواصل معنا"),
#             content=Text(":يمكنك التواصل عن طريق الاميل\nadamaaaaa1122@gmail.com"),
#             actions=[TextButton("شكرا", on_click=close_dialog)]
#         )
#         page.dialog.open = True
#         page.update()
#     def route_change(e :RouteChangeEvent):
#         page.views.clear()
    

    
#     #  متغيرات تسجيل و تمييز الصوت 
#     source = sr.Microphone()
#     recognizer = sr.Recognizer()
    
    
#     # style and colors
#     light_color = colors.DEEP_PURPLE_50
#     light_color2 = colors.INDIGO_100
#     dark_color = colors.INDIGO_600
#     bs=ButtonStyle(shape=RoundedRectangleBorder(5),bgcolor=colors.DEEP_PURPLE_50,color=colors.INDIGO_800)
#     ebs=ButtonStyle(shape=RoundedRectangleBorder(8),bgcolor=colors.INDIGO_600,color=colors.DEEP_PURPLE_50,icon_color=colors.DEEP_PURPLE_50)
#     light_gradiant = LinearGradient(colors=[colors.DEEP_PURPLE_50,colors.INDIGO_100,colors.DEEP_PURPLE_50])
#     dark_gradint = LinearGradient(colors=[colors.BLUE_400,colors.INDIGO_400,colors.BLUE_500])

#     def on_change_tab(e):
#         cs = ["/","/database"]
#         page.go(cs[e.control.selected_index])
#         # معايرة الضوضاء المحيطة عند فتح الصفحة التسجيل
#         if cs[e.control.selected_index] == "/":
#             with source:
#                 recognizer.adjust_for_ambient_noise(source)
    
#     listview = ListView(expand=True,spacing=5 ,auto_scroll=False)

    

    
#     # مرجع النص المحول
#     converted_text_ref = Ref[Text]()

#     def lv_element(text):
#         '''return element for listview as container and fill all controls with data for fils in database'''
#         return Container(content =
#             Row(controls=[
#                 Column(controls=[
#                     IconButton(icon=icons.COPY,on_click=fc.partial(copy2clipboard,t=text),style=ebs,tooltip=Tooltip(message="نسخ")),
#                     IconButton(icon=icons.DELETE,on_click=fc.partial(delete,t=text),style=ebs,tooltip=Tooltip(message="حذف"))
#                 ]),
#                 Column(controls=[
#                 Text(value=text,size=18,color=colors.WHITE,text_align=TextAlign.RIGHT),
#                 ],spacing=40,width=page.window.width*3//5,horizontal_alignment=CrossAxisAlignment.END),
                
#             ],width=page.window.width*(9)//10

#             ),
            
#             border_radius=10,padding=10,border=border.all(2,color=colors.WHITE38),
#             gradient=dark_gradint,
#         )
    
#     def copy2clipboard(e,t):
#         page.set_clipboard(t)
#         page.update()
#         page.overlay.append(SnackBar(Text("تم النسخ"),open=True))
#         page.update()


#     def route_change(route):
#         page.views.clear()
#         '''
#         # page.views.append(
#         #     View(
#         #         "/",
#         #         [
#         #             AppBar(
#         #                 title=Text("مرحبا بكم في برنامج", size=20, weight=FontWeight.BOLD),
#         #                 center_title=True,
#         #                 bgcolor=colors.GREEN_300,
#         #             ),
#         #             Container(Row([
#         #                 Text("تحويل صوت إلى كلام", size=20, weight=FontWeight.BOLD, color=colors.GREEN_300)
#         #             ], alignment=MainAxisAlignment.CENTER),
#         #                 padding=padding.only(top=60)
#         #             ),
#         #             Container(Row([
#         #                 Image(src="images.png")
#         #             ], alignment=MainAxisAlignment.CENTER),
#         #                 padding=padding.only(top=40)
#         #             ),
#         #             Container(Row([
#         #                 ElevatedButton("أبدء", width=200, bgcolor=button_bgcolor, color=colors.WHITE,
#         #                                on_click=lambda e: page.go("/login")),
#         #             ], alignment=MainAxisAlignment.CENTER),
#         #                 padding=padding.only(top=20)
#         #             ),
                    
#         #         ],
#         #     )
#         # )
#         '''

#         if page.route == "/":
#             page.views.append(
#                 View(
#                     "/",
#                     [
#                         AppBar(
#                             title=Text("تحويل صوت إلى كلام", size=20, weight=FontWeight.BOLD,color=colors.WHITE),
#                             center_title=True,
#                             bgcolor=colors.INDIGO_500,
#                             # leading=IconButton(icons.HOME, on_click=lambda e: page.go("/"),icon_color=colors.WHITE),
#                             # leading_width=60,
                            
#                             actions=[
#                                 PopupMenuButton(
#                                     items=[
#                                         PopupMenuItem(text="معلومات عن المطورين", on_click=show_help),
#                                         PopupMenuItem(text="من نحن", on_click=am),
#                                         PopupMenuItem(text="--------------------",disabled=True),
#                                         PopupMenuItem(text="تواصل مع المطورين", on_click=ll),
#                                     ],icon_color=colors.WHITE
#                                 )
#                             ],
#                         ),
                       
                        
#                         Container(
#                             content=
#                             Column(
#                                 controls=
#                             [
                                
#                                 Row([
#                                 Container(
#                                     content=
#                                         Text(
#                                         ref=converted_text_ref,  # مكان عرض النص المحول مع استخدام ref للوصول إليه لاحقًا
#                                         color=dark_color,
#                                         width=320,
#                                         text_align=TextAlign.RIGHT,
#                                         size=20,tooltip=Tooltip(message="مساحة ظهور النص"),
                                        
                                        
                                
#                                         # expand=True
#                                         ), 
#                                     height=350,
#                                     bgcolor=light_color2,
#                                     expand=True,
                                    
                                    
#                                     ),
                                    
                                    
                                    
#                                     ], alignment=MainAxisAlignment.END),
#                                 Row(controls=[
#                                     ElevatedButton(text=language_name[:2].capitalize(), icon=icons.LANGUAGE,
#                                                 on_click=language,style=ebs,
#                                                 # tooltip=Tooltip(message="حفظ النص لإستعادته لاحقا")
#                                                 ),
#                                     ElevatedButton("تعديل",icon=icons.EDIT,
#                                                 on_click=edit,style=ebs,
#                                                 # tooltip=Tooltip(message="حفظ النص لإستعادته لاحقا")
#                                                 ),
                                    
#                                     ElevatedButton("حفظ", icon=icons.SAVE_ALT,
#                                                 on_click=save_to_database,style=ebs,
#                                                 tooltip=Tooltip(message="حفظ النص لإستعادته لاحقا")
#                                                 ),
                                    
                                    
#                                 ], alignment=MainAxisAlignment.CENTER)
#                                 ,
#                                 Row(controls=[
#                                     ElevatedButton("اضغط لتسجيل الصوت", width=200, color=colors.WHITE,
#                                                 on_click=toggle_recording,style=ebs),
#                                 ], alignment=MainAxisAlignment.CENTER),
                            
#                                 Row(controls=[
#                                     ElevatedButton("مسح", width=100, color=colors.WHITE,
#                                                 on_click=clear_text,style=ebs),
#                                 ], alignment=MainAxisAlignment.CENTER),
                                
#                             ]),
#                             gradient=light_gradiant,expand=True
#                         ),
                        
#                         NavigationBar(
#                             destinations=[
                                
#                                 NavigationBarDestination(icon=icons.MIC,
#                                                          label="تسجيل"
#                                                          ),
#                                 NavigationBarDestination(icon=icons.HISTORY, label="محفوظات",
#                                                          ),
#                                 # NavigationBarDestination(icon=icons.HOME, label=""),
#                             ],
#                                 selected_index=0,
#                                 on_change=on_change_tab,
                                
#                                 bgcolor=dark_color,
#                                 indicator_color=light_color2,
#                                 # shadow_color=colors.WHITE,
#                                 # surface_tint_color=colors.WHITE,
#                                 # overlay_color=colors.WHITE
#                                 )
#                     ],bgcolor=colors.DEEP_PURPLE_50
#                 )
#             )
#             page.bgcolor=colors.DEEP_PURPLE_50
#         if page.route == "/database":
#             page.views.append(
#                 View(
#                     "/database",
#                     [
#                         AppBar(
#                             title=Text("محفوظات", size=20, weight=FontWeight.BOLD,color=light_color),
#                             center_title=True,
#                             bgcolor=dark_color,
#                             leading=IconButton(icons.ARROW_BACK, on_click=lambda e: page.go("/"),icon_color=light_color),
#                             # leading_width=60,
                            
#                             actions=[
#                                 PopupMenuButton(
#                                     items=[
#                                         PopupMenuItem(text="معلومات عن المطورين", on_click=show_help),
#                                         PopupMenuItem(text="من نحن", on_click=am),
#                                         PopupMenuItem(text="--------------------",disabled=True),
#                                         PopupMenuItem(text="تواصل مع المطورين", on_click=ll),
#                                     ]
                                    
#                                 )
#                             ],
#                         ),
#                         # مكان عرض النص المحول مع استخدام ref للوصول إليه لاحقًا
#                         Container(content=listview,
#                                   gradient=light_gradiant,expand=True),
#                         NavigationBar(
#                             destinations=[
                                
#                                 NavigationBarDestination(icon=icons.MIC,
#                                                          label="تسجيل"
#                                                          ),
#                                 NavigationBarDestination(icon=icons.HISTORY,
#                                                          label="محفوظات"
#                                                          ),
#                                 # NavigationBarDestination(icon=icons.HOME, label=""),
#                                 ],
#                                 selected_index=1,
#                                 on_change=on_change_tab,
#                                 bgcolor=dark_color,
#                                 indicator_color=light_color2,
#                                 shadow_color=colors.AMBER,
#                                 # surface_tint_color=colors.AMBER,
#                                 # overlay_color=colors.AMBER,


#                                 )
                        
#                     ],bgcolor=colors.DEEP_PURPLE_50
#                 )
#             )
            
        
#         page.update()
    
#     def handle_close(e,t):
#         converted_text_ref.current.value = t.value
#         # print(type(e.control.parent))
#         page.update()
#         page.close(e.control.parent)
    
#     def edit(e):
#         t =TextField(value=converted_text_ref.current.value,multiline=True,color=dark_color)
#         page.open(
#             AlertDialog(
#                 title=Text("تصحيح النص",color=dark_color),
#                 content=t,
#             actions=[
#                 TextButton("تعديل", on_click=fc.partial(handle_close,t=t),style=ebs),
#                 ],
#                 bgcolor=light_color2

#             )
#         )


#     def change_language(e,cnt):
#         global language_name
#         language_name = e.control.value
#         cnt.control.text = language_name[:2].capitalize()
#         page.update()
#         page.close(e.control.parent)
#         # print(type(e.control.value))

#     def language(e):
#         lang = ["ar-SA","en-US"]
#         ls = Dropdown(width=100,value=language_name,text_size=20,
#                  options=[
#                      dropdown.Option("ar-SA"),
#                      dropdown.Option("en-US"),
#                  ],
                 
                 
#                  on_change=fc.partial(change_language,cnt=e),
#                  bgcolor=light_color2,
#                  color=dark_color
#                       )
#         page.open(
#             AlertDialog(
#                 title=Text("تحديد لغة الصوت",color=dark_color),
#                 content=ls,bgcolor=light_color2

#             )
#         )

#     # دالة للتبديل بين التسجيل والإيقاف
#     def toggle_recording(e):
#         if not(internet_on()):
#             return
#         global is_recording
#         if not is_recording:
#             # البدء في التسجيل
#             e.control.text = 'اضغط مرة اخري للإيقاف'
#             e.control.bgcolor=colors.RED
#             page.overlay.append(SnackBar(Text("جاري التسجيل...."),open=True))
#             page.update()
#             recognizer.energy_threshold = 300
#             is_recording = True
#             myrecord_audio()
#         else:
#             # إيقاف التسجيل
#             page.overlay.append(SnackBar(Text("تم إيقاف التسجيل"),open=True))
#             e.control.text = "اضغط لتسجيل الصوت"
#             e.control.bgcolor=colors.GREEN_300
#             # source.stream.close()
#             recognizer.energy_threshold = 300 * 100
#             page.update()
#             is_recording = False

#     # دالة لتحويل الصوت إلى نص وعرضه
#     def convert_audio_to_text(page):
#         if is_recording:
#             pass
#             # page.overlay.append(SnackBar(Text("يرجى إيقاف التسجيل أولاً"),open=True))
#             # page.update()
#         else:
#             text = record_and_save_audio()
#             if text:
#                 # تحديث النص المحول في الصفحة باستخدام المرجع
#                 converted_text_ref.current.value += "\n"+text
#                 page.overlay.append(SnackBar(Text(f"تم تحويل الصوت إلى نص: {text}"),open=True))
#                 page.update()

#     # دالة لتسجيل الصوت وتحويله إلى نص وحفظه في قاعدة البيانات
#     def record_and_save_audio():
#         text = record_audio()  # تسجيل الصوت
#         if text:
#             save_to_database()  # حفظ النص في قاعدة البيانات
#             return text
#         return "تعذر تسجيل الصوت"

#     # دالة لتسجيل الصوت باستخدام speech_recognition
#     def record_audio():
#         recognizer = sr.Recognizer()
#         with sr.Microphone() as source:
            
#             print("Recording...")
#             # recognizer.non_speaking_duration *= (int(is_recording)+0.01)

#             recognizer.adjust_for_ambient_noise(source)
#             audio = recognizer.listen(source)
            
#             try:
#                 # تحويل الصوت إلى نص (اللغة العربية)
#                 text = recognizer.recognize_google(audio, language="ar-SA")
#                 print("You said: " + text)

                
#                 return text
            
#             except sr.UnknownValueError:
#                 print("لا يمكن فهم الصوت")
#             except sr.RequestError as e:
#                 print(f"خطأ في التعرف على الكلام : {e}")
#         return None

    
    
#     def myrecord_audio():
        
        
#         with source:    
#             # print("Recording...")
#             audio = recognizer.listen(source)
            
#             try:
#                 # تحويل الصوت إلى نص (اللغة العربية)
#                 text = recognizer.recognize_google(audio, language=language_name)
#                 # print("You said: " + text)
#                 if converted_text_ref.current.value:
#                     converted_text_ref.current.value += "\n"+text
#                 else:
#                     converted_text_ref.current.value = text
#                 page.overlay.append(SnackBar(Text(f"تم تحويل الصوت إلى نص: {text}"),open=True))
#                 page.update()

#                 return text
            
#             except sr.UnknownValueError:
#                 page.overlay.append(SnackBar(Text("لا يمكن فهم الصوت"),open=True))
#                 page.update()
#                 # print("لا يمكن فهم الصوت")
#             except sr.RequestError as e:
#                 page.overlay.append(SnackBar(Text(f"خطأ في التعرف على الكلام : {e}"),open=True))
#                 page.update()
#                 # print(f"خطأ في التعرف على الكلام : {e}")
        
    
#     def clear_text(e):
#         converted_text_ref.current.value = ""
#         page.update()

    
#     def create_data_base():
#         conn = sqlite3.connect('audio_records.db')
#         cursor = conn.cursor()

#         # إنشاء الجدول إذا لم يكن موجوداً
#         cursor.execute('''CREATE TABLE IF NOT EXISTS records
#                         (id INTEGER PRIMARY KEY, text TEXT)''')
    
#     create_data_base()

#     # دالة لحفظ النص في قاعدة البيانات
#     def save_to_database(e):
#         if converted_text_ref.current.value != "":
#             t = converted_text_ref.current.value
#             conn = sqlite3.connect('audio_records.db')
#             cursor = conn.cursor()

#             # إدخال النص المحول
#             cursor.execute("INSERT INTO records (text) VALUES (?)", (t,))

#             # حفظ التغييرات وإغلاق الاتصال
#             conn.commit()
#             conn.close()
#             clear_text(e)
#         update_db_listview()
#         page.overlay.append(SnackBar(Text("تم الحفظ"),open=True))
#         page.update()

#     def get_all_from_database():
#         conn = sqlite3.connect('audio_records.db')
#         cursor = conn.cursor()
#         texts = []
#         ss = "SELECT text FROM records"
#         cursor.execute(ss)
#         if cursor.fetchall:
#             for f in cursor.fetchall():
#                 texts.append(f[0])
#         return texts


#     def delete(e, t):
#         conn = sqlite3.connect('audio_records.db')
#         curr = conn.cursor()
#         curr.execute("DELETE FROM records WHERE text = ? ",(t,)) 
#         conn.commit()
#         conn.close()
#         update_db_listview()
#         page.overlay.append(SnackBar(Text("تم الحذف"),open=True))
#         page.update()

#     # دالة اختبار الاتصال بالانترنت
#     def internet_on():
#         try:
#             request.urlopen('http://www.google.com', timeout=1)
#             return True
#         except request.URLError as err: 
#             page.overlay.append(SnackBar(Text("لا يوجد اتصال بالإنترنت"),open=True))
#             page.update()
#             return False

#     def update_db_listview():
#         listview.controls.clear()
#         files_in_db = get_all_from_database()
#         if files_in_db:
#             for f in files_in_db:
#                 listview.controls.append(lv_element(f))
#         page.update()
    
#     update_db_listview()



#     # دالة لعرض المعلومات
#     def show_info(message):
#         page.overlay.append(SnackBar(Text(message),open=True))
#         page.update()

#     def view_pop(e: ViewPopEvent) ->None:
#         page.views.pop()
#         top_view: View = page.views[-1]
#         page.go(top_view.route)
    
#     page.on_view_pop = view_pop
#     page.on_route_change = route_change
#     page.go(page.route)

# app(target=main, assets_dir="assets")

# # pip install speechRecognition
# # pip install PyAudio
# # pip install setuptools
