todo_list = []
def add_todo():
    todo = input("할 일을 입력하세요: ")
    todo_list.append({"task": todo, "completed": False})
    print("할 일이 추가되었습니다.")