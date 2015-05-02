#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

int hammingWeight(uint32_t n)
{
	int count = 0;
	while (n)
	{
		if (n & 0x1)
		{
			count++;
		}
		n >>= 1;
	}

	return count;
}

int main(int argc, char *argv[])
{
	uint32_t test = 0b10101010101;
	printf("ans = %d\n", hammingWeight(test));
	return 0;
}

