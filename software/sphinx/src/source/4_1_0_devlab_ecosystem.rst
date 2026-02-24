devlab ecosystem integration
=============================

devlab concept
--------------

discover unit electronics' devlab ecosystem, its universal connector, and how it facilitates rapid and modular prototyping.

introduction
~~~~~~~~~~~~

devlab is a modular ecosystem proposed by unit electronics, geared towards rapid prototyping, immediate assembly and flexibility in electronic design.

its purpose is to accelerate hardware development through integrated modules, sensors, and tools that share a common interconnection standard, without imposing restrictions on the physical form factor of the boards. the key element of the devlab ecosystem is the universal 1.0 mm, 4-pin jst sh connector, combined with a development part number nomenclature, which formally identifies products belonging to the ecosystem.

definition
~~~~~~~~~~

devlab is a development ecosystem composed of electronic modules, sensors, boards, and accessories that meet these essential principles:

.. list-table:: devlab core principles
   :widths: 30 70
   :header-rows: 1

   * - feature
     - definition
   * - **rapid prototyping**
     - immediate integration with minimal configuration
   * - **simple assembly**
     - direct connection between modules using a standard connector
   * - **pcb free format**
     - there is no mandatory size or shape

devlab connector
----------------

the devlab universal connector is based on a 4-pin jst sh 1.0mm and is used as a common interface for communication, control, and power.

.. note::
   the devlab connector is multiprotocol, but not simultaneous; this means that only one protocol should be used per connector at a time.

compatible protocols
~~~~~~~~~~~~~~~~~~~~

the connector allows operation with various protocols depending on the module:

- **i2c** (sda/scl)
- **uart** (rx/tx)
- **pwm**
- **analog inputs** (adc)
- **multipurpose gpio**
- **rgb led control**
- **swd/io** for programming and debugging

purpose
~~~~~~~

the devlab connector functions as a multiprotocol interface, allowing:

- connect sensors
- power modules
- pwm outputs
- converters
- programmable devices
- expanders or multiplexers
- purification systems

.. warning::
   **technical note**: the devlab connector is multiprotocol, but not simultaneous. only one protocol should be used per connector at a time; many of the signals are not compatible with each other when mixed in the same module or cable. the function of the connector will depend on the design of each module and the pin assignment made on the main board.

official recommendation
~~~~~~~~~~~~~~~~~~~~~~~~

to avoid electrical or communication conflicts, it is recommended to use a single protocol for each devlab connector, especially when the connected modules come from different families (i2c, uart, pwm, swd, etc.).

this rule ensures the integrity of the ecosystem, protects devices, and guarantees predictable and safe operation.

design philosophy
-----------------

devlab does not define a single form factor like arduino r3, feather, or raspberry pi pico. devlab modules can have any mechanical design: round, rectangular, miniature, large-scale, and intended for assembly into end products.

**the only mandatory standard is to include the devlab connector.**

exceptions
~~~~~~~~~~

there are boards that use the devlab connector, but they do not officially belong to the ecosystem because their development part number does not include the devlab nomenclature.

.. list-table:: compatible non-devlab boards
   :widths: 30 70
   :header-rows: 1

   * - development part number
     - product
   * - ue0071
     - pulsar h2 development board
   * - ue0072
     - touch dot s3
   * - ue0081
     - jun r3 development board

first generation
~~~~~~~~~~~~~~~~

the first implementation of the devlab concept occurred with the dualmcu family, considered the first generation, where the following was introduced:

- the use of the devlab universal connector
- the integration of multiple microcontrollers
- the multi-protocol philosophy
- compatibility with existing formats (nano, r3, circular)
- the concept of interconnectable independent modules

official identification
-----------------------

for a product to be officially devlab-certified, it must:

.. list-table:: certification requirements
   :widths: 15 85
   :header-rows: 1

   * - number
     - requirement
   * - 1
     - include the word "devlab" in your official name
   * - 2
     - be registered with a development part number within the ue00xx series
   * - 3
     - integrate the devlab connector
   * - 4
     - maintain the modular, multi-protocol and rapid prototyping philosophy

qwiic/stemma qt compatibility
------------------------------

the devlab multi hub shield features 7 qwiic-stemma compatible connectors (jst 1mm pitch) that enable seamless integration with the devlab ecosystem and third-party i2c modules. this standardized connector system allows for tool-free, daisy-chainable connections to hundreds of sensors and modules.

what is qwiic/stemma qt?
~~~~~~~~~~~~~~~~~~~~~~~~

qwiic (developed by sparkfun) and stemma qt (developed by adafruit) are compatible i2c connector standards that share:

- same jst sh 4-pin connector (1mm pitch)
- identical pinout
- cross-compatible modules
- standardized i2c communication

benefits
~~~~~~~~

- no soldering required
- hot-pluggable connections
- daisy-chain multiple devices
- standardized voltage (3.3v)
- polarity protection
- wide ecosystem compatibility

technical specifications
-------------------------

