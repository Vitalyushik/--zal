from tkinter import *
from random import *
from datetime import datetime
from tkinter import font

from PIL import ImageTk, Image
import itertools

def r():
    l1['image'] = m2
    br['command'] = r1


def r1():
    l1['image'] = m3
    br['command'] = r2


def r2():
    l1['image'] = m1
    br['command'] = r


def l():
    l1['image'] = m3
    bl['command'] = l11


def l11():
    l1['image'] = m2
    bl['command'] = l2


def l2():
    l1['image'] = m1
    bl['command'] = l

def rd():
    l1['image'] = md2
    br['command'] = r1d


def r1d():
    l1['image'] = md3
    br['command'] = r2d


def r2d():
    l1['image'] = md1
    br['command'] = rd


def ld():
    l1['image'] = md3
    bl['command'] = l11d


def l11d():
    l1['image'] = md2
    bl['command'] = l2d


def l2d():
    l1['image'] = md1
    bl['command'] = ld


def b1():
    def korz1():
        def chek():
            ch = Toplevel(wk)
            ch.geometry('345x600+200+50')
            ch.resizable(False, False)
            ch.title('Чек')
            ch.configure(bg=wh)
            dat = datetime.today()
            dat1 = dat.strftime('%Y.%m.%d')
            tim = dat.strftime('%H:%M:%S')
            n = randrange(100000, 999999)
            n1 = randrange(100000000, 999999999)
            n2 = randrange(1_000_000_000, 9999999999)
            h = f'''ООО "ПРЕМЬЕР ЗАЛ"
Екатеринбург, ул. Сулимова, 50
Кассовый чек №{n}
________________________________________________________________________'''
            lch = Label(ch, text=h, bg=wh)
            lch.pack()
            kon = f'''_______________________________________________________________________
   ИНН: {n1}                          ФП: {n2} 
 Кассир: Иванов И.И.
       Дата: {dat1}                          Время: {tim}
'''
            for o in cs:
                if o > 0:
                    cs1.extend(str(o))
            for i in range(len(g1)):
                g3 = f'''{g2[i]}'''
                cs2 = f'''                         {cs1[i]}
            {g2[i][-6:]}  *  {cs1[i]} = {int(g2[i][-6:-2]) * int(cs1[i])}p.'''
                lk1 = Label(ch, text=g3, bg=wh, font=('Calibri', '10'))
                lk1.place(x=2, y=100 + 50 * i)
                lc = Label(ch, text=cs2, bg=wh, font=('Calibri', '10'))
                lc.place(x=200, y=100 + 50 * i)
            lck = Label(ch, text=kon, bg=wh, justify='left')
            lck.place(x=0, y=82 + 50 * len(g1))
            ch.grab_set()
            ch.mainloop()

        global g, cs, lc1
        wk = Toplevel()
        wk.resizable(False, False)
        wk.geometry('400x600+200+50')
        wk.iconbitmap('icon.ico')
        wk.title('Корзина')
        lk = Label(wk, image=korzina)
        lk.place(x=-2, y=-2)
        lp = Label(wk, width=0, height=0, bg='#58C893')
        lp.pack()
        cs = [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16]
        g1 = set(g)
        g2 = list(g1)
        cs = list(cs)
        cs1 = list()
        s = 0
        for o in cs:
            if o > 0:
                cs1.extend(str(o))
        for i in range(len(g1)):
            s += (int(g2[i][-6:-2]) * int(cs1[i]))
            g3 = f'''{g2[i]}'''
            cs2 = f'''                         {cs1[i]}
{g2[i][-6:]}  *  {cs1[i]} = {int(g2[i][-6:-2]) * int(cs1[i])}p.'''
            lk1 = Label(wk, text=g3, bg=wh1, font=('Inter', '10'), fg=wh2)
            lk1.place(x=2, y=21 + 50*i)
            lc = Label(wk, text=cs2, bg=wh1, font=('Inter', '10'), fg=wh2)
            lc.place(x=270, y=21 + 50*i)
            li = Label(wk, text=f'''Всегo:{s}p.
 Заказ будет ждать вас в магазине
 Оплата при получении''', bg=wh1, font=('Inter', '10'), fg=wh2)
            li.place(x=2, y=500)
        op = Button(wk, image=d, borderwidth=0, bg=wh1, highlightthickness=0, command=chek)
        op.place(x=250, y=530)
        wk.grab_set()
        wk.mainloop()

