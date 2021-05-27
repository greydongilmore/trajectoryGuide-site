---
template: overrides/main_noedit.html
title: Installation
---

# Installation

## Requirements

### 3D Slicer

- 3D Slicer **(Version 4.11.0 or later)**, Download from the <a href="https://download.slicer.org/" target="_blank">3D Slicer website</a>.

### trajectoryGuide source code

- download the latest version of trajectoryGuide from the <a href="https://github.com/greydongilmore/trajectoryGuide" target="_blank">GitHub repository</a>.
- unzip the folder and save it somewhere on your system

### Template space directory

- you will need to download the template space directory from this <a href="https://drive.google.com/file/d/1qlJXICMB-P0FxyjGA1PvGtsPkfjw5wn6/view?usp=sharing" target="_blank">Google drive folder</a>.
- you will need to unzip this folder and place it inside the trajectoryGuide directory at the path `resources/ext_libs/space`

## 3D Slicer setup

### Install Python libraries

1. You will first need to install a few Python libraries before loading trajectoryGuide. Click the Blue and Yellow Python button located in the top menu to the right.

    <center>
        <figure>
            <img src="/widgets/img/python_icon.png" alt="python_icon"/>
            <figcaption>Python interactor button.</figcaption>
        </figure>
    </center>

2. The Python interactor should now be visible at the bottom of the 3D Slicer window.

    <center>
        <figure>
            <img src="/widgets/img/python_interactor.png" alt="python_interactor"/>
            <figcaption>3D Slicer Python interactor.</figcaption>
        </figure>
    </center>

3. Copy and paste the command below into the Python interactor box, press `Enter` to run the command.

    ```console
    pip_install('scikit-image pandas scipy shapely')

    ```

### Add trajectoryGuide module

1. In the top menu, click on the `Edit` menu and select `Application settings`

    <center>
        <figure>
            <img src="/widgets/img/edit_menu.png" alt="edit_menu"/>
            <figcaption>3D Slicer Edit menu.</figcaption>
        </figure>
    </center>

2. In the settings dialog window select `Modules`, click the right-facing arrows next to the box with the text `Additional module paths` and click `Add`

3. Navigate to where you stored the source code for trajectoryGuide, select the top (root) trajectoryGuide folder and click `Choose`

    <center>
        <figure>
            <img src="/widgets/img/add_module.png" alt="add_module"/>
            <figcaption>3D Slicer add module path.</figcaption>
        </figure>
    </center>

4. 3D Slicer will want to restart at this point, click `Yes`

    <center>
        <figure>
            <img src="/widgets/img/restart_slicer.png" alt="restart_slicer"/>
            <figcaption>3D Slicer restart notification.</figcaption>
        </figure>
    </center>

5. Now when 3D Slicer restarts, **trajectoryGuide** will be included in Slicer's modules menu.

<br>
<br>
<br>