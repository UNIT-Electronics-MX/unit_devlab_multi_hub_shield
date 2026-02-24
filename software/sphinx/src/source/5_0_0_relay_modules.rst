Relay Modules
=============

Overview
--------

The DevLab Multi Hub Shield integrates 2 electromechanical relay modules that enable control of high-voltage and high-current loads. These relays act as electrically isolated switches, allowing low-voltage microcontrollers to safely control AC/DC appliances, motors, lights, and other power devices.

Technical Specifications
------------------------

.. list-table:: Relay Specifications
   :header-rows: 1
   :widths: 30 70

   * - Parameter
     - Value
   * - **Number of Relays**
     - 2 independent modules
   * - **Type**
     - SPDT (Single Pole Double Throw)
   * - **Coil Voltage**
     - 5V DC
   * - **Contact Rating**
     - 10A @ 250VAC, 10A @ 30VDC
   * - **Control Signal**
     - 3.3V/5V logic compatible
   * - **Isolation**
     - Optically isolated control
   * - **Switching Time**
     - <10ms
   * - **Terminals**
     - Screw terminals
   * - **Indicators**
     - LED status per relay

Relay Construction
------------------

**SPDT Configuration**

Each relay has three terminals:

- **COM** (Common): Input terminal
- **NO** (Normally Open): Closed when relay is activated
- **NC** (Normally Closed): Open when relay is activated

.. code-block:: text

   Relay OFF (Deenergized):
   COM ──┬── NC (connected)
         └── NO (disconnected)
   
   Relay ON (Energized):
   COM ──┬── NC (disconnected)
         └── NO (connected)

**Terminal Layout**

.. code-block:: text

   ┌─────────────────┐
   │  COM  NC   NO   │  Relay 1
   │   ●    ●    ●   │
   └─────────────────┘
   
   ┌─────────────────┐
   │  COM  NC   NO   │  Relay 2
   │   ●    ●    ●   │
   └─────────────────┘

Control Interface
-----------------

**Digital Control**

Each relay is controlled by a single GPIO pin:

- **HIGH (1)**: Relay energized (NO closed, NC open)
- **LOW (0)**: Relay de-energized (NO open, NC closed)

**Pin Assignment**

- **Relay 1 Control Pin**: GPIO (platform specific)
- **Relay 2 Control Pin**: GPIO (platform specific)

**Status LEDs**

- Each relay has an onboard LED indicator
- LED ON: Relay energized
- LED OFF: Relay de-energized

Programming Examples
--------------------

Basic Control (Arduino)
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: cpp

   // Define relay control pins
   #define RELAY1_PIN 7
   #define RELAY2_PIN 8
   
   void setup() {
     pinMode(RELAY1_PIN, OUTPUT);
     pinMode(RELAY2_PIN, OUTPUT);
     
     // Initialize relays to OFF state
     digitalWrite(RELAY1_PIN, LOW);
     digitalWrite(RELAY2_PIN, LOW);
   }
   
   void loop() {
     // Turn relay 1 ON for 2 seconds
     digitalWrite(RELAY1_PIN, HIGH);
     delay(2000);
     digitalWrite(RELAY1_PIN, LOW);
     delay(1000);
     
     // Turn relay 2 ON for 2 seconds
     digitalWrite(RELAY2_PIN, HIGH);
     delay(2000);
     digitalWrite(RELAY2_PIN, LOW);
     delay(1000);
   }

Timed Control
~~~~~~~~~~~~~

.. code-block:: cpp

   unsigned long relay1Timer = 0;
   unsigned long relay2Timer = 0;
   bool relay1State = false;
   bool relay2State = false;
   
   void setup() {
     pinMode(RELAY1_PIN, OUTPUT);
     pinMode(RELAY2_PIN, OUTPUT);
     digitalWrite(RELAY1_PIN, LOW);
     digitalWrite(RELAY2_PIN, LOW);
   }
   
   void loop() {
     unsigned long currentTime = millis();
     
     // Relay 1: ON for 5 seconds every 10 seconds
     if (!relay1State && currentTime - relay1Timer >= 10000) {
       digitalWrite(RELAY1_PIN, HIGH);
       relay1State = true;
       relay1Timer = currentTime;
     } else if (relay1State && currentTime - relay1Timer >= 5000) {
       digitalWrite(RELAY1_PIN, LOW);
       relay1State = false;
       relay1Timer = currentTime;
     }
     
     // Relay 2: Similar logic with different timing
   }