#ФУНКЦИИ ВЫЗЫВАЮЩИЕ ОПИСАНИЕ КАЖДОГО ФИЛЬМА
    def vit():

        vit = Toplevel(w1)
        vit.title('О ФИЛЬМЕ ПУШИСТЫЙ ВОЯЖ')
        vit.iconbitmap('icon.ico')
        vit.geometry('1280x960')
        vit.resizable(False, False)
        lv = Label(vit, image=iw1)
        lv.pack(anchor=W)
        label_text = Label(vit, text="О ФИЛЬМЕ ПУШИСТЫЙ ВОЯЖ", font=("Helvetica", 32))
        label_text.place(x=264, y=120)
        label_text0 = Label(vit, text="1 час 33 минуты Мультфильм, комедия, приключения 6+", font=("Helvetica", 16))
        label_text0.place(x=220, y=240)
        label_text2 = Label(vit, text="Страна: США, Канада", font=("Helvetica", 16))
        label_text2.place(x=220, y=290)
        label_text3 = Label(vit, text="Режиссер: Кевин Донован, Готтфрид Рудт", font=("Helvetica", 16))
        label_text3.place(x=220, y=340)
        label_text4 = Label(vit, text="Актеры: Билл Найи, Брук Шилдс, Дэнни Трехо",
                            font=("Helvetica", 16), justify='left')
        label_text4.place(x=220, y=390)
        label_text1 = Label(vit, text="Во время переезда двое домашних любимцев, Педро и Грейси, теряют своих хозяев."
                                      "\nОказавшись в пугающем и неизвестном мире, они пытаются воссоединиться с семьей."
                                      "\nНа пути их ждет множество приключений и опасностей, справиться с которыми можно,"
                                      "\nтолько действуя сообща.Смогут ли они разрешить свои разногласия и вернуться домой?",
                            font=("Helvetica", 16), justify='left')
        label_text1.place(x=220, y=440)

        vit.grab_set()
        vit.mainloop()

    def sltn():

        sltn = Toplevel(w1)
        sltn.title('О ФИЛЬМЕ СТО ЛЕТ ТОМУ ВПЕРЕД')
        sltn.iconbitmap('icon.ico')
        sltn.geometry('1280x960')
        sltn.resizable(False, False)
        lv = Label(sltn, image=iw1)
        lv.pack(anchor=W)
        label_text = Label(sltn, text="О ФИЛЬМЕ СТО ЛЕТ ТОМУ ВПЕРЕД", font=("Helvetica", 32))
        label_text.place(x=264, y=120)
        label_text0 = Label(sltn, text="2 часа 35 минут Приключения, экшн 6+", font=("Helvetica", 16))
        label_text0.place(x=220, y=240)
        label_text2 = Label(sltn, text="Страна: Россия", font=("Helvetica", 16))
        label_text2.place(x=220, y=290)
        label_text3 = Label(sltn, text="Режиссер: Александр Андрющенко", font=("Helvetica", 16))
        label_text3.place(x=220, y=340)
        label_text4 = Label(sltn, text="Актеры: Даша Верещагина, Марк Эйдельштейн, Александр Петров, Юра Борисов, "
                                         "\nВиктория Исакова, Константин Хабенский, Федор Бондарчук, Софа Цибирева",
                            font=("Helvetica", 16), justify='left')
        label_text4.place(x=220, y=390)
        label_text1 = Label(sltn, text="Они живут в разных мирах. Коля Герасимов — в сегодняшней Москве, Алиса"
                                       "\nСелезнева — на сто лет позже. Коля – обычный парень, ему нет дела до"
                                       "\nбудущего. Алису не отпускает прошлое: она должна найти маму, которую"
                                       "\nпотеряла, когда была совсем ребенком. Встреча Алисы и Коли станет началом"
                                       "\nневероятных приключений, в которых нашим героям предстоит отвоевать у"
                                       "\nкосмических пиратов Вселенную, восстановить ход времени и обрести самое"
                                       "\nдорогое: любовь и дружбу.",
                            font=("Helvetica", 16), justify='left')
        label_text1.place(x=220, y=470)

        sltn.grab_set()
        sltn.mainloop()

    def superp():

        superp = Toplevel(w1)
        superp.title('О ФИЛЬМЕ СУПЕРПТАШКИ')
        superp.iconbitmap('icon.ico')
        superp.geometry('1280x960')
        superp.resizable(False, False)
        lv = Label(superp, image=iw1)
        lv.pack(anchor=W)
        label_text = Label(superp, text="О ФИЛЬМЕ СУПЕРПТАШКИ", font=("Helvetica", 32))
        label_text.place(x=264, y=120)
        label_text0 = Label(superp, text="1 час 31 минута Анимация 0+", font=("Helvetica", 16))
        label_text0.place(x=220, y=240)
        label_text2 = Label(superp, text="Страна: Италия, Испания", font=("Helvetica", 16))
        label_text2.place(x=220, y=290)
        label_text3 = Label(superp, text="Режиссер: Нестор Ф. Деннис", font=("Helvetica", 16))
        label_text3.place(x=220, y=340)
        label_text4 = Label(superp, text="Актеры: Тай Шеридан, Шон Пенн, Гбенга Акиннагбе",
                            font=("Helvetica", 16), justify='left')
        label_text4.place(x=220, y=390)
        label_text1 = Label(superp, text="Птичка Джонни и его пернатые друзья обладают суперспособностями. Однажды"
                                       "\nони отправляются на секретную миссию, в ходе которой им предстоит спасти"
                                       "\nродной город от коварных планов злодея Отто фон Моржа.",
                            font=("Helvetica", 16), justify='left')
        label_text1.place(x=220, y=440)

        superp.grab_set()
        superp.mainloop()

    def adel():

        adel = Toplevel(w1)
        adel.title('О ФИЛЬМЕ АСФАЛЬТОВЫЕ ДЖУНГЛИ')
        adel.iconbitmap('icon.ico')
        adel.geometry('1280x960')
        adel.resizable(False, False)
        lv = Label(adel, image=iw1)
        lv.pack(anchor=W)
        label_text = Label(adel, text="О ФИЛЬМЕ АСФАЛЬТОВЫЕ ДЖУНГЛИ", font=("Helvetica", 32))
        label_text.place(x=264, y=120)
        label_text0 = Label(adel, text="2 часа 5 минут Триллер, драма 18+", font=("Helvetica", 16))
        label_text0.place(x=220, y=240)
        label_text2 = Label(adel, text="Страна: США", font=("Helvetica", 16))
        label_text2.place(x=220, y=290)
        label_text3 = Label(adel, text="Режиссер: Жан-Стефан Совер", font=("Helvetica", 16))
        label_text3.place(x=220, y=340)
        label_text4 = Label(adel, text="Актеры: Тай Шеридан, Шон Пенн, Гбенга Акиннагбе",
                            font=("Helvetica", 16), justify='left')
        label_text4.place(x=220, y=390)
        label_text1 = Label(adel, text="Это история врача и его первого года на работе в середине 90-х в Гарлеме."
                                      "\nЭто взгляд изнутри на уличную жизнь: перестрелки, плохие копы, безнадежные"
                                      "\nпациенты, черный юмор в странных обстоятельствах и попытка одного медика"
                                      "\nсохранить свое желание помочь, несмотря на его растущую черствость.",
                            font=("Helvetica", 16), justify='left')
        label_text1.place(x=220, y=440)

        adel.grab_set()
        adel.mainloop()


    def nez():

        nez = Toplevel(w1)
        nez.title('О ФИЛЬМЕ НЕЗНАКОМЦЫ')
        nez.iconbitmap('icon.ico')
        nez.geometry('1280x960')
        nez.resizable(False, False)
        lv = Label(nez, image=iw1)
        lv.pack(anchor=W)
        label_text = Label(nez, text="О ФИЛЬМЕ НЕЗНАКОМЦЫ", font=("Helvetica", 32))
        label_text.place(x=264, y=120)
        label_text0 = Label(nez, text="1 час 37 минут Хоррор-слэшер 18+", font=("Helvetica", 16))
        label_text0.place(x=220, y=240)
        label_text2 = Label(nez, text="Страна: США", font=("Helvetica", 16))
        label_text2.place(x=220, y=290)
        label_text3 = Label(nez, text="Режиссер: Ренни Харлин", font=("Helvetica", 16))
        label_text3.place(x=220, y=340)
        label_text4 = Label(nez, text="Актеры: Мэделин Петш, Гэбриел Бассо, Рэйчел Шентон, Ричард Брэйк",
                            font=("Helvetica", 16), justify='left')
        label_text4.place(x=220, y=390)
        label_text1 = Label(nez, text="Майя и Райан решили отметить пятую годовщину, не подозревая, что она может стать"
                                     "\nих последней. Путешествуя на своем пикапе через всю страну, они совершают"
                                      "\nвынужденную остановку в маленьком городе, где местные жители, даже дети,"
                                      "\nвстречают их с большим интересом. Оставаться в этом странном месте пара не хочет,"
                                      "\nно вынуждена провести ночь в доме, куда вскоре нагрянут безумцы в кукольных масках.",
                            font=("Helvetica", 16), justify='left')
        label_text1.place(x=220, y=440)

        nez.grab_set()
        nez.mainloop()

    def vp():

        vp = Toplevel(w1)
        vp.title('О ФИЛЬМЕ ВИННИ ПУХ')
        vp.iconbitmap('icon.ico')
        vp.geometry('1280x960')
        vp.resizable(False, False)
        lv = Label(vp, image=iw1)
        lv.pack(anchor=W)
        label_text = Label(vp, text="О ФИЛЬМЕ ВИННИ ПУХ", font=("Helvetica", 32))
        label_text.place(x=264, y=120)
        label_text0 = Label(vp, text="1 час 37 минут Ужасы, триллер 18+", font=("Helvetica", 16))
        label_text0.place(x=220, y=240)
        label_text2 = Label(vp, text="Страна: Великобритания", font=("Helvetica", 16))
        label_text2.place(x=220, y=290)
        label_text3 = Label(vp, text="Режиссер: Рис Фрейк-Уотерфилд", font=("Helvetica", 16))
        label_text3.place(x=220, y=340)
        label_text4 = Label(vp, text="Актеры: Скотт Чемберс, Таллула Эванс, Райан Олива, Тереза Бенхем",
                            font=("Helvetica", 16), justify='left')
        label_text4.place(x=220, y=390)
        label_text1 = Label(vp, text="После событий первого фильма, Винни-Пух и Пятак больше не могут продолжать"
                                       "\nохотиться в Стоакровомом лесу. Очередное предательство Кристофера Робина,"
                                       "\nраскрывшего миру их существование, ставит под угрозу не только их дом, но и"
                                     "\nжизни. Вот только звери больше не намерены прятаться в тени и вместе c друзьями"
                                     "\nСовенком и Тигрой, отправляются в город, чтобы навести в нем свои кровавые порядки.",
                            font=("Helvetica", 16), justify='left')
        label_text1.place(x=220, y=440)

        vp.grab_set()
        vp.mainloop()

    def sudn():

        sudn = Toplevel(w1)
        sudn.title('О ФИЛЬМЕ СУДНАЯ НОЧЬ')
        sudn.iconbitmap('icon.ico')
        sudn.geometry('1280x960')
        sudn.resizable(False, False)
        lv = Label(sudn, image=iw1)
        lv.pack(anchor=W)
        label_text = Label(sudn, text="О ФИЛЬМЕ СУДНАЯ НОЧЬ", font=("Helvetica", 32))
        label_text.place(x=264, y=120)
        label_text0 = Label(sudn, text="1 час 34 минуты Криминал, триллер 18+", font=("Helvetica", 16))
        label_text0.place(x=220, y=240)
        label_text2 = Label(sudn, text="Страна: США", font=("Helvetica", 16))
        label_text2.place(x=220, y=290)
        label_text3 = Label(sudn, text="Режиссер: Дэн Браун", font=("Helvetica", 16))
        label_text3.place(x=220, y=340)
        label_text4 = Label(sudn, text="Актеры: Ангус Клауд, Эллиот Найт, Джессика Гарза",
                            font=("Helvetica", 16), justify='left')
        label_text4.place(x=220, y=390)
        label_text1 = Label(sudn, text="Несколько человек становятся свидетелями джекпота в $156 миллионов долларов."
                                       "\nСлучайные посетители, полиция, преступники - все желают заполучить лотерейный"
                                       "\nбилет с огромным выигрышем. Эта судная ночь выпустит на волю все людские пороки.", font=("Helvetica", 16), justify='left')
        label_text1.place(x=220, y=440)

        sudn.grab_set()
        sudn.mainloop()

    def zam1():

        zam = Toplevel(w1)
        zam.title('О ФИЛЬМЕ ПЛАНЕТА ОБЕЗЬЯН')
        zam.iconbitmap('icon.ico')
        zam.geometry('1280x960')
        zam.resizable(False, False)
        lz = Label(zam, image=iw1)
        lz.pack(anchor=W)
        label_text = Label(zam, text="О ФИЛЬМЕ ПЛАНЕТА ОБЕЗЬЯН", font=("Helvetica", 32))
        label_text.place(x=264, y=120)
        label_text0 = Label(zam, text="2 часа 30 минут Фантастика, боевик, приключения 16+", font=("Helvetica", 16))
        label_text0.place(x=220, y=240)
        label_text2 = Label(zam, text="Страна: США", font=("Helvetica", 16))
        label_text2.place(x=220, y=290)
        label_text3 = Label(zam, text="Режиссер: Уэс Болл", font=("Helvetica", 16))
        label_text3.place(x=220, y=340)
        label_text4 = Label(zam, text="Актеры: Оуэн Тиг, Питер Макон, Фрейя Аллан",
                            font=("Helvetica", 16), justify='left')
        label_text4.place(x=220, y=390)
        label_text1 = Label(zam, text="Несколько поколений после правления Цезаря. Обезьяны являются доминирующим"
                                      "\nвидом, живущим в гармонии, а люди вынуждены оставаться в тени. Пока новый"
                                      "\nтиранический nлидер обезьян строит свою империю, один молодой шимпанзе "
                                      "\nотправляется в путешествие, которое заставит его усомниться во всём, что"
                                      "\nон знал о прошлом, и сделать выбор, который определит будущее как обезьян,"
                                      "\nтак и людей.", font=("Helvetica", 16), justify='left')
        label_text1.place(x=220, y=440)

        zam.grab_set()
        zam.mainloop()

    def tof1():
        tof = Toplevel(w1)
        tof.title('О ФИЛЬМЕ МИНЕСТЕРСТВО НЕДЖЕНТЕЛЬМЕНСКИХ ДЕЛ')
        tof.iconbitmap('icon.ico')
        tof.geometry('1280x960')
        tof.resizable(False, False)
        lt = Label(tof, image=iw1)
        lt.pack(anchor=W)
        label_text = Label(tof, text="О ФИЛЬМЕ МИНЕСТЕРСТВО \nНЕДЖЕНТЕЛЬМЕНСКИХ ДЕЛ", font=("Helvetica", 32))
        label_text.place(x=264, y=120)
        label_text0 = Label(tof, text="2 часа 7 минут Комедийный экшн 18+", font=("Helvetica", 16))
        label_text0.place(x=220, y=270)
        label_text2 = Label(tof, text="Страна: США, Великобритания", font=("Helvetica", 16))
        label_text2.place(x=220, y=320)
        label_text3 = Label(tof, text="Режиссер: Гай Ричи", font=("Helvetica", 16))
        label_text3.place(x=220, y=370)
        label_text4 = Label(tof, text="Актеры: Генри Кавилл, Эйса Гонсалес, Алан Ричсон, Алекс Петтифер",
                            font=("Helvetica", 16), justify='left')
        label_text4.place(x=220, y=420)
        label_text1 = Label(tof, text="Они — лучшие из лучших. Отпетые авантюристы и первоклассные спецы,привыкшие"
                                     "\nдействовать в одиночку. Но когда на кону стоит судьба всего мира, им "
                                     "\nприходится объединиться в сверхсекретное боевое подразделение и отправиться"
                                     "\nна дерзкую миссию против нацистов. Теперь их дело — война, и вести они её "
                                     "\nбудут совершенно не по-джентльменски.", font=("Helvetica", 16), justify='left')
        label_text1.place(x=220, y=470)
        tof.grab_set()
        tof.mainloop()

    def sn1():

        sn = Toplevel(w1)
        sn.title('О ФИЛЬМЕ МАЙОР ГРОМ')
        sn.iconbitmap('icon.ico')
        sn.geometry('1280x960')

        sn.resizable(False, False)
        ls5 = Label(sn, image=iw1)
        ls5.pack(anchor=W)
        label_text = Label(sn, text="О ФИЛЬМЕ МАЙОР ГРОМ", font=("Helvetica", 32))
        label_text.place(x=264, y=120)
        label_text0 = Label(sn, text="3 часа Приключения, экшн 16+", font=("Helvetica", 16))
        label_text0.place(x=220, y=220)
        label_text2 = Label(sn, text="Страна: Россия", font=("Helvetica", 16))
        label_text2.place(x=220, y=270)
        label_text3 = Label(sn, text="Режиссер: Олег Трофим", font=("Helvetica", 16))
        label_text3.place(x=220, y=320)
        label_text4 = Label(sn, text="Актеры: Тихон Жизневский, Александр Сетейкин, Алексей Маклаков, Любовь Аксенова,"
                                     "\n Сергей Горошко, Константин Хабенский, Матвей Лыков, Ольга Сутулова",
                            font=("Helvetica", 16), justify='left')
        label_text4.place(x=220, y=370)
        label_text1 = Label(sn, text="Сюжет «Игры» разворачивается спустя год после того, как майор Гром поймал"
                                      "\n Чумного Доктора. Санкт-Петербург оправился от потрясений, Сергей Разумовский"
                                      "\nоказался в психиатрической лечебнице, а Игорь Гром стал главной знаменитостью"
                                      "\nв городе. Жизнь майора Грома идеальна: днем он ловит преступников вместе с "
                                      "\nнапарником Димой Дубиным, а вечера проводит в компании журналистки Юлии "
                                      "\nПчёлкиной. Полную идиллию прерывает появление в городе таинственного злодея,"
                                      "\nназывающего себя Призраком. Он предлагает Грому сыграть в опасную игру, ставка"
                                      "\n в которой — жизни обычных людей.", font=("Helvetica", 16), justify='left')
        label_text1.place(x=220, y=440)



        sn.grab_set()
        sn.mainloop()


