#include <SoftwareSerial.h>
#include <Servo.h>
Servo alisA;//alis untuk kiri
Servo alisB;//alis untuk kanan
Servo mataA;//mata kanan kiri
Servo mataB;//mata bawah atas
Servo telingaA;//telinga kiri
Servo telingaB;//telinga kanan
Servo mulutAA;//mulut atas kiri
Servo mulutAB;//mulut atas kanan
Servo mulutBB;//mulut bawah kanan
Servo mulutBA;//mulut bawah kiri
Servo leherputar;
Servo leher;
String voice;


void setup()
{
  Serial.begin(9600);
// penggunaan pin
  alisA.attach(2);
  alisB.attach(3);
  mataA.attach(4);
  mataB.attach(5);
  telingaA.attach(6);
  telingaB.attach(7);
  mulutAA.attach(8);
  mulutAB.attach(9);
  mulutBB.attach(10);
  mulutBA.attach(11);
  
  //kondisi awal
  mataB.write(30);// Range (0-80)
  mataA.write(30);// Range (0-60)
  alisA.write(30);// Range (0-60)
  alisB.write(30);// Range (0-60)
  telingaB.write(45);// Range (0-90)
  telingaA.write(45);// Range (0-90)
  mulutAB.write(30);// Range (90-0)
  mulutAA.write(30);// Range (0-90)
  mulutBB.write(30);// Range (0-90)
  mulutBA.write(30);// Range (90-0)
  leher.write(90);// Range (0-135)
  leherputar.write(0);// Range (0-180)f
  
}

void loop()
{
  if(Serial.available()>0){
  byte voice=Serial.read();
   // agar stabil
//    char c = Serial.read(); //membaca serial
//    
//  if(c== '#') {break;} // keluar dari looping saat # kata terdeteksi
//  voice += c;
//  }
//  if (voice.length() > 0){
    Serial.println(voice);
    if(voice == 'f') //kondisi senyum
 {mulutAB.write(0);
 mulutAA.write(90);
 mulutBB.write(90);
 mulutBA.write(0);
  telingaB.write(45);// Range (0-90)
  telingaA.write(45);
  mataB.write(30);// Range (0-80)
  mataA.write(30);
  alisA.write(30);// Range (0-60)
  alisB.write(30);

}
 else if (voice == 'b')//kondisi kaget b 
{
  alisA.write(0);
  alisB.write(60);
 mulutAB.write(90);
 mulutAA.write(10);
 mulutBB.write(90);
 mulutBA.write(0);
 telingaA.write(0);
 telingaB.write(90);
}
else if (voice == 'r')//kondisi marah
{
  alisA.write(60);
  alisB.write(0);
  telingaB.write(90);
  telingaA.write(0);
   mulutAB.write(15);// Range (90-0)
  mulutAA.write(20);// Range (0-90)
  mulutBB.write(10);// Range (0-90)
  mulutBA.write(40);
  mataB.write(30);// Range (0-80)
  mataA.write(30);
  
}
else if (voice == 'l')//kondisi sedih
{
  alisA.write(0);
  alisB.write(60);
  telingaB.write(0);
  telingaA.write(90);
  mulutAB.write(90);
 mulutAA.write(0);
 mulutBB.write(0);
 mulutBA.write(90);
 mataB.write(0);// Range (0-80)
  mataA.write(60);
}
}}

