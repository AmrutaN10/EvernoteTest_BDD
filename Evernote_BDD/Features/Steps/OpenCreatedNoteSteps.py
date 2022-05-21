from Helper.helper import *


@then('Successfully Open created note from previouse scenario')
def openCreatedNote(context):
    context.accountpage.Home_click()
    context.page_notes.creatednote_click()
    context.accountpage.note_action()
    context.accountpage.delete_action()
    time.sleep(15)



