if __name__ == "__main__":
    from gym_machine_functions_v2 import create_gym_machine


else:
    # imported our function to create gym machines
    from website.gym_machine_functions_v2 import create_gym_machine



# used our function to create 7 gym machines
gym_machine_01 = create_gym_machine(
    "Squat Rack",
    image_file_name=["squat_rack.png", "squat_rack_use.png"],
    exercises={
        "squats": [
            "quads",
            "hamstrings",
            "calves",
            "glutes",
        ],
        "lunges": ["quads", "hamstrings", "calves", "glutes"],
        "deadlifts": [
            "quads",
            "hamstrings",
            "calves",
            "glutes",
            "lats",
            "traps",
            "forearms",
        ],
        "front_squats": ["quads", "hamstrings", "calves", "glutes", "abdominals"],
        "calf_raises": ["calves"],
        "shrugs": ["traps"],
    },
)

gym_machine_02 = create_gym_machine(
    "Pull Up Bar",
    image_file_name=["pull_up_bar.png", "pull_up_bar_use.png"],
    exercises={
        "pull_ups": ["lats", "biceps", "forearms"],
        "chin_ups": ["lats", "biceps", "forearms"],
        "leg_raises": ["abdominals", "forearms"],
        "front_levers": ["lats", "biceps", "abdominals", "forearms"],
        "rows": ["lats", "biceps", "forearms"],
        "muscle_ups": ["lats", "pecs", "biceps", "triceps", "abdominals", "forearms"],
    },
)

gym_machine_03 = create_gym_machine(
    "Olympic Rings",
    image_file_name=["olympic_rings.png", "olympic_rings_use.png"],
    exercises={
        "dips": ["pecs", "triceps"],
        "l_sits": ["abdominals"],
        "leg_raises": ["abdominals", "forearms"],
        "front_levers": ["lats", "biceps", "abdominals", "forearms"],
        "rows": ["lats", "biceps", "forearms"],
        "muscle_ups": ["lats", "pecs", "biceps", "triceps", "forearms"],
        "ring_press_ups": ["triceps", "pecs"],
    },
)

gym_machine_04 = create_gym_machine(
    "Dip Bar",
    image_file_name=["dip_bar.png", "dip_bar_use.png"],
    exercises={
        "dips": ["pecs", "triceps"],
        "l_sits": ["abdominals"],
        "leg_raises": ["abdominals", "forearms"],
        "muscle_ups": ["lats", "pecs", "biceps", "triceps", "forearms"],
        "press_ups": ["triceps", "pecs"],
    },
)

gym_machine_05 = create_gym_machine(
    "Leg Press",
    image_file_name=["leg_press.png", "leg_press_use.png"],
    exercises={
        "leg_press": [
            "quads",
            "hamstrings",
            "calves",
            "glutes",
        ],
        "single_leg_press": ["quads", "hamstrings", "calves", "glutes"],
        "calf_raises": ["calves"],
    },
)

gym_machine_06 = create_gym_machine(
    "Cable Machine",
    image_file_name=["cable_machine.png", "cable_machine_use.png"],
    exercises={
        "pec_flyes": ["pecs"],
        "cable_crunch": ["abdominals"],
        "bicep_curls": ["biceps", "forearms"],
        "face_pulls": ["lats", "traps", "forearms"],
        "rows": ["lats", "biceps", "forearms"],
        "tricep_pushdown": ["triceps"],
        "lateral_raise": ["delts"],
    },
)

gym_machine_07 = create_gym_machine(
    "Bench",
    image_file_name=["bench.png", "bench_use.png"],
    exercises={
        "dumbell_press": ["pecs", "triceps"],
        "dumbell_rows": ["lats", "biceps", "forearms"],
        "decline_bench_press": ["lats", "pecs", "biceps", "triceps", "forearms"],
        "flat_bench_press": ["triceps", "pecs"],
        "incline_bench_press": ["delts", "triceps", "pecs"],
        "overhead_dumbell_press": ["delts", "triceps", "pecs"],
    },
)

# created a list to hold our gym machines
gym_machines = [
    gym_machine_01,
    gym_machine_02,
    gym_machine_03,
    gym_machine_04,
    gym_machine_05,
    gym_machine_06,
    gym_machine_07,
]

# create a list to populate with our possible exercises
all_exercises = []

# create a for loop to populate our list with exercises
for machine in gym_machines:
    for exercise, muscles in machine["exercises"].items():
            if exercise not in all_exercises:
                all_exercises.append(exercise)

# create a dictionary to store our muscles with their images
exercise_dictionary = {}

