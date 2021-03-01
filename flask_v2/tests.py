import requests
from website import db

site_pages = [
    {"page":"homepage"}, {"page":"machines"}, {"page":"exercises"}, {"page":"muscles"}, 
    {"page":"manage_machines"}, {"page":"manage_exercises"}, {"page":"manage_muscles"}, 
    {"page":"edit_machine"}, {"page":"edit_exercise"}, {"page":"edit_muscle"},
    {"page":"add_machine"}, {"page":"add_exercise"}, {"page":"add_muscle"}
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
        print(f"test {test_id} 11: missing page for {page['page']}, passed")
        passes += 1
    else:
        print(f"test {test_id}: missing page for {page['page']}, failed")
        fails += 1

    print()
    print()




print(f"There were {fails} fails")
print(f"There were {passes} passes")


1/0


