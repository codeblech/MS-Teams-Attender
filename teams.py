from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from random import choice, uniform
import datetime
from pynput.keyboard import Controller, Key

physics_start = datetime.time(8, 0, 0)# ['0800', '0845']
physics_end = datetime.time(8, 45, 0)

computer_science_start = datetime.time(8, 50, 0) # ['0850', '0935']
computer_science_end = datetime.time(9, 35, 0)

english_start = datetime.time(9, 40, 0) #['0940', '1025']
english_end = datetime.time(10, 25, 0)

chemistry_start = datetime.time(10, 45, 0) #['1045', '1130']
chemistry_end = datetime.time(11, 30, 0)

maths_start = datetime.time(11, 35, 0) #['1135', '1220']
maths_end = datetime.time(12, 20, 0)


email = 'YOUR-EMAIL'
password = 'YOUR-PASSWORD'

driver = webdriver.Chrome('C:\\webdrivers\\chromedriver.exe')
driver.get("https://teams.microsoft.com")

driver.maximize_window()


def wait(extra=0):
    delay = uniform(3, 7)
    sleep(delay+extra)


def time_difference(t1, t2):
    t1_hour, t1_min, t1_sec = str(t1).split(':')
    t2_hour, t2_min, t2_sec = str(t2).split(':')
    hours = (int(t1_hour) - int(t2_hour))
    mins = (int(t1_min) - int(t2_min))
    secs = (int(t1_sec) - int(t2_sec))
    difference = hours * 3600 + mins * 60 + secs
    return difference


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
    try:
        wait()
        dismiss_notification_button = driver.find_element_by_xpath('//*[@id="toast-container"]/div/div/div[2]/div/button[2]')
        print('Clicking "Dismiss" for Notificaitons...')
        dismiss_notification_button.click()
        print('Clicked "Dismiss" for Notificaitons.')
        wait()
        driver.implicitly_wait(4)
    except:
        print('Yay! It didn\'t ask to allow for notificaitons.')
    finally:
        wait(7)


def change_tab_to_calendar():
    calendar = driver.find_element_by_xpath('//*[@id="app-bar-ef56c0de-36fc-4ef8-b417-3d82ba9d073c"]')
    calendar.click()
    print('Changed tab to Calendar.')

    wait(8)
    driver.implicitly_wait(4)


def click_view_button():
    wait(10)
    view_button = driver.find_element_by_xpath('//*[@id="page-content-wrapper"]/div[1]/div/div/calendar-bridge/div/div[2]/div/div/div/div/div[2]/div[2]')
    print('Clicking View Button...')
    view_button.click()
    print('Clicked View Button...')
    wait(2)
    driver.implicitly_wait(3)


def change_view_to_day():
    day_view = driver.find_element_by_xpath('//*[@id="id__16-menu"]/div/ul/li[1]/button/div/i')
    day_view.click()
    print('Changed view to Day.')
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

    elif physics_start < current_time < physics_end:
        physics = driver.find_element_by_xpath('//*[@id="page-content-wrapper"]/div[1]/div/div/calendar-bridge/div/div[4]/div[2]/div/div/div[1]/div/div[3]/div/div[3]/div[1]')
        physics.click()
        print('Clicked on Physics meeting.')

    elif computer_science_start < current_time < computer_science_end:
        computer_science = driver.find_element_by_xpath('//*[@id="page-content-wrapper"]/div[1]/div/div/calendar-bridge/div/div[4]/div[2]/div/div/div[1]/div/div[3]/div/div[3]/div[3]')
        computer_science.click()
        print('Clicked on CS meeting.')

    elif english_start < current_time < english_end:
        english = driver.find_element_by_xpath('//*[@id="page-content-wrapper"]/div[1]/div/div/calendar-bridge/div/div[4]/div[2]/div/div/div[1]/div/div[3]/div/div[3]/div[4]')
        english.click()
        print('Clicked on English meeting.')

    elif chemistry_start < current_time < chemistry_end:
        chemistry = driver.find_element_by_xpath('//*[@id="page-content-wrapper"]/div[1]/div/div/calendar-bridge/div/div[4]/div[2]/div/div/div[1]/div/div[3]/div/div[3]/div[5]')
        chemistry.click()
        print('Clicked on Chemistry meeting.')

    elif maths_start < current_time < maths_end:
        maths = driver.find_element_by_xpath('//*[@id="page-content-wrapper"]/div[1]/div/div/calendar-bridge/div/div[4]/div[2]/div/div/div[1]/div/div[3]/div/div[3]/div[6]')
        maths.click()
        print('Clicked on Maths meeting.')


def join_meeting():
    join_button = driver.find_element_by_xpath('//*[@id="page-content-wrapper"]/div[1]/div/div/calendar-dialog-bridge/div/div[1]/div[2]/button[1]')
    print('Clicking Join Button...')
    join_button.click()
    print('Clicked Join Button...')
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


