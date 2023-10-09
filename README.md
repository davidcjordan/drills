# Overview
This repository has 3 file types:
* drills in CSV format.  See row 4 of a DRLxxx.csv file for the column titles
* workouts in CSV format (WORKxxx.csv).  001 is the Boomer demonstration showing the capabilities using custom short drills.
* ui_drill_selection_lists.py: read by the python user interface code to define lists of drills and workouts.  These lists define which drills will be shown per category.

# Drill numbering convention

* 1-399: factory programmed drills; not to be modified by the user
* 401-699: Custom, site specific drills, not stored in this repository
* 761-780: Preset Calibration test drills
* 781-800: Preset Calibration drills
* 801-812: Test servoing for each ball type
* 813-820: more testing of servoing
* 821-850: Drills used for demo workout (WORK001)
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
* 912: net

The drill_load.h file has the following drill range defines used by both the launcher code and the UI:
```
#define BEEP_DRILL_NUMBER_START
#define BEEP_DRILL_NUMBER_END
#define THROWER_CALIB_DRILL_NUMBER_START
```

