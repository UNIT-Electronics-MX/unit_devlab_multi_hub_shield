LED Matrix
==========

Overview
--------

The DevLab Multi Hub Shield features a 5x5 RGB LED matrix that provides visual feedback, simple graphics display, and animation capabilities. Each LED is individually addressable and can display any color in the RGB spectrum.

Technical Specifications
------------------------

.. list-table:: LED Matrix Specifications
   :header-rows: 1
   :widths: 30 70

   * - Parameter
     - Value
   * - **Configuration**
     - 5x5 matrix (25 LEDs total)
   * - **LED Type**
     - RGB (Red, Green, Blue)
   * - **Control**
     - Individually addressable
   * - **Colors**
     - 16.7 million colors (24-bit)
   * - **Brightness**
     - Adjustable per LED
   * - **Protocol**
     - GPIO-controlled or addressable (WS2812/SK6812 compatible)
   * - **Voltage**
     - 5V supply for LEDs
   * - **Current**
     - ~60mA per LED at full white

Features
--------

**Individual Control**

Each of the 25 LEDs can be:
- Set to any RGB color independently
- Adjusted for brightness
- Turned on or off individually
- Updated at high refresh rates

**Color Capabilities**

- Full RGB spectrum (16.7M colors)
- Adjustable color temperature
- Smooth color transitions
- Color mixing and blending

**Animation Support**

- Scrolling text
- Pattern displays
- Animations and effects
- Game displays
- Status indicators

Pin Configuration
-----------------

The LED matrix connects to the microcontroller via:

- **Data Pin**: Single data line for addressable LEDs
- **Power (5V)**: LED power supply
- **Ground**: Common ground

Programming Examples
--------------------

Using FastLED Library (Arduino)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: cpp

   #include <FastLED.h>
   
   #define LED_PIN     6
   #define NUM_LEDS    25
   #define BRIGHTNESS  50
   #define LED_TYPE    WS2812B
   #define COLOR_ORDER GRB
   
   CRGB leds[NUM_LEDS];
   
   void setup() {
     FastLED.addLeds<LED_TYPE, LED_PIN, COLOR_ORDER>(leds, NUM_LEDS);
     FastLED.setBrightness(BRIGHTNESS);
   }
   
   void loop() {
     // Set all LEDs to red
     fill_solid(leds, NUM_LEDS, CRGB::Red);
     FastLED.show();
     delay(1000);
     
     // Set all LEDs to green
     fill_solid(leds, NUM_LEDS, CRGB::Green);
     FastLED.show();
     delay(1000);
     
     // Set all LEDs to blue
     fill_solid(leds, NUM_LEDS, CRGB::Blue);
     FastLED.show();
     delay(1000);
   }

Individual LED Control
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: cpp

   void setup() {
     FastLED.addLeds<WS2812B, LED_PIN, GRB>(leds, NUM_LEDS);
     FastLED.setBrightness(50);
   }
   
   void loop() {
     // Set specific LEDs
     leds[0] = CRGB::Red;       // Top-left corner
     leds[4] = CRGB::Blue;      // Top-right corner
     leds[20] = CRGB::Green;    // Bottom-left corner
     leds[24] = CRGB::Yellow;   // Bottom-right corner
     leds[12] = CRGB::White;    // Center LED
     
     FastLED.show();
     delay(2000);
     
     // Clear all
     FastLED.clear();
     FastLED.show();
     delay(1000);
   }

LED Matrix Mapping
~~~~~~~~~~~~~~~~~~

5x5 matrix layout (LED indices):

.. code-block:: text

   [0]  [1]  [2]  [3]  [4]
   [5]  [6]  [7]  [8]  [9]
   [10] [11] [12] [13] [14]
   [15] [16] [17] [18] [19]
   [20] [21] [22] [23] [24]

Helper function to access by row/column:

.. code-block:: cpp

   int getLEDIndex(int row, int col) {
     return row * 5 + col;
   }
   
   void setPixel(int row, int col, CRGB color) {
     if (row >= 0 && row < 5 && col >= 0 && col < 5) {
       leds[getLEDIndex(row, col)] = color;
     }
   }

Animation Examples
------------------

Rainbow Effect
~~~~~~~~~~~~~~

.. code-block:: cpp

   void rainbow() {
     static uint8_t hue = 0;
     
     for(int i = 0; i < NUM_LEDS; i++) {
       leds[i] = CHSV(hue + (i * 10), 255, 255);
     }
     
     FastLED.show();
     hue++;
     delay(20);
   }

Breathing Effect
~~~~~~~~~~~~~~~~

.. code-block:: cpp

   void breathe(CRGB color) {
     static int brightness = 0;
     static int direction = 1;
     
     fill_solid(leds, NUM_LEDS, color);
     FastLED.setBrightness(brightness);
     FastLED.show();
     
     brightness += direction * 5;
     if (brightness >= 255 || brightness <= 0) {
       direction *= -1;
     }
     
     delay(30);
   }

