#include <stdio.h>
#include "wiringPiI2C.h"

#define ADT7422_ADDRESS 0x48 // ADT7422 I2C Address

int main() {
    int fd = wiringPiI2CSetup(ADT7422_ADDRESS); // I2C connection setup

    // 온도 센서 설정
    wiringPiI2CWriteReg8(fd, 0x03, 0x80); // 16bit mode
    wiringPiI2CWriteReg8(fd, 0x02, 0x00); // Normal mode

    // 온도 읽기
    int msb = wiringPiI2CReadReg8(fd, 0x00); // read upper 8bits
    int lsb = wiringPiI2CReadReg8(fd, 0x01); // read lower 8bits
    int temp = (msb << 8) | lsb; // concatenate to 16bits
    if (temp & 0x8000) { // negative numbers
        temp = temp - 65536;
    }
    float temperature = temp * 0.0078125; // calc temp

    printf("Temperature: %.2f°C\n", temperature); // print temp

    return 0;
}
