from selenium.webdriver.common.by import By


class OrderButtonLocators:
    ORDER_BUTTON_TOP = (
        By.XPATH,
        '//div[contains(@class,"Header_Nav")]//button[normalize-space()="Заказать"]',
    )
    ORDER_BUTTON_BOTTOM = (
        By.XPATH,
        '//div[contains(@class,"Home_FinishButton")]//button[normalize-space()="Заказать"]',
    )


class OrderFormLocators:
    ORDER_TITLE = (By.XPATH, '//div[normalize-space()="Для кого самокат"]')
    NAME_FIELD = (By.XPATH, '//input[@placeholder="* Имя"]')
    LAST_NAME_FIELD = (By.XPATH, '//input[@placeholder="* Фамилия"]')
    ADDRESS_FIELD = (By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]')
    SUBWAY_FIELD = (By.XPATH, '//input[@placeholder="* Станция метро"]')
    SUBWAY_STATION_DROPDOWN = (
        By.XPATH,
        '//div[@class="select-search__select"]//button',
    )
    PHONE_FIELD = (
        By.XPATH,
        '//input[@placeholder="* Телефон: на него позвонит курьер"]',
    )
    NEXT_BUTTON = (By.XPATH, '//button[normalize-space()="Далее"]')


class AboutRentLocators:
    RENT_TITLE = (By.XPATH, '//div[normalize-space()="Про аренду"]')
    ORDER_DATE_FIELD = (By.XPATH, '//input[@placeholder="* Когда привезти самокат"]')
    ORDER_DATE_SELECT_DAY = (By.CSS_SELECTOR, ".react-datepicker__day--today")
    RENT_PERIOD_MENU = (
        By.CSS_SELECTOR,
        '.Dropdown-root .Dropdown-menu[aria-expanded="true"]',
    )
    RENT_PERIOD = (By.CSS_SELECTOR, ".Dropdown-root .Dropdown-control")
    RENT_PERIOD_ONE_DAY = (
        By.XPATH,
        '//div[contains(@class,"Dropdown-menu") and @aria-expanded="true"]'
        '//div[contains(@class,"Dropdown-option") and normalize-space()="сутки"]',
    )
    RENT_PERIOD_SEVEN_DAYS = (
        By.XPATH,
        '//div[contains(@class,"Dropdown-menu") and @aria-expanded="true"]'
        '//div[contains(@class,"Dropdown-option") and normalize-space()="семеро суток"]',
    )

    SCOOTER_COLOR_BLACK = (By.ID, "black")
    SCOOTER_COLOR_GREY = (By.ID, "grey")

    COMMENT_FIELD = (By.XPATH, '//input[@placeholder="Комментарий для курьера"]')
    ORDER_BUTTON = (
        By.XPATH,
        '//div[contains(@class,"Order_Buttons")]//button[normalize-space()="Заказать"]',
    )
    CONFIRM_BUTTON = (
        By.XPATH,
        '//div[contains(@class,"Order_Buttons")]//button[normalize-space()="Да"]',
    )
    SUCCESS_ORDER = (
        By.XPATH,
        '//div[contains(@class,"Order_ModalHeader") and contains(normalize-space(.), "Заказ оформлен")]',
    )
    CHECK_STATUS = (By.XPATH, '//button[normalize-space()="Посмотреть статус"]')


class OrderLogo:
    YANDEX_LOGO = (By.XPATH, '//a[contains(@href,"yandex.ru")]')
    SCOOTER_LOGO = (By.XPATH, '//a[@href="/"]')
