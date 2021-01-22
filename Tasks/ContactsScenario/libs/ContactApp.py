from uiautomator import Device
from uiautomator import device as d
from time import sleep


def open_contact_app():
    try:
        d(className="android.widget.TextView", text='Contacts').click()
    except Exception as e:
        print(e)


def add_contact(name, phone, email):
    try:
        d(descriptionContains="add new contact").click()
        d(className='android.widget.EditText', text='Name').set_text(name)
        sleep(1)
        d.press.enter()
        d(className='android.widget.EditText', text='Phone').set_text(phone)
        sleep(1)
        d.press.back()
        d(className='android.widget.EditText', text='Email').set_text(email)
        sleep(1)
        d.press.enter()
        d(resourceId='com.android.contacts:id/menu_save', descriptionContains='Save').click()
        sleep(2)
        d.press.back()
        search_contact(name)
    except Exception as e:
        print(e)


def search_contact(contact_name):
    try:
        d(className='android.widget.TextView', descriptionContains='Search').click()
        sleep(1)
        contact_exists = d(className='android.widget.EditText', text='Find contacts').set_text(contact_name)
        if contact_exists:
            print("Contact created successfully")
            d.screenshot("contact.png")
        else:
            print("Contact not created")
    except Exception as e:
        print(e)


# open_contact_app()
# add_contact('test', 1234, 'test@gmail')
# search_contact('test')
