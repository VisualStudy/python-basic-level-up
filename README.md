# Python Cafe Order Practice

파이썬 기본편을 학습하면서 배운 기본 문법을 활용해 만든 간단한 카페 주문 프로그램입니다.

A simple cafe ordering program created to practice the basic Python concepts covered in the Nado Coding Python Basic Course.

## 프로젝트 소개 | Project

카페 메뉴와 가격을 딕셔너리에 저장하고, 사용자가 메뉴와 수량을 입력하면 주문 금액과 총 금액을 계산합니다.

잘못된 메뉴나 숫자가 아닌 수량을 입력했을 때 처리하는 기능도 간단하게 구현했습니다.

The program stores cafe menu items and prices in a dictionary.
Users can select a drink and quantity, and the program calculates the order price and total payment.

It also handles invalid menu selections and incorrect quantity input.

## 사용한 문법 | Python Concepts

* 변수와 자료형 / Variables and data types
* 딕셔너리 / Dictionary
* 조건문 / Conditional statements
* `for`, `while` 반복문 / Loops
* 함수 / Functions
* 매개변수와 반환값 / Parameters and return values
* 사용자 입력 / User input
* `f-string`
* `try`, `except` 예외처리 / Exception handling

## 실행 방법 | How to Run

Python 3가 설치된 환경에서 다음 명령어로 실행합니다.

Run the program with Python 3:

```bash
python cafe_order.py
```

프로그램을 실행한 후 메뉴 이름과 주문 수량을 입력합니다.

`q`를 입력하면 주문이 종료되고 총 결제 금액이 출력됩니다.

Enter a menu name and quantity after running the program.

Enter `q` to finish the order and display the total payment.

## 실행 예시 | Example

```text
--- 카페 메뉴 ---
아메리카노: 3,000원
카페라떼: 4,000원
바닐라라떼: 4,500원

주문할 메뉴를 입력하세요. (종료: q): 아메리카노
수량을 입력하세요: 2

아메리카노 2개를 주문했습니다.
금액: 6,000원
현재 총 금액: 6,000원
```

## 파일 | File

```text
python-basic-level-up/
├── README.md
└── cafe_order.py
```

이번 실습을 통해 딕셔너리, 반복문, 조건문, 함수와 같은 기본 문법을 하나의 작은 프로그램에서 함께 사용하는 방법을 연습했습니다.

Through this practice, I learned how basic Python concepts such as dictionaries, loops, conditional statements, and functions can be used together in a small program.
