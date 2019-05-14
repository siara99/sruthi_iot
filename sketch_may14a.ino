int switchPin =0;//d3
int LedPin= 16;//d0
int switchValue; 
void setup() {
  pinMode(LedPin,OUTPUT);
  pinMode(switchPin,INPUT_PULLUP);
  // put your setup code here, to run once:

}

void loop() {
  
  // put your main code here, to run repeatedly:
  //read the switch value
  switchValue = digitalRead(switchPin);
  digitalWrite(LedPin,!switchValue);

}
