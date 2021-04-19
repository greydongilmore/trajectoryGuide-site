
# Check EDF Type

    for a detailed explanation of the EDF format see the [description page](../index.html#edf-file-structure)

## EDF Type Overview

Only EDF+ files can be stored in either a continuous (EDF+C) or discontinuous (EDF+D) format, while EDF files can only be continuous. A discontinuity within the EDF+ file would occur when the recording is stopped and subsequently started again, resulting in a lapse in recording time. There are two ways to account for the missing data during the non-recording period:

* **Continuous:** to keep the timeline in the file continuous, the data record during the non-recording time can be filled with zeros. This would maintain the timeline within the file.
* **Discontinuous:** ignore the time the recording stopped and "Glue" the different recording sessions together. This creates a jump in the timeline of the EDF+ file.

For most applications, the EDF+ file will need to be in `EDF+C` format. The majority of softwares and analysis tools require this.

## Convert EDF Type

You need to ensure all EDF+ files are in continuous format (EDF+C). This is easy to check within **edf2bids**. 

1. Ensure your input directory [has been organized](04_input_dir_setup.html#setup-a-working-directory) prior to opening within **edf2bids**.
2. Within **edf2bids** select the input directory and check the `EDF Type` column. You should flag any file that is in `EDF+D` format.
3. Once you have identified the files that are in `EDF+D` format, open [EDFBrowser](../installation.html#edfbrowser), select **Tools** at the top and **Convert EDF+D to EDF+C**.

![drawing](img/check_edf_type_01.png)
4. A dialog box will open allowing you to select one of the identified files that is in `EDF+D` format, select one file.
5. Once conversion is complete you will notice the original file remains but now there are several smaller files with a 4 digit suffix accounting for the number of times the recording was stopped/started.

