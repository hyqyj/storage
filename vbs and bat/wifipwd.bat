for /F "tokens=2 delims=:" %%i in ('netsh wlan show profiles TP-LINK_A7DA key^=clear ^| findstr "�ؼ�����"') do echo TP-LINK_A7DA �����ǣ� %%i 
