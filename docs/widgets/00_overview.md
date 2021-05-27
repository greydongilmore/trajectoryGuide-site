---
template: overrides/main.html
title: Overview
---

## Neuronavigation

The main goal of image guidance in neurosurgery is to accurately project magnetic resonance imaging (MRI) and/or computed tomography (CT) data into the operative field for defining anatomical landmarks, pathological structures and margins oftumors. To achieve this, "neuronavigation" software solutions have been developed to provide precise spatial information to neurosurgeons. Safe and accurate navigation of brain anatomy is of great importance when attempting to avoid important structures such as arteries and nerves.

Neuronavigation software provides orientation information to the surgeon during all three phases of surgery: 1) pre-operative trajectory planning, 2) the intraoperative steroetactic procedure, and 3) post-operative visualization. Trajectory planning is performed prior to surgery using preoperative MRI data. On the day of surgery, the plans are transferred to sterotactic space using a frame or frame-less system. In both instances, a set of radiopaque fiducials are detected, providing the transformation matrix from anatomical space to sterotactic space. During the surgical procedure, the plans are updated according to intraoperative data collected (i.e. microelectrode recordings, electrode stimulation etc.). After the surgery, post-operative MRI or CT imaging confirms the actual position of the trajectory(ies).

## trajectoryGuide?

**trajectoryGuide** is an open-source software suite that provides the capability to plan neurosurgical trajectories within 3D Slicer. **trajectoryGuide** contains several modules that span the three phases of surgical intervention: pre-op, intra-op, and post-op.

<br>
<br>
<br>