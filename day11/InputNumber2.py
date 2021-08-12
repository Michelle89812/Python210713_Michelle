def input_number():
    try:
        x = int(input('請輸入分子: '))
        y = int(input('請輸入分母: '))
        z = x / y

    except ValueError as e:
        print('錯誤原因:', e)
        print('錯誤類型:', e.__class__.__name__)
        print('您輸入的不是數字，請重新輸入~')
        input_number()
    except ZeroDivisionError as e:
        print('錯誤原因:', e)
        print('錯誤類型:', e.__class__.__name__)
        print('分母不可為0，程式結束!')
        return
    except Exception as e:
        print('錯誤原因:', e)
        print('錯誤類型:', e.__class__.__name__)
        print('其他的錯誤，程式結束!')
        return
    else:  # 若無錯誤則執行
        print(x, '/', y, '=', z)
    finally:  # 不論是否有錯誤，都要執行
        print('我一定要執行')


if __name__ == '__main__':
    input_number()
