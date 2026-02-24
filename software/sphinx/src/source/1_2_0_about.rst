General Information
===================

The **DevLab Multi Hub Shield** is a modular shield expansion board designed to be compatible with various microcontroller platforms. It provides a comprehensive set of interfaces and features that make it ideal for prototyping, education, IoT projects, and automation applications.


Supported Microcontroller Platforms
------------------------------------

The shield is compatible with the following development board formats:

* **Pulsar** — UNIT Electronics flagship development board
* **Seeed Xiao** — Compact form factor (ESP32, RP2040, SAMD21, etc.)
* **Raspberry Pi Pico** — RP2040-based boards
* **Adafruit Feather** — Feather-compatible boards
* **ESP32 Devkit V4** — Standard ESP32 development boards
* **Mikro Bus** — MikroElektronika Click boards ecosystem


All platforms can be connected via dedicated pin headers that provide access to power, GPIO, I2C, SPI, UART, and ADC interfaces.

.. only:: html

    .. rubric:: Schematic Diagram

    .. raw:: html

      <div style="text-align: center;">
      <button style="background-color: rgb(226, 142, 15); color: white; border: none; padding: 10px 20px;"
      onclick="window.open('./_static/unit_pinout_v_1_0_0_ue0064_multishield_es.pdf', '_blank')">
      Download Schematics (PDF)
      </button>
      </div>
      <br>
      <iframe src="./_static/unit_pinout_v_1_0_0_ue0064_multishield_es.pdf" style="width:100%; height:900px;" frameborder="0"></iframe>

  

Supported Interfaces and Features
----------------------------------

The DevLab Multi Hub Shield integrates multiple interfaces and peripherals for versatile application development:

.. list-table:: Interface and Feature Overview
   :widths: 25 75
   :header-rows: 1

   * - Interface/Feature
     - Description
   * - **I2C**
     - Standard I2C bus for sensor and module communication
   * - **SPI**
     - High-speed serial peripheral interface
   * - **UART**
     - Serial communication interface
   * - **GPIO**
     - General purpose input/output pins
   * - **ADC**
     - Analog-to-digital converter inputs via potentiometer
   * - **LED Matrix**
     - 5x5 RGB LED matrix for visual feedback and displays
   * - **OLED Display**
     - I2C 128x64 OLED display with TFT configuration options
   * - **Relay Modules**
     - 2 relay modules for switching applications
   * - **PWM Outputs**
     - 2 PWM modules for motor control and LED dimming
   * - **Buzzer**
     - PWM-driven buzzer for audio feedback
   * - **Buttons**
     - 4 tactile buttons for user input
   * - **Status LEDs**
     - 4 indicator LEDs for feedback
   * - **DevLab Connectors**
     - 7 QWIIC-STEMMA compatible connectors (JST 1mm pitch)
   * - **Gravity Interface**
     - 4 Gravity connectors (2x4 and 2x3 pin configurations)
   * - **Breadboard Lines**
     - 4 breadboard-compatible expansion lines
   * - **Expansion Connector**
     - 20-pin header for additional modules and custom shields


Power Options
-------------

The DevLab Multi Hub Shield supports multiple power input methods:

- **USB-C**: Direct power via USB-C connector (5V)
- **3.3V Rail**: Low-voltage power supply for compatible modules
- **5V Rail**: Standard voltage for most peripherals
- **External Supply**: Dedicated input for external power sources

.. note::
   Power distribution is managed through on-board voltage regulators. Ensure proper voltage selection when connecting external modules.


DevLab Ecosystem Integration
-----------------------------

The shield features **7 QWIIC-STEMMA compatible connectors** (JST 1mm pitch) that enable seamless integration with the DevLab ecosystem and third-party I2C modules. These connectors support:

- Daisy-chaining multiple sensors and modules
- Hot-plugging capability
- Standardized pinout (VCC, GND, SDA, SCL)
- Compatibility with SparkFun QWIIC and Adafruit STEMMA QT systems


Relay Modules
-------------

Two integrated relay modules provide:

- Switching capability for AC/DC loads
- Isolated control signals
- LED indicators for relay status
- Screw terminal connections


PWM Interfaces
--------------

Two dedicated PWM outputs allow:

- Motor speed control
- Servo positioning
- LED brightness control
- Variable frequency signal generation


Display Options
---------------

**LED Matrix (5x5 RGB)**

- Individual addressable RGB LEDs
- Visual feedback and simple graphics
- Animation capabilities
- Programmable via GPIO

**OLED Display (128x64)**

- I2C interface
- High contrast ratio
- Text and graphics support
- TFT configuration options for expanded functionality


Gravity Connectors
------------------

Four Gravity-compatible connectors (DFRobot standard) provide:

- **2x4 pin connectors** (2 units): For digital/analog sensors
- **2x3 pin connectors** (2 units): For compact sensor modules
- Color-coded for easy identification
- Wide sensor compatibility


Expansion Options
-----------------

**Breadboard Lines**

4 breadboard-compatible lines with standard 2.54mm pitch for:

- Custom circuit prototyping
- Temporary connections
- Wire jumper access to signals

**20-Pin Expansion Connector**

High-density connector providing:

- Access to all major bus signals
- Power distribution
- GPIO expansion
- Stacking capability for additional shields


Board Specifications
--------------------

.. list-table:: Technical Specifications
  :widths: 30 70
  :header-rows: 1

  * - Parameter
    - Value
  * - **Compatible Formats**
    - Pulsar, Xiao, Pi Pico, Feather, Devkit V4, Mikro Bus
  * - **Operating Voltage**
    - 3.3V / 5V (selectable)
  * - **Input Power**
    - USB-C 5V, External 3.3V-5V
  * - **I2C Connectors**
    - 7x QWIIC-STEMMA (JST 1mm)
  * - **Gravity Connectors**
    - 4x (2x4 pins + 2x3 pins)
  * - **Relays**
    - 2x electromechanical relays
  * - **PWM Outputs**
    - 2 channels
  * - **LEDs**
    - 4 status LEDs + 5x5 RGB matrix
  * - **Buttons**
    - 4 tactile push buttons
  * - **Display**
    - 128x64 I2C OLED
  * - **Expansion**
    - 20-pin header + 4 breadboard lines