#АФИША С ВЫБОРОМ ФИЛЬМА

    w1 = Toplevel(m)
    w1.configure(bg=wh)
    w1.iconbitmap('icon.ico')
    w1.geometry('1280x960')
    w1.resizable(False, False)
    lw1 = Label(w1, image=iw1)
    lw1.pack(anchor=W)
    w1.title('АФИША')

    label_text = Label(w1, text="Выберите фильм", font=("Helvetica", 32))
    label_text.place(x=264, y=120)


    ik1 = PhotoImage(file='Майор Гром.png')
    ik1t = PhotoImage(file='Майор Гром темный.png')
    def dk1(e):
        k1['image'] = ik1
    def dk1t(e):
        k1['image'] = ik1t
    ik2 = PhotoImage(file='Министерство неджентельменских дел.png')
    ik2t = PhotoImage(file='Министерство неджентельменских дел темный.png')
    def dk2(e):
        k2['image'] = ik2
    def dk2t(e):
        k2['image'] = ik2t
    ik3 = PhotoImage(file='Планета обезьян.png')
    ik3t = PhotoImage(file='Планета обезьян темный.png')
    def dk3(e):
        k3['image'] = ik3
    def dk3t(e):
        k3['image'] = ik3t
    ik4 = PhotoImage(file='Пушистый вояж.png')
    ik4t = PhotoImage(file='Пушистый вояж темный.png')
    def dk4(e):
        k4['image'] = ik4
    def dk4t(e):
        k4['image'] = ik4t
    ik5 = PhotoImage(file='Сто лет тому вперед.png')
    ik5t = PhotoImage(file='Сто лет тому вперед темный.png')
    def dk5(e):
        k5['image'] = ik5
    def dk5t(e):
        k5['image'] = ik5t
    ik6 = PhotoImage(file='незнакомцы.png')
    ik6t = PhotoImage(file='Незнакомцы темная.png')
    def dk6(e):
        k6['image'] = ik6
    def dk6t(e):
        k6['image'] = ik6t
    ik7 = PhotoImage(file='Винни Пух.png')
    ik7t = PhotoImage(file='Винни Пух темный.png')
    def dk7(e):
        k7['image'] = ik7
    def dk7t(e):
        k7['image'] = ik7t
    ik8 = PhotoImage(file='суперпташки.png')
    ik8t = PhotoImage(file='суперпташки темная.png')
    def dk8(e):
        k8['image'] = ik8
    def dk8t(e):
        k8['image'] = ik8t
    ik9 = PhotoImage(file='судная ночь.png')
    ik9t = PhotoImage(file='судная ночь темный.png')
    def dk9(e):
        k9['image'] = ik9
    def dk9t(e):
        k9['image'] = ik9t
    ik10 = PhotoImage(file='Асфальтовые джунгли.png')
    ik10t = PhotoImage(file='Асфальтовые джунгли темный.png')
    def dk10(e):
        k10['image'] = ik10
    def dk10t(e):
        k10['image'] = ik10t

    k1 = Button(w1, image=ik1, bg=wh, borderwidth=0, activebackground=wh, command=sn1)
    k1.place(x=264, y=200)
    k1.bind('<Enter>', dk1t)
    k1.bind('<Leave>', dk1)
    k2 = Button(w1, image=ik2, bg=wh, borderwidth=0, activebackground=wh, command=tof1)
    k2.place(x=417, y=200)
    k2.bind('<Enter>', dk2t)
    k2.bind('<Leave>', dk2)
    k3 = Button(w1, image=ik3, bg=wh, borderwidth=0, activebackground=wh, command=zam1)
    k3.place(x=567, y=200)
    k3.bind('<Enter>', dk3t)
    k3.bind('<Leave>', dk3)
    k4 = Button(w1, image=ik4, bg=wh, borderwidth=0, activebackground=wh, command=vit)
    k4.place(x=716, y=200)
    k4.bind('<Enter>', dk4t)
    k4.bind('<Leave>', dk4)
    k5 = Button(w1, image=ik5, bg=wh, borderwidth=0, activebackground=wh, command=sltn)
    k5.place(x=864, y=200)
    k5.bind('<Enter>', dk5t)
    k5.bind('<Leave>', dk5)
    k6 = Button(w1, image=ik6, bg=wh, borderwidth=0, activebackground=wh, command=nez)
    k6.place(x=264, y=519)
    k6.bind('<Enter>', dk6t)
    k6.bind('<Leave>', dk6)
    k7 = Button(w1, image=ik7, bg=wh, borderwidth=0, activebackground=wh, command=vp)
    k7.place(x=417, y=519)
    k7.bind('<Enter>', dk7t)
    k7.bind('<Leave>', dk7)
    k8 = Button(w1, image=ik8, bg=wh, borderwidth=0, activebackground=wh, command=superp)
    k8.place(x=567, y=519)
    k8.bind('<Enter>', dk8t)
    k8.bind('<Leave>', dk8)
    k9 = Button(w1, image=ik9, bg=wh, borderwidth=0, activebackground=wh, command=sudn)
    k9.place(x=716, y=519)
    k9.bind('<Enter>', dk9t)
    k9.bind('<Leave>', dk9)
    k10 = Button(w1, image=ik10, bg=wh, borderwidth=0, activebackground=wh, command=adel)
    k10.place(x=864, y=519)
    k10.bind('<Enter>', dk10t)
    k10.bind('<Leave>', dk10)

    w1.grab_set()
    w1.mainloop()
