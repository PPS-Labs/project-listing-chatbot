"""
Seed data for the robotics project chatbot.
Run with: python manage.py seed_db
"""
from django.core.management.base import BaseCommand
from robohelper.models import Component, Project, ProjectComponent


COMPONENTS_DATA = [
    # Microcontrollers
    {
        'name': 'Arduino Uno',
        'category': 'microcontroller',
        'description': 'Popular 8-bit microcontroller board based on ATmega328P',
        'keywords': 'arduino, uno, atmega328, atmega, microcontroller, board'
    },
    {
        'name': 'Arduino Mega',
        'category': 'microcontroller',
        'description': 'Arduino board with more I/O pins, based on ATmega2560',
        'keywords': 'arduino, mega, atmega2560, microcontroller, board'
    },
    {
        'name': 'Arduino Nano',
        'category': 'microcontroller',
        'description': 'Compact Arduino board for small projects',
        'keywords': 'arduino, nano, compact, small, microcontroller'
    },
    {
        'name': 'Raspberry Pi',
        'category': 'microcontroller',
        'description': 'Single-board computer with GPIO pins for robotics',
        'keywords': 'raspberry, pi, rpi, raspi, linux, computer, sbc'
    },
    {
        'name': 'ESP8266',
        'category': 'microcontroller',
        'description': 'WiFi-enabled microcontroller for IoT projects',
        'keywords': 'esp8266, esp, nodemcu, wifi, iot, wireless, wemos'
    },
    {
        'name': 'ESP32',
        'category': 'microcontroller',
        'description': 'Dual-core WiFi + Bluetooth microcontroller',
        'keywords': 'esp32, wifi, bluetooth, iot, wireless, dual core'
    },

    # Sensors
    {
        'name': 'Ultrasonic Sensor HC-SR04',
        'category': 'sensor',
        'description': 'Measures distance using ultrasound (2cm-400cm)',
        'keywords': 'ultrasonic, hcsr04, hc-sr04, distance, sonar, ultrasound, ranging'
    },
    {
        'name': 'IR Sensor',
        'category': 'sensor',
        'description': 'Infrared proximity/obstacle detection sensor',
        'keywords': 'ir, infrared, obstacle, proximity, line, detection, sensor'
    },
    {
        'name': 'PIR Motion Sensor',
        'category': 'sensor',
        'description': 'Passive infrared sensor for detecting motion/human presence',
        'keywords': 'pir, motion, human, detection, passive, infrared, presence, security'
    },
    {
        'name': 'DHT11 Temperature Sensor',
        'category': 'sensor',
        'description': 'Digital temperature and humidity sensor',
        'keywords': 'dht11, dht22, temperature, humidity, weather, climate, temp'
    },
    {
        'name': 'LDR Light Sensor',
        'category': 'sensor',
        'description': 'Light Dependent Resistor for detecting light intensity',
        'keywords': 'ldr, light, photoresistor, brightness, darkness, photocell'
    },
    {
        'name': 'MPU6050 Gyroscope',
        'category': 'sensor',
        'description': '6-axis accelerometer and gyroscope module',
        'keywords': 'mpu6050, gyroscope, accelerometer, gyro, imu, orientation, tilt, motion'
    },
    {
        'name': 'Soil Moisture Sensor',
        'category': 'sensor',
        'description': 'Measures soil moisture level for agriculture/gardening',
        'keywords': 'soil, moisture, water, agriculture, garden, plant, farming'
    },
    {
        'name': 'MQ2 Gas Sensor',
        'category': 'sensor',
        'description': 'Detects combustible gases and smoke',
        'keywords': 'mq2, gas, smoke, lpg, methane, fire, combustible, detection'
    },
    {
        'name': 'TCS3200 Color Sensor',
        'category': 'sensor',
        'description': 'Detects and identifies colors',
        'keywords': 'tcs3200, color, colour, detection, rgb, identification'
    },
    {
        'name': 'Load Cell HX711',
        'category': 'sensor',
        'description': 'Weight measurement sensor with HX711 amplifier',
        'keywords': 'load cell, weight, hx711, scale, force, measurement'
    },

    # Actuators
    {
        'name': 'Servo Motor SG90',
        'category': 'actuator',
        'description': 'Micro servo motor with 180° rotation',
        'keywords': 'servo, sg90, motor, rotation, actuator, micro servo, angular'
    },
    {
        'name': 'DC Motor',
        'category': 'actuator',
        'description': 'Standard DC motor for wheels and rotation',
        'keywords': 'dc, motor, wheel, rotation, speed, geared, drive'
    },
    {
        'name': 'Stepper Motor',
        'category': 'actuator',
        'description': 'Precise step-by-step rotation motor (NEMA17)',
        'keywords': 'stepper, motor, nema17, precise, step, rotation, cnc'
    },
    {
        'name': 'Buzzer',
        'category': 'actuator',
        'description': 'Piezoelectric buzzer for sound/alarm output',
        'keywords': 'buzzer, piezo, sound, alarm, beep, tone, audio'
    },
    {
        'name': 'Relay Module',
        'category': 'actuator',
        'description': 'Electrically controlled switch for high-power devices',
        'keywords': 'relay, switch, module, control, power, high voltage, on off'
    },
    {
        'name': 'Water Pump',
        'category': 'actuator',
        'description': 'Small submersible water pump for irrigation',
        'keywords': 'pump, water, irrigation, submersible, flow, liquid'
    },

    # Modules
    {
        'name': 'L298N Motor Driver',
        'category': 'module',
        'description': 'Dual H-Bridge motor driver for controlling DC/Stepper motors',
        'keywords': 'l298n, motor driver, h-bridge, dual, driver, motor control, shield'
    },
    {
        'name': 'HC-05 Bluetooth Module',
        'category': 'module',
        'description': 'Serial Bluetooth module for wireless communication',
        'keywords': 'hc-05, hc05, bluetooth, bt, wireless, serial, communication, module'
    },
    {
        'name': 'RF Module 433MHz',
        'category': 'module',
        'description': 'Radio frequency transmitter/receiver module',
        'keywords': 'rf, radio, 433mhz, transmitter, receiver, wireless, frequency'
    },
    {
        'name': 'GPS Module NEO-6M',
        'category': 'module',
        'description': 'GPS receiver module for location tracking',
        'keywords': 'gps, neo-6m, location, tracking, navigation, satellite, coordinates'
    },

    # Displays
    {
        'name': 'LCD 16x2 Display',
        'category': 'display',
        'description': '16x2 character LCD display for showing text',
        'keywords': 'lcd, 16x2, display, screen, text, character, i2c'
    },
    {
        'name': 'OLED Display',
        'category': 'display',
        'description': '0.96" OLED display for graphics and text',
        'keywords': 'oled, display, screen, ssd1306, graphics, i2c'
    },
    {
        'name': 'LED',
        'category': 'display',
        'description': 'Light Emitting Diode for visual indicators',
        'keywords': 'led, light, indicator, diode, rgb, neopixel'
    },

    # Other
    {
        'name': 'Potentiometer',
        'category': 'other',
        'description': 'Variable resistor for analog input control',
        'keywords': 'potentiometer, pot, knob, variable, resistor, analog, control'
    },
    {
        'name': 'Joystick Module',
        'category': 'other',
        'description': 'Analog joystick for directional control',
        'keywords': 'joystick, analog, direction, control, x y, axis, gaming'
    },
    {
        'name': 'Keypad 4x4',
        'category': 'other',
        'description': '4x4 matrix keypad for numeric/character input',
        'keywords': 'keypad, 4x4, matrix, numeric, input, buttons, keyboard'
    },
    {
        'name': 'Camera Module',
        'category': 'other',
        'description': 'Camera module for image capture and processing',
        'keywords': 'camera, webcam, image, video, capture, vision, ov7670'
    },
    {
        'name': 'Battery Pack',
        'category': 'power',
        'description': 'Battery holder/pack for portable power',
        'keywords': 'battery, power, portable, supply, pack, holder, rechargeable'
    },
]


