#include <unistd.h>
#include <sys/mman.h>
#include <fcntl.h>
#include <sys/stat.h>
#include <sys/types.h>

int main(void){
	int fd;
	struct stat bufx;
	char *x;

	fd = open("teste.txt",O_RDONLY);

	if(fd == -1)
		return 1;

	fstat(fd, &bufx);

	x = mmap(0, bufx.st_size, PROT_READ, MAP_PRIVATE, fd, 0);

	write(1, x, bufx.st_size);
	close(fd);

	return 0;
}