# create a for loop to fill our dictionary with muscles and corresponding images
for exercise in all_exercises:
    exercise_dictionary.update({exercise:{"description":""}})

exercise_dictionary["squats"]["description"] = f"""
Squat down by bending hips back while allowing knees to bend forward, 
keeping back straight and knees pointed same direction as feet. 
Descend until thighs are just past parallel to floor. 
Extend knees and hips until legs are straight. 
Return and repeat."""

exercise_dictionary["lunges"]["description"] = f"""
Step forward with one leg and squat down through your hips. 
Keep your back straight and be careful to maintain your balance. 
Inhale as you lower yourself.
Continue lowering your body until your alternate knee is nearly touching the floor.
Return to the start position by pushing through your heel, exhaling as you do so."""

exercise_dictionary["deadlifts"]["description"] = f"""
Squat down, keeping your back straight and grip the bar with an overhand grip at shoulder width.
Keep your arms fully extended and stand up with the barbell.
As you lift the barbell, your hips and shoulders should rise together and your back should be straight.
Lower the barbell back to the floor in the same squatting motion you used to lift it."""

exercise_dictionary["front_squats"]["description"] = f"""
Keeping your elbows high, place your arms up and under the bar. 
The bar should be resting on the front of your shoulders. 
Core is tight. Back is flat.
Maintaining control, lift the bar up. Bend your knees forward and allow your hips to bend back as if sitting down. 
Pause when thighs are parallel with the floor.
Return to the starting position and repeat."""

exercise_dictionary["calf_raises"]["description"] = f"""
With a tight core and flat back, raise yourself up with your feet only. 
Pause at the top of the raise.
Slowly lower yourself down but do not touch the ground. 
Raise yourself back up."""

exercise_dictionary["shrugs"]["description"] = f"""
Using an overhand grip at a little more than shoulder width, hold a weight in front of you.
Your arms should be fully extended towards the floor, 
palms facing in towards your thighs. This is the start position.
Exhale and raise or shrug your shoulders up in a slow controlled movement. 
Do not use your biceps to assist in lifting the weight."""

exercise_dictionary["pull_ups"]["description"] = f"""
Reach up and hold onto the bar/rings with an overhand grip. 
Keep your arms straight and hang from the bar so that your arms are taking all of your weight.
Keeping your body straight and not swinging your weight, 
pull your body up towards the bar by pulling your elbows down towards your torso at an angle.
Continue lifting until your chest is nearly touching the bar. 
You should feel a “squeeze” at the base of your lats as they contract.
Once your lats have completely contracted at the top of the movement, 
slowly lower your body to the starting position."""

exercise_dictionary["chin_ups"]["description"] = f"""
Step up to the bar/rings and grasp with your palms facing you and arms close together.
Your arms should be fully extended.
Pull your body up until your elbows are completely bent and close to your body, 
reaching your chin to the bar.
Lower your body until your arms and legs are fully extended in the starting position."""

exercise_dictionary["leg_raises"]["description"] = f"""
Grip rings/chin up/ pull up bar with a firm overhand grip.
Hang from the bar with your legs straight.
Raise your legs by flexing your hips forward and bending your knees up towards your chest.
Continue to raise your knees towards your chest by flexing your waist forward. 
Don’t swing your body to use momentum. 
Use your abdominals to pull your legs up.
Return to the starting position, lowering your legs slowly until they are straight.
Repeat."""

exercise_dictionary["front_levers"]["description"] = f"""
Squat down by bending hips back while allowing knees to bend forward, 
keeping back straight and knees pointed same direction as feet. 
Descend until thighs are just past parallel to floor. 
Extend knees and hips until legs are straight. 
Return and repeat."""

exercise_dictionary["rows"]["description"] = f"""
Squat down by bending hips back while allowing knees to bend forward, 
keeping back straight and knees pointed same direction as feet. 
Descend until thighs are just past parallel to floor. 
Extend knees and hips until legs are straight. 
Return and repeat."""

exercise_dictionary["muscle_ups"]["description"] = f"""
Hang from a pull-up bar/rings with a false grip (thumbs on top the bar, not around).
Perform a pull up (chest to the bar).
‘Roll’ the chest over the bar as a transition from a pull-up to a dip.
Press hands down and drive the body upwards (the dip)."""

exercise_dictionary["dips"]["description"] = f"""
Squat down by bending hips back while allowing knees to bend forward, 
keeping back straight and knees pointed same direction as feet. 
Descend until thighs are just past parallel to floor. 
Extend knees and hips until legs are straight. 
Return and repeat."""

