from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from random import choice, uniform
import datetime
from pynput.keyboard import Controller, Key
from typing import List
from itertools import zip_longest

# If the Time Table changes, only the "start and end timings" and "choose_meeting" function have to be changed.
# In "choose_meeting" function, the first 5 conditional statements have to modified according to the new order of meetings,
# along with the new wait time. The new wait time will be affected by the order of meetings
# In the try-except blocks, only the wait times in except blocks will need to be changed, according to the new
# order of meetings 

first_start = datetime.time(8, 0, 0)  # ['0800', '0845']
first_end = datetime.time(8, 45, 0)

second_start = datetime.time(8, 50, 0)  # ['0850', '0935']
second_end = datetime.time(9, 35, 0)

third_start = datetime.time(9, 40, 0)  # ['0940', '1025']
third_end = datetime.time(10, 25, 0)

fourth_start = datetime.time(10, 45, 0)  # ['1045', '1130']
fourth_end = datetime.time(11, 30, 0)

fifth_start = datetime.time(11, 35, 0)  # ['1135', '1220']
fifth_end = datetime.time(12, 20, 0)

email = 'YOUR-EMAIL'
password = 'YOUR-PASSWORD'

driver = webdriver.Chrome('C:\\webdrivers\\chromedriver.exe')
driver.get("https://teams.microsoft.com")

driver.maximize_window()


def wait(extra=0):
    delay = uniform(6, 10)
    sleep(delay + extra)


def time_string_list_generator(*times):   # creates a List[str] from given time values
    time_strings = []
    for time in times:
        time_str = time.strftime('%H:%M')
        time_str = time_str.lstrip('0')
        time_strings.append(time_str)
    return time_strings


def time_to_seconds(time):
    hours, minutes, seconds = str(time).split(':')
    time_in_seconds = int(hours) * 3600 + int(minutes) * 60 + int(seconds)
    return time_in_seconds


def time_difference(t1, t2):
    t1_hour, t1_min, t1_sec = str(t1).split(':')
    t2_hour, t2_min, t2_sec = str(t2).split(':')
    hours = (int(t1_hour) - int(t2_hour))
    mins = (int(t1_min) - int(t2_min))
    secs = (int(t1_sec) - int(t2_sec))
    difference = hours * 3600 + mins * 60 + secs
    return difference


def find_and_click_element_by_tag_name_and_attribute_value(tag_name, attribute_name, attribute_value):
    all_tags_by_given_tag_name = driver.find_elements_by_tag_name(tag_name)
    print(f'Found {tag_name} tags.')
    for tag in all_tags_by_given_tag_name:
        if tag.get_attribute(attribute_name) == attribute_value:
            print(f'Found {tag_name} tag with {attribute_name}= "{attribute_value}"')
            tag.click()
            print(f'Clicked {tag_name} tag with {attribute_name} = "{attribute_value}".')
            break


def find_and_click_element_by_tag_name_and_attribute_values(tag_name, attribute_name, attribute_values):
    all_tags_by_given_tag_name = driver.find_elements_by_tag_name(tag_name)
    print(f'Found {tag_name} tags.')
    for tag in all_tags_by_given_tag_name:
        for attribute_value in attribute_values:
            if attribute_value in tag.get_attribute(attribute_name):
                print(f'Found {tag_name} tag with "{attribute_value}" in {attribute_name} attribute.')
                tag.click()
                print(f'Clicked {tag_name} tag with "{attribute_value}" in {attribute_name} attribute.')
                break


def find_and_click_element_by_tag_name_and_text(tag_name, required_text_list: List[str],
                                                irrelevant_text_list: List[str] = []):
    all_tags_by_given_tag_name = driver.find_elements_by_tag_name('tag_name')
    print(f'Looking for {required_text_list} in {tag_name} tags.')
    for tag in all_tags_by_given_tag_name:
        for required_text, irrelevant_text in zip_longest(required_text_list, irrelevant_text_list, fillvalue='?'):
            if (required_text in tag.text) and (irrelevant_text not in tag.text):
                print(
                    f'Found {tag_name} tag with text: {required_text_list} and doesn\'t contain {irrelevant_text_list}.')
                tag.click()     
                print(
                    f'Clicked {tag_name} tag with text: {required_text_list} and doesn\'t contain {irrelevant_text_list}.')
                break




