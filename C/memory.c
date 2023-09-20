#include <windows.h>
#include <stdio.h>

int int main(int argc, char const *argv[])
{
	HANDLE processHandle;
	PROCESS_MEMORY_COUNTERS_EX pmc;

	processHandle = OpenProcess(PROCESS_QUERY_INFORMATION | PROCESS_VM_READ, FALSE, 1234); // 1234为进程ID
	if (processHandle == NULL){
		printf("OpenProcess failed.\n");
		return 1;
	}
	if (GetProcessMemoryInfo(processHandle, (PROCESS_MEMORY_COUNTERS*)&pmc, sizeof(pmc))){
		printf("Virtual Memory: %lld bytes\n", pmc.PrivateUsage);
	}
	CloseHandle(processHandle);
	return 0;
}