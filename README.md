# drills
CSV format drill files

Drill Number Ranges:
* 1-399: factory programmed drills; not to be modified by the user
* 401-699: Custom, site specific drills, not stored in this repository
* 761-780: Preset Calibration test drills
* 781-800: Preset Calibration drills
* 901-950: Preset Beep drills
* 951-979: TBD Custom Beep drills
* 980-999: drills used in regression testing

Drills other than 401-699 are stored in this repository

Preset beep drills follow this convention, where the range of 5 is determined by the difficulty (VeryEasy..VeryHard)
* 901-905: mini-tennis 
* 906-910: volley
* 911-915 flat
* 916-920 loop
* 921-925 chip
* 926-930 topspin
* 931-935 random

The drill_load.h file has the following drill range defines used by both the launcher code and the UI:

#define BEEP_DRILL_NUMBER_START
#define BEEP_DRILL_NUMBER_END

#define THROWER_CALIB_DRILL_NUMBER_START
