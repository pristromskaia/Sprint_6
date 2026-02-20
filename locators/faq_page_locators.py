from selenium.webdriver.common.by import By


class FaqLocators:
    PRICE_QUESTION = (By.ID, "accordion__heading-0")
    PRICE_ANSWER = (By.ID, "accordion__panel-0")
    QUANTITY_QUESTION = (By.ID, "accordion__heading-1")
    QUANTITY_ANSWER = (By.ID, "accordion__panel-1")
    RENT_TIME_QUESTION = (By.ID, "accordion__heading-2")
    RENT_TIME_ANSWER = (By.ID, "accordion__panel-2")
    TODAY_ORDER_QUESTION = (By.ID, "accordion__heading-3")
    TODAY_ORDER_ANSWER = (By.ID, "accordion__panel-3")
    RETURN_OR_EXTEND_QUESTION = (By.ID, "accordion__heading-4")
    RETURN_OR_EXTEND_ANSWER = (By.ID, "accordion__panel-4")
    CHARGER_DELIVERY_QUESTION = (By.ID, "accordion__heading-5")
    CHARGER_DELIVERY_ANSWER = (By.ID, "accordion__panel-5")
    ORDER_CANCELLATION_QUESTION = (By.ID, "accordion__heading-6")
    ORDER_CANCELLATION_ANSWER = (By.ID, "accordion__panel-6")
    ORDER_AREA_QUESTION = (By.ID, "accordion__heading-7")
    ORDER_AREA_ANSWER = (By.ID, "accordion__panel-7")