Button Control
~~~~~~~~~~~~~~

.. code-block:: cpp

   #define BUTTON1_PIN 2
   #define BUTTON2_PIN 3
   #define RELAY1_PIN 7
   #define RELAY2_PIN 8
   
   bool relay1State = false;
   bool relay2State = false;
   
   void setup() {
     pinMode(BUTTON1_PIN, INPUT_PULLUP);
     pinMode(BUTTON2_PIN, INPUT_PULLUP);
     pinMode(RELAY1_PIN, OUTPUT);
     pinMode(RELAY2_PIN, OUTPUT);
     
     digitalWrite(RELAY1_PIN, LOW);
     digitalWrite(RELAY2_PIN, LOW);
   }
   
   void loop() {
     // Toggle relay 1 on button 1 press
     if (digitalRead(BUTTON1_PIN) == LOW) {
       delay(50);  // Debounce
       if (digitalRead(BUTTON1_PIN) == LOW) {
         relay1State = !relay1State;
         digitalWrite(RELAY1_PIN, relay1State);
         while(digitalRead(BUTTON1_PIN) == LOW);  // Wait for release
       }
     }
     
     // Similar logic for relay 2
   }

MicroPython Example
~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from machine import Pin
   import time
   
   # Initialize relay pins
   relay1 = Pin(7, Pin.OUT)
   relay2 = Pin(8, Pin.OUT)
   
   # Turn relays off initially
   relay1.off()
   relay2.off()
   
   while True:
       # Relay 1 on for 2 seconds
       relay1.on()
       time.sleep(2)
       relay1.off()
       time.sleep(1)
       
       # Relay 2 on for 2 seconds
       relay2.on()
       time.sleep(2)
       relay2.off()
       time.sleep(1)

Wiring Examples
---------------

Controlling AC Lamp (120V/220V)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: text

   AC Source (Hot) ──→ COM
                       NO ──→ Lamp ──→ AC Source (Neutral)
                       NC ──→ (not connected)
   
   When relay ON: Lamp receives power
   When relay OFF: Lamp is disconnected

**IMPORTANT SAFETY**: Always consult a licensed electrician for AC wiring!

Controlling DC Motor
~~~~~~~~~~~~~~~~~~~~

.. code-block:: text

   Battery (+) ──→ COM
                   NO ──→ Motor (+)
                   NC ──→ (not connected)
   Motor (-) ──→ Battery (-)
   
   When relay ON: Motor runs
   When relay OFF: Motor stops

Reversing Motor Direction
~~~~~~~~~~~~~~~~~~~~~~~~~~

Using both relays with H-bridge configuration:

.. code-block:: text

   Relay 1 controls motor positive connection
   Relay 2 controls motor negative connection
   
   Forward:  Relay1=ON,  Relay2=OFF
   Reverse:  Relay1=OFF, Relay2=ON
   Brake:    Relay1=OFF, Relay2=OFF

Safety Considerations
---------------------

**Electrical Safety**

.. warning::
   Relays can switch dangerous voltages!
   
   - Never touch relay terminals when powered
   - Use appropriate wire gauge for current
   - Install proper fuses and circuit breakers
   - Follow local electrical codes
   - Consider hiring a licensed electrician for AC wiring

**Load Considerations**

- Do not exceed 10A contact rating
- Use inductive load suppression for motors
- Consider relay contact bounce
- Account for surge currents during switching
- Use appropriate wire insulation for voltage

**Inductive Load Protection**

For inductive loads (motors, solenoids, relays):

