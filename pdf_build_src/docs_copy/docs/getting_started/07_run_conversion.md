
# Run Conversion

## Input directory selection

The input directory selected here should be organized according to the first section in this documentation. Prior to loading the data, make sure all the settings in the settings panel have been configured to your specification (found at the bottom left of the main window).

1. In the software, select **Input Directory** and choose the directory that contains the data to be converted (select the main/root directory that contains all subject directories). Click **Select Folder** in the window and the data will load into the **Input Directory** window.


2. You will now be able to review the information that was detected about the input files. Each subject is expandable by clicking the box beside the subject name. The columns displayed are:

    for a complete list of column explanations see the [definitions page](02_definitions.html#edf2bids-terms)

## Output directory selection

1. Once you have confirmed the input data is correct, click **Output Directory** and select the directory you want the BIDS dataset to appear. The **Output Directory** window will now present the final output file information (prior to conversion). This is the final check to ensure that any changes have been updated.


        EDF/EDF+ files in the Input Directory will be **COPIED** to the new location and will be renamed to be BIDS compliant. Thus, you will have two copies of the EDF/EDF+ files. This is a safety measure in case an error occurs in the conversion, the source data will remain intact.


2. If you are converting data for a participant that already has recordings in the output folder, the checkboxes for those recordings will appear checked in the **Output Directory** window.

## Convert to BIDs

1. Once you have confirmed the Output Directory file information is correct press the green **Convert** button.

2. During the conversion process you can cancel the conversion at any time by pressing the **Cancel** button. However, if you cancel the conversion you will need to delete the contents of the output directory and start over.

3. You will receive updates in the **Conversion Status** window. The final notice, once the conversion is complete, will show **Your data has been BIDsified!**. 


## Convert to SPReD (EpLink)

        files will be moved from the BIDS structure to SPReD structure (the BIDs format will be destroyed)

The format required to upload the Brain-CODE is different from BIDS. This conversion step will provide a SPReD compliant format output.

1. Following successful conversion to BIDS, a new button in the main window will become active named **SPReD**.

2. Press the **SPReD** button and wait for the conversion to complete.
    

## Imaging Anonymization

If an `imaging` directory was supplied in the input directory then the blue **imaging** button will be active. Certain DICOM viewers and analysis tools require specific DICOM header tags to be present. Complete removal of these tags may render the DICOMS unreadable by these tools. Instead, the DICOM header tags that are deemed an identifier are overwritten by random data. The tool used to perform this action is <a href="https://github.com/blairconrad/dicognito" target="_blank">dicognito</a>.

??? note "Anonymized DICOM tags"
    | Attribute     | Description         |
    |---------------|---------------------|
    | AccessionNumber (0008,0050) | A RIS generated number that identifies the order for the Study. |
    | FillerOrderNumberImagingServiceRequest (0040,2017) | The order number assigned to the Imaging Service Request by the party filling the order. |
    | InstitutionName (0008,0080) | Institution where the equipment that produced the Composite Instances is located. |
    | InstitutionAddress (0008,0081) | Mailing address of the institution where the equipment that produced the Composite Instances is located. |
    | InstitutionalDepartmentName (0008,1040) | Department in the institution where the equipment that produced the Composite Instances is located. |
    | OtherPatientNames (0010,1001) | Other names used to identify the Patient. |
    | PatientID (0010,0020) | Primary hospital identification number or code for the patient. |
    | PerformedProcedureStepID (0040,0253) | User or equipment generated identifier of that part of a Procedure that has been carried out within this step. |
    | PlacerOrderNumberImagingServiceRequest (0040,2016) | The order number assigned to the Imaging Service Request by the party placing the order. |
    | RequestedProcedureID (0040,1001) | Identifier that identifies the Requested Procedure in the Imaging Service Request. |
    | ScheduledProcedureStepID (0040,0009) | Identifier that identifies the Scheduled Procedure Step. |
    | StationName (0008,1010) | User defined name identifying the machine that produced the Composite Instances. |
    | StudyID (0020,0010) | User or equipment generated Study identifier. |

??? note "Removed DICOM tags"
    | Attribute/Tag | Description         |
    |---------------|---------------------|
    | CountryOfResidence (0010,2150) | Country in which patient currently resides. |
    | Occupation (0010,2180) | Occupation of the Patient. |
    | PatientAddress (0010,1040) | Legal address of the named patient. |
    | RegionOfResidence (0010,2152) | Region within patient's country of residence. |
    

1. Following conversion to BIDS/SPReD, press the blue button named **Imaging**.

2. Wait for the conversion to complete.
    
![drawing</center>
](img/final_message_imaging.png)
