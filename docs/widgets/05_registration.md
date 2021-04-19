---
template: overrides/main.html
title: Registration
---

## Register patient imaging data

<p align="center"><img src="img/image_registration.png" alt="widget04" /></p>

* **Reference Volume:** the imaging volume that all other images will be registered to.
* **CT Frame:** the imaging volume contains the sterotactic frame.
* **Template Space (optional):** select the template space to be registered to the patients space. 
* **Floating volumes:** the imaging volumes that will be co-registered to the reference volume. You can un-check any imaging volumes you do not want registered.

### Choose registration algorithm

#### NiftyReg

#### FSL

#### ANTS


### Run registration algorithm

Click `Run Registration`. The registration progression will be updated within the `Registration Progress` window. Once registration is completed, you will see the co-registered volumes appear in the floating drop-down box (under `Co-registered Volumes`).

You will now confirm that the registration results by clicking the `Compare Volumes` button. For each registration you will either select `Confirm Registration` or `Decline Registration`. If you choose to decline a registration, you will be able to re-run the registration with a different algorithm.



<br>
<br>
<br>