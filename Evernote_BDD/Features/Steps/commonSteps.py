from Helper.helper import *


@given('Launch Firefox browser')
def launchBrowser(context):
    #global driver
    context.driver = webdriver.Firefox()
    context.driver.implicitly_wait(25)
    context.driver.maximize_window()
    context.Login = homepage(context.driver)
    context.credentials = wrapper(context.driver)
    context.accountpage = dashboard(context.driver)
    context.page_notes = Notes(context.driver)

@when('Open Evernote website')
def openEvernoteSite(context):
    context.driver.get("https://evernote.com/")


@when('Click on login for already registered user')
def registeredLogin(context):
    context.Login.reglogin_click()


@when('Enter valid registered "{Email}" and "{Password}"')
def enterEmailID(context, Email, Password):
    context.credentials.enter_emailid(Email)
    time.sleep(4)
    context.credentials.continue_button_click()
    time.sleep(2)
    context.credentials.enter_passwrd(Password)


@when('click on sign button')
def sign(context):
    context.credentials.signin_button_click()
    time.sleep(15)

@then('signout from the account')
def signout(context):
    context.accountpage.account_dropdown_click()
    time.sleep(2)
    context.accountpage.signout_menu_click()
    time.sleep(2)

@then('close the browser')
def closeBrowser(context):
    context.driver.close()



