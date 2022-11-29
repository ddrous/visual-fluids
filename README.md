# Neural Fluids

A collection of repos from TUM to run fluid simulations and ML experiments then visualise results in Blender.


## Getting started

Our overall goal is to convert `.NPZ` files into volumetric `.VDB` now supported in Blender. The following steps are only valid for Linux, namely __Ubuntu__. It is recommended to use __VSCode__ to build `mantaflow` binaries.

1. Install `PhiFlow` and run experiments
    ```
    pip install phiflow dash
    ```

2. Run a PhiFlow simulation. For example, run [`TUM.py`](./phiflow2blender/tutorial/TUM.py) using Python3. The results will be saved in `.NPZ` format.

3. Install `mantaflow` dependencies:
    - __CMake, etc.__: 
        ```
        sudo apt-get install cmake g++ git python3-dev
        ```
    - __NumPy__: 
        ```
        sudo apt install python3-numpy
        ```
    - __OpenVDB__: 
        ```
        sudo apt-get install libopenvdb-dev
        ```
        NB: _On Windows, one should consider using the prebuilt libraries from [here](http://mantaflow.com/download/openvdb.zip)_.
    - __TBB__: Download deb files for [libtbb2](https://packages.ubuntu.com/focal/libtbb2) and [libtbb-dev](https://packages.ubuntu.com/focal/libtbb-dev) and install using 
        ```
        sudo apt install ./<path_to_deb>
        ```
        NB: _TBB went through a massive change to morph into oneTBB. Remark that TBB (version <2020) is required here, not OneTBB (version >2021)._

4. Build `mantaflow` from source with CMake options `-DNUMPY`, `-DOPENVDB`, and `-DTBB` enabled.

    NB: _Remember to `Delete Cache and Reconfigure` if CMake options are not taken into account. Also, you might get warnings for some deprecated TBB headers. Ignore them !_

5. Now let's convert the `.NPZ` files from step 2 into `.VDB`. Simple, just locate the [manta2vdb.py](./phiflow2blender/tutorial/manta2vdb.py) scene definition script and run the command 
    ```
    ./path/to/manta path/to/manta2vdb.py -d path/to/scene/data -res 128 64 192
    ```
    NB: _It is advised to run the above command from the location of the `manta2vdb.py` script._

6. Open Blender, press `Shift + A`, then `Volumes`, then `import OpenVDB` to load your volumetric scene files. To make awesome renderings, follow [Nils Thuerey's video](https://youtu.be/xI1ARz4ZSQU). That's all, ENJOY !
