// PWM duty print on Serial Monitor

int PWM_IN1 = 20;   // PWM pin 1
int STEP = 5;       //Indicador led de la Pulsar C6
void setup() {
  Serial.begin(115200);  
  Serial.println("Serial inicializado..."); 
  delay(200);           

  pinMode(PWM_IN1, OUTPUT);  // Salida de PWM

  Serial.println("Starting fade...");
}

void loop() {
  // Fade up
  for (int duty = 0; duty <= 255; duty += STEP) {
    analogWrite(PWM_IN1, duty);
    Serial.print("Duty: ");
    Serial.println(duty);
    delay(100);
  }

  // Fade down
  for (int duty = 255; duty >= 0; duty -= STEP) {
    analogWrite(PWM_IN1, duty);
    Serial.print("Duty: ");
    Serial.println(duty);
    delay(100);
  }
}