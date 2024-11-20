# Environment setup

[« Previous](.) \| [Up ↑](.) \| [Next »](./introduction)

<div class="alert alert-danger">
Please follow <b>every single step</b> below.<br/> If you miss a step, things will only work partially.
</div>

You will need to set up **by yourself** the following pieces:

- Download and install [Visual Studio Code](https://code.visualstudio.com/).  
  If you already have Visual Studio Code, install the latest version.

- the `pixi` tool: you will get installation instructions [here](https://pixi.sh/latest/).  
  For Windows, follow the "PowerShell" instructions (look for a PowerShell on your system, it's there I promise.)  
  For those who already know a little, `pixi` is a minimal tool providing environments similar to Anaconda, but we will not use Anaconda;

<div class="alert alert-warning">
<b>Warning</b> If you already have anaconda, and see when you open the terminal your line starting with <code>(base)</code>:<br/> <code>conda config --set auto_activate_base false</code> 
</div>

- understand that you will need a terminal for cloning learning materials, installing dependencies and more.

  - MacOS and Linux users should be familiar with their usual terminal application;
  - MacOS users will probably need to install common tools and dependencies with [brew](https://brew.sh/);
  - Windows users should find out how to run their PowerShell.

  You are expected to be familiar with the most basic shell commands to list a directory, create and move files, change permissions, etc.

- the `git` (or `git.exe` for Windows users) program, for version control.  
  Using Git falls out of scope of this seminar, but you are **strongly encouraged** to become proficient with it.  
  You may find resources on [GitHub Learning Lab](https://lab.github.com/), e.g. the following course for [first-timers](https://lab.github.com/lmachens/git-and-github-first-timers).

  Try running `git --version`. If necessary, install `git`:

  | Operating system  | Installation command      |
  | ----------------- | ------------------------- |
  | Linux (Ubuntu)    | `sudo apt install git`    |
  | MacOS (preferred) | `brew install git`        |
  | Windows or MacOS  | `pixi global install git` |

- clone the resources for the course:

  ```sh
  git clone https://github.com/xoolive/optim4ai
  ```

  **Windows users** should install the dependencies within their Ubuntu subsystem.

  You may move the folder at any time if you prefer to keep things sorted differently on your computer.

- install the dependencies with pip when needed

[« Previous](.) \| [Up ↑](.) \| [Next »](./introduction)
