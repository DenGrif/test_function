def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")

    # Вызов inner_function внутри test_function
    inner_function()

# Вызов test_function
test_function()

# Вызов inner_function приводит к ошибке NameError, так как она не существует в глобальной области видимости.
inner_function()