exercise_dictionary["l_sits"]["description"] = f"""
Squat down by bending hips back while allowing knees to bend forward, 
keeping back straight and knees pointed same direction as feet. 
Descend until thighs are just past parallel to floor. 
Extend knees and hips until legs are straight. 
Return and repeat."""

exercise_dictionary["ring_press_ups"]["description"] = f"""
Squat down by bending hips back while allowing knees to bend forward, 
keeping back straight and knees pointed same direction as feet. 
Descend until thighs are just past parallel to floor. 
Extend knees and hips until legs are straight. 
Return and repeat."""

exercise_dictionary["press_ups"]["description"] = f"""
Squat down by bending hips back while allowing knees to bend forward, 
keeping back straight and knees pointed same direction as feet. 
Descend until thighs are just past parallel to floor. 
Extend knees and hips until legs are straight. 
Return and repeat."""

exercise_dictionary["leg_press"]["description"] = f"""
Squat down by bending hips back while allowing knees to bend forward, 
keeping back straight and knees pointed same direction as feet. 
Descend until thighs are just past parallel to floor. 
Extend knees and hips until legs are straight. 
Return and repeat."""

exercise_dictionary["single_leg_press"]["description"] = f"""
Squat down by bending hips back while allowing knees to bend forward, 
keeping back straight and knees pointed same direction as feet. 
Descend until thighs are just past parallel to floor. 
Extend knees and hips until legs are straight. 
Return and repeat."""

exercise_dictionary["pec_flyes"]["description"] = f"""
Squat down by bending hips back while allowing knees to bend forward, 
keeping back straight and knees pointed same direction as feet. 
Descend until thighs are just past parallel to floor. 
Extend knees and hips until legs are straight. 
Return and repeat."""

exercise_dictionary["cable_crunch"]["description"] = f"""
Squat down by bending hips back while allowing knees to bend forward, 
keeping back straight and knees pointed same direction as feet. 
Descend until thighs are just past parallel to floor. 
Extend knees and hips until legs are straight. 
Return and repeat."""

exercise_dictionary["bicep_curls"]["description"] = f"""
Squat down by bending hips back while allowing knees to bend forward, 
keeping back straight and knees pointed same direction as feet. 
Descend until thighs are just past parallel to floor. 
Extend knees and hips until legs are straight. 
Return and repeat."""

exercise_dictionary["face_pulls"]["description"] = f"""
Squat down by bending hips back while allowing knees to bend forward, 
keeping back straight and knees pointed same direction as feet. 
Descend until thighs are just past parallel to floor. 
Extend knees and hips until legs are straight. 
Return and repeat."""

exercise_dictionary["tricep_pushdown"]["description"] = f"""
Squat down by bending hips back while allowing knees to bend forward, 
keeping back straight and knees pointed same direction as feet. 
Descend until thighs are just past parallel to floor. 
Extend knees and hips until legs are straight. 
Return and repeat."""

exercise_dictionary["lateral_raise"]["description"] = f"""
Squat down by bending hips back while allowing knees to bend forward, 
keeping back straight and knees pointed same direction as feet. 
Descend until thighs are just past parallel to floor. 
Extend knees and hips until legs are straight. 
Return and repeat."""

exercise_dictionary["dumbell_press"]["description"] = f"""
Squat down by bending hips back while allowing knees to bend forward, 
keeping back straight and knees pointed same direction as feet. 
Descend until thighs are just past parallel to floor. 
Extend knees and hips until legs are straight. 
Return and repeat."""

exercise_dictionary["dumbell_rows"]["description"] = f"""
Squat down by bending hips back while allowing knees to bend forward, 
keeping back straight and knees pointed same direction as feet. 
Descend until thighs are just past parallel to floor. 
Extend knees and hips until legs are straight. 
Return and repeat."""

exercise_dictionary["decline_bench_press"]["description"] = f"""
Squat down by bending hips back while allowing knees to bend forward, 
keeping back straight and knees pointed same direction as feet. 
Descend until thighs are just past parallel to floor. 
Extend knees and hips until legs are straight. 
Return and repeat."""

exercise_dictionary["incline_bench_press"]["description"] = f"""
Squat down by bending hips back while allowing knees to bend forward, 
keeping back straight and knees pointed same direction as feet. 
Descend until thighs are just past parallel to floor. 
Extend knees and hips until legs are straight. 
Return and repeat."""

exercise_dictionary["overhead_dumbell_press"]["description"] = f"""
Squat down by bending hips back while allowing knees to bend forward, 
keeping back straight and knees pointed same direction as feet. 
Descend until thighs are just past parallel to floor. 
Extend knees and hips until legs are straight. 
Return and repeat."""

