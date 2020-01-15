# Methodology Assignment 1

## Using Remote Servers

### Due Friday Jan 17 11:59 PM

The methodology assignments are small assignments (doable within the
scope of lab hours) that introduce you to a tool or concept through a
simple `hello world` example.

Follow the instructions in [Lecture
02](https://github.com/afraenkel/DSC180A-DS-Methodology/blob/master/week02/Lecture%2002.pdf)
and the [documentation](http://go.ucsd.edu/2CZladZ) to log onto a
configurable campus server.

Note, from the ITS document:
> Students should login to the front-end nodes using either their UCSD
email username (e.g. ‘jsmith’), or in some cases, a “course specific”
account, e.g. “cs253wXX" for CSE253, Winter 2018. Consult the [ITS/ETS
Account Lookup
Tool](https://www.google.com/url?q=https://sdacs.ucsd.edu/~icc/index.php&sa=D&ust=1579049815630000)
for instructions on activating course specific accounts.

This is a multi-step process:
1. Log into your home directory on a "jump-box server".
2. Use a launch script (e.g. `launch-scipy-ml.sh`) to start up a
   container (similar to a DataHub instance).
3. Use the container from the command-line, or follow the URL on the
   containers startup screen to open a Jupyter Notebook.
   
### To Turn In

Start-up a container and turn the following information into
Gradescope in a file called `server.json`:

1. Upon logging into the jump-box server, run the command `uname -a`
   and save the output as a string in the `server.json` with key
   `"jump-box-info"`.
   
2. On the jump-box server, run the command `echo ~` and save the
   output as a string in the `server.json` with key
   `"home-directory"`.
   
3. Use the git command-line to clone the [methodology repository](https://github.com/afraenkel/DSC180A-DS-Methodology) into your home directory. As you work on your own projects, you will move code between your laptop and the remote server via GitHub. That way, you can seamlessly develop code on your laptop on smaller files and do larger processing on the server. (This step requires nothing to turn in).
   
3. Launch a container using the script `launch-scipy-ml.sh` and run
   the command `uname -a`. Save the output as a string in the `server.json` with key
   `"container-info"`.

4. Open a Jupyter Notebook from the URL given on the container's
   welcome screen. Save the URL as a string in `server.json` with key
   `"notebook-url"`.
   
To shutdown the container, type `ctrl-d`. Upload `server.json` to Gradescope.

Your `server.json` should look something like this:

```
{
    "jump-box-info": "Linux ... GNU/Linux",
    "home-directory": "/path/to/my/home/dir",
    "container-info": "Linux ... GNU/Linux",
    "notebook-url": "http://url.com/to/my/notebook"
}
```

Be sure to check your `server.json` file is valid json (e.g. using
pythons `json.load` function).
