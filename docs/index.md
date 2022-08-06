---
template: overrides/main_noedit.html
---

<center><img src="img/trajectoryGuide.svg" alt="drawing" style="width:30%;"/></center>

<center><em>An open-source software for neurosurgical trajectory planning, visualization, and postoperative assessment</em></center>

---

<p align="center" style="font-size:38px;">What is trajectoryGuide?</p>

**trajectoryGuide** provides the capability to plan surgical trajectories within 3D Slicer, an open-source medical imaging software. trajectoryGuide contains modules that span the three phases of neurosurgical trajectory planning:

## Preoperative features
   
* automatic stereotactic frame detection (supported frames: Leksell, BRW, and CRW)
* co-registration of MRI and CT scans (incorporated registration algorithms: ANTS, FSL, or NiftyReg)
* trajectory planning providing coordinates in anatomical and stereotactic space (including arc, ring angles)
      
![!Preoperative planning.](img/preoperative_features_01.png)

## Perioperative features

* update final electrode position based on intra-operative testing
* display microelectrode recordings (MER) within the patients MRI space

![!Perioperative planning.](img/preoperative_features_02.png)

## Postoperative features

* electrode localization (using post-op imaging)
* visualize stimulation settings as volume of activated tissue
* view data within a template space (provided spaces: MNI152NLin2009bAsym, MNI152NLin2009cAsym, and PD25)

![!Volume of activated tissue.](img/05_post_programming.png)

<br><br><br>