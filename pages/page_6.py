import streamlit as st


def visualization():
    st.markdown(f"""
    ## Лекарственные средства
    """)

    acts = [
        "Пенициллины",
        "Аминогликозиды",
        "Карбапенемы",
        "Нитрофураны",
        "Цефалоспорины",
        "Фторхинолоны"
    ]

    select_act = st.selectbox('Выберите группу препаратов', acts)

    if select_act == acts[0]:
        poisons = [
            'Бензилпенициллин',
            'Оксациллин',
            'Ампициллин',
            'Амоксициллин'
        ]
        select_poison = st.selectbox('Выберите препарат', poisons)

        if select_poison == poisons[0]:
            st.markdown("""
            ### Торговое наименование
            Бензилпенициллин, Бициллин, Бензилпенициллина натриевая соль, Бензилпенициллина новокаиновая соль
            
            ### Форма выпуска 
            Порошок для приготовления раствора для внутривенного и внутримышечного введения
            
            В дозировках: 1000000 ЕД
            
            ### Режим дозирования
            
            Вводят в/м, в/в, п/к, эндолюмбально.

            При в/м и в/в введении взрослым суточная доза варьирует от 250 000 до 60 млн. ЕД. Суточная доза для детей в возрасте до 1 года составляет 50 000-100 000 ЕД/кг, старше 1 года - 50 000 ЕД/кг; при необходимости суточную дозу можно увеличить до 200 000-300 000 ЕД/кг, по жизненным показаниям - до 500 000 ЕД/кг. Кратность введения 4-6 раз/сут.
            
            Эндолюмбально вводят в зависимости от заболевания и тяжести течения взрослым - 5000-10 000 ЕД, детям - 2000-5000 ЕД. Препарат разводят в стерильной воде для инъекций или в 0.9% растворе натрия хлорида из расчета 1 тыс.ЕД/мл. Перед инъекцией (в зависимости от уровня внутричерепного давления) извлекают 5-10 мл СМЖ и добавляют ее к раствору антибиотика в равном соотношении.
            
            П/к бензилпенициллин применяют для обкалывания инфильтратов (100 000-200 000 ЕД в 1 мл 0.25%-0.5% раствора новокаина).
            
            Бензилпенициллина калиевую соль применяют только в/м и п/к, в тех же дозах что и бензилпенициллина натриевую соль.
            
            Бензилпенициллина новокаиновую соль применяют только в/м. Средняя терапевтическая доза для взрослых: разовая - 300 000 ЕД, суточная - 600 000 ЕД. Детям в возрасте до 1 года - 50 000-100 000 ЕД/кг/сут, старше 1 года - 50 000 ЕД/кг/сут. Кратность введения 3-4 раза/сут.
            
            Длительность лечения бензилпенициллином в зависимости от формы и тяжести течения заболевания может составлять от 7-10 дней до 2 мес и более.
            
            ### Показания 
            
            Лечение заболеваний, вызванных чувствительными к бензилпенициллину микроорганизмами: крупозная и очаговая пневмония, эмпиема плевры, сепсис, септицемия, пиемия, острый и подострый септический эндокардит, менингит, острый и хронический остеомиелит, инфекции мочевыводящих и желчных путей, ангина, гнойные инфекции кожи, мягких тканей и слизистых оболочек, рожа, дифтерия, скарлатина, сибирская язва, актиномикоз, лечение гнойно-воспалительных заболеваний в акушерско-гинекологической практике, ЛОР-заболеваний, глазных болезней, гонорея, бленнорея, сифилис.
            
            ### Противопоказания
            
            Повышенная чувствительность к бензилпенициллину и другим препаратам из группы пенициллинов и цефалоспоринов. Эндолюмбальное введение противопоказано пациентам, страдающим эпилепсией.
            """)

        elif select_poison == poisons[1]:
            st.markdown("""
            ### Торговое наименование
            
            Оксациллин
            
            ### Форма выпуска
            
            * Таблетки 250 мг
            * Порошок для приготовления раствора для внутривенного и внутримышечного введения 250мг, 500мг, 1г
            * Порошок для приготовления раствора для инъекций 1г, 2г
            
            ### Режим дозирования
            
            При приеме внутрь разовая доза для взрослых, подростков и детей с массой тела более 40 кг составляет 0.5-1 г каждые 4-6 ч. Детям с массой тела до 40 кг - по 12.5-25 мг/кг каждые 6 ч.

            В/м или в/в взрослым, подросткам и детям с массой тела более 40 кг - по 0.25-1 г каждые 4-6 ч или в зависимости от этиологии заболевания - по 1.5-2 г каждые 4 ч. Новорожденным и недоношенным детям - по 6.25 мг/кг каждые 6 ч; детям с массой тела до 40 кг - по 12.5-25 мг/кг каждые 6 ч.
            
            Максимальная суточная доза для взрослых при приеме внутрь составляет 6 г.
            
            ### Показания
            
            Инфекционно-воспалительные заболевания, вызванные микроорганизмами, продуцирующими пенициллиназу (главным образом стафилококками), или при подозрении на такого рода инфекцию, до получения результатов лабораторных исследований (в т.ч. синуситы, инфекции кожи и мягких тканей, инфекции костей и суставов, бактериальный эндокардит, бактериальный менингит).
            
            ### Противопоказания
            
            Повышенная чувствительность к оксациллину и другим пенициллинам.
            """)
        elif select_poison == poisons[2]:
            st.markdown("""
            ### Торговое наименование
            
            Ампициллин, Ампициллина тригидрат, Ампициллин-Ферейн
            
            ### Форма выпуска
            
            * Порошок для приготовления раствора для внутривенного и внутримышечного введения 250мг, 500мг, 1г
            * Порошок для приготовления суспензии для приема внутрь 5 г (250 мг/5 мл)
            * Таблетки 250 мг
            
            ### Режим дозирования
            
            При приеме внутрь разовая доза для взрослых составляет 250-500 мг, суточная доза - 1-3 г. Максимальная суточная доза составляет - 4 г.

            Детям препарат назначают в суточной дозе 50-100 мг/кг, детям с массой тела до 20 кг - 12.5-25 мг/кг.
            
            Суточную дозу делят на 4 приема. Продолжительность лечения зависит от тяжести инфекции и эффективности лечения. Таблетки принимают внутрь независимо от приема пищи.
            
            При парентеральном введении (в/м, в/в струйно или в/в капельно) разовая доза для взрослых составляет 250-500 мг, суточная доза - 1-3 г; при тяжелых инфекциях суточная доза может быть увеличена до 10 г и более.
            
            Новорожденным детям препарат назначают в суточной дозе 100 мг/кг, детям остальных возрастных групп - 50 мг/кг. При тяжелом течении инфекции указанные дозы могут быть удвоены.
            
            Суточную дозу делят на 4-6 введений с интервалом 4-6 ч. Длительность в/м введения - 7-14 дней. Продолжительность в/в применения 5-7 дней, с последующим переходом (при необходимости) на в/м введение.
            
            Раствор для в/м введения готовят, добавляя к содержимому флакона 2 мл воды для инъекций.
            
            Для в/в струйного введения разовую дозу препарата (не более 2 г) растворяют в 5-10 мл воды для инъекций или изотонического раствора натрия хлорида и вводят медленно в течение 3-5 мин (1-2 г в течение 10-15 мин). Растворы используют сразу после приготовления.
            
            ### Показания
            
            Инфекционно-воспалительные заболевания, вызванные чувствительными к ампициллину микроорганизмами, в т.ч.:
            
            * инфекции дыхательных путей (в т.ч. бронхит, пневмония, абсцесс легкого);
            * инфекции ЛОР-органов (в т.ч. тонзиллит);
            * инфекции желчевыводящих путей (в т.ч. холецистит, холангит);
            * инфекции мочевыводящих путей (в т.ч. пиелит, пиелонефрит, цистит);
            * инфекции ЖКТ (в т.ч. сальмонеллоносительство);
            * гинекологические инфекции;
            * инфекции кожи и мягких тканей;
            * перитонит;
            * сепсис, септический эндокардит;
            * менингит;
            * ревматизм;
            * рожа;
            * скарлатина;
            * гонорея.
            
            ### Противопоказания
            
            * повышенная чувствительность к антибиотикам из группы пенициллина и другим беталактамным антибиотикам;
            * выраженные нарушения функции печени (для парентерального применения).
            """)

        else:
            st.markdown("""
            ### Торговое наименование
            
            Амоксициллин, Амоксициллин экспресс, Амоксиклав, Клавамокс, Оспамокс, Флемоксин Солютаб, Амосин
            
            ### Форма выпуска
            
            * Таблетки диспергируемые 125мг, 250мг, 500мг, 1г
            * Капсулы 250мг, 500мг
            * Порошок для приготовления суспензии для приема внутрь 125мг/5мл, 250мг/5мл, 500мг/5мл
            
            ### Режим дозирования
            
            Для приема внутрь разовая доза для взрослых и детей старше 10 лет (с массой тела более 40 кг) составляет 250-500 мг, при тяжелом течении заболевания - до 1 г. Для детей в возрасте 5-10 лет разовая доза составляет 250 мг; в возрасте от 2 до 5 лет - 125 мг. Интервал между приемами - 8 ч. Для детей с массой тела менее 40 кг суточная доза в зависимости от показаний и клинической ситуации может составлять 20-100 мг/кг в 2-3 приема.

            При парентеральном применении взрослым в/м - по 1 г 2 раза/сут, в/в (при нормальной функции почек) - 2-12 г/сут. Детям в/м - 50 мг/кг/сут, разовая доза - 500 мг, частота введения - 2 раза/сут; в/в - 100-200 мг/кг/сут.
            
            ### Показания
            
            Для применения в виде монотерапии и в комбинации с клавулановой кислотой: инфекционно-воспалительные заболевания, вызванные чувствительными микроорганизмами, в т.ч. бронхит, пневмония, ангина, пиелонефрит, уретрит, инфекции ЖКТ, гинекологические инфекции, инфекционные заболевания кожи и мягких тканей, листериоз, лептоспироз, гонорея.

            Для применения в комбинации с метронидазолом: хронический гастрит в фазе обострения, язвенная болезнь желудка и двенадцатиперстной кишки в фазе обострения, ассоциированные с Helicobacter pylori.
            
            ### Противопоказания
            
            Инфекционный мононуклеоз, лимфолейкоз, тяжелые инфекции ЖКТ, сопровождающиеся диареей или рвотой, респираторные вирусные инфекции, аллергический диатез, бронхиальная астма, сенная лихорадка, повышенная чувствительность к пенициллинам и/или цефалоспоринам.

            Для применения в комбинации с метронидазолом: заболевания нервной системы; нарушения кроветворения, лимфолейкоз, инфекционный мононуклеоз; повышенная чувствительность к производным нитроимидазола.

            Для применения в комбинации с клавулановой кислотой: указания в анамнезе на нарушения функции печени и желтуху, связанные с приемом амоксициллина в комбинации с клавулановой кислотой.
            """)