.. list-table:: qwiic/stemma specifications
   :header-rows: 1
   :widths: 30 70

   * - parameter
     - value
   * - **connector type**
     - jst sh 1mm pitch
   * - **number of connectors**
     - 7 ports
   * - **pins**
     - 4 (vcc, gnd, sda, scl)
   * - **voltage**
     - 3.3v
   * - **current per port**
     - 500ma max (total current shared)
   * - **i2c speed**
     - up to 400 khz (fast mode)
   * - **cable length**
     - up to 1m recommended
   * - **daisy-chain**
     - unlimited (limited by i2c address space)

pinout
------

standard 4-pin qwiic/stemma qt pinout:

.. list-table:: connector pinout
   :widths: 15 20 35 30
   :header-rows: 1

   * - pin
     - signal
     - function
     - wire color
   * - 1
     - gnd
     - ground
     - black
   * - 2
     - 3.3v
     - power supply
     - red
   * - 3
     - sda
     - i2c data
     - blue
   * - 4
     - scl
     - i2c clock
     - yellow

**color coding**

standard cable colors:
- **black**: ground
- **red**: 3.3v power
- **blue**: i2c data (sda)
- **yellow**: i2c clock (scl)

Compatible Modules
------------------

The shield is compatible with hundreds of QWIIC and STEMMA QT modules:

Environmental Sensors
~~~~~~~~~~~~~~~~~~~~~

.. list-table:: Popular Environmental Sensors
   :header-rows: 1
   :widths: 35 35 30

   * - Module
     - Measurements
     - I2C Address
   * - BME280
     - Temperature, Humidity, Pressure
     - 0x76/0x77
   * - BMP388
     - Pressure, Temperature
     - 0x76/0x77
   * - SHT31
     - Temperature, Humidity
     - 0x44/0x45
   * - ENS160
     - Air Quality (eCO2, TVOC)
     - 0x52/0x53
   * - VEML7700
     - Ambient Light
     - 0x10

Motion and Orientation
~~~~~~~~~~~~~~~~~~~~~~

.. list-table:: Motion Sensors
   :header-rows: 1
   :widths: 35 35 30

   * - Module
     - Features
     - I2C Address
   * - MPU6050
     - 6-axis IMU (Accel + Gyro)
     - 0x68/0x69
   * - BNO085
     - 9-axis IMU with fusion
     - 0x4A/0x4B
   * - LIS3DH
     - 3-axis Accelerometer
     - 0x18/0x19
   * - VL53L1X
     - Time-of-Flight Distance
     - 0x29

Display Modules
~~~~~~~~~~~~~~~

.. list-table:: Display Options
   :header-rows: 1
   :widths: 35 35 30

   * - Module
     - Type
     - I2C Address
   * - SSD1306
     - 128x64 OLED
     - 0x3C/0x3D
   * - SH1107
     - 128x128 OLED
     - 0x3C/0x3D
   * - HT16K33
     - LED Matrix Driver
     - 0x70-0x77

Input/Output Expansion
~~~~~~~~~~~~~~~~~~~~~~

.. list-table:: I/O Modules
   :header-rows: 1
   :widths: 35 35 30

   * - Module
     - Features
     - I2C Address
   * - PCA9685
     - 16-channel PWM
     - 0x40-0x7F
   * - MCP23017
     - 16-bit GPIO Expander
     - 0x20-0x27
   * - ADS1115
     - 16-bit ADC (4-channel)
     - 0x48-0x4B

Other Useful Modules
~~~~~~~~~~~~~~~~~~~~

- GPS modules (PA1010D)
- RTC (Real-Time Clock) modules
- EEPROM storage modules
- DAC (Digital-to-Analog) modules
- Color sensors (TCS34725)
- Gesture sensors (APDS9960)

Daisy-Chaining
--------------

**Concept**

Multiple QWIIC modules can be connected in series using the dual connectors on each module:

.. code-block:: text

   Shield → Module 1 → Module 2 → Module 3 → ...
   
   Each module has 2 QWIIC ports for daisy-chaining

**Configuration Example**

.. code-block:: text

   DevLab Shield
        │
        ├── BME280 (Temp/Humidity/Pressure)
        │     └── SSD1306 (OLED Display)
        │           └── MPU6050 (IMU)
        │
        ├── VL53L1X (Distance Sensor)
        │
        └── ADS1115 (ADC Module)

**Advantages**

- Single I2C bus for all devices
- Minimal wiring
- Easy to add/remove modules
- No breadboard needed
- Clean installations

Programming Examples
--------------------

Scanning for Devices
~~~~~~~~~~~~~~~~~~~~

.. code-block:: cpp

   #include <Wire.h>
   
   void setup() {
     Wire.begin();
     Serial.begin(115200);
     delay(1000);
     Serial.println("I2C Scanner");
   }
   
   void loop() {
     byte error, address;
     int nDevices = 0;
   
     Serial.println("Scanning...");
   
     for(address = 1; address < 127; address++) {
       Wire.beginTransmission(address);
       error = Wire.endTransmission();
   
       if (error == 0) {
         Serial.print("Device found at 0x");
         if (address < 16) Serial.print("0");
         Serial.println(address, HEX);
         nDevices++;
       }
     }
   
     if (nDevices == 0)
       Serial.println("No devices found");
     else
       Serial.println("Scan complete");
   
     delay(5000);
   }

