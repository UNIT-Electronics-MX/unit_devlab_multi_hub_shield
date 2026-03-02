Display Hub - OLED Display
===========================

Overview
--------

The DevLab Multi Hub Shield features an integrated 128x64 I2C OLED display that provides a compact, high-contrast visual interface for displaying text, graphics, and sensor data. The display uses the SSD1306 controller and communicates via the I2C bus.

Technical Specifications
------------------------

.. list-table:: OLED Display Specifications
   :header-rows: 1
   :widths: 30 70

   * - Parameter
     - Value
   * - **Resolution**
     - 128 x 64 pixels
   * - **Controller**
     - SSD1306 (or compatible)
   * - **Interface**
     - I2C
   * - **I2C Address**
     - 0x3C (default) or 0x3D
   * - **Display Type**
     - OLED (Organic LED)
   * - **Color**
     - Monochrome (White/Blue/Yellow)
   * - **Viewing Angle**
     - >160 degrees
   * - **Voltage**
     - 3.3V logic, 7-9V internal charge pump
   * - **Current**
     - ~20mA typical
   * - **Brightness**
     - Adjustable (0-255)
   * - **Power**
     - Low power consumption

Display Features
----------------

**High Contrast**

- OLED technology provides true black pixels
- No backlight needed
- Excellent readability in various lighting conditions
- High contrast ratio (>2000:1)

**Fast Response**

- No ghosting or motion blur
- Instant pixel switching
- Suitable for animations
- Smooth scrolling capabilities

**Wide Viewing Angle**

- Readable from extreme angles
- No color shift
- Consistent brightness across viewing angles

Pin Connections
---------------

The OLED display connects via I2C:

- **SDA**: I2C Data line
- **SCL**: I2C Clock line
- **VCC**: 3.3V Power
- **GND**: Ground

These are shared with the QWIIC/STEMMA connectors on the same I2C bus.

Programming Libraries
---------------------

Arduino Libraries
~~~~~~~~~~~~~~~~~

**Adafruit SSD1306** (Recommended)

.. code-block:: cpp

   #include <Wire.h>
   #include <Adafruit_GFX.h>
   #include <Adafruit_SSD1306.h>
   
   #define SCREEN_WIDTH 128
   #define SCREEN_HEIGHT 64
   #define OLED_RESET -1  // No reset pin
   #define SCREEN_ADDRESS 0x3C
   
   Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);

**U8g2 Library** (Alternative)

.. code-block:: cpp

   #include <U8g2lib.h>
   
   U8G2_SSD1306_128X64_NONAME_F_HW_I2C u8g2(U8G2_R0, U8X8_PIN_NONE);

Basic Examples
--------------

Initialization
~~~~~~~~~~~~~~

.. code-block:: cpp

   #include <Wire.h>
   #include <Adafruit_GFX.h>
   #include <Adafruit_SSD1306.h>
   
   #define SCREEN_WIDTH 128
   #define SCREEN_HEIGHT 64
   #define OLED_RESET -1
   
   Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);
   
   void setup() {
     Serial.begin(115200);
     
     // Initialize display
     if(!display.begin(SSD1306_SWITCHCAPVCC, 0x3C)) {
       Serial.println(F("SSD1306 allocation failed"));
       for(;;);  // Don't proceed, loop forever
     }
     
     // Clear the buffer
     display.clearDisplay();
     display.display();
   }

Text Display
~~~~~~~~~~~~

.. code-block:: cpp

   void displayText() {
     display.clearDisplay();
     
     // Set text properties
     display.setTextSize(1);              // Normal 1:1 pixel scale
     display.setTextColor(SSD1306_WHITE); // White text
     display.setCursor(0, 0);             // Start at top-left
     
     // Display text
     display.println(F("DevLab Shield"));
     display.println(F("Multi Hub"));
     display.println();
     display.setTextSize(2);
     display.println(F("Hello!"));
     
     // Update display
     display.display();
   }

