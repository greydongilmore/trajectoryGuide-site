---
template: overrides/main.html
title: Data Import
---

!!! warning
    If you have not installed **trajectoryGuide** into 3D Slicer please follow the <a href="../installation.html" target="_blank">installation instructions</a>.

&emsp;&emsp;The first module in **trajectoryGuide** handles the import of patient imaging data. The data should be within a single directory, this directory will be selected within the import window (do not select the files within the directory). During the initial data import for a patient, **trajectoryGuide** will store a copy of the imaging data into a `source` directory as a backup, these files will remain unchanged.

&emsp;&emsp;**trajectoryGuide** stores all imaging data in *NIFTI (Neuroinformatics Technology Initiative)* format, with the file extension `.nii.gz`. If the original imaging data is in DICOM format, the files will first need to be converted to NIFTI according to BIDS (see section above).

## Data directory

### Input directory structure

&emsp;&emsp;**trajectoryGuide** requires the input data folder to be organized according to <a href="https://bids.neuroimaging.io/" target="_blank">Brain Imaging Data Structure (BIDS)</a>. The following is an example input directory.

```
bids/
    ├── dataset_description.json
    └── sub-<subject_label>/
        └── ses-<ses_label>/
            ├── anat/
            │   ├── sub-<subject_label>_ses-<ses_label>_T1w.nii.gz
            │   ├── sub-<subject_label>_ses-<ses_label>_PD.nii.gz
            │   └── sub-<subject_label>_ses-<ses_label>_acq-Tra_T2w.nii.gz
            └── ct/
                └── sub-<subject_label>_ses-<ses_label>_acq-Frame_ct.nii.gz
```

### Output directory structure

&emsp;&emsp;**trajectoryGuide** trajectoryGuide stores processed data within the derivatives directoy of the BIDS dataset.

```java
bids/
    ├── dataset_description.json
    └── sub-<subject_label>/...
derivatives/
    └── trajectoryGuide/
        └── sub-<subject_label>/
                ├── sub-<subject_label>_surgical_data.json
                ├── sub-<subject_label>_T1w.nii.gz
                ├── sub-<subject_label>_T1w.json
                ├── sub-<subject_label>_space-T1w_acq-Tra_T2w.nii.gz
                ├── sub-<subject_label>_space-T1w_acq-Tra_T2w.json
                ├── sub-<subject_label>_desc-rigid_from-TraT2w_to-T1w_xfm.h5
                ├── sub-<subject_label>_space-T1w_PD.nii.gz
                ├── sub-<subject_label>_space-T1w_PD.json
                ├── sub-<subject_label>_desc-rigid_from-PD_to-T1w_xfm.h5
                ├── sub-<subject_label>_ses-pre_coordsystem.json
                ├── settings/...
                ├── source/...
                ├── space/...
                └── summaries/...
```

&emsp;&emsp;Each image volume has an associated `.json` file that stores metadata associated with the volume as it progresses through the **trajectoryGuide** workflow. Select the import options prior to loading the patient directory.

<center>
    <figure>
        <img src="img/patient_directory_wig.png" alt="patient_directory_wig"/>
        <figcaption>Patient directory module in trajectoryGuide.</figcaption>
    </figure>
</center>

* **Implanted Sides:** indicate if the trajectory plan will be unilateral or bilateral
* **Rename Scans:** trajectoryGuide will rename the imaging data to comply with BIDS format, the imaging filenames will be shortened
* **Use Previously Values:** this option is recommended. If the patient directory has already been loaded by trajectoryGuide, then the previous data values will be re-loaded

<br>
<br>
<br>