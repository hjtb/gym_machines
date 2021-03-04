-- MySQL dump 10.13  Distrib 8.0.23, for Win64 (x86_64)
--
-- Host: localhost    Database: my_db_schema
-- ------------------------------------------------------
-- Server version	8.0.23

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `alembic_version`
--

DROP TABLE IF EXISTS `alembic_version`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL,
  PRIMARY KEY (`version_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alembic_version`
--

LOCK TABLES `alembic_version` WRITE;
/*!40000 ALTER TABLE `alembic_version` DISABLE KEYS */;
INSERT INTO `alembic_version` VALUES ('17a21c5d7e68');
/*!40000 ALTER TABLE `alembic_version` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `exercises`
--

DROP TABLE IF EXISTS `exercises`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `exercises` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `description` varchar(500) NOT NULL,
  `created_date` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=89 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `exercises`
--

LOCK TABLES `exercises` WRITE;
/*!40000 ALTER TABLE `exercises` DISABLE KEYS */;
INSERT INTO `exercises` VALUES (17,'Squats','Squat down by bending hips back while allowing knees to bend forward, \r\nkeeping back straight and knees pointed same direction as feet. \r\nDescend until thighs are just past parallel to floor. \r\nExtend knees and hips until legs are straight.\r\nReturn and repeat.','2021-02-18 07:55:41'),(18,'Lunges','Step forward with one leg and squat down through your hips.  Keep your back straight and be careful to maintain your balance.  Inhale as you lower yourself. Continue lowering your body until your alternate knee is nearly touching the floor. Return to the start position by pushing through your heel, exhaling as you do so','2021-02-18 08:03:20'),(19,'Deadlifts','With the bar on the floor, squat down, keeping your back straight and grip the bar with an overhand grip at shoulder width. Keep your arms fully extended and stand up with the barbell. As you lift the barbell, your hips and shoulders should rise together and your back should be straight. Lower the barbell back to the floor in the same squatting motion you used to lift it.','2021-02-18 08:06:07'),(20,'Front Squats','Squat down, keeping your back straight and grip the bar with an overhand grip at shoulder width. Keep your arms fully extended and stand up with the barbell. As you lift the barbell, your hips and shoulders should rise together and your back should be straight. Lower the barbell back to the floor in the same squatting motion you used to lift it.','2021-02-18 08:59:02'),(32,'Calf Raises','With a tight core and flat back, raise yourself up with your feet only.  Pause at the top of the raise. Slowly lower yourself down but do not touch the ground.  Raise yourself back up.','2021-02-18 12:39:09'),(33,'Muscle-ups','Hang from a pull-up bar/rings with a false grip (thumbs on top the bar, not around). Perform a pull up (chest to the bar). ‘Roll’ the chest over the bar as a transition from a pull-up to a dip. Press hands down and drive the body upwards above the bar (the dip).','2021-02-18 18:50:22'),(35,'Shrugs','Using an overhand grip at a little more than shoulder width, hold a weight in front of you.\r\nYour arms should be fully extended towards the floor, \r\npalms facing in towards your thighs. This is the start position.\r\nExhale and raise or shrug your shoulders up in a slow controlled movement. \r\nDo not use your biceps to assist in lifting the weight.','2021-02-22 08:09:09'),(36,'Pull-ups','Reach up and hold onto the bar/rings with an overhand grip. \r\nKeeping your body straight and not swinging, \r\npull your body upwards to the bar by pulling your chest to the bar. \r\nOnce your lats have completely contracted at the top of the movement, \r\nslowly lower your body to the starting position','2021-02-22 08:10:55'),(37,'Chin-ups','Step up to the bar/rings and grasp with your palms facing you and arms close together.\r\nYour arms should be fully extended.\r\nPull your body up until your chin is over the bar.\r\nLower your body until your arms are fully extended in the starting position.','2021-02-22 08:23:44'),(38,'Leg Raises','Grip rings/pull up bar with a firm overhand grip.\r\nHang from the bar with your legs straight.\r\nUse your abdominals to pull your legs until they are horizontal. \r\nDon’t swing your body to use momentum. \r\nLower your legs slowly until they are straight and repeat.','2021-02-22 08:26:27'),(39,'Front Levers','Assume an inverted(upside-down) hang position on a pull-up bar or gym rings.\r\nKeeping the body perfectly straight, \r\nlower the body slowly down until completely horizontal. (your body facing upwards).\r\nMaintain the hold as long as good form will allow.','2021-02-22 08:34:53'),(40,'Rows','Set the rings/bar to the appropriate height (the lower the more difficult the exercise).\r\nGrip the rings/bar and lean back until your arms are straight.\r\nKeep your body straight and pull your chest up level with your hands.\r\nSlowly lower yourself back down to the starting position and repeat.','2021-02-22 08:38:24'),(42,'Dips','Adjust the height of the rings/bars so that your feet won\'t touch the ground.\r\nStart above the bars/rings, arms straight, supporting your body weight.\r\nLower your body steadily down by bending at the elbows, until your shoulders touch your hands.\r\nPress your body back to the original starting position.','2021-02-22 09:05:52'),(43,'L-Sits','Start above the bars/rings, arms straight, supporting your body weight. \r\nThen, lift up your legs while keeping them straight until they are parallel to the floor so your body makes an \"L\" shape.\r\nDraw your shoulders back and down, keep your back straight, \r\nand look straight ahead with a neutral neck','2021-02-22 09:10:47'),(44,'Ring Press-ups','Adjust the height of rings for the appropriate level of difficulty. (Lower is harder)\r\nStart supporting your bodyweight with shoulders over the rings. \r\nLower slowly until chest touches the rings by bending the elbows, \r\nensuring to keep them tight to the body.\r\nPress back to the start and repeat.\r\n','2021-02-22 09:22:02'),(45,'Leg-Press','Sit on the machine with your back and head resting comfortably, \r\nfeet on the footplate about hip-width apart.\r\nPush the platform away with your heels.\r\nDo not lock out your knees at the top.\r\nSlowly lower footplate to the starting position by gradually bending the knees, repeat.','2021-02-22 09:28:03'),(46,'Single Leg-Press','Sitting in the leg press machine, \r\nline your foot up with your shoulder on the platform, \r\npush the platform away by extending the leg without locking your knee at the top. \r\nSlowly lower the platform to the starting position. \r\nSwap legs and repeat.','2021-02-22 09:36:29'),(47,'Pec flyes','Stand in the centre of the cable machine grabbing a handle from each side. \r\nBend your torso forwards slightly, \r\nand bend your elbows slightly as well, \r\nwith your wrists facing the floor. \r\nPull both handles down and across your body until they nearly touch. \r\nSlowly reverse to the start position, keeping the bend in your elbows throughout.','2021-02-22 11:22:54'),(48,'Cable Crunches','Attach a tricep rope handle to a cable station. \r\nAdjust the carriage so that it\'s near the top third of the machine.\r\nSet in a kneeling position facing the machine.\r\nSimultaneously pull both handles with bent arms and perform a crunch.\r\nWith control return to the starting position, repeat.','2021-02-22 11:27:33'),(49,'Bicep Curls','Using a cable machine/dumbells/barbell grab a weight/handle/bar in each hand.\r\nLet your arms relax, fully extended.\r\nKeeping your upper arms stable and shoulders relaxed, \r\nbend at the elbow and lift so that the hands nearly reach the shoulders. \r\nYour elbows should stay tucked in.\r\nlower the hands and repeat.','2021-02-22 11:33:49'),(50,'Face-pulls','Set up a cable machine with a double-rope attachment fixed to the high pulley. \r\nPull the handles towards you, keeping your upper arms parallel to the floor, so that the handles go either side of your face. Then return to the starting position, \r\nkeeping the tension in the cable. \r\nKeep your movements slow and controlled throughout the exercise.','2021-02-22 11:39:58'),(51,'Tricep Extensions','There are many variations of tricep extensions. \r\nThey can be performed with dumbells, barbells or cables.\r\nThe basic movement is that of a full extension of the elbow under tension,\r\nwhile keeping the elbows close to the body.\r\nThis is followed by a controlled bend of the elbow under tension to the start position.\r\nThen, repeat.','2021-02-22 11:45:59'),(52,'Lateral Raise','Using dumbells for resistance or a low pulley on the cable machine, grab a weight/handle in each hand.\r\nLift the dumbbell/handle until your arms are fully extended horizontally. \r\nSlowly return to start position and repeat','2021-02-22 11:50:44'),(53,'Dumbell Press','Lying on a bench with dumbells in both hands, lift the dumbbells to chest height. \r\nBreathe out and push the dumbbells up until your arms are fully extended, using your pecs to power the movement. Then slowly bring them back down as you inhale','2021-02-22 11:52:52'),(54,'Dumbell Rows','Hold a dumbell in one hand a use a bench to support your weight with the other hand, \r\nbring the dumbbell up to your chest, concentrating on lifting it with your back and shoulder muscles rather than your arms. Keep your chest still as you lift. \r\nLower the dumbbell slowly until your arm is fully extended again. Repeat.','2021-02-22 11:55:32'),(55,'Decline Bench Press','Lying on a bench on a decline, ideally with the feet secured properly to avoid sliding off the bench.\r\nAllow the shoulder and elbow joints to bend as you lower the bar with the elbows tight to the body.\r\nOnce you have assumed a deep and stretched position in the bottom of the decline bench press, press the weight back up to the locked out position, and repeat.','2021-02-22 11:58:55'),(56,'Incline Bench Press','Lying on a bench at a 30-45 degree angle. \r\nGrab the bar at shoulder width, take it off the rack and lower to the chest slowly.\r\nPress back to the top, keeping the elbows tight to the body.\r\nRepeat.','2021-02-22 12:06:00'),(57,'Overhead Dumbell-Press','Sitting on a bench with the torso upright, holding dumbells in each hand, \r\nsling the dumbells up so they\'re held at shoulder height.\r\nRaise the weights above the head in a controlled motion while exhaling. \r\nPause at the top of the motion. \r\nReturn the dumbbells to the shoulders while inhaling. Repeat.','2021-02-22 12:08:34');
/*!40000 ALTER TABLE `exercises` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `exercises_muscles`
--

DROP TABLE IF EXISTS `exercises_muscles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `exercises_muscles` (
  `exercise_id` int NOT NULL,
  `muscle_id` int NOT NULL,
  PRIMARY KEY (`exercise_id`,`muscle_id`),
  KEY `muscle_id` (`muscle_id`),
  CONSTRAINT `exercises_muscles_ibfk_1` FOREIGN KEY (`exercise_id`) REFERENCES `exercises` (`id`),
  CONSTRAINT `exercises_muscles_ibfk_2` FOREIGN KEY (`muscle_id`) REFERENCES `muscles` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `exercises_muscles`
--

LOCK TABLES `exercises_muscles` WRITE;
/*!40000 ALTER TABLE `exercises_muscles` DISABLE KEYS */;
INSERT INTO `exercises_muscles` VALUES (17,1),(18,1),(19,1),(20,1),(45,1),(46,1),(17,8),(18,8),(19,8),(20,8),(38,8),(39,8),(43,8),(48,8),(33,50),(36,50),(37,50),(39,50),(40,50),(54,50),(56,50),(33,51),(42,51),(44,51),(47,51),(55,51),(56,51),(57,51),(52,52),(56,52),(57,52),(19,53),(35,53),(50,53),(52,53),(54,53),(17,54),(18,54),(19,54),(20,54),(32,54),(45,54),(46,54),(17,55),(18,55),(19,55),(20,55),(45,55),(46,55),(19,56),(33,56),(35,56),(36,56),(37,56),(38,56),(39,56),(40,56),(47,56),(48,56),(49,56),(50,56),(51,56),(52,56),(54,56),(33,57),(36,57),(37,57),(39,57),(40,57),(49,57),(54,57),(33,58),(39,58),(42,58),(44,58),(51,58),(55,58),(56,58),(57,58);
/*!40000 ALTER TABLE `exercises_muscles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `machines`
--

DROP TABLE IF EXISTS `machines`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `machines` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `description` varchar(500) NOT NULL,
  `created_date` datetime DEFAULT CURRENT_TIMESTAMP,
  `image` varchar(100) NOT NULL,
  `image_use` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `machines`
--

LOCK TABLES `machines` WRITE;
/*!40000 ALTER TABLE `machines` DISABLE KEYS */;
INSERT INTO `machines` VALUES (1,'Squat Rack','The squat rack is one of the most versatile pieces of gym equipment. The adjustable squat rack will let you perform many exercises safely, without a spotter, which is something very hard to do when working out alone in your home gym. With a squat rack, you will be able to push yourself to failure, beating your PR. Use this machine to do barbell squats and various other exercises using the structure.','2021-02-03 09:22:06','squat_rack.png',''),(2,'Bench','There are many exercises you can do with a weight bench, which is what makes them so versatile.\r\nThey can all be done in the comfort of your own home when combined with other equipment.\r\nAlong with the traditional bench press variations the bench can be used for many other exercises.','2021-02-03 09:22:06','bench.png',''),(13,'Pull Up Bar','The pull up bar is a piece of equipment you can attach to a wall, ceiling, or doorframe. Portable versions can be easily stored or transported. There are many exercises you can perform using the pull up bar. The majority of which are done by hanging underneath the bar gripping it.','2021-02-27 17:32:50','pull_up_bar.png',''),(16,'Dip Bar','Dip bars consist of 2 parallel bars with handles to hold mounted on either a wall or bracket. The two bars surround the user\'s body at the waist. \r\nThey were named after the dips exercise but they are not only limited to these. The list of exercises a user can perform on them is only limited by the users imagination.\r\nPerform dips, leg raises, vertical knee raises, ab workouts and more. Dip bars prove incredibly useful in building tricep and chest muscle.','2021-03-01 08:29:56','dip_bar.png',''),(17,'Leg Press','There are two types of leg press machines commonly found in gyms: the standard horizontal leg press and the 45-degree leg press that has a seat that reclines at an angle while your legs press the platform upward in a diagonal direction. The leg press is a great machine for developing the glutes, hamstrings, quads, and even calf muscles.','2021-03-01 08:40:27','leg_press.png',''),(19,'Olympic Rings','Olympic rings, also called still rings, consist of two small circles that are suspended by straps from an overhead support and grasped while performing various exercises. The rings have been part of the gymnastics program in the Olympic Games since its modern revival in 1896. If smartly planned, ring training combines strength, hypertrophy and joint health, forcing your body to work in unexpected ways and build the straight-arm strength that’s so important in calisthenics.','2021-03-01 08:48:23','olympic_rings.png',''),(20,'Cable Machine','The cable machine is a large piece of gym equipment with adjustable cable pulleys that can have variable resistance added to suit the user. The resistance of the cables allows you to perform numerous exercises in a variety of directions. Some machines have one or two cable stations, while others have multiple. The exercises that can be performed is nearly unlimited on this versatile machine.','2021-03-01 08:59:01','cable_machine.png','');
/*!40000 ALTER TABLE `machines` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `machines_exercises`
--

DROP TABLE IF EXISTS `machines_exercises`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `machines_exercises` (
  `machine_id` int NOT NULL,
  `exercise_id` int NOT NULL,
  PRIMARY KEY (`machine_id`,`exercise_id`),
  KEY `exercise_id` (`exercise_id`),
  CONSTRAINT `machines_exercises_ibfk_1` FOREIGN KEY (`exercise_id`) REFERENCES `exercises` (`id`),
  CONSTRAINT `machines_exercises_ibfk_2` FOREIGN KEY (`machine_id`) REFERENCES `machines` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `machines_exercises`
--

LOCK TABLES `machines_exercises` WRITE;
/*!40000 ALTER TABLE `machines_exercises` DISABLE KEYS */;
INSERT INTO `machines_exercises` VALUES (1,17),(1,18),(1,19),(1,20),(1,32),(17,32),(13,33),(19,33),(1,35),(13,36),(19,36),(13,37),(19,37),(13,38),(16,38),(19,38),(13,39),(19,39),(13,40),(19,40),(20,40),(16,42),(19,42),(16,43),(19,43),(19,44),(17,45),(17,46),(20,47),(20,48),(2,49),(20,49),(20,50),(2,51),(20,51),(2,52),(20,52),(2,53),(2,54),(2,55),(2,56),(2,57);
/*!40000 ALTER TABLE `machines_exercises` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `muscles`
--

DROP TABLE IF EXISTS `muscles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `muscles` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `description` varchar(500) NOT NULL,
  `image` varchar(100) NOT NULL,
  `created_date` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=70 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `muscles`
--

LOCK TABLES `muscles` WRITE;
/*!40000 ALTER TABLE `muscles` DISABLE KEYS */;
INSERT INTO `muscles` VALUES (1,'Glutes','The glute muscle consists of three muscles which make up the buttocks:  the gluteus maximus, gluteus medius and gluteus minimus. The functions include extension, abduction and hip internal and external rotation.','glutes.png','2021-02-03 09:22:06'),(8,'Abdominals','The abs are divided into four groups:  the external obliques, the internal obliques, the transversus abdominis, and the rectus abdominis. They provide torso flexion and rotation aswell as spinal stability.','abdominals.png','2021-02-11 08:05:47'),(50,'Lats','The latissimus dorsi muscles, known as the lats,  are the large muscles that connect your arms to your vertebral column.  Your lats help with shoulder and arm movement and support good posture.','lats.png','2021-02-18 12:45:32'),(51,'Pecs','The pecs  are the muscles that connect the chest with the upper arm and shoulder. It contains four muscles: the pec major, pec minor, serratus and subclavius. They move the arms across the body and up and down.','pecs.png','2021-02-18 12:46:39'),(52,'Delts','The deltoid muscle is the main muscle of the shoulder.  It consists of three muscle heads: the anterior deltoid, lateral deltoid, and posterior deltoid.  All assist with arm elevation of the arm.','delts.png','2021-02-21 10:57:33'),(53,'Traps','The trapezius is an upper back muscle.\r\n It runs from the occipital bone in the skull to the thoracic spine in the back. \r\nThere are three segments: superior, middle, and inferior. \r\nAssist in moving the neck and shoulders.','traps.png','2021-02-21 11:15:33'),(54,'Calves','Calves are on the back of the lower leg.\r\nConsisting of the gastrocnemius and soleus that join to the achilles tendon.  \r\nDuring walking, running, or jumping, the calf muscle pulls the heel up to allow forward movement.','calves.png','2021-02-21 11:36:13'),(55,'Hamstrings','The hamstrings at the back of the thigh, \r\nconsist of three muscles: biceps femoris, semitendinosus and semimembranosus, all attach the back of the knee. \r\nProviding hip extension, and flexion at the knee.','hamstrings.png','2021-02-21 11:36:58'),(56,'Forearms','The forearm contains many muscles, \r\nincluding the flexors and extensors of the digits, a flexor of the elbow, \r\nand pronators and supinators that turn the hand to face down or upwards.','forearms.png','2021-02-21 11:37:30'),(57,'Biceps','The biceps is a muscle on the front part of the upper arm. \r\nThe biceps includes a “short head” and a “long head” that work as a single muscle.\r\nThe main function is flexion of the elbow and supination of the forearm.','biceps.png','2021-02-21 11:37:54'),(58,'Triceps','The triceps muscle consists of a long, medial and lateral head, \r\nthat originate from the humerus and scapula, and attach to the ulna. \r\nThe main function of triceps is extension of the forearm at the elbow joint.','triceps.png','2021-02-21 11:38:18'),(63,'Quads','The quadriceps muscle consists of four muscles in the front thigh that connect to the knee. They straighten the knee, move the leg forward and absorb shock during walking.','quads.png','2021-02-23 12:36:32');
/*!40000 ALTER TABLE `muscles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_age` int NOT NULL,
  `created_date` datetime DEFAULT CURRENT_TIMESTAMP,
  `password` varchar(80) DEFAULT NULL,
  `username` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=301 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,31,'2021-01-25 12:41:18','sha256$E80L9LvL$141c777b449171382a482d2fbbac9dc7fb9cb7bf916b57594006b802b5f36d2e','will');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-03-04 12:31:30
