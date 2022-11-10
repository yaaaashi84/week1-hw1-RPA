import pyautogui
import webbrowser
import pyperclip
import time

# google立ち上げ
pyperclip.copy("平泉 観光")
google = "http://google.com/"
webbrowser.open_new(google)
time.sleep(2)

# "平泉 観光"検索
pyperclip.copy("平泉 観光")
pyautogui.hotkey("enter")  # この文がないとなぜかvで検索されてしまいます。
pyautogui.hotkey("command", "v")
pyautogui.hotkey("enter")
time.sleep(2)

screenshot = pyautogui.screenshot('hiraizumi.png')
screenshot.save('hiraizumi.png')


# # chromeアイコンのクリック
# chrome = pyautogui.locateOnScreen("./chrome.jpeg", confidence=0.3)
# chrome_x, chrome_y = pyautogui.center(chrome)
# print(chrome_x, chrome_y)
# pyautogui.click(chrome_x, chrome_y)
# time.sleep(5)


# # writeの日本語変換関数
# def searchString(a):
#     pyperclip.copy(a)
#     pyautogui.hotkey('command', 'v')


# # 虫眼鏡横にある検索バーのクリック->平泉町観光の検索
# search_point = pyautogui.locateOnScreen("./search.png", confidence=0.3)
# search_x, search_y = pyautogui.center(search_point)
# search_x += 200
# pyautogui.click(search_x, search_y)
# searchString("平泉町 観光")
# pyautogui.press('Enter')
# time.sleep(5)

# # スクリーンショット
# pyautogui.screenshot('hiraizumi_ss.png')
