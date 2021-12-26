# Environment setup

[« Previous](.) \| [Up ↑](.) \| [Next »](./introduction)

<div class="alert alert-danger">

First thing first: <b>Windows users</b><p>
should first activate WSL using the official <a href="https://docs.microsoft.com/en-us/windows/wsl/install-win10">instructions</a> (<a href="https://docs.microsoft.com/fr-fr/windows/wsl/install-win10">French version</a>). Please install the most recent Ubuntu version unless you have another version ready.

</p>
Thou shall read specific instructions for Windows.
</div>

You will need to set up **by yourself** the following pieces:

- [Visual Studio Code](https://code.visualstudio.com/), then install the [Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python):

  ```sh
  code --install-extension ms-python.python ms-toolsai.jupyter
  ```

  **Windows users** should install Visual Studio Code in Windows (not WSL) then activate the Remote WSL extension:

  ```sh
  code --install-extension ms-vscode-remote.remote-wsl
  ```

- an Anaconda distribution, from the [following link](https://www.anaconda.com/products/individual). In case the question arises, it is very likely that the best suited version for your needs is the 64 bits one. Anaconda is more than a Python distribution: it also provides additional dependencies you may need;

  **Windows users** should install the Anaconda distribution within their Ubuntu subsystem.

- the `git` (or `git.exe` for Windows users) program, for version control. Using Git falls out of scope of this seminar, but you are **strongly encouraged** to become proficient with it. You may find resources on [GitHub Learning Lab](https://lab.github.com/), e.g. the following course for [first-timers](https://lab.github.com/lmachens/git-and-github-first-timers).

  Try running `git --version`. If necessary, install `git`:

  | Operating system | Installation command   |
  | ---------------- | ---------------------- |
  | MacOS            | `brew install git`     |
  | Linux (Ubuntu)   | `sudo apt install git` |

- clone the resources for the course:

  ```sh
  git clone https://github.com/xoolive/optim4ai
  ```

  **Windows users** should install the dependencies within their Ubuntu subsystem.

  You may move the folder at any time if you prefer to keep things sorted differently on your computer.

- install the dependencies with pip when needed

[« Previous](.) \| [Up ↑](.) \| [Next »](./introduction)
