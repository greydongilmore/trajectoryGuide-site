---
template: overrides/main.html
title: Overview
---

## Neuronavigation

The main goal of image guidance in neurosurgery is to accurately project magnetic resonance imaging (MRI) and/or computed tomography (CT) data into the operative field for defining anatomical landmarks, pathological structures and margins oftumors. To achieve this, "neuronavigation" software solutions have been developed to provide precise spatial information to neurosurgeons. Safe and accurate navigation of brain anatomy is of great importance when attempting to avoid important structures such as arteries and nerves.

Neuronavigation software provides orientation information to the surgeon during all three phases of surgery: 1) pre-operative trajectory planning, 2) the intraoperative steroetactic procedure, and 3) post-operative visualization. Trajectory planning is performed prior to surgery using preoperative MRI data. On the day of surgery, the plans are transferred to sterotactic space using a frame or frame-less system. In both instances, a set of radiopaque fiducials are detected, providing the transformation matrix from anatomical space to sterotactic space. During the surgical procedure, the plans are updated according to intraoperative data collected (i.e. microelectrode recordings, electrode stimulation etc.). After the surgery, post-operative MRI or CT imaging confirms the actual position of the trajectory(ies).

## trajectoryGuide

**trajectoryGuide** is an open-source software suite that provides the capability to plan neurosurgical trajectories within 3D Slicer. **trajectoryGuide** contains several modules that span the three phases of surgical intervention: pre-op, intra-op, and post-op.

## Prior Art

### Open source

#### PyDBS

Developed by Pierre Jannin. The software is not freely available, a description of the tool can be found in <a href="https://hal.archives-ouvertes.fr/inserm-01116063" target="_blank">this publication</a>.

#### Tactics

Developed by David G. Gobbi and Yves P.Starreveld. The software is available on <a href="https://github.com/Atamai/tactics" target="_blank">GitHub</a>.

#### Ogles2

Developed by Johannes A. Koeppen and based on **Ogle** written by Dr. Michael J Gourlay. The software can be downloaded from <a href="https://sourceforge.net/projects/ogles/files/ogles2/" target="_blank">Sourceforge</a> or the <a href="http://neuranse.com/projects.html" target="_blank">Neuranse</a> website.

### Commercial software

#### StealthStation S8

Developed by Medtronic. More information can be found on their <a href="https://www.medtronic.com/ca-en/healthcare-professionals/products/neurological/surgical-navigation-systems/stealthstation/stealthstation-s8.html" target="_blank">website</a>.

#### neuroinspire

Developed by Renishaw. More information can be found on their <a href="https://www.renishaw.com/en/neuroinspire-neurosurgical-planning-software--8244" target="_blank">website</a>.

#### Elements

Developed by Brainlab. More information can be found on their <a href="https://www.brainlab.com/surgery-products/overview-neurosurgery-products/brainlab-elements/" target="_blank">website</a>.

#### Inomed Planning System

Developed by Inomed. More information can be found on their <a href="https://www.en.inomed.com/products/functional-neurosurgery/ips/" target="_blank">website</a>.

#### MNPS

Developed by Mevis. More information can be found on their <a href="http://www.mevis.com.br/mnps-2.html" target="_blank">website</a>.

#### NeuroSight

Developed by Integra. More information can be found on their <a href="https://integralife.eu/products/neuro/stereotaxy/neurosight-arc-software-laptop/" target="_blank">website</a>.

<br>
<br>
<br>