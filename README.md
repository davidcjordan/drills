# drills
CSV format drill files

Drill Number Ranges:
* 1-399: factory programmed drills; not to be modified by the user
* 401-699: Custom, site specific drills, not stored in this repository
* 761-780: Preset Calibration test drills
* 781-800: Preset Calibration drills
* 801-812: Test servoing for each ball type
* 901-912: Preset Beep drills
* 912-979: TBD Custom Beep drills
* 980-999: drills used in regression testing

Drills other than 401-699 are stored in this repository

Preset beep drills:
* 901-905: mini-tennis: very easy, easy, medium, hard, very hard
* 906: volley
* 907: topspin
* 908: flat
* 909: loop
* 910: chip
* 911: random

The drill_load.h file has the following drill range defines used by both the launcher code and the UI:

#define BEEP_DRILL_NUMBER_START
#define BEEP_DRILL_NUMBER_END

#define THROWER_CALIB_DRILL_NUMBER_START
