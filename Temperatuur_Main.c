#include <avr/io.h>
#include <string.h>
#include <avr/sfr_defs.h>
#define F_CPU 16E6
#include <util/delay.h>
#define UBBRVAL 51
#include "adc.h"

// Function prototypes
void transmit(uint8_t data);
void send_adc_info();
void uart_init();

void uart_init() {
	// set the baud rate
	UBRR0H = 0;
	UBRR0L = UBBRVAL;
	// disable U2X mode
	UCSR0A = 0;
	// enable transmitter and receiver
	UCSR0B |= (1 << RXEN0) | (1 << TXEN0);
	// set frame format : asynchronous, 8 data bits, 1 stop bit, no parity
	UCSR0C = _BV(UCSZ01) | _BV(UCSZ00);
}

void transmit(uint8_t data) {
	// wait for an empty transmit buffer
	// UDRE is set when the transmit buffer is empty
	loop_until_bit_is_set(UCSR0A,UDRE0);
	// send the data
	UDR0 = data;
}

void send_adc_info() {
	transmit((int8_t)(0.48828125*get_adc_value(0)-50));
}

int main(void)
{
	init_adc();
	uart_init();
	
	while (1)
	{
		send_adc_info();
		_delay_ms(1000); // 1 sec
	}
}

