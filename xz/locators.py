from selenium.webdriver.common.by import By
class LocatorsBurgers:
    # кнопка "личный кабинет"
    ACCOUNT_BUTTON = (By.CSS_SELECTOR, "[href='/account']")

    # кнопка "Зарегистрироваться"
    REGISTER_BUTTON = (By.CSS_SELECTOR, "[href='/register']")

    # поле ввода "имя"
    NAME_FIELD = (By.XPATH, "//label[contains(text(), 'Имя')]/following-sibling::input")

    # поле ввода "email"
    EMAIL_FIELD = (By.XPATH, "//label[contains(text(), 'Email')]/following-sibling::input")

    # поле ввода "Пароль"
    PASSWORD_FIELD = (By.XPATH, "//input[@name='Пароль']")

    # Кнопка "Зарегистрироваться"
    REGISTER_FINAL_BUTTON = (By.XPATH, "//button[contains(@class, 'button_button__33qZ0')]")

    # Сообщение о неккоретном пароле
    MESSAGE_INCORRECT_PASSWORD = (By.XPATH, "//p[@class='input__error text_type_main-default' and text()='Некорректный пароль']")

    # Кнопка "Войти"
    INPUT_MAIN_BUTTON = (By.XPATH, "//button[contains(@class, 'button_button__33qZ0')]")

    # Кнопка "Войти" на странице восстановления пароля
    INPUT_REGISTER_BUTTON = (By.CSS_SELECTOR, "[href='/login']")

    # Кнопка "Восстановить пароль"
    PASSWORD_RECOVERY_BUTTON = (By.CSS_SELECTOR, "[href='/forgot-password']")

    # Разделы личного кабинте(Профиль, История закзазов, Выход)
    SECTIONS = (By.CSS_SELECTOR, "[class='Account_nav__Lgali']")

    # Кнопка конструктора
    CONSRUKTOR_BUTTON = (By.CSS_SELECTOR, "[class='AppHeader_header__link__3D_hX']")

    # Логотип программы
    LOGOTIP_BUTTON = (By.CSS_SELECTOR, "[class='AppHeader_header__logo__2D0X2']")

    # Надпись "Соберите бургер"
    SOBERITE_BURGER = (By.CSS_SELECTOR, "[class='text text_type_main-large mb-5 mt-10']")

    # Кнопка "Выход"
    EXIT_BUTTON = (By.CSS_SELECTOR, "[class='Account_button__14Yp3 text text_type_main-medium text_color_inactive']")

    # Раздел "Булки"
    BULKI_SECTION = (By.XPATH, "//span[text()='Булки']/parent::*")

    # Раздел "Соусы"
    SOUS_SECTION = (By.XPATH, "//span[text()='Соусы']/parent::*")

    # Раздел "Начинки"
    NACHINKI_SECTION = (By.XPATH, "//span[text()='Начинки']/parent::*")