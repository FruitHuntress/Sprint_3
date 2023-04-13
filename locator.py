
class Locator:

    profile_button = "//p[contains(text(),'Личный Кабинет')]"   #кнопка входа в Личный кабинет
    login_button = ".//button[contains(text(),'Войти в аккаунт')]"   #кнопка входа в аккаунт
    registration_link = ".//a[contains(text(), 'Зарегистрироваться')]"  #кнопка регистрации
    registration_email = "//label[contains(text(),'Email')]/following-sibling::input"  #поле ввода почты на форме регистрации
    registration_password = ".//input[@name='Пароль']"  # поле ввода пароля на форме регистрации
    registration_button = "//button[contains(text(),'Зарегистрироваться')]"  # кнопка регистрации на форме регистрации
    registration_title = "//h2[contains(text(),'Регистрация')]"  #заголовок формы регистрации
    name = "name"  # поле для ввода имени на форме регистрации
    login_title = ".//h2[contains(text(),'Вход')]"  #заголовок формы авторизации
    authorization_email = "name"  #поле ввода почты на форме авторизации
    authorization_password = ".//input[@name='Пароль']" # поле ввода пароля на форме авторизации
    authorization_button = "//button[contains(text(),'Войти')]"  # кнопка входа на форме авторизации
    constructor_title = "//h1[contains(text(),'Соберите бургер')]" #заголовок конструктора
    login_link = "//a[contains(text(),'Войти')]"  # ссылка на форму авторизации
    pass_restoration_link = "//a[contains(text(),'Восстановить пароль')]"  # ссылка на форму восстановления пароля
    pass_restoration_title = "//h2[contains(text(),'Восстановление пароля')]"  # заголовок формы восстановления пароля
    profile_link = "//a[contains(text(),'Профиль')]"  # кнопка "Профиль" в личном кабинете
    constructor_button = "//p[contains(text(),'Конструктор')]"    # кнопка "Конструктор" на главной странице
    logo = ".//div[@class='AppHeader_header__logo__2D0X2']"   # логотип "Stellar Burgers"
    sauces = ".//span[contains(text(),'Соусы')]"  # кнопка "Соусы"
    buns = ".//span[contains(text(),'Булки')]"   # кнопка "Булки"
    toppings = ".//span[contains(text(),'Начинки')]"   # кнопка "Начинки"
    logout_button = "//button[contains(text(),'Выход')]"    # кнопка деавторизации
    incorrect_pass = "//p[contains(text(),'Некорректный пароль')]"    # сообщение о некорректном пароле
    active_section = "//*[contains(@class, 'tab_tab_type_current')]"