def b2():
    def vit1():
        def korz1():
            def chek():
                ch = Toplevel(wk)
                ch.geometry('345x600+200+50')
                ch.resizable(False, False)
                ch.title('Чек')
                ch.configure(bg=wh)
                dat = datetime.today()
                dat1 = dat.strftime('%Y.%m.%d')
                tim = dat.strftime('%H:%M:%S')
                n = randrange(100000, 999999)
                n1 = randrange(100000000, 999999999)
                n2 = randrange(1_000_000_000, 9999999999)
                h = f'''ООО "ПРЕМЬЕР ЗАЛ"
Екатеринбург, ул. Сулимова, 50
Кассовый чек №{n}
________________________________________________________________________'''
                lch = Label(ch, text=h, bg=wh)
                lch.pack()
                kon = f'''_______________________________________________________________________
   ИНН: {n1}                          ФП: {n2} 
 Кассир: Иванов И.И.
       Дата: {dat1}                          Время: {tim}
'''
                for o in cs:
                    if o > 0:
                        cs1.extend(str(o))
                for i in range(len(g1)):
                    g3 = f'''{g2[i]}'''
                    cs2 = f'''                         {cs1[i]}
{g2[i][-6:]}  *  {cs1[i]} = {int(g2[i][-6:-2]) * int(cs1[i])}p.'''
                    lk1 = Label(ch, text=g3, bg=wh, font=('Calibri', '10'))
                    lk1.place(x=2, y=100 + 50 * i)
                    lc = Label(ch, text=cs2, bg=wh, font=('Calibri', '10'))
                    lc.place(x=200, y=100 + 50 * i)
                lck = Label(ch, text=kon, bg=wh, justify='left')
                lck.place(x=0, y=82 + 50 * len(g1))
                ch.grab_set()
                ch.mainloop()

            global g, cs, lc1
            wk = Toplevel()
            wk.resizable(False, False)
            wk.geometry('400x600+200+50')
            wk.iconbitmap('icon.ico')
            wk.title('Корзина')
            lk = Label(wk, image=korzina)
            lk.place(x=-2, y=-2)
            lp = Label(wk, width=0, height=0, bg='#58C893')
            lp.pack()
            cs = [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16]
            g1 = set(g)
            g2 = list(g1)
            cs = list(cs)
            cs1 = list()
            s = 0
            for o in cs:
                if o > 0:
                    cs1.extend(str(o))
            for i in range(len(g1)):
                s += (int(g2[i][-6:-2]) * int(cs1[i]))
                g3 = f'''{g2[i]}'''
                cs2 = f'''                         {cs1[i]}
{g2[i][-6:]}  *  {cs1[i]} = {int(g2[i][-6:-2]) * int(cs1[i])}p.'''
                lk1 = Label(wk, text=g3, bg=wh1, font=('Inter', '10'), fg=wh2)
                lk1.place(x=2, y=21 + 50 * i)
                lc = Label(wk, text=cs2, bg=wh1, font=('Inter', '10'), fg=wh2)
                lc.place(x=270, y=21 + 50 * i)
                li = Label(wk, text=f'''Всегo:{s}p.
 Заказ будет ждать вас в магазине
 Оплата при получении''', bg=wh1, font=('Inter', '10'), fg=wh2)
                li.place(x=2, y=500)
            op = Button(wk, image=d, borderwidth=0, bg=wh1, highlightthickness=0, command=chek)
            op.place(x=250, y=530)
            wk.grab_set()
            wk.mainloop()

        def bk(e):
            korz.configure(bg=dgr)

        def bk1(e):
            korz.configure(bg='#93F9B9')

        vit = Toplevel(w2)
        vit.title('Расписание')
        vit.iconbitmap('icon.ico')
        vit.geometry('834x300+200+50')
        vit.resizable(False, False)
        lv = Label(vit, image=ivit)
        lv.place(x=0, y=-2)
        kor = PhotoImage(file='kor.png')
        korz = Button(vit, image=kor, borderwidth=0, height=300, bg='#93F9B9', width=30, command=korz1, activebackground=dgr)
        korz.place(x=802, y=0)
        korz.bind('<Enter>', bk)
        korz.bind('<Leave>', bk1)
        vit.grab_set()
        vit.mainloop()
    global bz2
    w2 = Toplevel(m)
    w2.iconbitmap('icon.ico')
    w2.title('Витамины')
    w2.resizable(False, False)
    w2.geometry('800x330+200+50')
    lw2 = Label(w2, image=iw2)
    lw2.pack()
    but = PhotoImage(file='but.png')
    if k == 1:
        bz2k = ser
    else:
        bz2k = wh
    bz2 = Button(w2, image=but, borderwidth=0, bg=bz2k, activebackground=bz2k, command=vit1)
    bz2.place(x=630, y=271)
    w2.grab_set()
    w2.mainloop()


