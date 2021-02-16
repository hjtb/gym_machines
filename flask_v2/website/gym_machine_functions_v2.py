# created a function to create dictionaries to represent gym machines and their traits
def create_gym_machine(name, image_file_name, exercises=None):
    if exercises == None:
        exercises = {}
    if image_file_name == None:
        image_file_name = []

    new_machine = {}
    new_machine["name"] = name
    new_machine["image_file_name"] = image_file_name
    new_machine["exercises"] = exercises

    return new_machine

# test the function against a sample machine to determine functionality
if __name__ == "__main__":
    test_machine_01 = create_gym_machine(
        "Squat Rack",
        image_file_name=["squat_rack.png", "squat_rack_use.png"],
        exercises={
            "squats": ["quads", "hamstrings", "calves", "glutes"],
            "lunges": ["quads", "hamstrings", "calves", "glutes"],
            "deadlifts": ["quads", "hamstrings", "calves", "glutes", "lats", "traps"],
            "front_squats": ["quads", "hamstrings, calves", "glutes", "abdominals"],
            "calf_raises": ["calves"],
            "shrugs": ["traps"]})

    if test_machine_01["name"] == "Squat Rack":
        print("test 1 passed")
    else:
        print("test 1 failed")

    if test_machine_01["image_file_name"][0] == "squat_rack.png":
        print("test 2.1 passed")
    else:
        print("test 2.1 failed")

    if test_machine_01["image_file_name"][1] == "squat_rack_use.png":
        print("test 2.2 passed")
    else:
        print("test 2.2 failed")

    if test_machine_01["exercises"] == {
        "squats": ["quads", "hamstrings", "calves", "glutes"],
        "lunges": ["quads", "hamstrings", "calves", "glutes"],
        "deadlifts": ["quads", "hamstrings", "calves", "glutes", "lats", "traps"],
        "front_squats": ["quads", "hamstrings, calves", "glutes", "abdominals"],
        "calf_raises": ["calves"],
        "shrugs": ["traps"]
    }:
        print("test 3 passed")
    else:
        print("test 3 failed")

    print()

    if test_machine_01["name"] == "":
        print("test 4 failed")
    else:
        print("test 4 passed")

    # initiate more test machines with exercises and muscles_used keywords missing

    test_machine_02 = create_gym_machine(
        "Squat Rack",
        image_file_name=["squat_rack.png", "squat_rack_use.png"],
        exercises={},
    )

    if test_machine_02["exercises"] == {}:
        print("test 5 passed")
    else:
        print("test 5 passed")

    test_machine_03 = create_gym_machine(
        "Squat Rack",
        image_file_name=[],
        exercises={
            "squats": ["quads", "hamstrings", "calves", "glutes"],
            "lunges": ["quads", "hamstrings", "calves", "glutes"],
            "deadlifts": ["quads", "hamstrings", "calves", "glutes", "lats", "traps"],
            "front_squats": ["quads", "hamstrings, calves", "glutes", "abdominals"],
            "calf_raises": ["calves"],
            "shrugs": ["traps"]
        })

    if test_machine_03["image_file_name"] == []:
        print("test 6 passed")
    else:
        print("test 6 passed")
