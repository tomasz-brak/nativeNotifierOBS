# nativeNotifierOBS

Easy to setup and effective way to get visual and audio feedback from OBS. **THIS is the only script you need to install, no additional programs needed!**. Remember to enable notification on top of apps and disable *do not disturb* mode

![*A notification on garuda linux*](https://github.com/tomasz-brak/nativeNotifierOBS/assets/62989490/f3e4852d-2d3d-42e7-a3ec-b89da5324e52 "A notification on garuda linux")
*A notification on garuda linux*

## Installation

### Linux

1. Install python (tested on 3.11), alsa-utils
1. Install python packages: `notify-py`
1. Setup obs
1. Clone the repository to:

    ```bash
    $HOME/.config/obs-studio/scripts
    ```

1. Launch obs, go to tools > scripts
1. Click the add button and then navigate to the directory where you have cloned the repository
1. select obs_notify.py

#### Footnotes

- Assuming you have followed the instruction above you can now configure the notifications in:

    ```bash
    nano $HOME/.config/obs-studio/scripts/nativeNotifierOBS/obsNativeNotifier/config.toml
    ```

### Windows

1. Install python, [download](https://www.python.org/downloads/)
1. Install OBS
1. Open Terminal and run:

    ```powershell
    python -m pip install notify-py
    ```

1. Clone the repository or download zip
1. Open the location of your obs install (go to start menu, search OBS, select open file location)
1. Then go to data/obs-plugins/frontend-tools/scripts
1. Copy here obsNativeNotifier folder and obs_notify.py from the repository
1. Launch obs and go to tools > scripts
1. Select obs_notify.py that you have copied
1. To edit configuration edit config.toml inside obsNativeNotifier folder

![*Configuration file*](https://github.com/tomasz-brak/nativeNotifierOBS/assets/62989490/a89ceb05-08a4-4b83-91b0-dace9da221e8 "Configuration file")
*Configuration file*

## External libraries and resources

- [notify-py](https://github.com/ms7m/notify-py)
- [BeautyLine icon](https://gitlab.com/garuda-linux/themes-and-settings/artwork/beautyline)
- [obs](https://github.com/obsproject/obs-studio)
- [python](https://github.com/python/cpython)

## Notes

- I use arch (btw) and i have not tested nor used the software on other operating systems, if you spot any bugs or inaccuracies in the installation procedure on other os's please let me know.
