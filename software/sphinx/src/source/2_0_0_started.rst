Getting Started
===============

This guide will help you set up and start using the **DevLab Multi Hub Shield** with your preferred microcontroller platform.


Hardware Setup
--------------

**Step 1: Select Your Microcontroller Platform**

The DevLab Multi Hub Shield is compatible with multiple platforms. Choose one of the following:

- Pulsar (UNIT Electronics)
- Seeed Xiao (ESP32, RP2040, SAMD21, etc.)
- Raspberry Pi Pico
- Adafruit Feather
- ESP32 Devkit V4
- Mikro Bus compatible boards

**Step 2: Mount the Shield**

1. Align the pin headers of your microcontroller board with the corresponding socket on the shield
2. Gently press the boards together ensuring all pins are properly seated
3. Verify that the boards are securely connected

**Step 3: Power Connection**

The shield can be powered through multiple methods:

- **USB-C**: Connect a USB-C cable to the shield's USB-C port (5V)
- **Microcontroller Power**: Power is shared from the microcontroller board
- **External Supply**: Use dedicated power input (check voltage requirements)

.. warning::
   Do not power the shield and microcontroller from multiple sources simultaneously unless you understand the power distribution design.


**Step 4: Verify Power**

Check the power indicator LEDs on the shield. If lit, the shield is receiving power correctly.


Software Setup
--------------

**Arduino IDE Configuration**

For Arduino-compatible boards (Xiao, Pico, ESP32):

1. Install the Arduino IDE from `arduino.cc <https://www.arduino.cc/en/software>`_
2. Add your board's support package:
   
   - **Xiao ESP32**: Install "esp32" boards via Board Manager
   - **Raspberry Pi Pico**: Install "Arduino Mbed OS RP2040" or "Raspberry Pi Pico/RP2040"
   - **ESP32 Devkit**: Install "esp32" boards
   - **Pulsar**: Follow UNIT Electronics documentation

3. Select your board from **Tools → Board**
4. Select the correct port from **Tools → Port**

**MicroPython Setup**

For boards supporting MicroPython (Pico, ESP32):

1. Flash MicroPython firmware to your board
2. Use Thonny IDE or similar tool to connect
3. Upload example scripts from the ``software/examples/mp/`` directory


Quick Test - LED Blink
-----------------------

Let's verify your setup by blinking one of the status LEDs.

**Arduino Code**

.. code-block:: cpp

   // Define LED pin (check your shield pinout)
   #define LED_PIN 13

   void setup() {
     pinMode(LED_PIN, OUTPUT);
   }

   void loop() {
     digitalWrite(LED_PIN, HIGH);
     delay(500);
     digitalWrite(LED_PIN, LOW);
     delay(500);
   }

**MicroPython Code**

.. code-block:: python

   from machine import Pin
   import time

   # Define LED pin (check your shield pinout)
   led = Pin(13, Pin.OUT)

   while True:
       led.on()
       time.sleep(0.5)
       led.off()
       time.sleep(0.5)


Testing Peripherals
--------------------

**Buttons**

The shield includes 4 buttons for user input. Test them with:

.. code-block:: cpp

   #define BUTTON_PIN 5  // Adjust to your button pin

   void setup() {
     Serial.begin(115200);
     pinMode(BUTTON_PIN, INPUT_PULLUP);
   }

   void loop() {
     if (digitalRead(BUTTON_PIN) == LOW) {
       Serial.println("Button pressed!");
       delay(200);  // Simple debounce
     }
   }

**Buzzer**

Test the PWM buzzer:

.. code-block:: cpp

   #define BUZZER_PIN 9  // Adjust to your buzzer pin

   void setup() {
     pinMode(BUZZER_PIN, OUTPUT);
   }

   void loop() {
     tone(BUZZER_PIN, 1000);  // 1kHz tone
     delay(500);
     noTone(BUZZER_PIN);
     delay(500);
   }

**Potentiometer (ADC)**

Read analog values:

