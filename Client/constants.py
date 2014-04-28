__author__ = 'csh7kd'

# Added constants.py, which contains prompt responses and httpResponses so that changes to these are global.
# All HttpResponses and prompt reponses have been rewritten as fields in constants.py (words are the same as of file creation).

#prompts used in Client/main.py
p_welcome = 'Welcome to OneDir!'
p_login_success = 'Login successful.'
p_login_fail = 'Login unsuccessful.'
p_register_success = 'Registration successful!'
p_register_fail = 'Registration failed - username already in use.'
p_passwords_dont_match = "Passwords don't match."
p_incorrect_input = 'Incorrect input.'
p_incorrect_password = 'Incorrect password.'
p_listFiles_fail = 'Failed to retrieve list of files.'
p_listFiles_nofiles = 'You currently have no files on the server.'
p_listFiles_success = 'Your files on the server: '
p_goodbye = '\nThanks for using OneDir!'

#HttpResponses used in Server/DJServer/views.py
h_welcome_beta = 'Welcome to OneDir, Beta coming soon!'
h_uploadFile_success = 'Successful upload'
h_loggedIn_true = 'User is currently logged in.'
h_loggedIn_false = 'User is NOT currently logged in.'
h_createUser_success = 'User has been created.'
h_changePassword_success = 'User password changed successfully.'
h_changePassword_fail = 'Password change was unsuccessful.'
h_listFiles_fail = 'Unauthorized'


#new prompts should be left-aligned while responses to user input will be indented
def indent(string):
    return '   ' + string


server_url = 'http://127.0.0.1:8000'