def b4():
    w4 = Toplevel(m)
    w4.title('О нас')
    w4.iconbitmap('icon.ico')
    w4.resizable(False, False)
    w4.geometry('800x535+200+50')
    lw4 = Label(w4, image=iw4)
    lw4.place(x=-2, y=0)
    w4.grab_set()
    w4.mainloop()


def b3():
    w3 = Toplevel(m)
    w3.title('Расписание')
    w3.iconbitmap('icon.ico')
    w3.resizable(False, False)
    w3.geometry('800x501+200+50')
    lw3 = Label(w3, image=iw3)
    lw3.pack()
    w3.grab_set()
    w3.mainloop()


def fb1(e):
    bw1.configure(fg=purple)


def fb1l(e):
    bw1.configure(fg=black)


def fb2(e):
    bw2.configure(fg=purple)


def fb2l(e):
    bw2.configure(fg=black)


def fb3(e):
    bw3.configure(fg=purple)


def fb3l(e):
    bw3.configure(fg=black)

def fs(e):
    bs.configure(bg=dgr)


def fsl(e):
    bs.configure(bg=gr)

def fbre(e):
    br.place(x=1232,y=382)
def fbrl(e):
    br.place(x=1230,y=380)
def fble(e):
    bl.place(x=10, y=382)