Scrolling Pattern
~~~~~~~~~~~~~~~~~

.. code-block:: cpp

   void scrollPattern() {
     static int offset = 0;
     
     FastLED.clear();
     
     for(int i = 0; i < 5; i++) {
       int pos = (i + offset) % 5;
       leds[getLEDIndex(pos, i)] = CRGB::Cyan;
     }
     
     FastLED.show();
     offset = (offset + 1) % 5;
     delay(200);
   }

Display Patterns
~~~~~~~~~~~~~~~~

.. code-block:: cpp

   // Smiley face
   void showSmiley() {
     FastLED.clear();
     
     // Eyes
     leds[getLEDIndex(1, 1)] = CRGB::Yellow;
     leds[getLEDIndex(1, 3)] = CRGB::Yellow;
     
     // Smile
     leds[getLEDIndex(3, 1)] = CRGB::Yellow;
     leds[getLEDIndex(3, 3)] = CRGB::Yellow;
     leds[getLEDIndex(4, 2)] = CRGB::Yellow;
     
     FastLED.show();
   }
   
   // Cross pattern
   void showCross() {
     FastLED.clear();
     
     for(int i = 0; i < 5; i++) {
       leds[getLEDIndex(i, 2)] = CRGB::Red;  // Vertical
       leds[getLEDIndex(2, i)] = CRGB::Red;  // Horizontal
     }
     
     FastLED.show();
   }

MicroPython Example
~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from machine import Pin
   import neopixel
   import time
   
   # Initialize LED matrix
   np = neopixel.NeoPixel(Pin(6), 25)
   
   # Set color (R, G, B)
   def set_pixel(index, r, g, b):
       np[index] = (r, g, b)
       np.write()
   
   # Rainbow cycle
   def rainbow():
       for i in range(25):
           hue = int((i / 25) * 255)
           np[i] = hue_to_rgb(hue)
       np.write()
   
   # Clear all LEDs
   def clear():
       for i in range(25):
           np[i] = (0, 0, 0)
       np.write()

Practical Applications
-----------------------

Status Indicators
~~~~~~~~~~~~~~~~~

- System status visualization
- Progress bars
- Battery level indicators
- Connection status
- Error/warning displays

Games and Entertainment
~~~~~~~~~~~~~~~~~~~~~~~

- Simple games (Snake, Pong)
- Reaction time games
- Pattern matching
- Music visualizer
- Dice simulator

Educational Projects
~~~~~~~~~~~~~~~~~~~~

- Learning RGB color mixing
- Animation programming
- Pattern recognition
- Visual feedback for sensors
- Binary number display

Data Visualization
~~~~~~~~~~~~~~~~~~

- Bar graphs
- Temperature indicators
- Sound level meters
- Sensor data representation
- Real-time monitoring

Best Practices
--------------

**Power Considerations**

- Limit brightness when running from USB (500mA limit)
- Use external power for full brightness
- Calculate total current: LEDs × 60mA × brightness factor

**Performance**

- Update LEDs only when needed
- Use FastLED.show() sparingly
- Batch updates for smooth animation
- Optimize color calculations

**Color Selection**

- Use HSV for easier color manipulation
- Pre-calculate color palettes
- Consider color blindness accessibility
- Test colors in actual lighting conditions

**Programming Tips**

- Create reusable animation functions
- Use arrays for pattern storage
- Implement state machines for complex displays
- Add user controls for brightness/speed

Power Consumption
-----------------

.. list-table:: Current Consumption Examples
   :header-rows: 1
   :widths: 40 30 30

   * - Scenario
     - Current Draw
     - Notes
   * - All LEDs off
     - ~1 mA
     - Standby current
   * - 5 LEDs at 50% white
     - ~150 mA
     - Typical usage
   * - 25 LEDs at 100% white
     - ~1500 mA
     - Maximum draw
   * - 25 LEDs at 25% brightness
     - ~375 mA
     - Recommended for USB power

Troubleshooting
---------------

**LEDs not lighting**

- Check data pin connection
- Verify 5V power supply
- Confirm correct LED_PIN definition
- Test with simple example first

**Wrong colors displayed**

- Check COLOR_ORDER setting (RGB vs GRB)
- Verify data line integrity
- Test individual color channels
- Check for power supply issues

**Flickering or random colors**

- Add capacitor (100-1000µF) across power
- Shorten data wire if possible
- Add 330Ω resistor in data line
- Ensure stable power supply

**First LED works, others don't**

- Check for broken LED in chain
- Verify data passes through each LED
- Test continuity of data line
- Replace faulty LED if needed
