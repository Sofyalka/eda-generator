#!/usr/bin/env python
# coding: utf-8

# In[1]:
#pip install streamlit

# In[18]:
import streamlit as st
import pandas as pd
import requests
import uuid

# Уникальный ID сессии
session_id = str(uuid.uuid4())

# Боковая панель
st.sidebar.markdown(
    """
    <div style="background-color: #f2f2f2; padding: 15px; border-radius: 10px; 
                box-shadow: 2px 2px 5px rgba(0,0,0,0.1); font-size: 14px;">
        <h3 style="color: #333333;">О проекте</h3>
        <p>
            Этот сервис позволяет загружать <b>CSV</b> или <b>Excel</b> файл и получать 
            автоматический <b>EDA-отчёт</b> в формате HTML. <br><br>
            Используется библиотека <code>ydata_profiling</code>. <br>
            Полезно для первичного анализа данных.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)


# Заголовок
st.title("Генерация EDA-отчета")
uploaded_file = st.file_uploader("Загрузите файл (CSV или Excel)", type=["csv", "xlsx"])

if uploaded_file is not None:
    with st.status("Загрузка файла...", expanded=True) as status:
        st.write("Отправка файла на сервер")
        files = {"file": (uploaded_file.name, uploaded_file, uploaded_file.type)}
        
        try:
            response = requests.post("http://localhost:8000/upload/", files=files)
        except Exception as e:
            st.error(f"Ошибка подключения к серверу: {e}")
            st.stop()
        
        if response.status_code == 200:
            st.write("Генерация отчета завершена ")
            status.update(label="Готово!", state="complete")

            st.download_button(
                label=" Скачать отчет (HTML)",
                data=response.content,
                file_name="EDA_Report.html",
                mime="text/html"
            )
            
            st.markdown(
                """
                <p>Чтобы сохранить отчет в формате PDF:</p>
                <ol>
                    <li>Откройте скачанный HTML-файл в браузере</li>
                    <li>Нажмите <b>Ctrl+P</b> (или ⌘+P на Mac)</li>
                    <li>Выберите «Сохранить как PDF»</li>
                </ol>
                """,
                unsafe_allow_html=True
            )
            
        else:
            status.update(label="Ошибка ", state="error")
            st.error(f"Ошибка при генерации отчета: {response.text}")

# Отображение ID сессии внизу
st.markdown(
    f"""
    <div style='position: fixed; bottom: 10px; left: 50%; transform: translateX(-50%);
                background-color: #f0f2f6; padding: 5px 15px; border-radius: 8px;
                font-size: 12px; color: grey; box-shadow: 0px 0px 8px rgba(0,0,0,0.1);'>
        ID сессии: {session_id}
    </div>
    """,
    unsafe_allow_html=True
)
