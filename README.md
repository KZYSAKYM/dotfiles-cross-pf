# dotfiles-cross-pf

Cross Platform Dotfiles Manager

The tools of dotfiles for cross-platform.
Currently, supported Linux, MacOS, and Windows.

This project is distributed under the MIT License, see LICENSE.
However, all files under `dotfiles/` are not licensed.

## Getting Started

- General

```sh
$ git clone https://github.com/KZYSAKYM/dotfiles-cross-pf.git
$ cd dotfiles-cross-pf
$ pip3 install pyyaml
```

- Windows
  - Open Powershell as Admin
  - Install Chocolately or your desired package manager
  - Execute the following
    ```sh
    $ python -m main.py
    ```

- Linux/Mac
  - Open command line
  - Execute the following
    ```sh
    $ python main.py
    ```

## How to write my configurations?

- dotfiles-cross-pf manages pairs of cmd and args as yaml
- the format of yaml is like the following
  ```
  linux:
    prehook:
      cmd: '<command executed initially>'
      args: '<args of command executed initially>'
    main:
      cmd: '<command executed after prehook>'
      args: '<args of command executed after prehook>'
    posthook:
      cmd: '<command executed after main>'
      args: '<args of command executed after main>'
  mac:
    prehook:
      cmd: '<command executed initially>'
      args: '<args of command executed initially>'
    main:
      cmd: '<command executed after prehook>'
      args: '<args of command executed after prehook>'
    posthook:
      cmd: '<command executed after main>'
      args: '<args of command executed after main>'
  windows:
    prehook:
      cmd: '<command executed initially>'
      args: '<args of command executed initially>'
    main:
      cmd: '<command executed after prehook>'
      args: '<args of command executed after prehook>'
    posthook:
      cmd: '<command executed after main>'
      args: '<args of command executed after main>'
  ```
- prehook and posthook entries can be empty like the following
  ```
  linux:
    prehook:
      cmd: '<command executed initially>'
      args: '<args of command executed initially>'
    main:
      cmd: '<command executed after prehook>'
      args: '<args of command executed after prehook>'
  mac:
    main:
      cmd: '<command executed after prehook>'
      args: '<args of command executed after prehook>'
    posthook:
      cmd: '<command executed after main>'
      args: '<args of command executed after main>'
  windows:
    main:
      cmd: '<command executed after prehook>'
      args: '<args of command executed after prehook>'
  ```
