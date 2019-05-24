#include <SPI.h>
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

#define OLED_RESET D5
/* Object named display, of the class Adafruit_SSD1306 */
Adafruit_SSD1306 display(OLED_RESET);

#if (SSD1306_LCDHEIGHT != 64)
#error("Height incorrect, please fix Adafruit_SSD1306.h!");
#endif
int switchpin=D5;
int switchvalue;
int ledpin=D0;
void setup() {
  // put your setup code here, to run once:
  pinMode(ledpin,OUTPUT);
  pinMode(switchpin,INPUT_PULLUP);
  display.begin(SSD1306_SWITCHCAPVCC, 0x3C); /* Initialize display with address 0x3C */
  display.clearDisplay();  /* Clear display */
  display.setTextSize(1);  /* Select font size of text. Increases with size of argument. */
  display.setTextColor(WHITE);

}

void loop() {
  switchvalue=digitalRead(switchpin);
  digitalWrite(ledpin,switchvalue);
  updateWatch();/* Every second increment clock and display */
  delay(1000);
  // put your main code here, to run repeatedly:

}
void updateWatch() {
  if(switchvalue)
  {
    writeOLED1();
  }
  else
  {
    writeOLED2();
  }
}

void writeOLED1(){
  
  display.clearDisplay();  /* Clear display */
  
  
  drawStr(50, 10, "display");
  drawStr(40, 30, "led on");
  drawStr(20, 50, "smarbridge");
  display.display();
}

void writeOLED2(){
  
  display.clearDisplay();  /* Clear display */
  
  
  drawStr(50, 10, "display");
  drawStr(40, 30, "led off");
  drawStr(20, 50, "smarbridge");
  display.display();
}
void drawStr(uint8_t x, uint8_t y, char* str){
  display.setCursor(x, y);  /* Set x,y coordinates */
  display.println(str);
}








 
