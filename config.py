from json_manager import JsonManager

manager = JsonManager()
browser_path = str(input("ブラウザのパスを入力: "))
class_id = str(input("クラスを入力 (例: 1S): "))
number = str(input("出席番号を入力 (例: 01): "))
name = str(input("名前を入力: "))

try:
    manager.write(
        browser_path=browser_path,
        class_id=class_id,
        number=number,
        name=name
    )

except:
    print("設定に失敗しました")
    exit(1)

print("設定に成功しました")
exit(0)
