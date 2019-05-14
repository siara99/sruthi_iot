int switchPin =0;//d3
int switchPin2=D1;//d1
int LedPin= 16;//d0
int LedPin2=D4;

int switchValue;
int switchValue2; 
void setup() {
  pinMode(LedPin,OUTPUT);
   pinMode(LedPin2,OUTPUT);
  
  pinMode(switchPin,INPUT_PULLUP);
  
  pinMode(switchPin2,INPUT_PULLUP);
  // put your setup code here, to run once:

}

void loop() {
  
  // put your main code here, to run repeatedly:
  //read the switch value
  
switchValue = digitalRead(switchPin);
switchValue2 = digitalRead(switchPin2);
  
  digitalWrite(LedPin,!switchValue);
  digitalWrite(LedPin2,switchValue2);

}