Multi-Sensor Example
~~~~~~~~~~~~~~~~~~~~

.. code-block:: cpp

   #include <Wire.h>
   #include <Adafruit_BME280.h>
   #include <Adafruit_MPU6050.h>
   #include <Adafruit_SSD1306.h>
   
   Adafruit_BME280 bme;
   Adafruit_MPU6050 mpu;
   Adafruit_SSD1306 display(128, 64, &Wire, -1);
   
   void setup() {
     Wire.begin();
     Serial.begin(115200);
     
     // Initialize sensors
     if (!bme.begin(0x76)) {
       Serial.println("BME280 not found!");
     }
     
     if (!mpu.begin()) {
       Serial.println("MPU6050 not found!");
     }
     
     if (!display.begin(SSD1306_SWITCHCAPVCC, 0x3C)) {
       Serial.println("Display not found!");
     }
     
     display.clearDisplay();
     display.setTextSize(1);
     display.setTextColor(SSD1306_WHITE);
   }
   
   void loop() {
     // Read BME280
     float temp = bme.readTemperature();
     float humidity = bme.readHumidity();
     float pressure = bme.readPressure() / 100.0F;
     
     // Read MPU6050
     sensors_event_t a, g, temp_event;
     mpu.getEvent(&a, &g, &temp_event);
     
     // Display on OLED
     display.clearDisplay();
     display.setCursor(0, 0);
     display.print("Temp: ");
     display.print(temp, 1);
     display.println(" C");
     display.print("Hum: ");
     display.print(humidity, 1);
     display.println(" %");
     display.print("AccX: ");
     display.println(a.acceleration.x, 1);
     display.display();
     
     delay(1000);
   }

MicroPython Example
~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from machine import Pin, I2C
   import bme280
   import ssd1306
   import time
   
   # Initialize I2C
   i2c = I2C(0, scl=Pin(22), sda=Pin(21))
   
   # Scan for devices
   devices = i2c.scan()
   print("I2C devices found:", [hex(d) for d in devices])
   
   # Initialize sensors
   bme = bme280.BME280(i2c=i2c, address=0x76)
   oled = ssd1306.SSD1306_I2C(128, 64, i2c, addr=0x3C)
   
   while True:
       # Read sensor
       temp, pressure, humidity = bme.read_compensated_data()
       
       # Display
       oled.fill(0)
       oled.text(f"Temp: {temp/100:.1f}C", 0, 0)
       oled.text(f"Hum: {humidity/1024:.1f}%", 0, 10)
       oled.show()
       
       time.sleep(1)

Best Practices
--------------

**Addressing Conflicts**

- Check I2C addresses before connecting multiple modules
- Some modules allow address configuration via jumpers
- Use I2C scanner to verify all devices
- Document your module addresses

**Cable Management**

- Keep cables as short as practical
- Avoid running I2C cables near power lines
- Use cable clips for organization
- Label cables for easier troubleshooting

**Power Considerations**

- Calculate total current draw of all modules
- Don't exceed 500mA total on QWIIC bus
- Use external power for high-current modules
- Consider voltage drops on long cables

**Reliability**

- Secure connectors to prevent disconnection
- Test each module individually first
- Update firmware/libraries regularly
- Use quality QWIIC cables

Common Issues and Solutions
---------------------------

**Device Not Detected**

- Verify cable connections
- Check module power LED
- Run I2C scanner
- Try different QWIIC port
- Check I2C pull-up resistors

**Communication Errors**

- Reduce cable length
- Lower I2C clock speed
- Check for address conflicts
- Verify power supply stability
- Add decoupling capacitors

**Intermittent Operation**

- Secure loose connections
- Check cable quality
- Verify power supply capacity
- Reduce electromagnetic interference
- Test individual modules

Project Ideas
-------------

Weather Station
~~~~~~~~~~~~~~~

Modules needed:
- BME280 (Temperature, Humidity, Pressure)
- VEML7700 (Light sensor)
- SSD1306 (Display)
- RTC module (Time stamping)

Motion Tracker
~~~~~~~~~~~~~~

Modules needed:
- MPU6050 or BNO085 (IMU)
- GPS module
- MicroSD module (Data logging)
- Display module

Air Quality Monitor
~~~~~~~~~~~~~~~~~~~

Modules needed:
- ENS160 (Air quality sensor)
- BME280 (Environmental data)
- SSD1306 (Display)
- RGB LED module (Visual alerts)

Robotic Sensor Array
~~~~~~~~~~~~~~~~~~~~~

Modules needed:
- Multiple VL53L1X (Distance sensors)
- IMU module (Orientation)
- GPIO expander (Control outputs)
- PWM driver (Motor control)

Ecosystem Resources
-------------------

**SparkFun QWIIC**
- Product catalog: https://www.sparkfun.com/qwiic
- Tutorials and guides
- Open-source designs

**Adafruit STEMMA QT**
- Product catalog: https://www.adafruit.com/category/620
- Learn guides
- CircuitPython libraries

**Third-Party Modules**
- DFRobot Gravity sensors
- Seeed Grove I2C modules
- Many compatible designs