def dismiss_notification():
    try:
        wait()
        dismiss_notification_button = driver.find_element_by_xpath(
            '//*[@id="toast-container"]/div/div/div[2]/div/button[2]')
        print('Clicking "Dismiss" for Notifications...')
        dismiss_notification_button.click()
        print('Clicked "Dismiss" for Notifications.')
        wait()
        driver.implicitly_wait(4)
    except NoSuchElementException:
        print('Yay! It didn\'t ask to allow for notifications.')
    finally:
        wait(7)


def reach_teams():
    email_box = driver.find_element_by_xpath('//*[@id="i0116"]')
    print('Entering Email ID...')
    email_box.send_keys(email)
    print('Entered Email ID.')

    wait()
    driver.implicitly_wait(4)

    next_button = driver.find_element_by_xpath('//*[@id="idSIButton9"]')
    next_button.click()
    print('Clicked Next Button.')

    wait()
    driver.implicitly_wait(4)

    password_box = driver.find_element_by_xpath('//*[@id="i0118"]')
    print('Entering Password...')
    password_box.send_keys(password)
    print('Entered Password.')
    wait()

    driver.implicitly_wait(4)

    sign_in_button = driver.find_element_by_xpath('//*[@id="idSIButton9"]')
    print('Clicking Sign In Button...')
    sign_in_button.click()
    print('Clicked Sign In Button.')

    wait()
    driver.implicitly_wait(4)

    no_button = driver.find_element_by_xpath('//*[@id="idBtn_Back"]')
    print('Clicking No Button...')
    no_button.click()
    print('Clicked No Button.')

    wait()
    driver.implicitly_wait(4)

    use_web_app = driver.find_element_by_xpath('//*[@id="download-desktop-page"]/div/a')
    print('Clicking "Use WebApp"...')
    use_web_app.click()
    print('Clicked "Use WebApp".')

    wait()
    driver.implicitly_wait(4)

    dismiss_notification()


def change_tab_to_calendar():
    # try:
    calendar = driver.find_element_by_xpath('//*[@id="app-bar-ef56c0de-36fc-4ef8-b417-3d82ba9d073c"]')
    calendar.click()
    # except NoSuchElementException:
    #     find_and_click_element_by_tag_name_and_attribute_value('button', 'aria-label', 'Calendar Toolbar')
    # finally:
    #     print('Changed tab to Calendar.')
    wait(8)
    driver.implicitly_wait(4)


def click_view_button():
    wait(10)
    # try:
    view_button = driver.find_element_by_xpath(
        '//*[@id="page-content-wrapper"]/div[1]/div/div/calendar-bridge/div/div[2]/div/div/div/div/div[2]/div[2]')
    view_button.click()
    print('Clicked View Button...')
    # except NoSuchElementException:
    #     find_and_click_element_by_tag_name_and_attribute_value('button', 'title', 'Switch your calendar view')
    # finally:
    wait(2)
    driver.implicitly_wait(3)


def change_view_to_day():
    # try:
    day_view_button = driver.find_element_by_xpath('//*[@id="id__16-menu"]/div/ul/li[1]/button/div/i')
    day_view_button.click()
    print('Changed view to Day.')
    # except NoSuchElementException:
    #     find_and_click_element_by_tag_name_and_attribute_value('button', 'aria-label', 'Day view')
    #     print('Changed view to Day.')
    # finally:
    wait()
    driver.implicitly_wait(4)


