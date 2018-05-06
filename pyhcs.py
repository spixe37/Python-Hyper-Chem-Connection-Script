import ctypes
import os

path = os.getcwd() + './hapi.dll'
hapi = ctypes.WinDLL(path)

hcConnect = hapi.hcConnect
hcConnect.restype = ctypes.c_bool

hcDisconnect = hapi.hcDisconnect
hcDisconnect.restype = ctypes.c_bool

hcExecTxt = hapi.hcExecTxt
hcExecTxt.argtypes = [ctypes.c_char_p]
hcExecTxt.restype = ctypes.c_bool

hcQueryTxt = hapi.hcQueryTxt
hcQueryTxt.argtypes = [ctypes.c_char_p]
hcQueryTxt.restype = ctypes.c_char_p

def exec_text(query: str) -> bool:
    return hcExecTxt(query.encode())

def query_text(query: str) -> str:
    return hcQueryTxt(query.encode()).decode('utf-8')

def connect():
    return hcConnect(b"")

def disconnect():
    return hcDisconnect()
        
# hcConnect("")
# hcExecTxt(b"window-color yellow")