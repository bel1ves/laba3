import streamlit as st
import requests
import schemas

# Функция для отправки запроса на создание пользователя
def create_user(name, email, password):
    url = "http://127.0.0.1:8000/users/"
    user = schemas.UserCreate(name=name, email=email, password=password)
    response = requests.post(url, json=user.dict())
    return response.json()

# Главная функция Streamlit
def main():
    st.title("Создание пользователя")

    # Форма для ввода имени и электронной почты
    name = st.text_input("Имя")
    email = st.text_input("Электронная почта")
    password = st.text_input("Пароль", type="password")

    # Кнопка для отправки формы
    if st.button("Создать пользователя"):
        if name and email:
            result = create_user(name, email, password)
            st.success(f"Пользователь успешно создан: {result}")
        else:
            st.error("Пожалуйста, заполните все поля.")

if __name__ == "__main__":
    main()