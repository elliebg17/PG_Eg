import pyautogui as pg

pg.hotkey ('ctrl', 'winleft', 'd')
pg.hotkey ('winleft')
pg.typewrite ('chrome/n', 0.5)
pg.hotkey ('winleft','up')

pg.typewrite('snopes.com/n', 0.5)
time.sleep(4)

pg.hotkey('tab')
time.sleep(.2)
pg.hotkey ('tab')
time.sleep(.4)

