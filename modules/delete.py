from modules.add import todo_list
from modules.view import view_todo
def delete_todo():
    view_todo()
    if not todo_list:
        return
    try:
        index = int(input("삭제할 할 일의 번호를 입력하세요: ")) - 1
        if 0 <= index < len(todo_list):
            del todo_list[index]
            print("할 일이 삭제되었습니다.")
        else:
            print("잘못된 번호입니다.")
    except ValueError:
        print("숫자를 입력해주세요.")