# create a list to populate with our possible muscles
all_muscles = []

# create a for loop to populate our list with muscles
for machine in gym_machines:
    for exercise, muscles in machine["exercises"].items():
        for muscle in muscles:
            if muscle not in all_muscles:
                all_muscles.append(muscle)

# create a dictionary to store our muscles with their images
muscle_dictionary = {}

# create a for loop to fill our dictionary with muscles and corresponding images
for muscle in all_muscles:
    muscle_dictionary.update({muscle:{"image": f"{muscle}.png", "description":""}})

muscle_dictionary["traps"]["description"] = f"""The trapezius is an upper back muscle.
 It runs from the occipital bone in the skull to the thoracic spine in the back. 
There are three segments: superior, middle, and inferior. 
Assist in moving the neck and shoulders."""

muscle_dictionary["delts"]["description"] = f"""The deltoid muscle is the main muscle of the shoulder. 
It consists of three muscle heads: the anterior deltoid, lateral deltoid, and posterior deltoid. 
All assist with arm elevation of the arm."""

muscle_dictionary["pecs"]["description"] = f'''The pecs 
are the muscles that connect the chest with the upper arm and shoulder.
It contains four muscles: the pec major, pec minor, serratus and subclavius.
They move the arms across the body and up and down.'''

muscle_dictionary["lats"]["description"] = f"""The latissimus dorsi muscles, known as the lats, 
are the large muscles that connect your arms to your vertebral column. 
Your lats help with shoulder and arm movement and support good posture."""

muscle_dictionary["abdominals"]["description"] = f"""The abs are divided into four groups: 
the external obliques, the internal obliques, the transversus abdominis, and the rectus abdominis.
They provide torso flexion and rotation aswell as spinal stability."""

muscle_dictionary["calves"]["description"] = f"""Calves are on the back of the lower leg.
Consisting of the gastrocnemius and soleus that join to the achilles tendon.  
During walking, running, or jumping, the calf muscle pulls the heel up to allow forward movement."""

muscle_dictionary["hamstrings"]["description"] = f"""The hamstrings at the back of the thigh, 
consist of three muscles: biceps femoris, semitendinosus and semimembranosus, all attach the back of the knee. 
Providing hip extension, and flexion at the knee."""

muscle_dictionary["forearms"]["description"] = f"""The forearm contains many muscles, 
including the flexors and extensors of the digits, a flexor of the elbow, 
and pronators and supinators that turn the hand to face down or upwards."""

muscle_dictionary["biceps"]["description"] = f"""The biceps is a muscle on the front part of the upper arm. 
The biceps includes a “short head” and a “long head” that work as a single muscle.
The main function is flexion of the elbow and supination of the forearm."""

muscle_dictionary["triceps"]["description"] = f"""The triceps muscle consists of a long, medial and lateral head, 
that originate from the humerus and scapula, and attach to the ulna. 
The main function of triceps is extension of the forearm at the elbow joint."""

muscle_dictionary["glutes"]["description"] = f"""The glute muscle consists of three muscles which make up the buttocks: 
the gluteus maximus, gluteus medius and gluteus minimus.
The functions include extension, abduction and hip internal and external rotation."""


muscle_dictionary["quads"]["description"] = f"""The quadriceps muscle
consists of four muscles in the front thigh that connect to the knee. 
They straighten the knee, move the leg forward and absorb shock during walking."""

if __name__ == "__main__":

    print()
    for key, value in exercise_dictionary.items():
        print(f'{key}: {value}')
        print()
    print()
    for key, value in muscle_dictionary.items():
        print(f'{key}: {value}')
        print()
    print()
    print(f"These are the muscles you can train:\n{all_muscles}")
    print()

    # asked for user input to determine which muscle the user wanted to train
    target_muscle = input("What muscle would you like to train?: ")
    print()

    # printed out our machines with all attributes
    for machine in gym_machines:
        for key, value in machine.items():
            print(f"{key}: {value}")
        print()

    specific_machines = []

    for gym_machine in gym_machines:
        for exercise, muscles in gym_machine["exercises"].items():
            if target_muscle in muscles:
                if gym_machine not in specific_machines:
                    specific_machines.append(gym_machine)
    
    print(specific_machines)

    # create a for loop to loop through our machines to determine which machines can be used for the target muscle
    for machine in gym_machines:
        for exercise, muscles in machine["exercises"].items():
            if target_muscle in muscles:
                print(
                    f'you can do {exercise} to train {target_muscle} by using the {machine["name"]}'
                )