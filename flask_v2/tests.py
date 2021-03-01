import requests
from website import db

site_pages = [
    {"page":"homepage", "status_code":200}, {"page":"machines", "status_code":200}, {"page":"exercises", "status_code":200}, {"page":"muscles", "status_code":200}, 
    {"page":"manage_machines", "status_code":200}, {"page":"manage_exercises", "status_code":200}, {"page":"manage_muscles", "status_code":200}, 
    {"page":"edit_machine", "status_code":200}, {"page":"edit_exercise?exercise_id=17", "status_code":200}, {"page":"edit_muscle", "status_code":200},
    {"page":"add_machine", "status_code":200}, {"page":"add_exercise", "status_code":200}, {"page":"add_muscle", "status_code":200},
    {"page":"this page does not exist", "status_code":404}
    ]

fails = 0
passes = 0
test_id = 0


for page in site_pages:
    test_id += 1
    gym_response = requests.get(f"http://127.0.0.1:5000/{page['page']}")

    if gym_response.status_code == 200:
        print(f"test {test_id} : {page['page']}, passed")
        passes += 1 
    else:
        print(f"test {test_id}: index {page['page']}, failed")
        fails += 1

    gym_response = requests.get(f"http://127.0.0.1:5000/{page['page']}s")

    if gym_response.status_code == 404:
        print(f"test {test_id}: missing page for {page['page']}, passed")
        passes += 1
    else:
        print(f"test {test_id}: missing page for {page['page']}, failed")
        fails += 1

    print()
    print()




print(f"There were {fails} fails")
print(f"There were {passes} passes")


1/0


