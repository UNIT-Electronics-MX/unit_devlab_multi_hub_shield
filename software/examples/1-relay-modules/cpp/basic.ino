int IN_PIN  = 4;  // Digital pin where the IN pin is connected
int T = 1000;     // Interval in milliseconds

void setup() {
  // Initialize the pin as an output
  pinMode(IN_PIN, OUTPUT);

  // Initialize the Serial port at 9600 baud
  Serial.begin(9600);
  while (!Serial) ;
}

void loop() {
  // --- LOW (Relay ON) ---
  digitalWrite(IN_PIN, LOW);
  Serial.print("NO: On ");
  Serial.println("NC: Off");
  delay(T);

  // --- HIGH (Relay OFF) ---
  digitalWrite(IN_PIN, HIGH);
  Serial.print("NO: Off ");
  Serial.println("NC: On");
  delay(T);
}