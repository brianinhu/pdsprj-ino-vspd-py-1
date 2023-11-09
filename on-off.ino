const int led_D1 = 13;
const int led_D2 = 12;
char flag = '0';

void setup() {
  pinMode(led_D1, OUTPUT);
  pinMode(led_D2, OUTPUT);
  Serial.begin(9600);
  Serial.println("Conexión establecida");
}

void loop() {
  if (Serial.available()) {
    flag = Serial.read();
    
    if (flag == '1') {
      digitalWrite(led_D1, HIGH);
      digitalWrite(led_D2, HIGH);
    } else if (flag == '0') {
      digitalWrite(led_D1, LOW);
      digitalWrite(led_D2, LOW);
    }
  }
}