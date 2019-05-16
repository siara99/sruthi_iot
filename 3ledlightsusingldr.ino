
int LedPin1=D6;
int LedPin2=D2;
int LedPin3=D1;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(LedPin1,OUTPUT);
  pinMode(LedPin2,OUTPUT);
  pinMode(LedPin3,OUTPUT);
  

}

void loop() {
  // put your main code here, to run repeatedly:
  int dutycycle=analogRead(A0);
  if(dutycycle>1&& dutycycle<601)
  {
  Serial.print("Duty Cycle1: ");
  Serial.println(dutycycle);
  digitalWrite(LedPin1,HIGH);
  digitalWrite(LedPin2,LOW);
  digitalWrite(LedPin3,LOW);
  
  
  delay(1000);
  }
  if(dutycycle>600&& dutycycle<800)
  {
  Serial.print("Duty Cycle2: ");
  Serial.println(dutycycle);
  digitalWrite(LedPin1,LOW);
  digitalWrite(LedPin2,HIGH);
  digitalWrite(LedPin3,LOW);
  delay(1000);
  }
  if(dutycycle>800)
  {
  
  Serial.print("Duty Cycle3: ");
  Serial.println(dutycycle);
  digitalWrite(LedPin1,LOW);
  digitalWrite(LedPin2,LOW);
  digitalWrite(LedPin3,HIGH);
  delay(1000);
  }

}