def choose_meeting(current_time):
    if current_time < first_start:
        print('Waiting for first Meeting to start.')
        wait(time_difference(first_start, current_time))

    elif first_end < current_time < second_start:
        print('Waiting for second Meeting to start.')
        wait(time_difference(second_start, current_time))

    elif second_end < current_time < third_start:
        print('Waiting for third Meeting to start.')
        wait(time_difference(third_start, current_time))

    elif third_end < current_time < fourth_start:
        print('Waiting for fourth Meeting to start.')
        wait(time_difference(fourth_start, current_time))

    elif fourth_end < current_time < fifth_start:
        print('Waiting for fifth Meeting to start.')
        wait(time_difference(fifth_start, current_time))

    # Each of the following try-except blocks searches for <span> tags
    # IF FOUND: it searches for the 'text' inside the <span> tag corresponding to the class
    # currently running(according to current time). THen it clicks on the tag.
    # IF NOT FOUND: it waits for the next class to start.

    try:
        if first_start <= current_time <= first_end:
            time_strings = time_string_list_generator(first_start, first_start)
            find_and_click_element_by_tag_name_and_attribute_values('div', 'title', time_string)

    except NameError:
        print('first class isn\'t in calendar.')
        wait(time_difference(second_start, current_time))

    try:
        if second_start <= current_time <= second_end:
            time_strings = time_string_list_generator(second_start, second_start)
            find_and_click_element_by_tag_name_and_attribute_values('div', 'title', time_string)
            return
    except NameError:
        print('second class isn\'t in calendar.')
        wait(time_difference(third_start, current_time))

    try:
        if third_start <= current_time <= third_end:
            time_strings = time_string_list_generator(third_start, third_start)
            find_and_click_element_by_tag_name_and_attribute_values('div', 'title', time_string)
    except NameError:
        print('third class isn\'t in calendar.')
        wait(time_difference(fourth_start, current_time))

    try:
        if fourth_start <= current_time <= fourth_end:
            time_strings = time_string_list_generator(fourth_start, fourth_start)
            find_and_click_element_by_tag_name_and_attribute_values('div', 'title', time_string)
            return
    except NameError:
        print('fourth class isn\'t in calendar.')
        wait(time_difference(fifth_start, current_time))

    try:
        if fifth_start <= current_time <= fifth_end:
            time_strings = time_string_list_generator(fifth_start, fifth_start)
            find_and_click_element_by_tag_name_and_attribute_values('div', 'title', time_string)
            return
    except NameError:
        print('fifth class isn\'t in calendar.')


def join_meeting():
    # try:
    # join_button = driver.find_element_by_xpath(
    #     '//*[@id="page-content-wrapper"]/div[1]/div/div/calendar-dialog-bridge/div/div[1]/div[2]/butto
    #     n[1]')
    # join_button.click()
    # print('Clicked Join Button...xpath')
    # except NoSuchElementException:
    find_and_click_element_by_tag_name_and_attribute_value('button', 'aria-label', 'Join meeting')
    # finally:
    #     wait()
    #     driver.implicitly_wait(4)


def allow_access():
    keyboard = Controller()
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    keyboard.press(Key.enter)
    wait()
    driver.implicitly_wait(2)


def turn_off_video():
    wait(3)
    video_button = driver.find_element_by_xpath(
        '//*[@id="page-content-wrapper"]/div[1]/div/calling-pre-join-screen/div/div/div[2]/div[1]/div[2]/div/div/section/div[2]/toggle-button[1]/div/button/span[1]')
    print('Turning off Video...')
    state = video_button.get_attribute('title')
    if state == 'Turn camera off':
        video_button.click()
        print('Turned off Video...')
    else:
        print('Audio is already off.')
    wait()
    driver.implicitly_wait(2)


def turn_off_audio():
    wait(3)
    audio_button = driver.find_element_by_xpath('//*[@id="preJoinAudioButton"]/div/button/span[1]')
    print('Turning off Audio...')
    state = audio_button.get_attribute('title')
    if state == 'Mute microphone':
        audio_button.click()
        print('Turned off Audio...')
    else:
        print('Audio is already off.')
    wait()
    driver.implicitly_wait(2)


def finally_join():
    join_button = driver.find_element_by_xpath(
        '//*[@id="page-content-wrapper"]/div[1]/div/calling-pre-join-screen/div/div/div[2]/div[1]/div[2]/div/div/section/div[1]/div/div/button')
    print('Make way for me, I am entering the meeting...!')
    join_button.click()
    print('Entered meeting.')
    wait(3)
    driver.implicitly_wait(2)


def message():
    driver.implicitly_wait(20)
    # message_options_network = ['Sir, net nahi chal raha.', 'Sir, network issue ho raha hai',
    #                            'sir net slow chal raha hai']
    message_options_attendance = ['Sir, I am present.', 'sir i am present',
                                  'present']  # , 'sir net slow chal raha hai', 'Sir, meri attendence laga dijiye.']

    keyboard = Controller()
    try:
        keyboard.press('a')
        keyboard.release('a')
        message_button = driver.find_element_by_xpath('//*[@id="chat-button"]')
        message_button.click()
        print('Message button clicked.')
        wait()

        reply_box = driver.find_element_by_xpath('//*[@id="cke_29_contents"]/div')
        print('Reply box found.')
        send_button = driver.find_element_by_xpath('//*[@id="send-message-button"]')
        print('Send Button found.')

        reply_box.send_keys(choice(message_options_attendance))
        send_button.click()
        print('Sent attendence message.')

        # driver.implicitly_wait(5)

        # reply_box.send_keys(choice(message_options_network))
        # send_button.click()
        # print('Sent network message.')
        close_chat_box_button()
    except NoSuchElementException:
        print('Administrator has disabled chat.')


