from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

from pdf_to_text_converter import PDFToTextConverter
from gemini import Gemini
from json_manager import JsonManager

manager = JsonManager()
gemini = Gemini()
converter = PDFToTextConverter()
browser_path = manager.get_all()["browser_path"]
email = manager.get_all()["email"]
class_id = manager.get_all()["class_id"]
number = manager.get_all()["number"]
name = manager.get_all()["name"]
url = input("授業感想のフォームのURLを入力: ")
document_path = input("授業資料のパスを入力: ")

try:
    document = converter.pdf_to_text(document_path)

except Exception as e:
    print(f"エラーが発生しました: {e}")
    exit(1)

try:
    thoughts = gemini.thoughts(document)

except Exception as e:
    print(f"エラーが発生しました: {e}")
    exit(2)

options = Options()
options.binary_location = browser_path
driver = webdriver.Chrome(options=options)

try:
    driver.get(url)

    email_field = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div[1]/input')
    class_id_field = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    number_field = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    name_field = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input')
    thoughts_field = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div[2]/textarea')
    # send_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[3]/div[1]/div')

    email_field.send_keys(email)
    class_id_field.send_keys(class_id)
    number_field.send_keys(number)
    name_field.send_keys(name)
    thoughts_field.send_keys(thoughts)
    # send_button.click()

    while (True):
        try:
            driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[3]/div[1]/div')
            time.sleep(1)

        except:
            break

except Exception as e:
    print(f"エラーが発生しました: {e}")
    exit(3)

finally:
    time.sleep(1)
    driver.quit()
    exit(0)
