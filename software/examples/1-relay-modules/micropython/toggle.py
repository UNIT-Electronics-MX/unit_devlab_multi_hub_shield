# --------------------------------------------------
# Relay Blink with On/Off read from terminal Serial
# --------------------------------------------------

import utime
from machine import Pin

# ————— Configuration —————
RELAY_PIN = Pin(14, Pin.OUT)   # GPIO pin for the relay
ON_TIME   = 1000               # ON duration in milliseconds
OFF_TIME  = 1500               # OFF duration in milliseconds
PREVIOUS_TIME = 0;
# Initialize state
last_tick = utime.ticks_ms()
relay_on  = False
RELAY_PIN.value(1)  # Start with relay OFF (HIGH = OFF for active LOW)

# ————— Main loop (non‑blocking) —————
while True:
    now = utime.ticks_ms()

    # Comprobamos si hay caracteres esperando en el buffer de entrada
    res = select.select([sys.stdin], [], [], 0)
    
    if res[0]:
        # Leemos un carácter de la consola
        char = sys.stdin.read(1)
        print(f"Recibiste: {char}")
    if not relay_on and utime.ticks_diff(now, last_tick) >= OFF_TIME:
        relay_on   = True
        last_tick  = now
        RELAY_PIN.value(0)  # LOW = Relay ON (active LOW)
        print("NO: On NC: Off")

    elif relay_on and utime.ticks_diff(now, last_tick) >= ON_TIME:
        relay_on   = False
        last_tick  = now
        RELAY_PIN.value(1)  # HIGH = Relay OFF (active LOW)
        print("NO: Off NC: On")
