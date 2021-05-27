---
template: overrides/main.html
title: Frame Detection
---

!!! note
    To navigate through the 2D view:<br>
    &nbsp;&nbsp;&nbsp;&nbsp;**Move crosshairs in all views**: hold `Shift` while moving the mouse<br>
    &nbsp;&nbsp;&nbsp;&nbsp;**Zoom in/out**: hold the `right` mouse button while moving mouse up/down (can hold `Control/Command` and scroll)<br>
    &nbsp;&nbsp;&nbsp;&nbsp;**Pan (translate) scan**: hold `middle-mouse button` while moving the mouse<br>

## Automatic frame detection

Automatic frame detection will work for CT and MRI. From the drop-down menu, next to `Fiducial Volume`, select the volume containing the stereotactic frame. Choose the stereotactic frame that is captured in the CT volume and press `Detect Frame Fiducials`. 

<center>
    <figure>
        <img src="img/frame_detection.png" alt="frame_detection"/>
        <figcaption>Frame detection widget interface.</figcaption>
    </figure>
</center><br>

If the automatic detection was successful you will see an image like this:

<center>
    <figure>
        <img src="img/detected_fiducials.png" alt="frame_fiducials"/>
        <figcaption>Frame fiducials with frame registration errors.</figcaption>
    </figure>
</center><br>

Scroll up/down the slices to check the accuracy of the frame detection. The displayed numbers are the fiducial registration errors, lower values indicate a more accurate registration. Values lower than 0.5mm appear in <span style="color:green">**Green**</span>, while values above 0.5mm appear in <span style="color:red">**Red**</span>. On the left-hand side you will see the overall frame registration error (anything below 0.5 mm should be acceptable).

If you are satisfied with the results, select **Confirm Frame Fiducials**. If you are not satisfied, you can try adjusting frame registration settings and re-run autodection (see ensuing section).

## Adjust frame registration settings

You can modify the default frame registration settings by clicking the **Advanced Settings** box in the frame detection widget.

<center>
    <figure>
        <img src="img/frame_advanced_settings.png" alt="frame_detection_settings"/>
        <figcaption>Frame detection advanced settings.</figcaption>
    </figure>
</center>

* **Transform type (default: Rigidbody):** Rigidbody, Similarity, Affine.
* **Iterations (default: 100):** Set the maximum number of iterations.
* **Max Landmarks (default: 200):** Set the maximum number of frame fiducials to use, each slice in the CT scan contains a set of fiducial points. For instance, if a CT scan is acquired with 124 slices, using a Leksell frame, there would be ~ 600 fiducial points.
* **Match Centroids (default: No):** Starts the process by translating source centroid to target centroid.
* **Reverse Source/Target (default: No):** Will invert the transform so the source is fixed and the target is floating. This is helpful if the target has fewer data samples than the source.
* **Target Point Radius (default: 0.5 mm):** Radius to use for the target frame fiducials.
* **Mean Distance Measure (Default: RMS):** metric to use when measuring the point registration error.

### Troubleshooting automatic frame detection

The first parameter to adjust would be **Match Centroids**, select **Yes**. A pop-up message will appear asking if you want to overwrite the previous frame registration data, select **Yes**:

<center>
    <figure>
        <img src="img/frame_detection_message.png" alt="frame_detection_message"/>
        <figcaption>Frame detection pop-up message.</figcaption>
    </figure>
</center>

If you are still not happy with the registration, try increasing the number of iterations to 200 and re-run. The other parameter you can adjust is the number of iterations, increasing the value to 300. You may also want to try decreasing the radius of the target by 0.1 mm.

The last choice would be to adjust the transform type, however this will introduce some non-linearity into the registration.

## Manual frame detection

To run manual frame detection select the button **Manual Detection**. You will need to identify each frame fiducial one-by-one on the same axial slice. If you are unsure of how the stereotactic frame fiducials are numbered you can press `Frame Fiducial Legend` to see the mapping. All point fiducials will need to be placed on the same axial slice. When you are finished, press **Confirm Frame Fiducials**.

<br><p align="center"><img src="img/manual_frame_dection.png" alt="manual_frame_dection" width="30%"/></p><br>

## Supported Frame Systems

### Leksell frame

<br><p align="center"><img src="img/leksell_drawing.svg" alt="leksell_drawing" width="70%"/></p><br>


<br>
<br>
<br>