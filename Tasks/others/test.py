from uiautomator import Device
from uiautomator import device as d

# found_contact = d(className='android.widget.EditText', text='Find contacts').set_text("test")
# print(found_contact)
contact = {}
contact = d(className='android.view.ViewGroup', index=5).child(resourceId='com.android.contacts:id/cliv_name_textview').info
print(contact)

