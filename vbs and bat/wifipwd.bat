for /F "tokens=2 delims=:" %%i in ('netsh wlan show profiles TP-LINK_A7DA key^=clear ^| findstr "¹Ø¼üÄÚÈİ"') do echo TP-LINK_A7DA ÃÜÂëÊÇ£º %%i 
