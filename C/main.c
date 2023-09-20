#include <stdio.h>

//int main(int argc, char *argv[])
//{
//	printf("%d\n", argc);
//	for (int i=0; i < argc; i++){
//		printf("%s\n",argv[i]);
//	}
//	printf("think you!");
//	return 0;
//}

int main(){
	int x = 45;
	for (int i = 65; i <= 122; i++){
		printf("\e[%d%c | _ %d\n",x,i,i);
	}

	return 0;

}