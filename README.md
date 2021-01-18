# Desktop Peripherals

This code is to support a peripheral device I use for personal/work workflow enhancements.

Currently there is support for three potentiometers which I plan to use to create a sequencer/synth from this device as well. Currently though only one potentiometer is used to controll which "mode" the device is in. 

## Web Mode:

Lower 1/3 range of pots

Opens my personal bookmarks, stored a few sane defaults here. Add your own to the dictionary in controller_modes.web_mode

## Work Mode:

Middle third range of pots.

Opens work related bookmarks, edit in controller_modes.work_web_mode

## Shortcut Mode:

Upper third range of pots.

Keyboard shortcuts, edit in controller_modes.shortcut


## Uno Setup:

Plug it in, set it to com 3, baud 9600. Upload the sketch in trellis_and_potentiomenter.


## Run it:

```bash
pip3 install requirements.txt
python3 start.py
```