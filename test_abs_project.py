def test_abs1():
    assert abs(-42) == 42, "Should be absolute value of a number" 

if __name__ == "__main__":  # конструкция служит для подтверждения того, что данный скрипт был запущен напрямую, а не вызван внутри другого файла в качестве модуля.
    test_abs1()             # выполняет тестовый сценарий.
    print("All tests passed!")  #вывели сообщение, если все тесты прошли успешно.

def test_abs2():
    assert abs(-42) == 42, "Should be absolute value of a number"

def test_abs3():
    assert abs(-42) == -42, "Should be absolute value of a number"

if __name__ == "__main__":
    test_abs2()
    test_abs3()
    print("Everything passed")