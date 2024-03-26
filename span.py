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

physics_start = datetime.time(8, 0, 0)  # ['0800', '0845']
physics_end = datetime.time(8, 45, 0)

computer_science_start = datetime.time(8, 50, 0)  # ['0850', '0935']
computer_science_end = datetime.time(9, 35, 0)

english_start = datetime.time(9, 40, 0)  # ['0940', '1025']
english_end = datetime.time(10, 25, 0)

chemistry_start = datetime.time(10, 45, 0)  # ['1045', '1130']
chemistry_end = datetime.time(11, 30, 0)

maths_start = datetime.time(11, 35, 0)  # ['1135', '1220']
maths_end = datetime.time(12, 20, 0)

email = '1607@renbsr.onmicrosoft.com'
password = 'yash@123'

driver = webdriver.Chrome('C:\\webdrivers\\chromedriver.exe')
driver.get("https://teams.microsoft.com")

driver.maximize_window()


def wait(extra=0):
    delay = uniform(8, 10)
    sleep(delay + extra)


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


def find_and_click_element_by_tag_name_and_text(tag_name, required_text_list: List[str],
                                                irrelevant_text_list: List[str] = []):
    all_tags_by_given_tag_name = driver.find_elements_by_tag_name('tag_name')
    print(f'Looking for {required_text_list} in {tag_name} tags.')
    to_be_clicked_tags = []
    for tag in all_tags_by_given_tag_name:
        for required_text, irrelevant_text in zip_longest(required_text_list, irrelevant_text_list, fillvalue='?'):
            if (required_text in tag.text) and (irrelevant_text not in tag.text):
                print(
                    f'Found {tag_name} tag with text: {required_text_list} and doesn\'t contain {irrelevant_text_list}.')
                to_be_clicked_tags.append(tag)

    for tag in to_be_clicked_tags:
        try:
            tag.click()
            print(f'Clicked {tag_name} tag with text: {required_text_list} and doesn\'t contain {irrelevant_text_list}.')
            break
        except NoSuchElementException:
            continue


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

    use_web_app = driver.find_element_by_xpath(
        '//*[@id="download-desktop-page"]/div/a')
    print('Clicking "Use WebApp"...')
    use_web_app.click()
    print('Clicked "Use WebApp".')

    wait()
    driver.implicitly_wait(4)

    dismiss_notification()


def change_tab_to_calendar():
    # try:
    calendar = driver.find_element_by_xpath(
        '//*[@id="app-bar-ef56c0de-36fc-4ef8-b417-3d82ba9d073c"]')
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
    day_view_button = driver.find_element_by_xpath(
        '//*[@id="id__16-menu"]/div/ul/li[1]/button/div/i')
    day_view_button.click()
    print('Changed view to Day.')
    # except NoSuchElementException:
    #     find_and_click_element_by_tag_name_and_attribute_value('button', 'aria-label', 'Day view')
    #     print('Changed view to Day.')
    # finally:
    wait()
    driver.implicitly_wait(4)


def choose_meeting(current_time):
    if current_time < physics_start:
        print('Waiting for Physics Meeting to start.')
        wait(time_difference(physics_start, current_time))

    elif physics_end < current_time < computer_science_start:
        print('Waiting for CS Meeting to start.')
        wait(time_difference(computer_science_start, current_time))

    elif computer_science_end < current_time < english_start:
        print('Waiting for English Meeting to start.')
        wait(time_difference(english_start, current_time))

    elif english_end < current_time < chemistry_start:
        print('Waiting for Chemistry Meeting to start.')
        wait(time_difference(chemistry_start, current_time))

    elif chemistry_end < current_time < maths_start:
        print('Waiting for Maths Meeting to start.')
        wait(time_difference(maths_start, current_time))

    # Each of the following try-except blocks searches for <span> tags
    # IF FOUND: it searches for the 'text' inside the <span> tag corresponding to the class
    # currently running(according to current time). THen it clicks on the tag.
    # IF NOT FOUND: it waits for the next class to start.

    try:
        if physics_start <= current_time <= physics_end:
            subject = 'physics'
            teacher1 = 'naushad'
            teacher2 = 'ali'
            required_text_list = [subject, subject.upper(), subject.capitalize(), teacher1, teacher1.upper(
            ), teacher1.capitalize(), teacher2, teacher2.upper(), teacher2.capitalize()]

            find_and_click_element_by_tag_name_and_text(
                'span', required_text_list)
            # print('Clicked on Physics meeting.')
            return
    except NameError:
        print('Physics class isn\'t in calendar.')
        wait(time_difference(computer_science_start, current_time))

    try:
        if computer_science_start <= current_time <= computer_science_end:
            subject1 = 'computer science'
            subject2 = 'cs'
            teacher = 'avinash'
            required_text_list = [subject1, subject1.upper(), subject1.capitalize(), subject1.title(), subject2,
                                  subject2.upper(), subject2.capitalize(), subject2.title(), teacher1, teacher1.upper(), teacher1.capitalize()]

            irrelevant_text = 'canceled'
            irrelevant_text_list = [irrelevant_text.capitalize(
            ), irrelevant_text, irrelevant_text.upper()]

            find_and_click_element_by_tag_name_and_text(
                'span', required_text_list, irrelevant_text_list)
            # print('Clicked on CS meeting.')
            return
    except NameError:
        print('CS class isn\'t in calendar.')
        wait(time_difference(english_start, current_time))

    try:
        if english_start <= current_time <= english_end:
            subject = 'english'
            teacher1 = 'pashupati'
            teacher2 = 'nath'
            teacher3 = 'tiwari'
            required_text_list = [subject, subject.upper(), subject.capitalize(), teacher1, teacher1.upper(),
                                  teacher1.capitalize(), teacher2, teacher2.upper(), teacher2.capitalize(), teacher3,
                                  teacher3.upper(), teacher3.capitalize()]

            find_and_click_element_by_tag_name_and_text(
                'span', required_text_list)
            # print('Clicked on English meeting.')
            return
    except NameError:
        print('English class isn\'t in calendar.')
        wait(time_difference(chemistry_start, current_time))

    try:
        if chemistry_start <= current_time <= chemistry_end:
            subject = 'chemistry'
            teacher = 'karan'
            required_text_list = [
                subject, subject.upper(), subject.capitalize(), teacher, teacher.upper(), teacher.capitalize()]

            find_and_click_element_by_tag_name_and_text(
                'span', required_text_list)
            # print('Clicked on Chemistry meeting.')
            return
    except NameError:
        print('Chemistry class isn\'t in calendar.')
        wait(time_difference(maths_start, current_time))

    try:
        if maths_start <= current_time <= maths_end:
            subject1 = 'maths'
            subject2 = 'math'
            subject3 = 'mathematics'
            teacher = 'prabhat'
            required_text_list = [subject1, subject1.upper(), subject1.capitalize(), subject2, subject2.upper(),
                                  subject2.capitalize(), subject3, subject3.upper(), subject3.capitalize(),
                                  teacher, teacher.upper(), teacher.capitalize()]

            find_and_click_element_by_tag_name_and_text(
                'span', required_text_list)
            # print('Clicked on Maths meeting.')
            return
    except NameError:
        print('Maths class isn\'t in calendar.')


