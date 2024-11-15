import pyautogui
from python_imagesearch.imagesearch import imagesearch
import time

img_pouch = 'Pouch.png'
img_refresh = 'Refresh.png'
img_accept = 'Accept.png'
pyautogui.FAILSAFE = False
TIMELAPSE = 1
MAX_REFRESH_COUNT = 100
MAX_WAIT_TIME = 30

def run_random_green_contract(output_box):
    refresh_count = 0
    start_time = time.time()

    while True:
        elapsed_time = time.time() - start_time
        if elapsed_time > MAX_WAIT_TIME:
            output_box.insert("end", "Contract not found within 30 seconds. Exiting...\n")
            output_box.see("end")
            break

        output_box.insert("end", "Searching for contract...\n")
        output_box.see("end")
        pos_accept = imagesearch(img_accept, 0.8)

        if pos_accept[0] != -1:
            output_box.insert("end", "Contract found. Searching for pouch...\n")
            output_box.see("end")
            pos_pouch = imagesearch(img_pouch, 0.8)

            if pos_pouch[0] != -1:
                output_box.insert("end", "Pouch found. Confirming contract...\n")
                output_box.see("end")
                pos_accept = imagesearch(img_accept, 0.8)
                if pos_accept[0] != -1:
                    pyautogui.click(pos_accept[0], pos_accept[1])
                    output_box.insert("end", "Pouch contract accepted.\n")
                    output_box.see("end")
                    break
            else:
                if refresh_count < MAX_REFRESH_COUNT:
                    output_box.insert("end", f"Pouch not found. Refreshing... ({refresh_count + 1})\n")
                    output_box.see("end")
                    pos_refresh = imagesearch(img_refresh, 0.9)
                    if pos_refresh[0] != -1:
                        pyautogui.click(pos_refresh[0], pos_refresh[1])
                        refresh_count += 1
                        time.sleep(TIMELAPSE)
                    else:
                        output_box.insert("end", "Refresh button not found. Retrying...\n")
                        output_box.see("end")
                else:
                    output_box.insert("end", "Max refresh attempts reached. Clicking accept...\n")
                    output_box.see("end")
                    pos_accept = imagesearch(img_accept, 0.8)
                    if pos_accept[0] != -1:
                        pyautogui.click(pos_accept[0], pos_accept[1])
                        output_box.insert("end", "Contract accepted without pouch.\n")
                        output_box.see("end")
                    break
        else:
            time.sleep(TIMELAPSE)
