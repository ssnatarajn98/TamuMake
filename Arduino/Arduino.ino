/*
 * Created for TAMUMake
 * 3 Digital Output pins for LEDS. Dev Board used was a Mega 2560
 * Seth Barberee
 * 2/16/18
 */
char message = '0';
void setup() {
  pinMode(22, OUTPUT);
  pinMode(26, OUTPUT);
  pinMode(30, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  while(Serial.available() > 0){
    char message = (char)Serial.read();
    Serial.println(message);
   if(message == '3'){
    digitalWrite(22, HIGH);
    digitalWrite(26, HIGH);
    digitalWrite(30, HIGH);
    }
   else if(message == '2'){
     digitalWrite(22, LOW);
     digitalWrite(26, HIGH);
     digitalWrite(30, HIGH);
    }
  else if(message == '1'){
      digitalWrite(22, LOW);
      digitalWrite(26, LOW);
      digitalWrite(30, HIGH);
    }
  else if(message == '0') {
    digitalWrite(22, LOW);
    digitalWrite(26, LOW);
    digitalWrite(30, LOW);
    }
  }
}