def join_meeting():
    try:
        join_button = driver.find_element_by_xpath(
            '//*[@id="page-content-wrapper"]/div[1]/div/div/calendar-dialog-bridge/div/div[1]/div[2]/button[1]')
        join_button.click()
        print('Clicked Join Button...xpath')
    except NoSuchElementException:
        find_and_click_element_by_tag_name_and_attribute_value(
        'button', 'aria-label', 'Join meeting')
    finally:
        wait()
        driver.implicitly_wait(4)


def allow_access():
    keyboard = Controller()
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    keyboard.press(Key.enter)
    wait()
    driver.implicitly_wait(2)


def turn_off_audio():
    wait(3)
    audio_button = driver.find_element_by_xpath(
        '//*[@id="preJoinAudioButton"]/div/button/span[1]')
    print('Turning off Audio...')
    state = audio_button.get_attribute('title')
    if state == 'Mute microphone':
        audio_button.click()
        print('Turned off Audio...')
    else:
        print('Audio is already off.')
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

        reply_box = driver.find_element_by_xpath(
            '//*[@id="cke_29_contents"]/div')
        print('Reply box found.')
        send_button = driver.find_element_by_xpath(
            '//*[@id="send-message-button"]')
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


def time_to_wait_till_class_ends(current_time, physics_end_time, computer_science_end_time, english_end_time,
                                 chemistry_end_time,
                                 maths_end_time):
    if current_time < physics_end_time:
        time_to_wait = time_difference(physics_end_time, current_time)
    elif current_time < computer_science_end_time:
        time_to_wait = time_difference(computer_science_end_time, current_time)
    elif current_time < english_end_time:
        time_to_wait = time_difference(english_end_time, current_time)
    elif current_time < chemistry_end_time:
        time_to_wait = time_difference(chemistry_end_time, current_time)
    elif current_time < maths_end_time:
        time_to_wait = time_difference(maths_end_time, current_time)
    print('"Time to stay" calculated.', time_to_wait, '+ 120 seconds')
    print('Waiting till Meeting ends.')
    return time_to_wait + 120


def rejoin_if_removed():
    current_time = datetime.datetime.now().time().replace(microsecond=0)
    current_time_when_started_checking = datetime.datetime.now().time().replace(microsecond=0)
    time_to_wait = time_to_wait_till_class_ends(current_time, physics_end, computer_science_end, english_end,
                                                chemistry_end, maths_end)

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
        hangup_button = driver.find_element_by_xpath(
            '//*[@id="hangup-button"]')
        hangup_button.click()
        print(leave)
    except NoSuchElementException:
        try:
            hangup_button = driver.find_element_by_xpath(
                '//*[@id="hangup-button"]/ng-include/svg')
            hangup_button.click()
            print(leave)
        except NoSuchElementException:
            try:
                find_and_click_element_by_tag_name_and_attribute_value(
                    'button', 'id', 'hangup-button')
                print(leave)
            except NoSuchElementException:
                print('Looks like the meeting has already ended.')
    finally:
        wait(3)


def leave_the_rest_on_this_function():
    now = datetime.datetime.now().time().replace(
        microsecond=0)  # datetime.time(8 + i, 10, 0)
    while now < maths_end:
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
        now = datetime.datetime.now().time().replace(
            microsecond=0)  # datetime.time(8 + i, 10, 0)
        print('Time before calculating "wait time":', now)
        wait(
            time_to_wait_till_class_ends(now, physics_end, computer_science_end, english_end, chemistry_end, maths_end))

        hangup()

        change_tab_to_calendar()
        now = datetime.datetime.now().time().replace(
            microsecond=0)  # datetime.time(8 + i, 0, 0)


reach_teams()
change_tab_to_calendar()
click_view_button()
change_view_to_day()
leave_the_rest_on_this_function()
print('Done!')
