const int IN_PIN  = 4;                        // Digital pin where the IN pin is connected
const int T = 1000;                           // Interval in milliseconds
bool relayState = HIGH;                       //Turn off by default
unsigned long previousMillis = 0;             
const long interval = 2000;                   // ON/OFF Timer
int cycleCount = 0;                           //Cycle count


void setup() {
  // Initialize the Serial port at 115200 baud
  Serial.begin(115200);
  while (!Serial) ;

  // Initialize the pin as an output
  pinMode(IN_PIN, OUTPUT);

  digitalWrite(IN_PIN,relayState);
  Serial.println("Sistema de Control de Relevador Iniciado...");
  Serial.println("Envíe '1' para encender, '0' para apagar.");

}

void loop() {
  //Encendido por terminal serial
  if (Serial.available() > 0) {
    char command = Serial.read();
    if (command == '1') {
      activateRelay(LOW);
    } else if (command == '0') {
      activateRelay(HIGH);
    }
  }
  /*
  unsigned long currentMillis = millis();
  if (currentMillis - previousMillis >= interval) {
    previousMillis = currentMillis;
    relayState = !relayState;
    activateRelay(relayState);
  }
  */
}

void activateRelay(bool state) {
  digitalWrite(IN_PIN, state);
  if (state == LOW) {
    cycleCount++;
    Serial.print("Relevador ACTIVO. Ciclo nro: ");
    Serial.println(cycleCount);
  } else {
    Serial.println("Relevador INACTIVO.");
  }
}