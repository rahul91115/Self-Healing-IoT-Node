#include <Arduino.h>

void setup() {
  // Use a slower baud rate for maximum compatibility
  Serial.begin(9600); 
  pinMode(4, OUTPUT);
  Serial.println("--- SYSTEM STARTING ---");
}

void loop() {
  Serial.println("HEARTBEAT_HIGH");
  digitalWrite(4, HIGH);
  delay(1000); // 1 second ON

  Serial.println("HEARTBEAT_LOW");
  digitalWrite(4, LOW);
  delay(5000); // 1 second OFF
}