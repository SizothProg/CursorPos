#SizothProg mmoranu@sizoth.ru
import pyautogui
import time
print("Press CTRL-C to quit")



try:
    while True:
     
      x, y = pyautogui.position()
      
      positionStr = 'X:'+ str(x).rjust(4) +'  Y:'+ str(y).rjust(4)
     
      print(positionStr, end = '')
     
      
      print('\b'*len(positionStr), end = '', flush = True)
     
     
      time.sleep(0.01)





except KeyboardInterrupt:
    print('\nDone')
