/*
Autor: Javier Alonso Diaz Valderrama

Universidad de Valparaiso
javier.diazv@alumnos.uv.cl

Estaba aburrido, si le encuentran alguna funcion a la mano, de pana jasjjda yo no le veo ninguna :D
 */

#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>
Adafruit_PWMServoDriver servo = Adafruit_PWMServoDriver(0x40);

#define numOfValsRec 5
#define digitsPerValRec 1

// Definicion parametros para recivir por puerto señal desde python
int valsRec[numOfValsRec];
int largoString = numOfValsRec * digitsPerValRec + 1; //Sring entregado de la forma $00000
int contador = 0;
bool iniciarContador = false;
String recibirString;

//Definicion de rangos servos 
int angulo0 = 102;
int angulo180 = 512;

//BOTONES DE PRUEBA
int botVerde = 8;
int botNegro = 9;
int botBlanco = 10;
int botRojo = 11;
int botAzul = 12;


//Nombre y posicion Servos en PCA9685
int pulgar = 0;
int indice = 1;
int medio = 2;
int anular = 3;
int menique = 4;



void setup() {
  servo.begin();
  Serial.begin(9600);
  Serial.println("WENAPO");
  servo.setPWMFreq(50);
  pinMode(botVerde, INPUT);
  pinMode(botNegro, INPUT);
  pinMode(botBlanco, INPUT);
  pinMode(botRojo, INPUT);
  pinMode(botAzul, INPUT);

}


void loop() {
  recibirInfo();
  //Serial.println(Serial.read());
  
  if ((digitalRead(botVerde)==HIGH)or(valsRec[0] == 0)){Serial.println("Moviendo pulgar");setServo(0,180);}else{setServo(0,0);}
  if ((digitalRead(botNegro)==HIGH) or (valsRec[1] == 0)){Serial.println("Moviendo indice");setServo(1,180);}else{setServo(1,0);}
  if ((digitalRead(botBlanco)==HIGH) or (valsRec[2] == 0)){Serial.println("Moviendo medio");setServo(2,180);}else{setServo(2,0);}
  if ((digitalRead(botRojo)==HIGH) or (valsRec[3] == 0)){Serial.println("Moviendo anular");setServo(3,180);}else{setServo(3,0);}
  if ((digitalRead(botAzul)==HIGH) or (valsRec[4] == 0)){Serial.println("Moviendo menique");setServo(4,180);}else{setServo(4,0);}
  
  //Serial.println(valsRec[5]);
  /*
  if (valsRec[0] == 1){setServo(0,180);Serial.println("Moviendo pulgar");}else{setServo(0,0);}
  if (valsRec[1] == 1){setServo(1,180);Serial.println("Moviendo indice");}else{setServo(1,0);}
  if (valsRec[2] == 1){setServo(2,180);Serial.println("Moviendo medio");}else{setServo(2,0);}
  if (valsRec[3] == 1){setServo(3,180);Serial.println("Moviendo anular");}else{setServo(3,0);}
  if (valsRec[4] == 1){setServo(4,180);Serial.println("Moviendo menique");}else{setServo(4,0);}
  */
}







void recibirInfo(){
  while(Serial.available()){
    char c = Serial.read();
    if (c == '$'){
      iniciarContador = true;
    }
    if (iniciarContador){
      if (contador < largoString){
        recibirString = String(recibirString + c);
        contador++;
      }
      
      if (contador >= largoString){
        for (int i=0; i<numOfValsRec; i++){
          int num = (i*digitsPerValRec) + 1;
        valsRec[i] = recibirString.substring(num, num + digitsPerValRec).toInt();
        }
        recibirString = "";
        contador = 0;
        iniciarContador = false;
      }
      
    }
    
  }
  
}


void setServo(uint8_t num, int angulo){
  int duty;
  duty = map(angulo, 0, 180, angulo0, angulo180);
  servo.setPWM(num, 0, duty);
}

