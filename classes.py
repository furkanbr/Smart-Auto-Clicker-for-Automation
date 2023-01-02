import time
import pyautogui
import pygetwindow
import math

# import main

is_windows = False

if is_windows:
    import pydirectinput
    pygui = pydirectinput
else:
    pygui = pyautogui

previous_data_name = "jhg"
order_list = []


# Security Functions
def get_windows():
    return pygetwindow.getAllTitles()


def compare_with_previous():
    return True
    # global previous_data_name
    # active_window_names = pygetwindow.getAllTitles()
    # for window in active_window_names:
    #     if window.find("Data Access Choices"):
    #         print(window.split("-"))
    #         if window.split("-")[1] == previous_data_name:
    #             return False
    #         else:
    #             previous_data_name = window.split("-")[1]
    #             return True


def check_window_name(window_name):
    active_window_names = pygetwindow.getAllTitles()
    for window in active_window_names:
        try:
            if window.find(window_name):
                return True
        except SyntaxError:
            print("Syntax Error")
            pass
    print("Window name:", window_name , "Liste:", active_window_names)
    return False


class ButtonClick:
    def __init__(self, index, **kwargs):
        self.order_number = index
        self.image = kwargs.get("path")
        self.sleep_time = kwargs.get("sleep_time", 0.5)
        self.orderName = kwargs.get("orderName")
        self.move_away = kwargs.get("move_away", True)
        self.wait_until = kwargs.get("wait_until", True)
        self.interval = kwargs.get("interval", 0.5)
        self.time_limit = kwargs.get("time_limit", 30)
        self.is_time_limited = kwargs.get("is_time_limited", False)
        self.security_function = kwargs.get("security_function", check_window_name)
        self.window_name = kwargs.get("window_name", "")
        self.security_try_count = 0
        self.is_region = kwargs.get("is_region", False)
        self.region_area = kwargs.get("region_area") # 4-integer tuple of (left, top, width, height)
        self.is_located = kwargs.get("is_located", False)
        self.defined_location = kwargs.get("defined_location", ())

    def work(self):
        time.sleep(self.sleep_time)
        pixel_ratio = pyautogui.screenshot().size[0] / pyautogui.size().width
        coordinates = pyautogui.locateCenterOnScreen(self.image, region=(None if self.is_region else self.region_area))
        # Waiting condition
        start_time = time.time()

        # Security Check
        if self.security_function == check_window_name:
            while self.security_try_count < 5:
                if check_window_name(self.window_name):
                    break
                else:
                    self.security_try_count += 1
                    time.sleep(3)
        elif self.security_function == compare_with_previous:
            while self.security_try_count < 5:
                if compare_with_previous():
                    break
                else:
                    self.security_try_count += 1
                    time.sleep(3)
        if self.security_try_count == 5:
            pyautogui.hotkey("alt", "f4", interval=0.3)
            order_list[self.order_number - 1].work()
            self.security_try_count = 0

        while (time.time() - start_time < self.time_limit or not self.is_time_limited) and self.wait_until:
            if coordinates is not None:
                break
            else:
                time.sleep(self.interval)
                coordinates = pyautogui.locateCenterOnScreen(self.image, region=(None if self.is_region else self.region_area))

        if not self.is_located:
            try:
                pygui.moveTo(int(math.trunc(coordinates.x / pixel_ratio)), int(math.trunc(coordinates.y / pixel_ratio)))
                time.sleep(self.interval)
                pygui.click()
            except AttributeError as e:
                print(e)
                print("Could not find button, will try again after 15 seconds.")
                time.sleep(15)
                pygui.moveTo(int(math.trunc(coordinates.x / pixel_ratio)), int(math.trunc(coordinates.y / pixel_ratio)))
                time.sleep(1)
                pygui.click()
        else:
            pygui.moveTo(*self.defined_location)
            time.sleep(self.interval)
            pygui.click()

        if self.move_away:
            pygui.moveTo(0, pyautogui.size().height / 2)