def close_chat_box_button():
    try:
        close_button = driver.find_element_by_xpath(
            '//*[@id="page-content-wrapper"]/div[1]/div/calling-screen/div/div[2]/meeting-panel-components/calling-chat/div/right-pane-header/div/div/button/svg-include/svg')
    except NoSuchElementException:
        print("Couldn't find \"Close Chat Box\" Button.")
    else:
        close_button.click()
    driver.implicitly_wait(3)


def time_to_wait_till_class_ends(current_time, first_end_time, second_end_time, third_end_time,
                                 fourth_end_time,
                                 fifth_end_time):
    if current_time < first_end_time:
        time_to_wait = time_difference(first_end_time, current_time)
    elif current_time < second_end_time:
        time_to_wait = time_difference(second_end_time, current_time)
    elif current_time < third_end_time:
        time_to_wait = time_difference(third_end_time, current_time)
    elif current_time < fourth_end_time:
        time_to_wait = time_difference(fourth_end_time, current_time)
    elif current_time < fifth_end_time:
        time_to_wait = time_difference(fifth_end_time, current_time)
    print('"Time to stay" calculated.', time_to_wait, '+ 120 seconds')
    print('Waiting till Meeting ends.')
    return time_to_wait + 120


def rejoin_if_removed():
    current_time = datetime.datetime.now().time().replace(microsecond=0)
    current_time_when_started_checking = datetime.datetime.now().time().replace(microsecond=0)
    time_to_wait = time_to_wait_till_class_ends(current_time, first_end, second_end, third_end,
                                                fourth_end, fifth_end)

    while time_to_seconds(current_time) < time_to_seconds(current_time_when_started_checking) + (time_to_wait - 5 * 60):
        try:
            rejoin_button = driver.find_element_by_xpath(
                '//*[@id="pagAontent-wrapper"]/div[1]/div/calling-screen/div/div[2]/div[2]/div[2]/div/calling-retry-screen/div/div[3]/button[1]')
        except NoSuchElementException:
            print('Nobody removed us!')
        else:
            rejoin_button.click()
            print('Clicked "Rejoin" Button.')
        current_time = datetime.datetime.now().time().replace(microsecond=0)
        wait(5 * 60)


def hangup():
    keyboard = Controller()
    keyboard.press('a')
    keyboard.release('a')
    leave = 'Leaving Meeting...'
    try:
        hangup_button = driver.find_element_by_xpath('//*[@id="hangup-button"]')
        hangup_button.click()
        print(leave)
    except NoSuchElementException:
        try:
            hangup_button = driver.find_element_by_xpath('//*[@id="hangup-button"]/ng-include/svg')
            hangup_button.click()
            print(leave)
        except NoSuchElementException:
            try:
                find_and_click_element_by_tag_name_and_attribute_value('button', 'id', 'hangup-button')
                print(leave)
            except NoSuchElementException:
                print('Looks like the meeting has already ended.')
    finally:
        wait(3)


def leave_the_rest_on_this_function():
    now = datetime.datetime.now().time().replace(microsecond=0)  # datetime.time(8 + i, 10, 0)
    while now < fifth_end:
        print('Time before choosing meeting:', now)

        choose_meeting(now)

        dismiss_notification()

        join_meeting()

        allow_access()

        dismiss_notification()

        turn_off_audio()

        turn_off_video()

        dismiss_notification()

        finally_join()

        # message()

        # rejoin_if_removed()
        now = datetime.datetime.now().time().replace(microsecond=0)  # datetime.time(8 + i, 10, 0)
        print('Time before calculating "wait time":', now)
        wait(
            time_to_wait_till_class_ends(now, first_end, second_end, third_end, fourth_end, fifth_end))

        hangup()

        change_tab_to_calendar()
        now = datetime.datetime.now().time().replace(microsecond=0)  # datetime.time(8 + i, 0, 0)


reach_teams()
change_tab_to_calendar()
click_view_button()
change_view_to_day()
leave_the_rest_on_this_function()
print('Done!')