Multiple Text Sizes
~~~~~~~~~~~~~~~~~~~

.. code-block:: cpp

   void multiSizeText() {
     display.clearDisplay();
     
     // Size 1 (small)
     display.setTextSize(1);
     display.setCursor(0, 0);
     display.println("Size 1: Small");
     
     // Size 2 (medium)
     display.setTextSize(2);
     display.setCursor(0, 16);
     display.println("Size 2");
     
     // Size 3 (large)
     display.setTextSize(3);
     display.setCursor(0, 40);
     display.println("Big");
     
     display.display();
   }

Graphics Examples
-----------------

Drawing Shapes
~~~~~~~~~~~~~~

.. code-block:: cpp

   void drawShapes() {
     display.clearDisplay();
     
     // Draw rectangle
     display.drawRect(0, 0, 60, 30, SSD1306_WHITE);
     
     // Draw filled rectangle
     display.fillRect(70, 0, 58, 30, SSD1306_WHITE);
     
     // Draw circle
     display.drawCircle(30, 48, 15, SSD1306_WHITE);
     
     // Draw filled circle
     display.fillCircle(98, 48, 15, SSD1306_WHITE);
     
     display.display();
   }

Drawing Lines
~~~~~~~~~~~~~

.. code-block:: cpp

   void drawLines() {
     display.clearDisplay();
     
     for(int16_t i=0; i<display.width(); i+=4) {
       display.drawLine(0, 0, i, display.height()-1, SSD1306_WHITE);
     }
     
     for(int16_t i=0; i<display.height(); i+=4) {
       display.drawLine(0, 0, display.width()-1, i, SSD1306_WHITE);
     }
     
     display.display();
   }

Displaying Bitmaps
~~~~~~~~~~~~~~~~~~

.. code-block:: cpp

   // Define bitmap (16x16 pixels)
   const unsigned char icon_16x16 [] PROGMEM = {
     0x00, 0x00, 0x07, 0xe0, 0x18, 0x18, 0x20, 0x04,
     0x47, 0xe2, 0x48, 0x12, 0x90, 0x09, 0x90, 0x09,
     0x90, 0x09, 0x90, 0x09, 0x48, 0x12, 0x47, 0xe2,
     0x20, 0x04, 0x18, 0x18, 0x07, 0xe0, 0x00, 0x00
   };
   
   void displayIcon() {
     display.clearDisplay();
     display.drawBitmap(56, 24, icon_16x16, 16, 16, SSD1306_WHITE);
     display.display();
   }

Sensor Data Display
-------------------

Temperature Display
~~~~~~~~~~~~~~~~~~~

.. code-block:: cpp

   void displayTemperature(float temp) {
     display.clearDisplay();
     
     display.setTextSize(1);
     display.setCursor(0, 0);
     display.println("Temperature:");
     
     display.setTextSize(3);
     display.setCursor(10, 20);
     display.print(temp, 1);
     
     display.setTextSize(2);
     display.println(" C");
     
     display.display();
   }

Multi-Sensor Dashboard
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: cpp

   void displayDashboard(float temp, float hum, float press) {
     display.clearDisplay();
     
     display.setTextSize(1);
     
     // Temperature
     display.setCursor(0, 0);
     display.print("Temp: ");
     display.print(temp, 1);
     display.println(" C");
     
     // Humidity
     display.setCursor(0, 12);
     display.print("Hum:  ");
     display.print(hum, 1);
     display.println(" %");
     
     // Pressure
     display.setCursor(0, 24);
     display.print("Press:");
     display.print(press, 0);
     display.println(" hPa");
     
     // Time or status
     display.setCursor(0, 40);
     display.println("Status: OK");
     
     display.display();
   }

Progress Bar
~~~~~~~~~~~~

