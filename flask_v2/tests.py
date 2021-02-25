import requests
url = "https://www.bbc.co.uk"
response = requests.get(url)

fails = 0
passes = 0

gym_response = requests.get("http://127.0.0.1:5000")

if gym_response.status_code == 200:
    print("test 1: index page, passed")
    passes += 1 
else:
    print("test 1: index page, failed")



gym_response = requests.get("http://127.0.0.1:5000/machines_v2")

if gym_response.status_code == 200:
    print("test 2: machines page, passed")
else:
    print("test 2: machines page, failed")



gym_response = requests.get("http://127.0.0.1:5000/exercises_v2")

if gym_response.status_code == 200:
    print("test 3: exercises page, passed")
else:
    print("test 3: exercises page, failed")



gym_response = requests.get("http://127.0.0.1:5000/muscles_v2")

if gym_response.status_code == 200:
    print("test 4: muscles page, passed")
else:
    print("test 4: muscles page, failed")



gym_response = requests.get("http://127.0.0.1:5000/manage_machines")

if gym_response.status_code == 200:
    print("test 5: manage machines page, passed")
else:
    print("test 5: manage machines page, failed")



gym_response = requests.get("http://127.0.0.1:5000/manage_exercises")

if gym_response.status_code == 200:
    print("test 6: manage exercises page, passed")
else:
    print("test 6: manage exercises page, failed")



gym_response = requests.get("http://127.0.0.1:5000/manage_muscles")

if gym_response.status_code == 200:
    print("test 7: manage muscles page, passed")
else:
    print("test 7: manage muscles page, failed")



gym_response = requests.get("http://127.0.0.1:5000/edit_machine")

if gym_response.status_code == 200:
    print("test 8: edit machines page, passed")
else:
    print("test 8: edit machines page, failed")



gym_response = requests.get("http://127.0.0.1:5000/edit_exercise")

if gym_response.status_code == 200:
    print("test 9: edit exercises page, passed")
else:
    print("test 9: edit exercises page, failed")



gym_response = requests.get("http://127.0.0.1:5000/edit_muscle")

if gym_response.status_code == 200:
    print("test 10: edit muscles page, passed")
else:
    print("**failed test 10: edit muscles page,")



gym_response = requests.get("http://127.0.0.1:5000/edit_muscles")

if gym_response.status_code == 404:
    print("test 11: missing page, passed")
else:
    print("test 11: missing page, failed")


1/0


