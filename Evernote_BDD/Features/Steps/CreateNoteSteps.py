from Helper.helper import *


@then('click on new create note button and write note')
def createNote(context):
    context.accountpage.Home_click()
    context.accountpage.Notebutton_click()
    time.sleep(5)
    context.driver.switch_to.frame("qa-COMMON_EDITOR_IFRAME")
    context.page_notes.edit_NotesTitle("TestCase03")
    context.page_notes.edit_NotesBody("Hellooooo, this is to test valid login create note and logout")
    context.driver.switch_to.default_content()
    context.accountpage.Home_click()
    time.sleep(15)


