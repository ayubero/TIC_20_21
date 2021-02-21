#include <SoftwareSerial.h>
#include <Servo.h>

//Bluetooth
SoftwareSerial hc06(2,3);
char data = 0;

//Servo
Servo myServo;

//Motor pins
int leftMotorPin1 = 6;
int leftMotorPin2 = 7;
int leftPWM = 10;

int rightMotorPin1 = 4;
int rightMotorPin2 = 5;
int rightPWM = 9;

void setup() {
  Serial.begin(9600);
  hc06.begin(9600);

  myServo.attach(11);
  
  pinMode(rightMotorPin1, OUTPUT);
  pinMode(rightMotorPin2, OUTPUT);
  pinMode(leftMotorPin1, OUTPUT);
  pinMode(leftMotorPin2, OUTPUT);
  pinMode(rightPWM, OUTPUT); 
  pinMode(leftPWM, OUTPUT);
}

void loop() {
  if (hc06.available()){
    data = hc06.read();
    Serial.print(data);
    Serial.print("\n");
    switch(data) {
      case 'f':
        moveForward();
        break;
      case 'b':
        moveBackward();
        break;
      case 'l':
        moveLeft();
        break;
      case 'r':
        moveRight();
        break;
      case 'c':
        cease();
        break;
      case 'u': //Left
        ultrasonic(50);
        break;
      case 'v': //Right
        ultrasonic(100);
        break;
      case 'w': //Forward
        ultrasonic(75);
        break;
    }
  }
}

void ultrasonic(int pos) {
  myServo.write(pos);
}

void moveForward() {
  analogWrite(rightPWM, 255);
  analogWrite(leftPWM, 255);

  digitalWrite(rightMotorPin1, LOW);
  digitalWrite(rightMotorPin2, HIGH);

  digitalWrite(leftMotorPin1, HIGH);
  digitalWrite(leftMotorPin2, LOW);
}

void moveBackward() {
  analogWrite(rightPWM, 255);
  analogWrite(leftPWM, 255);

  digitalWrite(rightMotorPin1, HIGH);
  digitalWrite(rightMotorPin2, LOW);

  digitalWrite(leftMotorPin1, LOW);
  digitalWrite(leftMotorPin2, HIGH);
}

void moveLeft() {
  analogWrite(rightPWM, 0);
  analogWrite(leftPWM, 255);

  digitalWrite(rightMotorPin1, LOW);
  digitalWrite(rightMotorPin2, HIGH);

  digitalWrite(leftMotorPin1, HIGH);
  digitalWrite(leftMotorPin2, LOW);
}

void moveRight() {
  analogWrite(rightPWM, 255);
  analogWrite(leftPWM, 0);

  digitalWrite(rightMotorPin1, LOW);
  digitalWrite(rightMotorPin2, HIGH);

  digitalWrite(leftMotorPin1, HIGH);
  digitalWrite(leftMotorPin2, LOW);
}

void cease() {
  analogWrite(rightPWM, 0);
  analogWrite(leftPWM, 0);

  digitalWrite(rightMotorPin1, LOW);
  digitalWrite(rightMotorPin2, HIGH);

  digitalWrite(leftMotorPin1, HIGH);
  digitalWrite(leftMotorPin2, LOW);
}
