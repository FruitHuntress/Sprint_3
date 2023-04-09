
class Locator:

    profile_button = "//p[contains(text(),'Личный Кабинет')]"   #кнопка входа в Личный кабинет
    login_button = ".//button[contains(text(),'Войти в аккаунт')]"   #кнопка входа в аккаунт
    registration_link = ".//a[contains(text(), 'Зарегистрироваться')]"  #кнопка регистрации
    registration_email = "//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[2]/div[1]/div[1]/input[1]"  #поле ввода почты на форме регистрации
    registration_password = "//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[3]/div[1]/div[1]/input[1]"  # поле ввода пароля на форме регистрации
    registration_button = "//button[contains(text(),'Зарегистрироваться')]"  # кнопка регистрации на форме регистрации
    registration_title = "//h2[contains(text(),'Регистрация')]"  #заголовок формы регистрации
    name = "//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/input[1]"  # поле для ввода имени на форме регистрации
    login_title = ".//h2[contains(text(),'Вход')]"  #заголовок формы авторизации
    authorization_email = ".//form/fieldset[1]/div/div[1]/input"  #поле ввода почты на форме авторизации
    authorization_password = ".//form/fieldset[2]/div/div[1]/input" # поле ввода пароля на форме авторизации
    authorization_button = "//button[contains(text(),'Войти')]"  # кнопка входа на форме авторизации
    constructor_title = "//h1[contains(text(),'Соберите бургер')]" #заголовок конструктора
    login_link = "//a[contains(text(),'Войти')]"  # ссылка на форму авторизации
    pass_restoration_link = "//a[contains(text(),'Восстановить пароль')]"  # ссылка на форму восстановления пароля
    pass_restoration_title = "//h2[contains(text(),'Восстановление пароля')]"  # заголовок формы восстановления пароля
    profile_link = "//a[contains(text(),'Профиль')]"  # кнопка "Профиль" в личном кабинете
    constructor_button = "//p[contains(text(),'Конструктор')]"    # кнопка "Конструктор" на главной странице
    logo = "//header/nav[1]/div[1]/a[1]/*[1]"   # логотип "Stellar Burgers"
    sauces = "//body/div[@id='root']/div[1]/main[1]/section[1]/div[1]/div[2]"  # кнопка "Соусы"
    buns = "//body/div[@id='root']/div[1]/main[1]/section[1]/div[1]/div[1]"   # кнопка "Булки"
    toppings = "//body/div[@id='root']/div[1]/main[1]/section[1]/div[1]/div[3]"    # кнопка "Начинки"
    logout_button = "//button[contains(text(),'Выход')]"    # кнопка деавторизации
    incorrect_pass = "//p[contains(text(),'Некорректный пароль')]"    # сообщение о некорректном пароле
