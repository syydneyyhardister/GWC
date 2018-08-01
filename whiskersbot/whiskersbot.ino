s#include <Servo.h> 

int leftWhisker = 5;
int rightWhisker = 7;
Servo servoLeft;                             // Declare left servo signal
Servo servoRight;                            // Declare right servo signal

int PIEZOPIN = A0;       

int sam = 0;

void forward(int time)                       // Forward function
{
  servoLeft.writeMicroseconds(1350);         // Left wheel counterclockwise
  servoRight.writeMicroseconds(1650);        // Right wheel clockwise
  delay(time);                               // Maneuver for time ms
}

void turnLeft(int time)                      // Left turn function
{
  servoLeft.writeMicroseconds(1500);         // Left wheel clockwise
  servoRight.writeMicroseconds(1300);        // Right wheel clockwise
  delay(time);                               // Maneuver for time ms
}

void turnRight(int time)                     // Right turn function
{
  servoLeft.writeMicroseconds(1700);         // Left wheel counterclockwise
  servoRight.writeMicroseconds(1500);        // Right wheel counterclockwise
  delay(time);                               // Maneuver for time ms
}

void backward(int time)                      // Backward function
{
  servoLeft.writeMicroseconds(1700);         // Left wheel clockwise
  servoRight.writeMicroseconds(1300);        // Right wheel counterclockwise
  delay(time);                               // Maneuver for time ms
}

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(leftWhisker, INPUT);
  pinMode(rightWhisker, INPUT);
  pinMode(PIEZOPIN, INPUT);                 // Attach piezo to pin 5. 
  servoLeft.attach(13);                      // Attach left signal to pin 13
  servoRight.attach(12);                     // Attach right signal to pin 12 
  servoLeft.writeMicroseconds(1500);        // Calibrate left servo
  servoRight.writeMicroseconds(1500);       // Calibrate right servo   
}

void loop() {
  int left_value = digitalRead(leftWhisker);
  int right_value = digitalRead(rightWhisker);
     // put your main code here, to run repeatedly:
      if (right_value == 0 && left_value == 0) {
        Serial.println("both whisker touched");
      }
      else if (left_value == 0) {
        Serial.println("only leftWhisker touched"); 
      }
      else if (right_value == 0) {
        Serial.println("only rightWhisker touched");
      }
    delay(100);
  
  byte wLeft = digitalRead(5);               // Copy left result to wLeft  
  byte wRight = digitalRead(7);              // Copy right result to wRight

  if((wLeft == 0) && (wRight == 0))          // If both whiskers contact
  {
    if (sam > 0) {
      backward(2000);
      turnLeft(800);
    } 
    else {
    backward(2000);                          // Back up 1 second
    turnRight(800);                           // Turn left about 120 degrees
    }
    sam = sam + 1;
  }
  else if(wLeft == 0)                        // If only left whisker contact
  { 
    sam = 0;
    backward(1000);                          // Back up 1 second
    turnLeft(200);                          // Turn right about 60 degrees
  }
  else if(wRight == 0)                       // If only right whisker contact
  {
    sam = 0;
    backward(1000);                          // Back up 1 second
    turnRight(200);                           // Turn left about 60 degrees
  }
  else                                       // Otherwise, no whisker contact
  {
    sam = 0;
    forward(20);                             // Forward 1/50 of a second
  }
  Serial.print("A3 = ");                     // Display "A3 = "
  Serial.print(volts(A3));                    // Display measured A3 volts
  Serial.println(" volts");                  // Display " volts" & newline
  delay(1000);   
  
}
                                            
float volts(int adPin)                       // Measures volts at adPin
{                                            // Returns floating point voltage
 return float(analogRead(adPin)) * 5.0 / 1024.0;
}  

