
#include <Servo.h>

int servoPin = 9;
Servo servo_1;
void setup() {
  servo_1.attach(servoPin);
  // put your setup code here, to run once:

}

void loop() {
  servo_1.write(180);
  delay(1000);
  servo_1.write(-180);
  delay(1000);
  // put your main code here, to run repeatedly:

}
