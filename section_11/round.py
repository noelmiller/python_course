def main() -> None:
    a: float = 200.312399
    b: float = 18.12132
    c: float = 47.12312

    result: float = a + b + c
    print(round(result, 2)) # 265.56 - 2 decimal places
    print(round(result, 1)) # 265.6 - 1 decimal place
    print(round(result, 0)) # 266.0 - 0 decimal places
    print(round(result, -1)) # 270.0 - rouded to the nearest 10
    print(round(result, -2)) # 300.0 - rouded to the nearest 100

if __name__ == '__main__':
    main()