class ButtonDoubleClick:
    def __init__(self, index, **kwargs):
        self.order_number = index
        self.image = kwargs.get("path")
        self.sleep_time = kwargs.get("sleep_time", 0.5)
        self.orderName = kwargs.get("orderName")
        self.move_away = kwargs.get("move_away", True)
        self.wait_until = kwargs.get("wait_until", True)
        self.interval = kwargs.get("interval", 0.5)
        self.time_limit = kwargs.get("time_limit", 30)
        self.is_time_limited = kwargs.get("is_time_limited", False)
        self.security_function = kwargs.get("security_function", check_window_name)
        self.window_name = kwargs.get("window_name", "")
        self.security_try_count = 0
        self.is_region = kwargs.get("is_region", False)
        self.region_area = kwargs.get("region_area") # 4-integer tuple of (left, top, width, height)
        self.is_located = kwargs.get("is_located", False)
        self.defined_location = kwargs.get("defined_location")

    def work(self):
        time.sleep(self.sleep_time)
        pixel_ratio = pyautogui.screenshot().size[0] / pyautogui.size().width
        coordinates = pyautogui.locateCenterOnScreen(self.image, region=(None if self.is_region else self.region_area))
        # Waiting condition
        start_time = time.time()
        # Security Check
        if self.security_function == check_window_name:
            while self.security_try_count < 5:
                if check_window_name(self.window_name):
                    break
                else:
                    self.security_try_count += 1
                    time.sleep(3)
        elif self.security_function == compare_with_previous:
            while self.security_try_count < 5:
                if compare_with_previous():
                    break
                else:
                    self.security_try_count += 1
                    time.sleep(3)

        if self.security_try_count == 5:
            pyautogui.hotkey("alt", "f4", interval=0.3)
            order_list[self.order_number - 1].work()
            self.security_try_count = 0

        while (time.time() - start_time < self.time_limit or not self.is_time_limited) and self.wait_until:
            if coordinates is not None:
                break
            else:
                time.sleep(self.interval)
                coordinates = pyautogui.locateCenterOnScreen(self.image, region=(None if self.is_region else self.region_area))

        if not self.is_located:
            try:
                pygui.moveTo(int(math.trunc(coordinates.x / pixel_ratio)), int(math.trunc(coordinates.y / pixel_ratio)))
                time.sleep(self.interval)
                pygui.doubleClick()
            except AttributeError as e:
                print(e)
                print("Could not find button, will try again after 15 seconds.")
                time.sleep(15)
                pygui.moveTo(int(math.trunc(coordinates.x / pixel_ratio)), int(math.trunc(coordinates.y / pixel_ratio)))
                time.sleep(self.interval)
                pygui.doubleClick()
        else:
            pygui.moveTo(*self.defined_location)
            time.sleep(self.interval)
            pygui.doubleClick()

        if self.move_away:
            pygui.moveTo(0, pyautogui.size().height / 2)


class ButtonClickRelative:
    def __init__(self, index, **kwargs):
        self.order_number = index
        self.image = kwargs.get("path")
        self.sleep_time = kwargs.get("sleep_time", 0.5)
        self.orderName = kwargs.get("orderName")
        self.move_away = kwargs.get("move_away", True)
        self.wait_until = kwargs.get("wait_until", False)
        self.interval = kwargs.get("interval", 0.5)
        self.time_limit = kwargs.get("time_limit", 30)
        self.is_time_limited = kwargs.get("is_time_limited", False)
        self.security_function = kwargs.get("security_function", check_window_name)
        self.window_name = kwargs.get("window_name", "")
        self.security_try_count = 0
        self.mouse_move_x = kwargs.get("mouse_move_x")  # Increase while going right
        self.mouse_move_y = kwargs.get("mouse_move_y")  # Increase while going down
        self.is_located = kwargs.get("is_located", False)
        self.defined_location = kwargs.get("defined_location")

    def work(self):
        time.sleep(self.sleep_time)
        coordinates = pyautogui.locateCenterOnScreen(self.image)
        # Waiting condition
        start_time = time.time()

        # Security Check
        if self.security_function == check_window_name:
            while self.security_try_count < 5:
                if check_window_name(self.window_name):
                    break
                else:
                    self.security_try_count += 1
                    time.sleep(3)
        elif self.security_function == compare_with_previous:
            while self.security_try_count < 5:
                if compare_with_previous():
                    break
                else:
                    self.security_try_count += 1
                    time.sleep(3)

        if self.security_try_count == 5:
            order_list[self.order_number - 1].work()
            self.security_try_count = 0

        while (time.time() - start_time < self.time_limit or not self.is_time_limited) and self.wait_until:
            if coordinates is not None:
                break
            else:
                time.sleep(self.interval)
                coordinates = pyautogui.locateCenterOnScreen(self.image)

        if not self.is_located:
            try:
                pygui.move(self.mouse_move_x, self.mouse_move_y)
                time.sleep(self.interval)
                pygui.click()
            except AttributeError as e:
                print(e)
                print("Could not find button, will try again after 15 seconds.")
                time.sleep(15)
                pygui.move(self.mouse_move_x, self.mouse_move_y)
                time.sleep(self.interval)
                pygui.click()
        else:
            pygui.moveTo(*self.defined_location)
            time.sleep(self.interval)
            pygui.doubleClick()

        if self.move_away:
            pygui.moveTo(0, pyautogui.size().height / 2)


