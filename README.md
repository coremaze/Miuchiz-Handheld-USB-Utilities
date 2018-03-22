# Miuchiz-Handheld-USB-Utilities
Utilities for dealing with the Miuchiz handheld devices over USB

#### `HandheldCore.py` contains the `Handheld` class which deals with all low level interactions with the Miuchiz handheld device.


  Classmethod `Handheld.FindHandhelds()` will return a list of drives of all Miuchiz handhelds connected.
  
  Method `Handheld.IsHandheld()` determines if the associated drive is a Miuchiz device.
  
  Method `Handheld.ReadPage(bank, page)` returns a bytes object of length 0x1000 containing the data at some page of the device. Banks range from 0\~1 and pages range from 0\~255
  
  Method `Handheld.WritePage(data, bank, page)` writes a bytes object of length 0x1000 to some page of the device. Banks range from 0\~1 and pages range from 0\~255
  
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
 
 #### `SetCreditz.py` will set the number of creditz on the first connected Miuchiz.
 
    Usage: SetCreditz.py <creditz>
    Example: SetCreditz.py 123456
    
 ---
 
 #### `ReadButtons.py` will print out the currently pressed buttons of the first connected Miuchiz.
 
    Usage: ReadButtons.py
    
 ---
 
 #### `Eject.py` will disconnect the first connected Miuchiz from the computer.
 
    Usage: Eject.py 