PROJECTS_DATA = [
    {
        'title': 'Obstacle Avoiding Robot',
        'description': 'Build a smart robot that autonomously navigates around obstacles using ultrasonic sensor. '
                       'The robot detects objects in its path and turns to find a clear route.',
        'difficulty': 'beginner',
        'instructions': 'Mount the ultrasonic sensor on front of chassis. Use L298N to drive two DC motors. '
                        'Program Arduino to stop and turn when obstacle is detected within 20cm.',
        'components': [
            ('Arduino Uno', 1), ('Ultrasonic Sensor HC-SR04', 1),
            ('L298N Motor Driver', 1), ('DC Motor', 2), ('Battery Pack', 1)
        ]
    },
    {
        'title': 'Line Following Robot',
        'description': 'Create a robot that follows a black line on a white surface using IR sensors. '
                       'Perfect for understanding control systems and sensor feedback loops.',
        'difficulty': 'beginner',
        'instructions': 'Attach 2 IR sensors underneath the front of the chassis. '
                        'When left sensor detects line, turn left. When right sensor detects, turn right. '
                        'Both sensors on line = go straight.',
        'components': [
            ('Arduino Uno', 1), ('IR Sensor', 2),
            ('L298N Motor Driver', 1), ('DC Motor', 2), ('Battery Pack', 1)
        ]
    },
    {
        'title': 'Robotic Arm (3-DOF)',
        'description': 'Build a 3 degree-of-freedom robotic arm controlled by potentiometers. '
                       'Learn about servo control, mechanical design, and kinematics.',
        'difficulty': 'intermediate',
        'instructions': 'Use 3 servo motors for base rotation, shoulder, and elbow joints. '
                        'Map each potentiometer to a servo using analogRead() and Servo library.',
        'components': [
            ('Arduino Uno', 1), ('Servo Motor SG90', 3), ('Potentiometer', 3)
        ]
    },
    {
        'title': 'Smart Dustbin',
        'description': 'An automatic dustbin that opens its lid when someone approaches. '
                       'Uses ultrasonic sensor to detect hand proximity and servo to open lid.',
        'difficulty': 'beginner',
        'instructions': 'Mount ultrasonic sensor on the dustbin. When distance < 15cm, rotate servo to open lid. '
                        'Close lid when no hand detected for 3 seconds.',
        'components': [
            ('Arduino Uno', 1), ('Ultrasonic Sensor HC-SR04', 1), ('Servo Motor SG90', 1)
        ]
    },
    {
        'title': 'Bluetooth Controlled Car',
        'description': 'Build a car you can control from your smartphone via Bluetooth. '
                       'Supports forward, backward, left, right movement and speed control.',
        'difficulty': 'intermediate',
        'instructions': 'Connect HC-05 Bluetooth module to Arduino. Use a Bluetooth terminal app on phone. '
                        'Send characters (F/B/L/R/S) to control motor direction via L298N.',
        'components': [
            ('Arduino Uno', 1), ('HC-05 Bluetooth Module', 1),
            ('L298N Motor Driver', 1), ('DC Motor', 2), ('Battery Pack', 1)
        ]
    },
    {
        'title': 'Gesture Controlled Robot',
        'description': 'Control a robot with hand gestures using MPU6050 gyroscope. '
                       'Tilt your hand forward/backward/left/right to move the robot.',
        'difficulty': 'advanced',
        'instructions': 'Use two Arduinos: one on glove with MPU6050 + RF transmitter, '
                        'one on robot with RF receiver + L298N + DC motors. '
                        'Map tilt angles to motor directions.',
        'components': [
            ('Arduino Uno', 2), ('MPU6050 Gyroscope', 1), ('RF Module 433MHz', 1),
            ('L298N Motor Driver', 1), ('DC Motor', 2), ('Battery Pack', 1)
        ]
    },
    {
        'title': 'Smart Irrigation System',
        'description': 'Automatic plant watering system that monitors soil moisture and waters plants when dry. '
                       'Includes LCD display showing moisture levels and pump status.',
        'difficulty': 'beginner',
        'instructions': 'Read soil moisture sensor value. When soil is dry (value below threshold), '
                        'activate relay to turn on water pump. Display moisture % on LCD.',
        'components': [
            ('Arduino Uno', 1), ('Soil Moisture Sensor', 1), ('Water Pump', 1),
            ('Relay Module', 1), ('LCD 16x2 Display', 1)
        ]
    },
    {
        'title': 'Home Security System',
        'description': 'PIR-based motion detection security system with alarm buzzer and LED indicator. '
                       'Detects human presence and triggers visual and audio alerts.',
        'difficulty': 'beginner',
        'instructions': 'Connect PIR sensor to Arduino. When motion detected, activate buzzer alarm '
                        'and blink LED. Use a push button to arm/disarm the system.',
        'components': [
            ('Arduino Uno', 1), ('PIR Motion Sensor', 1), ('Buzzer', 1),
            ('LED', 1), ('LCD 16x2 Display', 1)
        ]
    },
    {
        'title': 'Weather Station',
        'description': 'Build a mini weather station that monitors temperature, humidity, and light levels. '
                       'Displays real-time data on an OLED display.',
        'difficulty': 'intermediate',
        'instructions': 'Connect DHT11 for temp/humidity and LDR for light. '
                        'Display readings on OLED screen. Update every 2 seconds.',
        'components': [
            ('Arduino Uno', 1), ('DHT11 Temperature Sensor', 1),
            ('LDR Light Sensor', 1), ('OLED Display', 1)
        ]
    },
    {
        'title': 'Self-Balancing Robot',
        'description': 'A two-wheeled robot that balances itself using PID control and MPU6050 gyroscope. '
                       'Learn about control theory and feedback systems.',
        'difficulty': 'advanced',
        'instructions': 'Use MPU6050 to read tilt angle. Implement PID controller to adjust DC motor speed '
                        'to keep robot balanced. Tune PID constants carefully.',
        'components': [
            ('Arduino Uno', 1), ('MPU6050 Gyroscope', 1),
            ('L298N Motor Driver', 1), ('DC Motor', 2), ('Battery Pack', 1)
        ]
    },
    {
        'title': 'Gas Leak Detector',
        'description': 'Safety system that detects gas leaks using MQ2 sensor and alerts with buzzer and LED. '
                       'Can be extended with WiFi for remote notifications.',
        'difficulty': 'beginner',
        'instructions': 'Read MQ2 analog value. If gas concentration exceeds threshold, '
                        'activate buzzer and red LED. Show ppm value on LCD.',
        'components': [
            ('Arduino Uno', 1), ('MQ2 Gas Sensor', 1), ('Buzzer', 1),
            ('LED', 1), ('LCD 16x2 Display', 1)
        ]
    },
    {
        'title': 'Color Sorting Machine',
        'description': 'A machine that detects the color of objects and sorts them into different bins '
                       'using a servo-based sorting mechanism.',
        'difficulty': 'intermediate',
        'instructions': 'Use TCS3200 to detect color. Servo rotates to position the correct bin '
                        'under the chute based on detected color (Red/Green/Blue).',
        'components': [
            ('Arduino Uno', 1), ('TCS3200 Color Sensor', 1),
            ('Servo Motor SG90', 2), ('LED', 3)
        ]
    },
    {
        'title': 'GPS Tracker',
        'description': 'Build a portable GPS tracker that logs location coordinates on an OLED display. '
                       'Can be used for vehicle tracking or hiking.',
        'difficulty': 'intermediate',
        'instructions': 'Connect NEO-6M GPS module to Arduino. Parse NMEA sentences to extract '
                        'latitude and longitude. Display coordinates on OLED.',
        'components': [
            ('Arduino Uno', 1), ('GPS Module NEO-6M', 1),
            ('OLED Display', 1), ('Battery Pack', 1)
        ]
    },
    {
        'title': 'IoT Home Automation',
        'description': 'Control home appliances (lights, fan) remotely using WiFi. '
                       'Build a web dashboard to toggle devices from your phone.',
        'difficulty': 'intermediate',
        'instructions': 'Use ESP8266/ESP32 to create a web server. Connect appliances through relay module. '
                        'Toggle relays via HTTP requests from the web interface.',
        'components': [
            ('ESP8266', 1), ('Relay Module', 2), ('LED', 2), ('DHT11 Temperature Sensor', 1)
        ]
    },
    {
        'title': 'Joystick Controlled Servo Arm',
        'description': 'Control a 2-axis robotic arm using a joystick module. '
                       'Move the joystick to pan and tilt the arm in real-time.',
        'difficulty': 'beginner',
        'instructions': 'Map joystick X-axis to one servo and Y-axis to another. '
                        'Use map() function to convert analog readings to servo angles.',
        'components': [
            ('Arduino Uno', 1), ('Joystick Module', 1), ('Servo Motor SG90', 2)
        ]
    },
    {
        'title': 'Password Door Lock',
        'description': 'Secure door lock system using a 4x4 keypad. Enter the correct password to unlock '
                       'the door via servo motor. LCD shows access status.',
        'difficulty': 'intermediate',
        'instructions': 'Use Keypad library to read 4-digit password. Compare with stored password. '
                        'If correct, rotate servo to unlock. Show status on LCD.',
        'components': [
            ('Arduino Uno', 1), ('Keypad 4x4', 1), ('Servo Motor SG90', 1),
            ('LCD 16x2 Display', 1), ('Buzzer', 1)
        ]
    },
    {
        'title': 'Smart Street Light System',
        'description': 'Automatic street light that turns on at night and off during the day using LDR sensor. '
                       'Includes PIR sensor to brighten when people are nearby.',
        'difficulty': 'beginner',
        'instructions': 'Read LDR to detect darkness. When dark, turn on LED. '
                        'Add PIR to increase brightness when motion is detected.',
        'components': [
            ('Arduino Uno', 1), ('LDR Light Sensor', 1), ('PIR Motion Sensor', 1), ('LED', 3)
        ]
    },
    {
        'title': 'Digital Weighing Scale',
        'description': 'Build a digital weight scale using load cell and HX711 amplifier. '
                       'Display weight on OLED screen with tare function.',
        'difficulty': 'intermediate',
        'instructions': 'Connect load cell to HX711 module. Use HX711 library to read calibrated weight. '
                        'Display on OLED. Add button for tare/zero function.',
        'components': [
            ('Arduino Uno', 1), ('Load Cell HX711', 1), ('OLED Display', 1)
        ]
    },
    {
        'title': 'Radar Scanner System',
        'description': 'Build a radar-like scanning system using ultrasonic sensor mounted on a servo. '
                       'Visualize detected objects in a radar sweep pattern.',
        'difficulty': 'intermediate',
        'instructions': 'Mount ultrasonic sensor on servo. Sweep servo from 0° to 180°. '
                        'At each angle, measure distance. Send data to PC via serial for visualization.',
        'components': [
            ('Arduino Uno', 1), ('Ultrasonic Sensor HC-SR04', 1), ('Servo Motor SG90', 1)
        ]
    },
    {
        'title': 'Automated Pet Feeder',
        'description': 'Timed pet food dispenser using servo motor. Set feeding schedules via keypad. '
                       'LCD shows next feeding time.',
        'difficulty': 'intermediate',
        'instructions': 'Use RTC module or millis() for timing. At scheduled times, rotate servo to '
                        'open food gate. Use keypad to set feeding times. Display schedule on LCD.',
        'components': [
            ('Arduino Uno', 1), ('Servo Motor SG90', 1), ('Keypad 4x4', 1),
            ('LCD 16x2 Display', 1), ('Buzzer', 1)
        ]
    },
]


