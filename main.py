import time

import classes
import os

orders = {
    0 : {
        "type" : classes.KeyPress,
        "parameters" : {"key": "enter",
                        "orderName": "Press 'Enter' Key",
                        "security_function": classes.check_window_name,
                        "window_name": "Prior Holter"}
    },
    1 : {
        "type" : classes.ButtonClick,
        "parameters" : {"path": "images/button_1.png",
                        "orderName": "Click 'Report' Button",
                        "security_function": classes.compare_with_previous}
    },
    2 : {
        "type" : classes.ButtonClick,
        "parameters" : {"path": "images/button_2.png",
                        "orderName": "Click 'PDF+DICOM' Button",
                        "security_function": classes.check_window_name,
                        "window_name": "Reports",
                        "is_located": True,
                        "defined_location": (1123, 139)}
    },
    3 : {
        "type" : classes.ButtonDoubleClick,
        "parameters" : {"path": "images/button_3.png",
                        "orderName": "Click 'PDF File' Button",
                        "security_function": classes.check_window_name,
                        "window_name": "PDF+DICOM",
                        "move_away": False}
    },
    4 : {
        "type" : classes.ButtonClickRelative,
        "parameters" : {"path": "images/button_4.png",
                        "orderName": "Click 'Create PDF File' in dropdown menu",
                        "security_function": classes.check_window_name,
                        "window_name": "PDF+DICOM",
                        "move_away": True,
                        "sleep_time": 1,
                        "is_located": True,
                        "defined_location": (713, 531)}
    },
    5 : {
        "type" : classes.WaitUntilAppear,
        "parameters" : {"path": "images/export_button.png",
                        "orderName": "Waiting for PDF File be created",
                        "is_region": True,
                        "region_area": (680, 365, 1359, 767),
                        "is_wait_instead_security": True,
                        "wait_instead_security_image": "images/wait_instead.png"}
    },
    6 : {
        "type" : classes.ButtonDoubleClick,
        "parameters" : {"path": "images/button_3.png",
                        "orderName": "Click 'PDF File' Button",
                        "security_function": classes.check_window_name,
                        "window_name": "PDF+DICOM",
                        "move_away": False}
    },
    7 : {
        "type" : classes.ButtonClickRelative,
        "parameters" : {"path": "images/button_5.png",
                        "orderName": "Click 'Preview' in dropdown menu",
                        "security_function": classes.check_window_name,
                        "window_name": "PDF+DICOM",
                        "move_away": True,
                        "sleep_time": 1,
                        "is_located": True,
                        "defined_location": (705, 555)}
    },
    8 : {
        "type" : classes.ButtonClick,
        "parameters" : {"path": "images/button_6.png",
                        "orderName": "Click 'Download' Icon",
                        "security_function": classes.check_window_name,
                        "window_name": "Google Chrome"}
    },
    9 : {
        "type" : classes.WaitUntilAppear,
        "parameters" : {"path": "images/download_screen.png",
                        "orderName": "Waiting for 'Save As' Screen to appear",
                        "is_region": True,
                        "region_area": (680, 365, 1359, 767),
                        "go_ahead": True}
    },
    10 : {
        "type" : classes.KeyPress,
        "parameters" : {"key": "enter",
                        "orderName": "Press 'Enter' Key",
                        "security_function": classes.check_window_name,
                        "window_name": "Farklı Kaydet"}
    },
    11 : {
        "type" : classes.HotKeyPress,
        "parameters" : {"key1": "altleft",
                        "key2": "f4",
                        "orderName": "Send 'ALT + F4' Key Combination",
                        "security_function": classes.check_window_name,
                        "window_name": "Google Chrome"}
    },
    12 : {
        "type" : classes.HotKeyPress,
        "parameters" : {"key1": "altleft",
                        "key2": "f4",
                        "orderName": "Send 'ALT + F4' Key Combination",
                        "security_function": classes.check_window_name,
                        "window_name": "PDF+DICOM"}
    },
    13 : {
        "type" : classes.HotKeyPress,
        "parameters" : {"key1": "altleft",
                        "key2": "f4",
                        "orderName": "Send 'ALT + F4' Key Combination",
                        "security_function": classes.check_window_name,
                        "window_name": "Reports"}
    },
    14 : {
        "type" : classes.HotKeyPress,
        "parameters" : {"key1": "altleft",
                        "key2": "f4",
                        "orderName": "Send 'ALT + F4' Key Combination",
                        "security_function": classes.check_window_name,
                        "window_name": "Data Access Choices"}
    },
    15 : {
        "type" : classes.KeyPress,
        "parameters" : {"key": "down",
                        "orderName": "Press 'Down' Key",
                        "security_function": classes.check_window_name,
                        "window_name": "Prior Holter"}
    },
}

test_order = {
    0 : {
        "type" : classes.ButtonClick,
        "parameters" : {"path": "images/button_test.png",
                        "move_away": False,
                        "orderName": "Click 'Report' Button"}
    }}

# Get all orders and create list of all order objects.

order_objects = [] # All order objects will be added here as ordered.
order_count = len(orders)
for order_number in range(order_count):
    order = orders[order_number]
    order_type = order["type"]
    order_object = order_type(index=order_number, **order["parameters"])
    order_objects.append(order_object)

# Loop limiter section
loop_counter = 0
is_loop_limited = True
loop_limit = 2
classes.order_list = order_objects

# Witting to before starting loop, this is just for preparation before starting.
time.sleep(5)

while loop_counter < loop_limit or not is_loop_limited:
    print(f"{loop_counter} loops is done so far.")
    for order in order_objects:
        order.work()
        print(f"Order: '{order.orderName}' is done.")
    loop_counter += 1
    os.system('cls' if os.name == 'nt' else 'clear')

print(f"End of the loop. {loop_counter} loops were made at total.")