def fbll(e):
    bl.place(x=8, y=380)
purple = '#951b81'
gr = '#54C590'
dgr = '#1F855C'
wh = 'white'
wh1 = 'white'
black= 'black'
ser = '#343434'
ls = '#4D5257'
red= '#fb3100'
g = list()
gray = 'gray'
c1 = 0
c2 = 0
c3 = 0
c4 = 0
c5 = 0
c6 = 0
c7 = 0
c8 = 0
c9 = 0
c10 = 0
c11 = 0
c12 = 0
c13 = 0
c14 = 0
c15 = 0
c16 = 0


m = Tk()

m.geometry('1280x960')

m.title('ПРЕМЬЕР ЗАЛ')
m.resizable(False, False)
m.iconbitmap('icon.ico')
m1 = PhotoImage(file='main1.png')
m2 = PhotoImage(file='main2.png')
m3 = PhotoImage(file='main3.png')

iw4 = PhotoImage(file='w4.png')
iw3 = PhotoImage(file='w3.png')
iw2 = PhotoImage(file='w2.png')
iw1 = PhotoImage(file='фон афиша.png')
korzina = PhotoImage(file='korz.png')
d = PhotoImage(file='zak.png')
l1 = Label(m, image=m1)
l1.place(x=-2, y=0)

