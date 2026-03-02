Platform Compatibility
======================

Overview
--------

The DevLab Multi Hub Shield is designed with universal compatibility in mind, supporting multiple popular microcontroller development board formats. This flexibility allows developers to use their preferred platform while accessing the shield's comprehensive feature set.

Supported Platforms
-------------------

Pulsar (UNIT Electronics)
~~~~~~~~~~~~~~~~~~~~~~~~~

**Description**

The Pulsar is UNIT Electronics' flagship development board featuring:

- ESP32-S3 dual-core processor
- Built-in Wi-Fi and Bluetooth
- USB-C connectivity
- Multiple GPIO pins

**Pin Compatibility**

The shield provides dedicated pin headers compatible with the Pulsar's pinout, ensuring full access to:

- I2C bus (SDA, SCL)
- SPI bus (MOSI, MISO, SCK, CS)
- UART (TX, RX)
- Analog inputs
- Digital GPIO pins

**Example Applications**

- IoT sensor hubs with cloud connectivity
- Wireless automation controllers
- Data logging with remote access
- Smart home integration

Seeed Xiao Series
~~~~~~~~~~~~~~~~~

**Description**

The Xiao series represents ultra-compact development boards with various microcontroller options:

- **Xiao ESP32-C3**: Wi-Fi and Bluetooth LE
- **Xiao ESP32-S3**: Dual-core with AI acceleration
- **Xiao RP2040**: Dual-core ARM Cortex-M0+
- **Xiao SAMD21**: ARM Cortex-M0+ for low power

**Pin Compatibility**

All Xiao variants share the same pinout, making the shield compatible with:

- 14-pin header configuration
- 3.3V logic level
- I2C, SPI, UART interfaces
- Multiple ADC channels

**Power Considerations**

The shield provides voltage regulation compatible with Xiao's power requirements. When using battery-powered Xiao boards, the shield can operate from USB-C or external power.

**Example Applications**

- Wearable sensor platforms
- Battery-powered environmental monitors
- Compact automation controllers
- Educational electronics projects

Raspberry Pi Pico
~~~~~~~~~~~~~~~~~

**Description**

The Raspberry Pi Pico features the RP2040 microcontroller:

- Dual-core ARM Cortex-M0+ @ 133MHz
- 264KB SRAM
- Flexible GPIO with PIO state machines
- MicroPython and C/C++ support

**Pin Compatibility**

The shield's Pico-compatible socket provides access to:

- 40-pin dual-row header
- 3.3V and 5V power rails
- Ground connections
- All GPIO pins including SPI, I2C, UART, PWM, ADC

**Unique Features**

The RP2040's PIO (Programmable I/O) feature can be used with the shield to:

- Implement custom protocols for the LED matrix
- Create precise timing for relay control
- Generate custom waveforms for sensors

**Example Applications**

- Real-time data acquisition systems
- LED matrix displays and animations
- Multi-sensor environmental monitoring
- Educational robotics platforms

Adafruit Feather
~~~~~~~~~~~~~~~~

**Description**

The Feather format is a popular ecosystem with many variants:

- **Feather ESP32**: Wi-Fi and Bluetooth
- **Feather M4 Express**: ARM Cortex-M4 with FPU
- **Feather nRF52840**: Bluetooth LE
- **Feather RP2040**: Dual-core RP2040

**Pin Compatibility**

The shield supports the standard Feather pinout:

- 28-pin configuration
- LiPo battery charging support (varies by board)
- 3.3V logic level
- Standard I2C, SPI, UART pins

**Battery Operation**

Many Feather boards include built-in LiPo battery charging. The shield is designed to work with battery-powered Feather boards, making it ideal for portable applications.

**Example Applications**

- Portable weather stations
- Mobile data loggers
- Battery-powered automation
- Remote sensing applications

ESP32 Devkit V4
~~~~~~~~~~~~~~~

**Description**

The ESP32 Devkit V4 is a popular development board featuring:

- ESP32 dual-core processor
- Wi-Fi 802.11 b/g/n
- Bluetooth Classic and BLE
- Rich peripheral set

