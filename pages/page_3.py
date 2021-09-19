import streamlit as st

def visualization():
    st.markdown('# Коррекция электролитов')

    elements = ['Кальций', 'Калий', 'Магний']

    st.markdown("Выберите нужный элемент:")
    option = st.radio('', elements)

    if option == elements[0]:
        st.markdown(f"""
        ## Коррекция кальция
        
        Кальций ФП$=0.1-0.5$ ммоль/кг/сут\n
        (у новорожденных, недоношенных $1-3$ ммоль/кг/сут)\n
        $Ca$ хлорид $10%=1$мл$=1$ ммоль\n
        $Ca$ глюконат $10%=1$ мл $= 0.25$\n
        Вводим $10%$ р-р\n
        $0.5$ мл/год/сут $(СаCl) -1$ мл/год/сут ($Са$ глюк.)\n
        (не более $10$ мл), за $1-2$ введения""")
    elif option == elements[1]:
        st.markdown("""
        ## Коррекция калия
        
        Калий ФП $= 1,0-2,0$ ммоль/кг/сут\n
        Скорость введения $К$ не должна превышать $0,5$ ммоль/кг/час\n
        Вводим:\n
        - в растворе глюкозы
        - при наличии диуреза
        - суточную дозу делим на $2$ введения
        - концентрация К в растворе не более $1%$
        $7.5%$ р-р $= 1$ мл $= 1$ ммоль\n
        $4%$ р-р $= 1$ мл $= 0.5$ ммоль\n
        Вводим\n
        $7.5%$ р-р $1-2$ мл/кг/сут\n
        $4%$ р-р $2-4$ мл/кг/сут
        """)
    elif option == elements[2]:
        st.markdown("""
        ## Коррекция магния
        
        Магний ФП $= 0.1-0.7$ ммоль/кг/сут\n
        $25% = 1$ мл $= 2$ ммоль\n
        Вводим в р-ре глюкозы\n
        $0,5-1$ мл/кг/сут не более $20$ мл за $2$ раза\n
        Натрий ФП $= 2 – 4$ ммоль/кг/сут\n
        $10%$ $NaCl=1$ мл $= 1,71$ ммоль\n
        $0,9%$ $NaCl=10$мл $= 1,53$ ммоль
        """)

