int LedPin=D6;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  analogWrite(LedPin,1024);

}

void loop() {
  // put your main code here, to run repeatedly:
  int dutycycle=analogRead(A0);
  if(dutycycle>1023) dutycycle=1023;
  Serial.print("Duty Cycle: ");
  Serial.println(dutycycle);
  analogWrite(LedPin,dutycycle);
  delay(100);

}