class Command(BaseCommand):
    help = 'Seed the database with robotics components and project ideas'

    def handle(self, *args, **options):
        self.stdout.write('[*] Seeding database...\n')

        # Clear existing data
        ProjectComponent.objects.all().delete()
        Project.objects.all().delete()
        Component.objects.all().delete()
        self.stdout.write('  Cleared existing data.')

        # Create components
        components_map = {}
        for comp_data in COMPONENTS_DATA:
            comp, created = Component.objects.get_or_create(
                name=comp_data['name'],
                defaults={
                    'category': comp_data['category'],
                    'description': comp_data['description'],
                    'keywords': comp_data['keywords'],
                }
            )
            components_map[comp.name] = comp
            tag = '[+] Created' if created else '[=] Exists'
            self.stdout.write(f'  {tag}: {comp.name}')

        self.stdout.write(f'\n  Total components: {len(components_map)}\n')

        # Create projects
        for proj_data in PROJECTS_DATA:
            project, created = Project.objects.get_or_create(
                title=proj_data['title'],
                defaults={
                    'description': proj_data['description'],
                    'difficulty': proj_data['difficulty'],
                    'instructions': proj_data.get('instructions', ''),
                }
            )
            if created:
                for comp_name, qty in proj_data['components']:
                    if comp_name in components_map:
                        ProjectComponent.objects.create(
                            project=project,
                            component=components_map[comp_name],
                            quantity=qty
                        )

            tag = '[+] Created' if created else '[=] Exists'
            self.stdout.write(f'  {tag}: {project.title}')

        self.stdout.write(
            f'\n  Seeding complete! '
            f'{Component.objects.count()} components, '
            f'{Project.objects.count()} projects loaded.\n'
        )