- Add flyback diode across DC loads
- Use snubber circuit for AC loads
- Prevents voltage spikes
- Protects relay contacts
- Extends relay lifetime

.. code-block:: text

   DC Motor Protection:
   Motor ──┬──→ Relay
           │
         Diode (1N4007 or similar)
           ↓
          GND

Practical Applications
----------------------

Home Automation
~~~~~~~~~~~~~~~

- Light control
- Fan control
- Appliance switching
- Irrigation systems
- Garage door control

Industrial Applications
~~~~~~~~~~~~~~~~~~~~~~~

- Motor control
- Pump control
- Valve actuation
- Heating element control
- Safety interlocks

IoT Projects
~~~~~~~~~~~~

- Remote power control
- Scheduled device control
- Sensor-triggered switching
- Energy monitoring systems
- Smart home integration

Educational Projects
~~~~~~~~~~~~~~~~~~~~

- Learning about relays and switching
- Building automation systems
- Understanding isolation
- Control system design
- Safety system implementation

Advanced Features
-----------------

PWM Control
~~~~~~~~~~~

.. code-block:: cpp

   // Variable duty cycle control
   void setup() {
     pinMode(RELAY1_PIN, OUTPUT);
   }
   
   void loop() {
     // 50% duty cycle (on 500ms, off 500ms)
     digitalWrite(RELAY1_PIN, HIGH);
     delay(500);
     digitalWrite(RELAY1_PIN, LOW);
     delay(500);
   }

**Applications:**
- Simple speed control for DC motors
- Heater temperature regulation
- Light dimming (not recommended for AC)

Interlock Logic
~~~~~~~~~~~~~~~

.. code-block:: cpp

   void setRelays(bool r1, bool r2) {
     // Ensure both relays are never on simultaneously
     if (r1 && r2) {
       // Conflict - turn both off
       digitalWrite(RELAY1_PIN, LOW);
       digitalWrite(RELAY2_PIN, LOW);
       return;
     }
     
     digitalWrite(RELAY1_PIN, r1);
     digitalWrite(RELAY2_PIN, r2);
   }

Failsafe Operation
~~~~~~~~~~~~~~~~~~

.. code-block:: cpp

   unsigned long lastCommandTime = 0;
   const unsigned long TIMEOUT = 5000;  // 5 seconds
   
   void loop() {
     if (millis() - lastCommandTime > TIMEOUT) {
       // No command received, turn off relays
       digitalWrite(RELAY1_PIN, LOW);
       digitalWrite(RELAY2_PIN, LOW);
     }
   }

Troubleshooting
---------------

**Relay Not Switching**

- Verify control signal (should be HIGH/3.3V or 5V)
- Check power supply to relay module
- Test with multimeter on COM and NO/NC
- Listen for clicking sound when switching
- Check LED indicator

**Relay Clicking but Not Switching Load**

- Verify load voltage and current are within ratings
- Check wiring connections
- Test relay contacts with multimeter
- Look for burned or welded contacts
- Replace relay if damaged

**Intermittent Operation**

- Check loose wire connections
- Verify stable power supply
- Look for electromagnetic interference
- Check control signal integrity
- Ensure proper grounding

**Relay Stays On**

- Check control signal is going LOW
- Inspect for stuck contacts
- Verify relay is not damaged
- Check for control circuit faults
- Replace relay module if needed

Specifications Summary
----------------------

.. list-table:: Operating Limits
   :header-rows: 1
   :widths: 40 30 30

   * - Parameter
     - Maximum
     - Notes
   * - AC Voltage
     - 250V
     - Use proper insulation
   * - DC Voltage
     - 30V
     - Lower than AC rating
   * - Current
     - 10A
     - Continuous rating
   * - Switching Frequency
     - 300 ops/min
     - Mechanical limitation
   * - Contact Resistance
     - <100mΩ
     - When closed
   * - Insulation Resistance
     - >100MΩ
     - When open
   * - Operating Temperature
     - -10°C to +55°C
     - Typical range