.. code-block:: cpp

   #define POT_PIN A0  // Adjust to your potentiometer pin

   void setup() {
     Serial.begin(115200);
   }

   void loop() {
     int value = analogRead(POT_PIN);
     Serial.print("Potentiometer value: ");
     Serial.println(value);
     delay(100);
   }


I2C Devices (QWIIC/STEMMA)
---------------------------

The shield provides 7 QWIIC-STEMMA compatible connectors for I2C devices.

**I2C Scanner Example**

.. code-block:: cpp

   #include <Wire.h>

   void setup() {
     Wire.begin();
     Serial.begin(115200);
     Serial.println("I2C Scanner");
   }

   void loop() {
     byte error, address;
     int nDevices = 0;

     Serial.println("Scanning...");

     for(address = 1; address < 127; address++ ) {
       Wire.beginTransmission(address);
       error = Wire.endTransmission();

       if (error == 0) {
         Serial.print("I2C device found at address 0x");
         if (address<16) Serial.print("0");
         Serial.println(address, HEX);
         nDevices++;
       }
     }
     
     if (nDevices == 0)
       Serial.println("No I2C devices found");
     else
       Serial.println("Scan complete");

     delay(5000);
   }


OLED Display
------------

The shield includes a 128x64 I2C OLED display.

**Required Library**

Install the Adafruit SSD1306 library via Arduino Library Manager.

**Example Code**

.. code-block:: cpp

   #include <Wire.h>
   #include <Adafruit_GFX.h>
   #include <Adafruit_SSD1306.h>

   #define SCREEN_WIDTH 128
   #define SCREEN_HEIGHT 64
   #define OLED_RESET -1
   
   Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);

   void setup() {
     if(!display.begin(SSD1306_SWITCHCAPVCC, 0x3C)) {
       Serial.println("SSD1306 allocation failed");
       for(;;);
     }
     
     display.clearDisplay();
     display.setTextSize(2);
     display.setTextColor(SSD1306_WHITE);
     display.setCursor(0,0);
     display.println("DevLab");
     display.println("Multi Hub");
     display.display();
   }

   void loop() {
     // Your code here
   }


Relay Control
-------------

Control the 2 relay modules:

.. code-block:: cpp

   #define RELAY1_PIN 7  // Adjust to your relay pins
   #define RELAY2_PIN 8

   void setup() {
     pinMode(RELAY1_PIN, OUTPUT);
     pinMode(RELAY2_PIN, OUTPUT);
     digitalWrite(RELAY1_PIN, LOW);  // Relay off
     digitalWrite(RELAY2_PIN, LOW);  // Relay off
   }

   void loop() {
     // Turn relay 1 on for 2 seconds
     digitalWrite(RELAY1_PIN, HIGH);
     delay(2000);
     digitalWrite(RELAY1_PIN, LOW);
     delay(1000);
     
     // Turn relay 2 on for 2 seconds
     digitalWrite(RELAY2_PIN, HIGH);
     delay(2000);
     digitalWrite(RELAY2_PIN, LOW);
     delay(1000);
   }

.. warning::
   Relays can switch high voltage/current. Use appropriate safety precautions and never exceed the relay ratings.


Next Steps
----------

- Explore example code in the ``software/examples/`` directory
- Check the pinout documentation for specific pin assignments
- Join the UNIT Electronics community for support and projects
- Visit the GitHub repository for updates and contributions


Troubleshooting
---------------

**No Power LEDs**

- Check USB-C cable and connection
- Verify microcontroller board is properly mounted
- Check external power supply if used

**I2C Devices Not Detected**

- Verify devices are properly connected to QWIIC connectors
- Check I2C pull-up resistors are present
- Run I2C scanner to detect device addresses
- Verify correct I2C pins for your platform

**Upload Failures**

- Check correct board selected in Arduino IDE
- Verify correct COM port selected
- Try pressing reset button before upload
- Check USB cable supports data transfer

**Display Not Working**

- Verify I2C address (usually 0x3C or 0x3D)
- Check display is properly connected
- Run I2C scanner to confirm device detection
- Verify correct library installed
