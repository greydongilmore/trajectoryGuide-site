
# Input Directory Setup

This section outlines how the data should be organized prior to running the **edf2bids** software. The data files should be in EDF/EDF+ format following the <a href="https://www.edfplus.info/specs/edf.html" target="_blank">specifications</a> provided by the EDF format developers. 

[Setup a working directory](04_input_dir_setup.html#setup-a-working-directory) is a recommemded way to organize your working directory of data (this is optional but highly recommended).

[Option 01: Do not specify visit/session number](04_input_dir_setup.html#option-01-do-not-specify-visitsession-number) should be followed if you do not have a specific naming convention for visits and sessions. In this option, the visit and session number are not supplied to the **edf2bids** software and instead are calculated based on the date/time of the EDF/EDF+ aquisition.

[Option 02: Specify visit/session number](04_input_dir_setup.html#option-02-specify-visitsession-number) should be followed for data from the **EpLink study**.

    At this moment the names of the EDF/EDF+ files are not yet BIDS compliant, but they do contain some metadata in the filename that will be used later.

## Setup a working directory

It is recommended that you establish a working directory to ensure your data remains organized. The optimal setup would be one with 4 directories:

* **unorganized**: this directory holds unorganized subject data ready to be organized for **edf2bids**
* **organized**: this directory holds organized subject data ready to be organized for **edf2bids** (according to either option below)
* **input**: this directory holds subject data ready to be converted with **edf2bids**
* **output**: this directory holds the output converted data from **edf2bids**

!!! warning
    When beginning a conversion with **edf2bids** ensure the **output** directory is empty and the **input** directory only contains the subject folders you wish to convert.

### Example

#### Static

```sh

working_dir/
├── unorganized/
├── organized/
├── input/
└── output/

```


<div id="tree"></div>
<script>
    $(document).ready(function() {
      $.ajax({
          url : "../../assets/working_dir.json",
          dataType: "text",
          success : function (tree) {
              $('#tree').bstreeview({ data: tree });
          }
      });
});
</script>

## Option 01: Do not specify visit/session number

If you do not need to specify the visit or session number for each EDF file for the subjects, then this option will assign session numbers based on the **Date** timestamp within the EDF files. So the earliest EDF file will be given **ses-001** while the latest EDF file will be given **ses-###** (### will be equal to the number of EDF files for that subject).

!!! important "Input directory"
    The input directory (`input`) should contain a sub-directory for each of the subjects you want to have converted (i.e. `input\sub-001`, `input\sub-002` etc.). Within the **edf2bids** software you select `input` as the input directory and not the individual subject directories

### Example

    for a complete list of terms see the [definitions page](02_definitions.html#filename-terms)

#### Static

```sh

input/
├── <sub_num>/                                          # Individual subject directory
│   ├── X~X_432a35cf-adg25-462-24aa-325db4e5e2d3.edf    # Individual EDF files
│   └── X~Xe_7d22151a-ac455-3adc312b-426aae3251ac.edf
│
└── <sub_num>/                                          # Individual subject directory
    ├── X_ X_35a1ed7a-7764-4cb0-8571-51026e3dbef4.edf   # Individual EDF files
    └── X_X_e515c5ac-6301-4acd-8a69-fb208d5fd097.edf

```


<div id="tree2"></div>
<script>
    $(document).ready(function() {
      $.ajax({
          url : "../../assets/no_ses_visit.json",
          dataType: "text",
          success : function (tree) {
              $('#tree2').bstreeview({ data: tree });
          }
      });
});
</script>

## Option 02: Specify visit/session number

In some instances you may want to manually assign the specific visit or session numbers for the EDF files. In this scenario you would need to place each EDF file into a directory with the following naming scheme:

```sh
<sub_num>_<visit_num>_<ses_num>_<type>_<task>_[RET]
```

    for a complete list of terms see the [definitions page](02_definitions.html#filename-terms)

```sh
sub-003_02_SE01_IEEG_FULL_RET
```

A folder with the above naming scheme would indicate this is subject 3's second visit and first session. The data collected was a full IEEG recording that was retrospective (recorded prior to the subject consent).

!!! important "Input directory"
    The input directory (`input`) should contain a sub-directory for each of the subjects you want to have converted (i.e. `input\sub-001`, `input\sub-002` etc.). Within the **edf2bids** software you select `input` as the input directory and not the individual subject directories
    
### Example

Each day of recording should be in a separate folder within the subject directory:

#### Static

```sh

input/
├── <sub_num>/                                                # Individual subject directory
│   │
│   ├── <sub_num>_<visit_num>_<ses_num>_<type>_<task>_[RET]/  # Specify visit, session, type, and task
│   │   │
│   │   ├── X~X_432a35cf-adg25-462-24aa-325db4e5e2d3.edf      # Individual EDF files
│   │   └── X~Xe_7d22151a-ac455-3adc312b-426aae3251ac.edf     # Individual EDF files
│   │
│   └── <sub_num>_<visit_num>_<ses_num>_<type>_<task>_[RET]/  # Specify visit, session, type, and task
│       │     
│       └── X~X_432a35cf-adg25-462-24aa-325db4e5e2d3.edf      # Individual EDF files
│
└── <sub_num>/                                                # Individual subject directory
    │
    └── <sub_num>_<visit_num>_<ses_num>_<type>_<task>_[RET]/  # Specify visit, session, type, and task
        │
        ├── X~X_432a35cf-adg25-462-24aa-325db4e5e2d3.edf      # Individual EDF files
        └── LastName~ FirstName_7d22151a-ac455-3adc312b-426aae3251ac.edf     # You can include the subject first/last name to be used when de-identifying the data

```


<div id="tree3"></div>
<script>
    $(document).ready(function() {
      $.ajax({
          url : "../../assets/specify_ses_visit.json",
          dataType: "text",
          success : function (tree) {
              $('#tree3').bstreeview({ data: tree });
          }
      });
});
</script>

## Imaging Data

**edf2bids** will anonymize imaging DICOM files if they are present within the input directory. The DICOMs should be within a directory named **imaging**, which is at the root of the subjects directory. Within the **imaging** directory should be another directory with the desired output name for the zipped directory (containing all the anonymized DICOMs). The directories containing the actual DICOM files can be given any name, genrally they are named after the specific sequence aquired for the DICOMs inside.

### Example

#### Static

```sh

input/
├── <sub_num>/                                          # Individual subject directory
    ├── X~X_432a35cf-adg25-462-24aa-325db4e5e2d3.edf    # Individual EDF files
    ├── X~Xe_7d22151a-ac455-3adc312b-426aae3251ac.edf
    └── <imaging>/                                      # Imaging directory for dicoms
        └── <sub_num>_<visit_num>_<ses_num>/            # session directory for dicoms, this name will be given to output zipped folder
            ├── T1w_scan/<*.dcm files>                  # DICOM directories, can be given any name
            ├── T2w_scan/<*.dcm files>
            └── dwi/<*.dcm files>

```


<div id="tree4"></div>
<script>
    $(document).ready(function() {
      $.ajax({
          url : "../../assets/imaging_data.json",
          dataType: "text",
          success : function (tree) {
              $('#tree4').bstreeview({ data: tree });
          }
      });
});
</script>


