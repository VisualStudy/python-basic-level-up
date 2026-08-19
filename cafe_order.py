# 카페 주문 프로그램
# 파이썬 기본 문법 실습

menu = {
    "아메리카노": 3000,
    "카페라떼": 4000,
    "바닐라라떼": 4500
}


def show_menu():
    print("\n--- 카페 메뉴 ---")

    for name, price in menu.items():
        print(f"{name}: {price:,}원")


def calculate_price(menu_name, quantity):
    return menu[menu_name] * quantity


total_price = 0

print("카페 주문 프로그램입니다.")

while True:
    show_menu()

    order = input("\n주문할 메뉴를 입력하세요. (종료: q): ")

    if order == "q":
        break

    if order not in menu:
        print("메뉴에 없는 음료입니다.")
        continue

    try:
        quantity = int(input("수량을 입력하세요: "))

        if quantity <= 0:
            print("수량은 1개 이상 입력해주세요.")
            continue

        price = calculate_price(order, quantity)
        total_price += price

        print(f"{order} {quantity}개를 주문했습니다.")
        print(f"금액: {price:,}원")
        print(f"현재 총 금액: {total_price:,}원")

    except ValueError:
        print("수량은 숫자로 입력해주세요.")


print("\n--- 주문 완료 ---")
print(f"총 결제 금액은 {total_price:,}원입니다.")