def turn_off_video():
    wait(3)
    video_button = driver.find_element_by_xpath('//*[@id="page-content-wrapper"]/div[1]/div/calling-pre-join-screen/div/div/div[2]/div[1]/div[2]/div/div/section/div[2]/toggle-button[1]/div/button/span[1]')
    print('Turning off Video...')
    state = video_button.get_attribute('title')
    if state == 'Turn camera off':
        video_button.click()
        print('Turned off Video...')
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
        wait()
        driver.implicitly_wait(2)


def finally_join():
    join_button = driver.find_element_by_xpath('//*[@id="page-content-wrapper"]/div[1]/div/calling-pre-join-screen/div/div/div[2]/div[1]/div[2]/div/div/section/div[1]/div/div/button')
    print('Make way for me, I am entering the meeting...!')
    join_button.click()
    print('Entered meeting.')
    wait(3)
    driver.implicitly_wait(2)


def message():
    driver.implicitly_wait(20)
    message_options_network = ['Sir, net nahi chal raha.', 'Sir, network issue ho raha hai', 'sir net slow chal raha hai']
    message_options_attendence = ['Sir, I am present.', 'sir i am present', 'present', 'sir net slow chal raha hai', 'Sir, meri attendence laga dijiye.']

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

        reply_box.send_keys(choice(message_options_attendence)) 
        send_button.click()
        print('Sent attendence message.')

        # driver.implicitly_wait(5)
        
        # reply_box.send_keys(choice(message_options_network))
        # send_button.click()
        # print('Sent network message.')
    except:
        print('Administrator has disabled chat.')


def close_chat_box_button():
    try:
        close_chat_box_button = driver.find_element_by_xpath('//*[@id="page-content-wrapper"]/div[1]/div/calling-screen/div/div[2]/meeting-panel-components/calling-chat/div/right-pane-header/div/div/button/svg-include/svg')
    except:
        print('Couldn\'t find "Close Chat Box" Button.')
    else:
        close_chat_box_button.click()
    driver.implicitly_wait(3)


def time_to_wait_till_class_ends(current_time, physics_end, computer_science_end, english_end, chemistry_end, maths_end):
    if current_time < physics_end:
        time_to_wait = time_difference(physics_end, current_time)
    elif current_time < computer_science_end:
        time_to_wait = time_difference(computer_science_end, current_time)
    elif current_time < english_end:
        time_to_wait = time_difference(english_end, current_time)
    elif current_time < chemistry_end:
        time_to_wait = time_difference(chemistry_end, current_time)
    elif current_time < maths_end:
        time_to_wait = time_difference(maths_end, current_time)
    time_to_wait = 10
    print('"Time to stay" calculated.', time_to_wait)
    print('Waiting till Meeting ends.')
    return time_to_wait


def rejoin_if_removed():
    current_time = time_to_seconds(datetime.datetime.now().time().replace(microsecond=0))
    current_time_when_started_checking = time_to_seconds(datetime.datetime.now().time().replace(microsecond=0))
    time_to_wait = time_to_wait_till_class_ends(current_time, physics_end, computer_science_end, english_end, chemistry_end, maths_end)
    
    while current_time < time_to_seconds(current_time_when_started_checking) + (time_to_seconds(time_to_wait) - 5 * 60):
        try:
            rejoin_button = driver.find_element_by_xpath('//*[@id="pagAontent-wrapper"]/div[1]/div/calling-screen/div/div[2]/div[2]/div[2]/div/calling-retry-screen/div/div[3]/button[1]')
        except:
            print('Nobody removed us!')
        else:
            rejoin_button.click()
            print('Clicked "Rejoin" Button.')
        current_time = time_to_seconds(datetime.datetime.now().time().replace(microsecond=0))
        wait(5*60)


def hangup():
    keyboard = Controller()
    keyboard.press('a')
    keyboard.release('a')
    hangup_button = driver.find_element_by_xpath('//*[@id="hangup-button"]')
    print('Leaving meeting...')
    hangup_button.click()
    wait(3)


def main():
    now = datetime.time(11, 40, 0) # datetime.datetime.now().time().replace(microsecond=0)
    while now < maths_end:        
        now = datetime.time(11, 40, 0) #datetime.datetime.now().time().replace(microsecond=0)
        print('Current Time:', now)
        choose_meeting(now)

        join_meeting()

        allow_access()

        turn_off_audio()

        turn_off_video()

        finally_join()

        message()

        close_chat_box_button()
        
        # rejoin_if_removed()

        hangup()

        change_tab_to_calendar()


reach_teams()
change_tab_to_calendar()
click_view_button()
change_view_to_day()
main()
# driver.quit()
