#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

int reverseBits(uint32_t n)
{
	int result = 0;
	int moveCount = 0;
	while (n)
	{
		result <<= 1;
		if (n & 0x1)
			result |= 1;
		n >>= 1;
		moveCount++;
	}

	result <<= (32 - moveCount);
	return result;
}

int main(int argc, char const *argv[])
{
	/* code */
	uint32_t test = 43261596;
	printf("result: %u\n", reverseBits(test));
	return 0;
}