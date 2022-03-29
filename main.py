from entity.employee import Employee, Admin

if __name__ == '__main__':
    e = Employee(1, "Martin", "Kokonyan", "mkk", "12345qwe", "mkk@it.com")
    a = Admin(2, "Tanya", "Kokonyan", "tkk", "12345qwe", "tkk@it.com")

    print(e)
    print(a)

    dict = e.__dict__
    print(dict)
    dict_vals = dict.values()
    print(*dict_vals)
    c = Admin(**{k[1::]: v for k, v in dict.items()})
    print(c)
