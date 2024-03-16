# live-daemon
Simple MIDI hander for Python 3.4

## System requirements
- Windows XP
- MIDI Device
- VIA C3-1000A (Intel Pentium 4 equivalent or higher recommended)
- 384 MB RAM (1GB or more recommended)
- 200 MB available disk space (100 MB if drivers are already installed)

## Prerequisites
- [Python 3.4.4](https://www.python.org/ftp/python/3.4.4/python-3.4.4.msi)
- [rtmidi 1.1.0](https://files.pythonhosted.org/packages/7c/0b/6fb1c8d1a00ae8347800b8a1fdfa06595fa952420b9ee6013fb878e950e5/python_rtmidi-1.1.0-cp34-cp34m-win32.whl) (for MIDI handling)

## Setup
### Installation
- Clone master and unzip root files to some directory. e.g.: `C:\Synth`
- Install Python 3.4.4. Be sure to tick the option to add Python to system PATH during installation.
- Rename `rtmidi-1.1.0-cp34-cp34m-win32.whl` to `python_rtmidi-1.1.0-cp34-none-any.whl`
- Install rtmidi using pip: `pip install python_rtmidi-1.1.0-cp34-none-any.whl`
### Configuration
- Run `get-ports.py`. All available MIDI ports on the system are displayed. The trailing digit is the ID of the port.
- Open `synth.cfg` using Notepad, and set the value `In` to the ID for your desired MIDI port. e.g.: `In = 0`

### Run at startup
- Navigate to your startup directory. e.g.: `C:\Documents and Settings\[Your Username]\Start Menu\Programs\Startup`
- Create a shortcut for `LIVE_Dumb_Daemon.py` in your startup directory.

## Files overview
### Scripts
- LIVE_Dumb_Daemon.py - main application that does everything important. Run at boot time or whenever you wish. Requires that USBLCDServer also be running.
- get_ports.py - show all the midi ports available on the system (this is needed to set up synth.cfg)
