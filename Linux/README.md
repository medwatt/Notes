# Applications

## firefox

Make `firefox` slightly more convenient to use.

Go to `about:config` and make the following changes:

- Double-click closes tab: `browser.tabs.closeTabByDblclick`
- Open bookmarks in a new tab: `browser.tabs.loadBookmarksInTabs`
- Disable those irritating autoplay videos: change `media.autoplay.default` to 5
- Enable hardware acceleration in Firefox v>=96: `media.ffmpeg.vaapi.enabled`

## vmware

Enable 3D acceleration:

- Add `mks.gl.allowBlacklistedDrivers = "TRUE"` to to the file `~/.vmware/preferences`

## docker

The root directory of Docker is determined by the `data-root` configuration
option in the Docker daemon configuration file (`/etc/docker/daemon.json`). By
default, the root directory is set to `/var/lib/docker`.

To change the root directory, you need to edit the `/etc/docker/daemon.json`
file and specify a new value for the `data-root` option.

- Stop the docker daemon: `sudo systemctl stop docker.service`
- Create/edit `/etc/docker/daemon.json` and add `{ "data-root": "/path/to/your/new/docker/root"}`
- Copy the current data directory to the new location: `sudo cp -rp /var/lib/docker/* "/path/to/your/new/docker/root/"`
- Rename or delete the old docker directory: `sudo mv /var/lib/docker /var/lib/docker.old`
- Restart the docker daemon: `sudo systemctl restart docker.service`

### images

- Build a Docker image from a Dockerfile: `docker build -t <image-name>:<tag> .`
- List all Docker images: `docker images`
- Remove a Docker image: `docker rmi <image-id>`
- Save a Docker image: `docker save <image-name>:<tag> > <file-name>.tar`
- Load a Docker image from a file: `docker load < <file-name>.tar`

#### docker run

Here is a list of some of the most commonly used options with `docker run`:

- `-it`: Runs the container in interactive mode, allowing you to run commands
  in the container's shell.
- `-e`: Sets environment variables in the container.
- `-p`: Maps a host port to a container port to expose the container's services
  to the host.
- `-v`: Mounts a host directory as a data volume in the container.
- `--name`: Specifies a custom name for the container.
- `--hostname`: Specifies the hostname for the container. By default, the
  hostname of the container is set to the container ID.
- `--mac-address`: Specifies a MAC address for the container's network
  interface.
- `--cpus`: Limits the number of CPU resources available to the container.
- `--memory`: Limits the amount of memory the container can use.
- `--entrypoint`: Specifies the command that should be executed when the
- `--rm`: Automatically removes the container when it exits.

#### X11 passthrough

X11 passthrough allows GUI applications running in the container to be
displayed on the host system.

To enable X11 passthrough, you will need to pass the host's X11 socket to the
container using the `-v` option. Here's an example of how to do this:

```bash
docker run -it -v /tmp/.X11-unix:/tmp/.X11-unix:ro -e DISPLAY=$DISPLAY <image-name>:<tag>
```

In this example, the host's X11 socket is mounted in the container at
`/tmp/.X11-unix`. The `:ro` suffix means that the volume is mounted in
read-only mode. By mounting the X11 socket as read-only, you are ensuring that
malicious applications running in the container cannot modify the X11 socket
and potentially exploit vulnerabilities in the X11 protocol. The `DISPLAY`
environment variable is also set to the host's display, so that applications in
the container can find the display and connect to it.

### containers

- Run a Docker container: `docker run -d <image-name>:<tag>`
- List all running Docker containers: `docker ps`
- List all Docker containers: `docker ps -a`
- Stop a Docker container: `docker stop <container-id>`
- Start a stopped Docker container: `docker start <container-id>`
- Execute a command inside a Docker container: `docker exec -it <container-id> <command>`
- Copy files from host to Docker container: `docker cp <host-file-path> <container-id>:<container-file-path>`
- Copy files from Docker container to host: `docker cp <container-id>:<container-file-path> <host-file-path>`
- Save a Docker container: `docker export <container-id> > <file-name>.tar`
- Load a Docker container from a file: `docker import <file-name>.tar <image-name>:<tag>`
- Commit a container to create a new image: `docker commit <container-id> <new-image-name>:<tag>`

