from modules.add import add_todo
from modules.view import view_todo
from modules.complete import complete_todo
from modules.delete import delete_todo
def show_menu():
    print("\n할 일 목록 프로그램")
    print("1. 할 일 추가")
    print("2. 할 일 보기")
    print("3. 할 일 완료")
    print("4. 할 일 삭제")
    print("5. 종료")
    return input("메뉴를 선택하세요: ")
while True:
    choice = show_menu()
    
    if choice == '1':
        add_todo()
    elif choice == '2':
        view_todo()
    elif choice == '3':
        complete_todo()
    elif choice == '4':
        delete_todo()
    elif choice == '5':
        print("프로그램을 종료합니다.")
        break
    else:
        print("잘못된 메뉴입니다.")