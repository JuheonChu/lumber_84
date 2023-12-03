# Softwares

1. WSL Ubuntu (Window Subsystem Linux)
2. Google Colab
3. Docker

# How to run the program?

## Command line Interface (CLI)

1. Download ANTLR4 framework
  * Go to a directory that stores configuration files along with the installation packages: ``` cd /usr/local/lib ```.
  * Download the ANTLR4 jar file: ``` sudo wget https://www.antlr.org/download/antlr-4.13.1-complete.jar ```.

2. Set ANTLR4 as an Environment Variable
  * Open your ``` .bashrc ``` file: ``` nano ~/.bashrc ```.
  * Add the following line at the end of the ```.bashrc``` file: ``` export CLASSPATH=".:/usr/local/lib/antlr-4.9.2-complete.jar:$CLASSPATH" ```
  * Save and close the file.
  * Activate the changes by running the ``` source ~/.bashrc ``` command.
3. Download Python:
  *  Update the packages:  ``` sudo apt-get update ```.
  *  Install Python module:  ``` sudo apt install python3 ```.
  *  Install pip packages:  ``` sudo apt install python3-pip ```.
4. At your home directory, clone this GitHub repository using ``` git clone "https://github.com/JuheonChu/lumber_84.git" ```. If your git command is not working, install git by running ``` sudo apt install git ``` and then try cloning it. 

5. Copy the grammar file ``` lumber_84/jchu98/Expr.g4 ``` into your working directory.
   
6. Run the ANTLR4 pipeline.
  * Run the pipeline w/o listener: ``` antlr4 -Dlanguage=Python3 Expr.g4 -o <folder name> ```
  * Run the pipeline w/ the listener: ``` antlr4 -Dlanguage=Python3 -visitor Expr.g4 -o <folder name> ```
