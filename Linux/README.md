# Linux Stuff

## Applications

### Firefox

Make `firefox` slightly more convenient to use. Go to `about:config` and change
the following:

- Double click closes tab: `browser.tabs.closeTabByDblclick`
- Open bookmarks in new tab: `browser.tabs.loadBookmarksInTabs`
- Disable those irritating auto play video: `media.autoplay.default`; set it to 5
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

## System

### Shut down hard drive when not in use

I have a 2TB hdd connected to the second storage bay of my laptop. I access it
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
    <your_username> ALL = NOPASSWD: /usr/bin/some_command
    <your_username> ALL = NOPASSWD: /bin/systemctl start some_service.service
    ```