f = font.Font(family="Rostov", size=30, weight="bold")
f.actual()
bw1 = Button(m, bg=wh, borderwidth=0, height=1, width=10, text='ФИЛЬМЫ', fg=black, font=f, activebackground=wh,
             activeforeground=black, command=b1)
bw1.place(x=300, y=23)
bw1.bind('<Enter>', fb1)
bw1.bind('<Leave>', fb1l)

bw2 = Button(m, bg=wh, borderwidth=0, height=1, width=12, text='РАСПИСАНИЕ', fg=black, font=f, activebackground=wh,
             activeforeground=black, command=b2)
bw2.place(x=550, y=23)
bw2.bind('<Enter>', fb2)
bw2.bind('<Leave>', fb2l)

bw3 = Button(m, bg=wh, borderwidth=0, height=1, width=10, text='КОНТАКТЫ', fg=black, font=f, activebackground=wh,
             activeforeground=black, command=b3)
bw3.place(x=865, y=23)

bw3.bind('<Enter>', fb3)
bw3.bind('<Leave>', fb3l)

br1 = ImageTk.PhotoImage(Image.open('r.png').resize((45,60)))
br = Button(m, image=br1,bg=red, borderwidth= 0,highlightthickness=0, command=r, activebackground=red)
br.place(x=1230, y=380)
br.bind('<Enter>', fbre)
br.bind('<Leave>', fbrl)
bl1 = ImageTk.PhotoImage(Image.open('l.png').resize((45,60)))
bl = Button(m, image=bl1,bg=red, borderwidth= 0,highlightthickness=0, command=l,activebackground=red)
bl.place(x=8, y=380)
bl.bind('<Enter>', fble)
bl.bind('<Leave>', fbll)
photos = [ImageTk.PhotoImage(Image.open(f"main{i}.png").resize((1280, 960))) for i in range(1, 4)]
photo_iterator = itertools.cycle(photos)

def update_photo():
    l1.config(image=next(photo_iterator))
    l1.after(5000, update_photo)
update_photo()

m.mainloop()