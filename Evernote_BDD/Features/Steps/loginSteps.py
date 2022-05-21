from Helper.helper import *



@then('verify successful login')
def loginsucess(context):
    try:
        context.text = context.accountpage.hometext()
    except:
        print("test failed")

    if context.text==True:
        print("Sucessful login")





