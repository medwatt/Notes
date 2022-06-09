# Linux Stuff

## Applications

### Firefox

Make `firefox` slightly more convenient to use. Go to `about:config` and change
the following:

- Double click closes tab: `browser.tabs.closeTabByDblclick`
- Open bookmarks in a new tab: `browser.tabs.loadBookmarksInTabs`
- Disable those irritating auto play videos: `media.autoplay.default`; set it to 5
- Enable hardware acceleration in Firefox v>=96: `media.ffmpeg.vaapi.enabled`

### Build nnn from source

`nnn` is my favourite command-line file manager. You can get it from your
distro's repos, but I prefer building it to enable a few options.

- Clone the `nnn` repo: `git clone https://github.com/jarun/nnn`
- Enter the `nnn` repo: `cd nnn`
- Build with the following options: `make O_NERD=1 O_PCRE=1 O_CTX8=1`
- Install: `sudo make install`

### Add all files in a folder to a playlist in VLC

- Copy the code below to a file, say `~/.config/vlc/vlc.sh`.
- Make it executable: `chmod +x vlc.sh`.
- Copy the desktop file of `VLC` located at `/usr/share/applications/vlc.desktop` to
  `~/.local/share/applications/vlc.desktop` and change the field `Exec` to the
  path of `vlc.sh` (remove argument `--started-from-file %U`).

    ```bash
    #!/bin/bash

    shopt -s extglob
    extensions='@(avi|mp4|mkv|m4v|mov|mpg|mpeg|wmv|ogg|flac|m4a|mp3|wav)'  # list of extensions for searching in current directory

    # kill other instances of vlc to keep playlist clean (one-instance mode)
    killall vlc; sleep 0.1

    # launch empty vlc if no argument provided
    if [ -z "$1" ]; then
        vlc; exit
    fi

    # parse argument
    filename=$(realpath -- "$1")
    dirname=$(dirname "$filename")
    basename=$(basename "$filename")

    # count files with matching extension, and get position of filename in current directory
    n=$(ls "${dirname}"/*.${extensions} -1 2>/dev/null | wc -l)
    pos=$(ls "${dirname}"/*.${extensions} -1 2>/dev/null | grep -n -F -- "${basename}" | cut -d: -f1)

    # if the filename does not have one of the extension above, launch vlc with provided filename
    if [ -z "$pos" ]; then
        vlc -- "${filename}"
        exit
    fi

    # change positions in playlist such as the first element is the opened file
    ls "${dirname}"/*.${extensions} -1 | tail -n$(($n-$pos+1)) >  /tmp/vlc.m3u
    ls "${dirname}"/*.${extensions} -1 | head -n$(($pos-1))    >> /tmp/vlc.m3u

    # launch playlist
    IFS=$'\n'; read -d '' -r -a files < /tmp/vlc.m3u; vlc "${files[@]}"
    ```

### Miniconda setup

#### Installing

- Download `miniconda` from [here](https://docs.conda.io/en/latest/miniconda.html#linux-installers).
- Make it executable and install.
- To prevent `miniconda` from initializing automatically when a terminal is started,
  remove the code that is used to start `miniconda` and put it in a separate file,
  which can be sourced with an `alias`.
    - Save the script below in a file (change `<user>` to yours).
    - Create an alias to the file in your `bashrc`: `alias mini="path_to_miniconda_setup.sh`"

    ```bash
    # >>> conda initialize >>>
    # !! Contents within this block are managed by 'conda init' !!
    __conda_setup="$('/home/<user>/miniconda3/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
    if [ $? -eq 0 ]; then
        eval "$__conda_setup"
    else
        if [ -f "/home/<user>/miniconda3/etc/profile.d/conda.sh" ]; then
            . "/home/<user>/miniconda3/etc/profile.d/conda.sh"
        else
            export PATH="/home/<user>/miniconda3/bin:$PATH"
        fi
    fi
    unset __conda_setup
    # <<< conda initialize <<<
    ```

#### Useful commands for managing environments

Miniconda creates a `base` environment by default. The only thing I install in
the `base` environment is `jupyter lab` so that I don't have to install it in
all other environments.

- To install jupyter lab: `conda install -c conda-forge jupyterlab`

I now create environments with different packages.

- For example, to create an environment called `work`: `conda create -n work`
- To remove an environment call `work`: `conda remove --name work --all`
- Activate environment: `conda activate work`
- Install packages in this environment: `conda install -c conda-forge <packages...>`
- Install the `ipykernel` to use environment with `jupyter lab`: `conda install ipykernel`
- Make kernel discoverable (the files will be placed in `~/.local/share/jupyter/kernels/`): `ipython kernel install --user --name=work`
- Deactivate environment: `conda deactivate`
- After installing packages, you can remove the downloaded files by running: `conda clean -a`

## System

### Shut down hard drive when not in use

I have a 2TB HDD connected to the second storage bay of my laptop. I access it
once in a while. It spins constantly and drives me insane. So, let's shut it
down after 2min 15s of not accessing it.

- Install `hdparm` if not already installed.
- We want `hdparm` to turn off the hard drive automatically. For this, we need
  to create a `systemd` service.
- Copy the code below into a file, say `hdd-sleep.sh`.
- Make the file executable: `chmod +x hdd-sleep.sh`
- Execute the file: `./hdd-sleep.sh`
- Enable the service to start when the system starts: `sudo systemctl enable hdd-sleep.service`
- The service can also be started now: `sudo systemctl start hdd-sleep.service`
- To check the status of the service: `systemctl status hdd-sleep.service`

    ```bash
    cat << EOF | sudo tee /etc/systemd/system/hdd-sleep.service
    [Unit]
    Description=hdparm sleep
    After=suspend.target hibernate.target multi-user.target

    [Service]
    Type=oneshot
    ExecStart=/usr/bin/hdparm -S 25 /dev/sda

    [Install]
    WantedBy=suspend.target hibernate.target multi-user.target
    EOF
    ```

### Run sudo commands without having to type password

- Edit `/etc/sudoers` with root privileges.
- Add the commands you'd like to run at the end of `/etc/sudoers` using the
  format shown below:

    ```bash
    <username> ALL = NOPASSWD: /usr/bin/some_command
    <username> ALL = NOPASSWD: /bin/systemctl start some_service.service
    ```

### Changing user shell

- List all installed shells: `cat /etc/shells`

Let's say we want to change the default shell to to `/bin/sh`. There are two
ways to do that:

1. Using `chsh`: `chsh --shell /bin/sh <username>`
2. Using `usermod`: `sudo usermod --shell /bin/sh <username>`

We can verify that the shell has been changed by checking the entry for
`<username>` in the `/etc/passwd` file. You need to logout for the change to
take effect.

### vmware

Enable 3D acceleration:

Add to the file  ~/.vmware/preferences `mks.gl.allowBlacklistedDrivers = "TRUE"`