**Pin Compatibility**

The shield provides a socket compatible with the Devkit V4's 38-pin configuration:

- 5V and 3.3V power
- All GPIO pins
- Touch sensor pins
- ADC/DAC channels

**Networking Features**

The ESP32's networking capabilities combined with the shield enable:

- IoT sensor networks
- Web-based control interfaces
- MQTT data publishing
- Remote monitoring systems

**Example Applications**

- Smart home hubs
- Industrial IoT gateways
- Environmental monitoring stations
- Wireless sensor networks

Mikro Bus
~~~~~~~~~

**Description**

The Mikro Bus standard by MikroElektronika provides:

- Standardized pinout for Click boards
- Flexible module expansion
- Extensive ecosystem of add-on boards

**Pin Compatibility**

The shield includes Mikro Bus compatible sockets providing:

- SPI interface
- I2C interface
- UART interface
- PWM, Analog, Interrupt, and Reset pins
- 3.3V and 5V power options

**Ecosystem Integration**

With Mikro Bus compatibility, users can add:

- Communication modules (LoRa, cellular, etc.)
- Additional sensors
- Display modules
- Motor control boards

**Example Applications**

- Modular sensor systems
- Expandable control platforms
- Rapid prototyping environments
- Educational modular electronics

Pin Mapping and Configuration
------------------------------

General Pin Assignments
~~~~~~~~~~~~~~~~~~~~~~~

While specific pin numbers vary by platform, the shield maintains consistent functional assignments:

.. list-table:: Standard Pin Functions
   :header-rows: 1
   :widths: 25 75

   * - Function
     - Description
   * - **I2C SDA**
     - Primary I2C data line for OLED, QWIIC connectors
   * - **I2C SCL**
     - Primary I2C clock line
   * - **SPI MOSI**
     - SPI Master Out Slave In
   * - **SPI MISO**
     - SPI Master In Slave Out
   * - **SPI SCK**
     - SPI Clock
   * - **SPI CS**
     - SPI Chip Select (multiple available)
   * - **UART TX**
     - Serial transmit
   * - **UART RX**
     - Serial receive
   * - **ADC**
     - Analog input from potentiometer
   * - **PWM**
     - PWM outputs for buzzer and modules
   * - **GPIO**
     - Digital I/O for buttons, LEDs, relays

Voltage Level Considerations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**3.3V Platforms**

- Xiao series
- Raspberry Pi Pico
- Feather boards (most)

**5V Tolerant**

- Some ESP32 boards
- Platform-specific checking required

**Level Shifting**

The shield includes appropriate level shifting where necessary to protect 3.3V platforms while interfacing with 5V peripherals.

Software Support
----------------

Arduino IDE
~~~~~~~~~~~

All supported platforms can be programmed using Arduino IDE with appropriate board packages:

- ESP32 boards package
- RP2040 boards package
- SAMD boards package
- Third-party board support

MicroPython
~~~~~~~~~~~

MicroPython support available for:

- Raspberry Pi Pico
- ESP32 variants
- SAMD21/51 (limited)

CircuitPython
~~~~~~~~~~~~~

Adafruit's CircuitPython supports:

- Feather boards
- Xiao SAMD21
- RP2040-based boards

Platform Selection Guide
------------------------

Choose your platform based on:

**For Wi-Fi/Bluetooth Projects**

- ESP32 Devkit V4 (best range and stability)
- Xiao ESP32-S3 (compact, AI features)
- Feather ESP32 (battery-friendly)

**For Low Power Applications**

- Xiao SAMD21
- Feather M0
- Pico with sleep modes

**For High Performance**

- ESP32-S3 (dual-core + AI)
- Feather M4 Express (FPU)
- Pico (PIO state machines)

**For Beginners**

- Raspberry Pi Pico (excellent documentation)
- Arduino-compatible boards
- Xiao series (simple, affordable)

**For Professional/Industrial**

- ESP32 Devkit (robust, well-supported)
- Feather (reliable, ecosystem)
- Mikro Bus (modular, expandable)
