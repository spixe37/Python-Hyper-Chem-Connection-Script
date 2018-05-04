# Python-Hyper-Chem-Connection-Script
Library to use python with HyperChem

This library allow use Python with HyperChem. 

Functions:

connect() -> bool
Returns can script be connected with HyperChem or not.

disconnect() -> None
Dissconnect from HyperChem.

exec_text(query: str) -> bool
Send text command to HyperChem. Returns bool that command is succefully or not.

query_text(query: str) -> str
Get value of parameter.