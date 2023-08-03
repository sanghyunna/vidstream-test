#include <stdio.h>
#include "wiringPiI2C.h"

#define ADT7422_ADDRESS 0x48 // ADT7422 I2C 주소

int main() {
    int fd = wiringPiI2CSetup(ADT7422_ADDRESS); // I2C 연결 설정

    // 온도 센서 설정
    wiringPiI2CWriteReg8(fd, 0x03, 0x80); // 16비트 모드로 설정
    wiringPiI2CWriteReg8(fd, 0x02, 0x00); // Normal 모드로 설정

    // 온도 읽기
    int msb = wiringPiI2CReadReg8(fd, 0x00); // 상위 8비트 읽기
    int lsb = wiringPiI2CReadReg8(fd, 0x01); // 하위 8비트 읽
    int temp = (msb << 8) | lsb; // 16비트로 합치기
    if (temp & 0x8000) { // 음수 처리
        temp = temp - 65536;
    }
    float temperature = temp * 0.0078125; // 온도 계산

    printf("Temperature: %.2f°C\n", temperature); // 온도 출력

    return 0;
}
