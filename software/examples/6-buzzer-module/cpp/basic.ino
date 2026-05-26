// The following example is based on the design from the Hardware Hacking practice. Visit the link for more information. Use this example ay tour own risk. 
// https://hardwarehackingmx.wordpress.com/2013/07/03/leccion-11-arduino-tocando-la-clasica-melodia-de-mario-bros/

#define NOTE_E6  1319
#define NOTE_G6  1568
#define NOTE_A6  1760
#define NOTE_AS6 1865
#define NOTE_B6  1976
#define NOTE_C7  2093
#define NOTE_D7  2349
#define NOTE_E7  2637
#define NOTE_F7  2794
#define NOTE_G7  3136
#define NOTE_A7  3520


#define REST 0

int buzzer = 21;

int melody[] = {
  NOTE_E7, NOTE_E7, REST, NOTE_E7,
  REST, NOTE_C7, NOTE_E7, REST,
  NOTE_G7, REST, REST, REST,
  NOTE_G6, REST, REST, REST,

  NOTE_C7, REST, REST, NOTE_G6,
  REST, REST, NOTE_E6, REST,
  REST, NOTE_A6, REST, NOTE_B6,
  REST, NOTE_AS6, NOTE_A6, REST,

  NOTE_G6, NOTE_E7, NOTE_G7,
  NOTE_A7, REST, NOTE_F7, NOTE_G7,
  REST, NOTE_E7, REST, NOTE_C7,
  NOTE_D7, NOTE_B6, REST, REST
};

int durations[] = {
  12, 12, 12, 12,
  12, 12, 12, 12,
  12, 12, 12, 12,
  12, 12, 12, 12,

  12, 12, 12, 12,
  12, 12, 12, 12,
  12, 12, 12, 12,
  12, 12, 12, 12,

  9, 9, 9, 12,
  12, 12, 12, 12,
  12, 12, 12, 12,
  12, 12, 12, 12
};

void setup() {
 // Nada que configurar
}

void loop() {
  for (int thisNote = 0; thisNote < sizeof(melody)/sizeof(int); thisNote++) {
    int noteDuration = 1000 / durations[thisNote];
    if (melody[thisNote] != REST) {
      tone(buzzer, melody[thisNote], noteDuration);
    }
    delay(noteDuration * 1.30);
    noTone(buzzer);
  }

  delay(2000);  // Pausa antes de repetir
}