void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  digitalWrite(LED_BUILTIN, HIGH); // turn the LED on
  delay(500);                      // wait for half a second
  digitalWrite(LED_BUILTIN, LOW);  // turn the LED off
  delay(500);                      // wait for half a second
}