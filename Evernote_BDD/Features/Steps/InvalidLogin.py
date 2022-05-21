from Helper.helper import *


@when('Enter Invalid not registered "{Email}"')
def enterNEmail(context, Email):
    context.credentials.enter_emailid(Email)
    time.sleep(4)


@then('Click on continue and verify unsuccessful login')
def Unsignin(context):
    context.credentials.continue_button_click()
    time.sleep(2)
    try:
        context.text = context.credentials.errortext()
    except:
        print("test failed")

    if context.text == True:
        print("UnSucessful login")