## VLC

Add all files in a folder to a playlist in VLC.

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

## nnn

`nnn` is my favourite command-line file manager. You can get it from your
distro's repos, but I prefer building it to enable a few options.

- Clone the `nnn` repo: `git clone https://github.com/jarun/nnn`
- Enter the `nnn` repo: `cd nnn`
- Build with the following options: `make O_NERD=1 O_PCRE=1 O_CTX8=1`
- Install: `sudo make install`

## Miniconda

### Installation

- Download `mambaforge` from [here](https://github.com/conda-forge/miniforge#mambaforge) and install it.
- To prevent `miniconda` from initializing automatically whenever a new
  terminal is spawned, remove the code that is used to start `miniconda` and
  put it in a separate file, which can be sourced with an `alias`.
    - Save the script below in a new file (change `<user>` to the username
      you're using).
    - Create an alias to the file in your `bashrc`: `alias mini="path_to_miniconda_setup.sh`"

        ```bash
        # >>> conda initialize >>>
        # !! Contents within this block are managed by 'conda init' !!
        __conda_setup="$('/home/<user>/mambaforge/bin/conda' 'shell.zsh' 'hook' 2> /dev/null)"
        if [ $? -eq 0 ]; then
            eval "$__conda_setup"
        else
            if [ -f "/home/<user>/mambaforge/etc/profile.d/conda.sh" ]; then
                . "/home/<user>/mambaforge/etc/profile.d/conda.sh"
            else
                export PATH="/home/<user>/mambaforge/bin:$PATH"
            fi
        fi
        unset __conda_setup

        if [ -f "/home/<user>/mambaforge/etc/profile.d/mamba.sh" ]; then
            . "/home/<user>/mambaforge/etc/profile.d/mamba.sh"
        fi
        # <<< conda initialize <<<
        ```

### Managing environments

Miniconda creates a `base` environment by default. The only thing I install in
the `base` environment is `jupyter lab` so that I don't have to install it in
all other environments.

- To install jupyter lab: `mamba install jupyterlab`

Here is a list of commonly-used commands to use with Miniconda:

- Create a new environment: `mamba create --name <env_name>`
- Create a new environment with specific Python version: `mamba create --name <env_name> python=<python_version>`
- Switch environment: `mamba activate <env_name>`
- Deactivate environment: `mamba deactivate`
- List environments: `mamba info --envs`
- List packages installed in an environment: `mamba list`
- Delete an environment: `mamba env remove --name <env_name>`
- Search for a package: `mamba search <package_name>`
- Install packages in an environment: `mamba install <package_name>`
- Update a package in an environment: `mamba update <package_name>`
- Delete the download cache: `mamba clean --all`
- Create a clone of an environment: `mamba create --name <new_env_name> --clone <exist_env_name>`
- Export an environment: `mamba env export --name <env_name> > environment.yml`
- Import an environment: `mamba env create -f environment.yml`

To make the environment discoverable inside jupyter lab:

- Install the ipykernel in an environment: `mamba install ipykernel`
- Make the kernel discoverable: `ipython kernel install --user --name=<env_name>`
    - This places the files in `~/.local/share/jupyter/kernels/`

### matplotlib interractive plots

- `sudo pacman -S python-pyqt5`
- Install `ipympl` in the environment where `matplotlib` is installed: `mamba install ipympl`
- Install matplotlib jupyter lab extension: `jupyter labextension install jupyter-matp%matplotlib widgetlotlib`
- Enable `ipympl` backend inside a notebook: `%matplotlib widget`

# System

## Shut down HDD

I have a HDD connected to the second storage bay of my laptop that I access
once in a while. The constant spinning of the hard drive is quite annoying.
Let's configure it to automatically shut down after 2 minutes and 15 seconds of
inactivity.

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

## Run sudo commands without password

In order to run a program or service without having to type `sudo` every time,
you can edit the `sudoers` file to allow the user to run the specific program
or service as a root user.

- Edit `/etc/sudoers` with root privileges.
- Add the commands you'd like to run at the end of the `/etc/sudoers` file
  following the format shown below:

    ```bash
    <username> ALL = NOPASSWD: /path/to/program
    <username> ALL = NOPASSWD: /bin/systemctl start <service_name>
    ```

## Change user shell

- List all installed shells: `cat /etc/shells`

Let's say we want to change the default shell to to `/bin/sh`. There are two
ways to do that:

1. Using `chsh`: `chsh --shell /bin/sh <username>`
2. Using `usermod`: `sudo usermod --shell /bin/sh <username>`

We can verify that the shell has been changed by checking the entry for
`<username>` in the `/etc/passwd` file. You need to logout for the change to
take effect.

## ssh authentication

**SSH** (Secure Shell) is a secure protocol used to remotely log into and execute
commands on a computer. One of the main features of SSH is secure
authentication, which ensures that only authorized users are able to access a
system.

There are two main methods of authentication in SSH: password-based
authentication and public key authentication.

**Password-based** authentication is the simplest and most common form of
authentication in SSH. It works by prompting the user to enter their username
and password, which are then transmitted to the server and checked against the
stored user credentials. If the username and password match, the user is
granted access.

**Public key** authentication, on the other hand, uses a pair of cryptographic
keys – a public key and a private key – to authenticate the user. The public
key is stored on the server, and the private key is stored on the client
machine. When the user tries to log in to the server, the server generates a
challenge and encrypts it with the user's public key. The client then uses its
private key to decrypt the challenge and sends the decrypted challenge back to
the server. If the decrypted challenge matches the original challenge, the user
is granted access.

Public key authentication provides several advantages over password-based
authentication, including stronger security and the ability to automate login
processes. However, it also requires more setup and configuration, as the
public and private keys need to be generated and properly distributed.

Public key authentication in SSH can be set up in several ways. The most
straight-forward way is given below.

1. Generate a public/private key pair on your local machine:

    ```bash
    ssh-keygen -t rsa -b 4096
    ```

    The `ssh-keygen` command will prompt you for a location to store the key
    pair. By default, the keys will be stored in `~/.ssh/id_rsa` and
    `~/.ssh/id_rsa.pub`.

2. Copy the public key to the server:

    ```bash
    ssh-copy-id username@server_ip_or_hostname
    ```

    Replace `username` with your username on the server and
    `server_ip_or_hostname` with the IP address or hostname of the server.
    You'll be prompted for your password to complete the copy process.

3. Test the public key authentication:

    ```bash
    ssh username@server_ip_or_hostname
    ```

    If the public key authentication is set up correctly, you should be able to
    log in to the server without being prompted for a password.

## systemd services

systemd is the init system and service manager for many Linux distributions. It
allows you to manage system services as units. Each unit represents a specific
service, such as the SSH daemon, or a custom application. The unit files
describe how the service should be started, stopped, restarted, and monitored.

Here's an example of how to create a systemd unit to manage a custom
application:

- Create a new file with the `.service` extension in the `/etc/systemd/system`
  directory. For example, if your application is called `myapp`, you could
  create a file named `/etc/systemd/system/myapp.service`.
- Open the file in a text editor and add the following content to define the
  unit:

  ```bash
  [Unit]
  Description=My Custom Application

  [Service]
  ExecStart=/usr/bin/myapp
  Restart=always

  [Install]
  WantedBy=multi-user.target
  ```

In this example:

- The `[Unit]` section provides a description of the service.
- The `[Service]` section specifies the behavior of a service.
- The `[Install]` section specifies how and where the service should be
  installed on the system.

After saving the file, you can use the `systemctl` command to manage the unit.

- To start the service: `sudo systemctl start myapp.service`
- To stop the service: `sudo systemctl stop myapp.service`
- To restart the service: `sudo systemctl restart myapp.service`
- To check the status of the service: `sudo systemctl status myapp.service`
- To enable the service to start automatically at boot time: `sudo systemctl enable myapp.service`

### service section

The `[Service]` section of a systemd unit file is used to specify the behavior
of a service. The following are some of the most common options that can be
used inside the `[Service]` section:

- `ExecStart`: Specifies the command to run when starting the service. This
  command is executed in a shell, so it can be a complex command line that
  includes multiple arguments and environment variables.

- `ExecStop`: Specifies the command to run when stopping the service. This is
  optional and is not required for all services.

- `Restart`: Specifies the restart policy for the service. The following are
  the most common values for this option:

    - `no`: The service will not be restarted automatically if it fails.
    - `on-success`: The service will be restarted if it exits successfully.
    - `on-failure`: The service will be restarted if it exits with a non-zero status.
    - `always`: The service will always be restarted, regardless of the exit status.

- `Type`: Specifies the type of service being defined. The following are the
  most common values for the `Type` option:

    - `simple`: Specifies that the service is a simple service that runs in the
      foreground and does not fork (creating new child process) into the
      background. This is the most common type of service and is appropriate
      for most services.

    - `forking`: Specifies that the service forks into the background after
      starting. This type of service is useful for services that need to
      continue running in the background even after the process that started
      them has exited. For example, a web server may start as a foreground
      process, but then fork into the background so that it can continue
      serving web pages even after the process that started it has exited.

    - `oneshot`: Specifies that the service runs once and then exits.

    - `dbus`: D-Bus is a message bus system that provides a way for
      applications to communicate with each other. When a service is specified
      as `dbus`, it means that the service provides a D-Bus interface that
      other applications can use to communicate with it.

    - `notify`: Specifies that the service is a notify service. This type of
      service is similar to a `simple` service, but it can notify systemd when
      it has finished starting up by sending a message over the bus.

- `TimeoutStartSec`: Specifies the time to wait for the service to start. If
  the service does not start within this time, systemd will assume that it has
  failed to start and will move on to starting other services.

- `TimeoutStopSec`: Specifies the time to wait for the service to stop. If the
  service does not stop within this time, systemd will assume that it has
  failed to stop and will move on to stopping other services.

- `User`: Specifies the user account that the service should run as. This is
  useful for services that require access to specific files or resources that
  can only be accessed by a specific user.

- `Group`: Specifies the group that the service should run as. This is similar
  to the `User` option and can be used to specify the group that the service
  should run as.

- `WorkingDirectory`: Specifies the working directory that the service should
  run in. This is useful for services that require a specific working directory
  to be set in order to function correctly.

- `Environment`: Specifies environment variables that should be set for the
  service. This can be used to pass information to the service, such as the
  location of configuration files or the hostname of the system.

### install section

The `[Install]` section of a systemd unit file is used to specify how and where
the service should be installed on the system. The following are the most
common options that can be specified in the `[Install]` section:

- `WantedBy`: Specifies the target unit that the service should be installed as
  a dependency of. This option determines when the service will be started and
  stopped relative to other services on the system. Here are some common values
  that can be specified for the `WantedBy` option:

  - `multi-user.target`: Specifies that the service should be started when the
    system enters the multi-user target and stopped when the system exits the
    multi-user target. The `multi-user.target` represents the state of the
    system when it is running in multi-user mode. In this mode, the system is
    fully operational and multiple users can log in and use the system
    simultaneously. This is the default target for most systems.

  - `graphical.target`: Specifies that the service should be started when the
    system enters the graphical target and stopped when the system exits the
    graphical target. This target is used for systems that provide a graphical
    user interface.

  - `network-online.target`: Specifies that the service should be started when
    the system network comes online and stopped when the network goes offline.
    This target is used for services that require network connectivity to
    function.

  - `local-fs.target`: Specifies that the service should be started when the
    local file system has been mounted and stopped when the local file system
    is unmounted. This target is used for services that require access to the
    local file system.

  - `timers.target`: Specifies that the service should be started when the
    timer daemon is running and stopped when the timer daemon is not running.
    This target is used for services that are triggered by timer events.

  - `shutdown.target`: Specifies that the service should be started when the
    system is shutting down and stopped when the system has finished shutting
    down. This target is used for services that need to perform cleanup actions
    before the system shuts down.

  - `suspend.target`: Specifies that the service should be started when the
    system is entering a suspend state and stopped when the system is leaving
    the suspend state. This target is used for services that need to perform
    specific actions when the system is suspending or resuming.

  - `hibernate.target`: Specifies that the service should be started when the
    system is entering a hibernate state and stopped when the system is leaving
    the hibernate state. This target is used for services that need to perform
    specific actions when the system is hibernating or resuming.

- `Alias`: Specifies an alias name for the service. This option allows the
  service to be referred to by multiple names, making it easier to find and
  manage.

- `Also`: Specifies additional units that the service should be installed as a
  dependency of. This option allows the service to be started and stopped in
  conjunction with other services.

## cron job

A cron job is a scheduled task that runs automatically at specified intervals.
The task is defined by a line in a special file called the cron table or
crontab, which is stored in the `/var/spool/cron/` directory, with each user
having their own separate crontab file.

The crontab file contains a list of commands that cron should run, along with
the schedule for when the commands should run.

Each line in the crontab file represents a single cron job, and has the
following format:

```bash
* * * * * command-to-run
```

The five fields in this line represent the following:

1. Minute (0-59)
2. Hour (0-23)
3. Day of the month (1-31)
4. Month (1-12)
5. Day of the week (0-7, with both 0 and 7 representing Sunday)

For example, the following cron job would run the `command-to-run` every day at
4:30 PM:

```bash
30 16 * * * command-to-run
```

You can use the `crontab` command to manage your cron jobs.

- `crontab -e`: Edit the crontab file for the current user. This opens the file
  in the default text editor, allowing you to add or modify cron jobs.

- `crontab -l`: List the current user's cron jobs. This displays the contents
  of the crontab file, showing the current set of cron jobs.

- `crontab -r`: Remove the current user's cron jobs. This deletes the crontab
  file, effectively removing all cron jobs for the user.

## chmod

`chmod` (Change Mode) is used to change the permissions of one or more files or
directories. It can be used in either symbolic or numerical mode.

- Give the owner read and write permissions: `chmod u+rw file.txt`
- Give the group read permission: `chmod g+r file.txt`
- Remove execute permission for others: `chmod o-x file.txt`
- Set read, write, and execute permissions for everyone: `chmod ugo+rwx file.txt`
- Remove all permissions for group and others: `chmod go-rwx file.txt`
- Set the owner's permissions to read and write only: `chmod u=rw file.txt`
- Give all permissions to the owner and read permission to the group: `chmod u+rwx,g+r file.txt`

The `-R` (or `--recursive`) option can be used with `chmod` to apply the
changes recursively to the files and directories within the specified
directory.

## chown

`chown` (Change Ownership) is used to change the ownership of a file or
directory.

- Change the owner of a file to a different user: `chown newuser file.txt`
- Change the group ownership of a file: `chown :newgroup file.txt`
- Change the owner and group of a file: `chown newuser:newgroup file.txt`
- Change the owner of a directory and all its contents recursively: `chown -R newuser mydir`

## adding new user

With root privileges:

- Add new user: `useradd <username>`
- Set a password for the new user: `passwd <username>`

## usermod

The `usermod` command is used to modify user account information, such as the
user's name, home directory, shell, or groups.

Here are some of the most commonly used options with `usermod`:

- `-l` or `--login`: This option is used to change the username of an existing
  user account. For example, to change the username from `user1` to `user2`,
  run the following command:

  ```bash
  usermod -l user2 user1
  ```

- `-d` or `--home`: This option is used to change the home directory of an
  existing user account. For example, to change the home directory from
  `/home/user1` to `/home/newuser1`, run the following command:

  ```bash
  usermod -d /home/newuser1 /home/newuser1
  ```

- `-s` or `--shell`: This option is used to change the shell of an existing
  user account. For example, to change the shell from `/bin/bash` to `/bin/sh`,
  run the following command:

  ```bash
  usermod -s /bin/sh user1
  ```

- `-g` or `--gid`: This option is used to change the primary group of an
  existing user account. For example, to change the primary group from `group1`
  to `group2`, run the following command:

  ```bash
  usermod -g group2 user1
  ```

- `-a` or `--append`: This option is used to add the user to one or more
  supplementary groups. For example, to add the user to the `sudo` group, run
  the following command:

  ```bash
  usermod -a -G sudo user1
  ```

- `-u` or `--uid`: This option is used to change the user ID (UID) of an
  existing user account. For example, to change the UID from `1000` to `2000`,
  run the following command:

  ```bash
  usermod -u 2000 user1
  ```
