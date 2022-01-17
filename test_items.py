from selenium.webdriver.common.by import By

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

# Код работает на браузере Chrome
# Code works on Chrome browser

def test_guest_should_see_button_add_to_basket(browser):
    # открытие ссылки
    # link opening
    browser.get(link)

    # проверка на наличие кнопки добавления в корзину
    # check for add to cart button
    button = browser.find_element(By.CLASS_NAME, 'btn-add-to-basket')

    # если кнопка не найдена, то возвращает ошибку
    # if the button is not found, it returns an error
    assert button is not None, 'element "button" is not found!'
