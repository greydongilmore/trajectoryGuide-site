---
template: overrides/main.html
title: Definitions
---

## Filename terms

Throughout this documentation the following filename terms will be used:

<center>

| term           | definition |
|---------------|------------------------------------------------------|
| `sub_num` <img width="100"></img> | specific subject number |
| `visit_num` | each stay within the hospital (2 digits) |
| `ses_num` | each day spent in hospital during the visit (2 digits starting with SE, ex. SE01) |
| `type` | type of data collected (should be _IEEG/_EEG) |
| `task` | format of the edf data (should be _CLIP/_FULL/_CS) |
| `RET`  | if included, indicates the study is retrospective <sup>1</sup> |

</center>

<sup>1</sup> if not present then study assumed to be prospective (PRO), so you do not need to include this flag for prospective sessions

!!! note "Note on Visit Numbers"
    * If any retrospective studies exist for a subject, they should be assigned the first visit number 01
    * All following admissions to the hospital would be given incremental visit numbers (i.e. visit 2: 02, visit 3: 03)
    * Two separate admissions to the hospital should not have the same visit number
    * Scalp and Intracranial recordings should have distinct visit numbers (ex. If 01 is used for the participant’s first stay in the EMU for scalp EEG, 02 should be used if they come back for intracranial EEG)

!!! note "Note on Session Numbers"
    If a day in sequence of sessions is missing/not present this session number should still be accounted for
    e.g. 
    ```sh
    ses-001 (data present), ses-002 (data missing), ses-003 (data present)
    ```
    The directory naming would look like:
    ```sh
    sub-003_01_SE01_IEEG_FULL_RET
    sub-003_01_SE03_IEEG_FULL_RET
    ```
    Notice that no folder is specified for the missing ses-002 but the number is still accounted for by skipping it.


## edf2bids terms

Within the edf2bids software, the columns present within the input/output windows are:

<center>

|term           |definition |
|---------------|------------------------------------------------------|
| `Name` <img width="250"></img> | this is the name of the subdirectory within the patient folder that contains the EDF/EDF+ file. If the EDF/EDF+ files are all in the same directory, then the name will be the name of the EDF/EDF+ files. |
| `Date` | the date the data was recorded |
| `Time` | the time the data was recorded |
| `Size` | the size of the EDF/EDF+ file in gigabytes |
| `Frequency`  **[modifiable]** | the frequency the data was recorded at. This is automatically calculated based on information extracted from the EDF/EDF+ file. However, if there is an error then the user can double click on the frequency box and manually change it |
| `Duration` | the total duration of the EDF/EDF+ file recording, which is automatically calculated |
| `EDF Type` | type of EDF+ file (EDF+D/EDF+C). This field should always show EDF+C, if EDF+D then the file should be [converted first](05_check_edf_type.html#convert-edf-type) |
| `Type`  **[selectable]** | the type of EEG data collected (Intracranial or Scalp). This value is automatically detected by the flags `_EEG/_IEEG` used in the directory name. This value can be changed by the user if there is an error |
| `Task`  **[selectable]** | the condition of the recorded file: Full, clip or cortical stimulation (CS). This value is automatically detected by the flags `_CLIP/_FULL/_CS` used in the directory name. This can be changed by the user if there is an error |
| `Ret/Pro`  **[selectable]** | whether the data file is retrospective or prospective. This value is automatically detected based on the RET flag used in the directory name. This value can be changed by the user if there is an error |
| `Channel File` | this indicates if a channel_labels.txt file was found. If you notice the labels changed in a specific session you can include a channel_label.txt file within each session folder. Yes indicates a channel label file was found, No otherwise |
| `Imaging Data` | this indicates if an `imaging` directory was found in the root of the subjects directory. Yes indicates the directory was found, No otherwise |

<br>
<br>
<br>