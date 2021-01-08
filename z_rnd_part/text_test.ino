#include <Adafruit_GFX.h>
#include <Adafruit_ST7735.h>
#include <Adafruit_ST7789.h>
#include <SPI.h>

#define TFT_CS 10
#define TFT_RST 9
#define TFT_DC 8

Adafruit_ST7735 tft = Adafruit_ST7735(TFT_CS, TFT_RST, TFT_DC);

void setup(void) {
    Serial.begin(9600);
    Serial.println('The start of test project!')
    delay(1000);

    tft.initR(INITR_144GREENTAB);
    Serial.println('Initialized');
}

void loop(void) {
    tft.fillScreen(ST77XX_BLACK)
    testdraw("My first text, HAPPY :))",ST77XX_WHITE);
    delay(500);
    testdraw("My first text, HAPPY :))",ST77XX_RED);
    delay(500);


}

void testdraw(char *text, uint16_t color) {
  tft.setCursor(0, 0);
  tft.setTextColor(color);
  tft.setTextWrap(true);
  tft.print(text);
}