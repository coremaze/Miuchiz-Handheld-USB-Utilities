# Miuchiz-Handheld-USB-Utilities
Utilities for dealing with the Miuchiz handheld devices over USB

---

These tools require Python3 to use. https://www.python.org/

These tools require pywin32. `pip.exe install pywin32`

You can download the tools here: https://github.com/ChrisMiuchiz/Miuchiz-Handheld-USB-Utilities/archive/master.zip

---

### Connecting a Miuchiz to a computer

  A Miuchiz can be connected to the computer in two ways:
  
  1) Navigate to the computer room on the handheld and use the computer. The Miuchiz can connect over USB.
  
  2) Hold LEFT and MENU while powering on the device. If the device has batteries, only pressing the RESET button will truly reboot the device. This will put it into PC mode and it will say "Please Connect to PC" and at that point it can connect over USB.


### Demo mode

  Sometimes, modifying the flash can cause a handheld to enter demo mode. To exit demo mode, hold DOWN and MENU while powering on the device. If the device has batteries, only pressing the RESET button will truly reboot the device.

---
---

#### `HandheldCore.py` contains the `Handheld` class which deals with all low level interactions with the Miuchiz handheld device.


  Classmethod `Handheld.FindHandhelds()` will return a list of valid `Handheld`s connected to the computer.
  
  Method `Handheld.IsHandheld()` determines if the associated drive is a Miuchiz device.
  
  Method `Handheld.ReadPage(bank, page)` returns a bytes object of length 0x1000 containing the data at some page of the device. Banks range from 0\~1 and pages range from 0\~255.
  
  Method `Handheld.WritePage(data, bank, page)` writes a bytes object of length 0x1000 to some page of the device. Banks range from 0\~1 and pages range from 0\~255.
  
  Method `Handheld.WriteFull(d, output=True)` writes an entire flash dump back to the device. `d` can be either a bytes object or a file name. `output` will make the program print out its progress.
  
  Method `Handheld.DumpFull(filename, output=True)` creates an entire flash dump of the device and writes it to a file. `output` will make the program print out its progress.
  
  Method `Handheld.Eject()` will cause the Miuchiz device to disconnect from the computer.
  
  Method `Handheld.ReadRamLeak()` returns some RAM data from the Miuchiz device.
  
  ---
  
  #### `DumpFlash.py` will dump the entire flash of the first connected Miuchiz to a file.
  
    Usage: DumpFlash.py <file>
    Example: DumpFlash.py miuchiz.dat
    
 ---
 
 #### `LoadFlash.py` will write an entire flash dump from a file to the first connected Miuchiz.
 
    Usage: LoadFlash.py <file>
    Example: LoadFlash.py miuchiz.dat
    
 ---
 
 #### `FastLoad.py` will write an entire flash dump to the first connected Miuchiz, but will maintain a local copy of the handheld's flash. 
 
This is in case you want to frequently test changes to a handheld and don't want to wait for unchanged pages to be written again.
 
    Usage: FastLoad.py <Flash clone file> <Flash load file>
    Example: FastLoad.py clonefile.dat writefile.dat
    
 ---

  
 #### `DumpOTP.py`  will dump the entire OTP of the first connected Miuchiz to a file. 
 
The OTP (**O**ne-**T**ime-**P**rogrammable) is a read-only portion of code responsible for booting the device.

    Usage: DumpOTP.py <file>
    Example: DumpOTP.py otp.dat
    
 ---
 #### `SetCreditz.py` will set the number of creditz on the first connected Miuchiz.
 
    Usage: SetCreditz.py <creditz>
    Example: SetCreditz.py 123456
    
 ---
 
 #### `ReadButtons.py` will print out the currently pressed buttons of the first connected Miuchiz.
 
    Usage: ReadButtons.py
    
 ---
 
 #### `Eject.py` will disconnect the first connected Miuchiz from the computer.
 
    Usage: Eject.py 

 ---
 
 #### `ReadCreditz.py` will print the number of creditz on the Miuchiz.
 
    Usage: ReadCreditz.py 
