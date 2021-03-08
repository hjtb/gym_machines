import requests
import re
from website import db
base_url = "http://127.0.0.1:5000/"
def get_logged_in_user():

    # quite a long and detailed test.
    # performs the sign up for a new user with a mock username
    # then logs that new user in
    # and finally tests the logging out

    # now try to log that user in
    url = f"{base_url}login"

    # now prepare the headers, email and password for the post
    headers = {"User-Agent": "Mozilla/5.0"}

    payload = dict(
                username="will",
                password="test",
            )

    try:
        # visit the login form to get the csrf token
        session = requests.Session()
        response = session.get(url)

        # now get the token and replace it in the payload
        csrf_token = get_csrf(response.text)
        payload["csrf_token"] = csrf_token

        # now submit the form using the csrf token
        response = session.post(url, headers=headers, data=payload)

        signed_in = response.text.find("You have logged in succesfully")

        if signed_in > 0:
            print("Login worked correctly")
        else:
            print("Login did not work correctly [error]")
            return None

    except:
        print("Login did not work correctly - request failed [error]")
        return None

    return session

def get_csrf(text):

    start_token = '<input id="csrf_token" name="csrf_token" type="hidden" value="'
    end_token = '">'

    start_index = text.find(start_token)
    remainder = text[start_index:]
    end_index = remainder.find(end_token) + len(end_token)
    bit = remainder[:end_index]
    csrf_token = bit[len(start_token) : -len(end_token)]

    # Alternaive way using regex
    # Following 3 lines replaces the lines above - those can be removed
    # Looking for a pattern : <input id="csrf_token" name="csrf_token" type="hidden" value="CSRF TOKEN CHARACTAERS">
    re_pattern = re.compile(r'<input\s+id="csrf_token"\s+name="csrf_token"\s+type="hidden"\s+value="(.+)">')
    match = re_pattern.search(text)
    csrf_token = match.group(1)

    return csrf_token

site_pages = [
    {"page":"registration", "status_code":200},
    {"page":"login", "status_code":200},
    {"page":"edit_exercise?exercise_id=1700", "status_code":200},
    {"page":"edit_exercise?exercise_id=17", "status_code":200},
    {"page":"edit_exercise?exercise_id=hello", "status_code":200},
    {"page":"edit_exercise", "status_code":200},
    {"page":"homepage", "status_code":200}, 
    {"page":"machines", "status_code":200}, 
    {"page":"exercises", "status_code":200}, 
    {"page":"muscles", "status_code":200}, 
    {"page":"manage_machines", "status_code":200}, 
    {"page":"manage_exercises", "status_code":200}, 
    {"page":"manage_muscles", "status_code":200}, 
    {"page":"edit_machine?machine_id=17", "status_code":200}, 
    {"page":"edit_exercise?exercise_id=17", "status_code":200}, 
    {"page":"edit_muscle?muscle_id=1", "status_code":200},
    {"page":"add_machine", "status_code":200}, 
    {"page":"add_exercise", "status_code":200}, 
    {"page":"add_muscle", "status_code":200},
    {"page":"login", "status_code":200},
    {"page":"this page does not exist", "status_code":404}
    ]

fails = 0
passes = 0
test_id = 0

# we used get logged in user which returns a requests session
logged_in_user = get_logged_in_user()

for page in site_pages:
    test_id += 1
    gym_response = logged_in_user.get(f"http://127.0.0.1:5000/{page['page']}")

    if gym_response.status_code == page["status_code"]:
        print(f"test {test_id} : {page['page']}, passed")
        passes += 1 
    else:
        print(f"test {test_id}: index {page['page']}, failed")
        fails += 1




    print()
    print()




print(f"There were {fails} fails")
print(f"There were {passes} passes")


1/0