class KeyPress:
    def __init__(self, index, **kwargs):
        self.order_number = index
        self.key = kwargs.get("key")
        self.sleep_time = kwargs.get("sleep_time", 0.2)
        self.orderName = kwargs.get("orderName")
        self.security_function = kwargs.get("security_function", check_window_name)
        self.window_name = kwargs.get("window_name", "")
        self.security_try_count = 0

    def work(self):
        time.sleep(self.sleep_time)
        # pyautogui.press(self.key)
        # Security Check
        if self.security_function == check_window_name:
            while self.security_try_count < 5:
                if check_window_name(self.window_name):
                    break
                else:
                    self.security_try_count += 1
                    time.sleep(3)
        elif self.security_function == compare_with_previous:
            while self.security_try_count < 5:
                if compare_with_previous():
                    break
                else:
                    self.security_try_count += 1
                    time.sleep(3)

        if self.security_try_count == 5:
            pyautogui.hotkey("alt", "f4", interval=0.3)
            order_list[self.order_number - 1].work()
            self.security_try_count = 0

        pygui.keyDown(self.key)
        time.sleep(0.5)
        pygui.keyUp(self.key)


class HotKeyPress:
    def __init__(self, index, **kwargs):
        self.order_number = index
        self.key1 = kwargs.get("key1")
        self.key2 = kwargs.get("key2")
        self.interval = kwargs.get("interval", 0.5)
        self.sleep_time = kwargs.get("sleep_time", 0.2)
        self.orderName = kwargs.get("orderName")
        self.security_function = kwargs.get("security_function", check_window_name)
        self.window_name = kwargs.get("window_name", "")
        self.security_try_count = 0

    def work(self):
        time.sleep(self.sleep_time)

        # Security Check
        if self.security_function == check_window_name:
            while self.security_try_count < 5:
                if check_window_name(self.window_name):
                    break
                else:
                    self.security_try_count += 1
                    time.sleep(3)
        elif self.security_function == compare_with_previous:
            while self.security_try_count < 5:
                if compare_with_previous():
                    break
                else:
                    self.security_try_count += 1
                    time.sleep(3)

        if self.security_try_count == 5:
            pyautogui.hotkey("alt", "f4", interval=0.3)
            order_list[self.order_number - 1].work()
            self.security_try_count = 0

        pyautogui.hotkey(self.key1, self.key2, interval=self.interval)


class WaitUntilAppear:
    def __init__(self, index, **kwargs):
        self.order_number = index
        self.image = kwargs.get("path")
        self.wait_instead_security_image = kwargs.get("wait_instead_security_image")
        self.is_wait_instead_security = kwargs.get("is_wait_instead_security", False)
        self.interval = kwargs.get("interval", 0.5)
        self.time_limit = kwargs.get("time_limit", 30)
        self.is_time_limited = kwargs.get("is_time_limited", False)
        self.orderName = kwargs.get("orderName")
        self.sleep_time = kwargs.get("sleep_time", 0.5)
        self.is_working = kwargs.get("is_working", True)
        self.is_region = kwargs.get("is_region", False)
        self.region_area = kwargs.get("region_area") # 4-integer tuple of (left, top, width, height)
        self.wait_instead_security_time = kwargs.get("wait_instead_security_time", 10)
        self.go_ahead = kwargs.get("go_ahead", False)

    def work(self):
        if self.go_ahead:
            time.sleep(2)
        elif self.is_wait_instead_security and pyautogui.locateCenterOnScreen(self.wait_instead_security_image, region=(600, 450, 1050, 540)) is not None:
            time.sleep(self.wait_instead_security_time)
        else:
            if not self.is_working:
                return

            time.sleep(self.sleep_time)
            start_time = time.time()

            while time.time() - start_time < self.time_limit or not self.is_time_limited:
                if pyautogui.locateCenterOnScreen(self.image, region=(None if self.is_region else self.region_area)) is not None:
                    break
                else:
                    time.sleep(self.interval)


class WaitUntilGone:
    def __init__(self, **kwargs):
        self.image = kwargs.get("path")
        self.interval = kwargs.get("interval", 0.5)
        self.time_limit = kwargs.get("time_limit", 30)
        self.is_time_limited = kwargs.get("is_time_limited", False)
        self.orderName = kwargs.get("orderName")
        self.sleep_time = kwargs.get("sleep_time", 2)

    def work(self):
        time.sleep(self.sleep_time)
        start_time = time.time()

        while time.time() - start_time < self.time_limit or not self.is_time_limited:
            if pyautogui.locateCenterOnScreen(self.image) is None:
                break
            else:
                time.sleep(self.interval)