.. code-block:: cpp

   void displayProgress(int percent) {
     display.clearDisplay();
     
     display.setTextSize(1);
     display.setCursor(0, 0);
     display.println("Progress:");
     
     // Draw progress bar outline
     display.drawRect(10, 20, 108, 12, SSD1306_WHITE);
     
     // Fill progress
     int fillWidth = map(percent, 0, 100, 0, 104);
     display.fillRect(12, 22, fillWidth, 8, SSD1306_WHITE);
     
     // Display percentage
     display.setCursor(50, 40);
     display.setTextSize(2);
     display.print(percent);
     display.print("%");
     
     display.display();
   }

Advanced Features
-----------------

Scrolling Text
~~~~~~~~~~~~~~

.. code-block:: cpp

   void setupScrolling() {
     display.clearDisplay();
     display.setTextSize(2);
     display.setCursor(0, 0);
     display.println("Scrolling");
     display.println("Text!");
     display.display();
     
     // Scroll left
     display.startscrollleft(0x00, 0x0F);
     delay(2000);
     display.stopscroll();
     
     // Scroll right
     display.startscrollright(0x00, 0x0F);
     delay(2000);
     display.stopscroll();
   }

Inverted Display
~~~~~~~~~~~~~~~~

.. code-block:: cpp

   void invertDisplay() {
     display.invertDisplay(true);  // Invert
     delay(1000);
     display.invertDisplay(false); // Normal
   }

Brightness Control
~~~~~~~~~~~~~~~~~~

.. code-block:: cpp

   void setBrightness(uint8_t brightness) {
     // brightness: 0-255
     display.ssd1306_command(SSD1306_SETCONTRAST);
     display.ssd1306_command(brightness);
   }

MicroPython Example
-------------------

.. code-block:: python

   from machine import Pin, I2C
   import ssd1306
   import time
   
   # Initialize I2C
   i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=400000)
   
   # Initialize display
   oled = ssd1306.SSD1306_I2C(128, 64, i2c, addr=0x3C)
   
   # Clear display
   oled.fill(0)
   oled.show()
   
   # Display text
   oled.text('DevLab Shield', 0, 0)
   oled.text('Multi Hub', 0, 10)
   oled.text('Hello World!', 0, 30)
   oled.show()
   
   # Simple animation
   for i in range(0, 128, 4):
       oled.fill(0)
       oled.rect(i, 28, 16, 16, 1)
       oled.show()
       time.sleep(0.05)

TFT Display Configuration
--------------------------

The shield supports TFT display customization for enhanced color graphics capabilities.

**TFT Display Options**

- Color TFT displays via SPI interface
- Touch screen support
- Higher resolution options
- Additional header connections required

**Configuration**

Consult the shield documentation for:
- Specific TFT models supported
- Jumper/switch settings
- Pin assignments for SPI TFT
- Touch controller integration

Best Practices
--------------

**Performance**

- Update display only when needed (not every loop)
- Use partial updates when possible
- Clear only the changed area
- Batch drawing operations before display.display()

**Power Management**

- Turn off display when not needed
- Reduce brightness for battery operation
- Use sleep modes in low-power applications

**Display Care**

- Avoid displaying static images for extended periods
- Vary content to prevent burn-in
- Use screensavers for always-on applications

**Memory**

- Use F() macro for string literals to save RAM
- Consider display buffer size (1KB for 128x64)
- Use PROGMEM for bitmaps and fonts

Troubleshooting
---------------

**Display Not Working**

- Check I2C address (0x3C vs 0x3D)
- Verify I2C connections (SDA, SCL)
- Run I2C scanner
- Check power supply
- Verify library installation

**Garbled Display**

- Wrong I2C address
- I2C bus speed too high
- Power supply issues
- Bad connections

**Dim Display**

- Adjust brightness/contrast
- Check power supply voltage
- Verify VCC is 3.3V, not 5V
- Display may be failing

**Display Freezes**

- Check for infinite loops
- Verify I2C bus isn't stuck
- Reset microcontroller
- Check for memory issues

Applications
------------

- Sensor data visualization
- System status display
- Menu systems
- Data logging display
- Animations and graphics
- User interface
- Debugging output
- Real-time monitoring
