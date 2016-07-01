## Installing miniconda on Mac

This guide is focused on how to install the miniconda package on a Mac.

**Background:**
[Continuum Analytics](https://www.continuum.io) has developed the Anaconda package management system for Python. This is a powerful tool that allows users to install packages easily and without root access. It also allows for simple control over virtual environments (called conda envs) that make dependency resolution for particular software or pipelines a breeze.

The entire Anaconda package is quite large. Rather than installing the whole thing, we will be installing [miniconda](http://conda.pydata.org/miniconda.html). Miniconda simply installs Python and the machinery to add additional packages that are enabled in the conda package management system. After we have finished installing miniconda, we will install a couple of useful packages that we plan to use during this workshop.

**Install Guide:**
Navigate to the [miniconda website](http://conda.pydata.org/miniconda.html). Click on the "64-bit (bash installer)" link underneath "Mac OS X".

![miniconda_install](https://cloud.githubusercontent.com/assets/1823345/16455409/38e9694e-3de2-11e6-97cf-3585974a7d74.png)

It should automatically be downloaded to your ```~/Downloads``` directory. However, if you are prompted to choose a location to save it in, choose the ```Downloads``` directory.

Open your terminal appliction. This can be found in your ```Utilities``` folder within the ```Applications``` folder.

![terminal_application](https://cloud.githubusercontent.com/assets/1823345/16456124/ccb32a82-3de4-11e6-97e8-b6dda72fe4c6.png)

It will look something like this:

![terminal](https://cloud.githubusercontent.com/assets/1823345/16456175/0c9c1032-3de5-11e6-92d8-cb2e797729e8.png)

Go ahead and navigate to your ```Downloads``` directory by entering the command:

```
$ cd ~/Downloads
```

_Note: whenever the '$' sign is used in a command, it indicates that this command should be made in the terminal shell. Do not copy the '$' into your actual command_

Now let's make sure that your miniconda install script is in your directory by listing the contents of your directory with:

```
$ ls
```

In the contents, there should be a file called something like ```Miniconda3-latest-MacOSX-x86_64.sh```.

If this file is not listed, go back to the original step and re-download it. Make sure that it is saved to your ```Downloads``` folder.

Now being the install with:

```
$ sh Miniconda3-latest-MacOSX-x86_64.sh
```

It will ask you if you want to continue the installation process, go ahead and press ENTER. Continue to press ENTER until you get through the license agreement. Eventually, it will prompt you with the following question:

```
Do you approve the license terms? [yes|no]
>>>
```
Go ahead and type ```yes```.

It will then request if you wish to install ```Miniconda3	``` into the default location. Press ENTER to confirm the location. 

The installer will then begin installing the packages. Once finisished, it will ask:

```
Do you wish the installer to prepend the Miniconda3 install location
to PATH in your /Users/frandsenp/.bash_profile ? [yes|no]
[yes] >>>
```

Type ```yes``` and press enter. When you do this, your default version of Python will change from the version that comes pre-installed on Macs to Python 3 installed with miniconda. You will need to open a new terminal window in order for this to become active. Let's do this. Go ahead and close the current terminal window with:

```
$ exit
```

Then reopen terminal. Let's test to make sure that the new version of Python was installed properly. We're going to use the Unix command ```which```:

```
$ which python
```

The output should look something like this (substitute your username for mine):

![which_python](https://cloud.githubusercontent.com/assets/1823345/16456844/5ceee85a-3de7-11e6-94c1-bedb2f0232ec.png)

Now that you're setup, we'll install a couple of important Python packages using the conda package manager. The first one that we will install is Jupyter so that we can take advantage of Jupyter notebooks later in the class. To do this, you only need to enter a single simple command:

```
$ conda install jupyter
```

Jupyter requires many other dependencies outside of the vanilla Python install. Fortunately, conda knows this and will automatically install each dependency that Jupyter requires. After issuing the command above, you will receive a prompt with the names of the dependencies that need to be installed/upgraded. Additionally, you will receive a prompt requesting whether you wish to proceed with the install:

```
Proceed ([y]/n)?
```

Go ahead and press ENTER. Conda will then install all necessary packages to your system.

That's all that we'll install for now. I hope this give you a good idea of how to easily install Python packages using conda.