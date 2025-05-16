from modules.add import todo_list
def view_todo():
    if not todo_list:
        print("할 일 목록이 비어 있습니다.")
        return
    for index, item in enumerate(todo_list):
        status = "[완료]" if item["completed"] else "[미완료]"
        print(f"{index + 1}. {item['task']} {status}")