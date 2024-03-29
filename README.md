🐇 You take the window/apple blue pill, the story ends, you get force update and believe whatever you want to believe.
You take the Linux red pill, you stay in wonderland, and I show you how deep the rabbit hole goes.


[My favorit applications 🌟](https://github.com/AmosNimos/Xstaller)

[Debian based setup ⚙️](https://github.com/AmosNimos/debian-based-setup)

[Bash terminal config ⚙️](https://github.com/AmosNimos/bashrc)

[Linux Games 🎮](https://www.slant.co/topics/1933/~best-open-source-games)

[vim 📝](https://github.com/AmosNimos/VIM)

## basic advice 
> Use the shortcut __ctrl-f__ to search topics on this page.

# Installing linux

> Begginer: I suggest you start with [Ubuntu LTS](https://ubuntu.com/download) as your first [gnu/linux](https://fr.wikipedia.org/wiki/Linux_ou_GNU/Linux) [distribution](https://fr.wikipedia.org/wiki/Distribution_Linux).

> Advance:  I suggest you try [Debian LTS](https://wiki.debian.org/DebianOldStable) for a more barebone distribution.

## Preparation
- You need to make sure your computer is connected to the internet befor you start the installation.
- Get Yourself a USB Flash Drive of at least 5 GB.

> Warning: Your GPU integrated WIFI, external WIFI or other hardware component, might not be compatible with some distribution, some [driver](https://tldp.org/LDP/tlk/dd/drivers.html#:~:text=The%20Linux%20kernel%20device%20drivers,abstracts%20the%20handling%20of%20devices.) might need to be installed sepparatly.
> [Hardware compatibility ⚙️](https://linux-hardware.org/index.php?id=pci:1002-9850-1025-104b)

# Create a bootable linux distro flash drive

- Download Iso file from the official distribution website.

- In your terminal execute the following command to list ports.
~~~ 
sudo lsblk 
~~~

- Phisically plug usb device to your computer hardware.

- In your terminal execute the following command again to see what port have been added.
~~~ 
sudo lsblk 
~~~ 

- Find the name of the __usb port__ by comparing both lsblk output
~~~ 
sudo umount /dev/__NameOfUsbPort__
sudo dd bs=4M if=__PathToYOurIsoFile__ of=/dev/__NameOfUsbPort__ status=progress oflag=sync
~~~ 
- Wait for it to be installed.
- Then disconnect the phisical usb drive from your computer hardware, and reconnect it to see if the change have been made.

> All this could probably be automated by a shell file.

---


# Terminal based spreadsheet editor
~~~
sc
~~~

# Bash terminal cursor movement tips
http://teohm.com/blog/shortcuts-to-move-faster-in-bash-command-line/

> Move to the end on a line ctrl-e move to the beginning of a line ctrl-a.

> Note: ("meta key" is the "alt key")

---

# tts (text to speech)
https://www.youtube.com/watch?v=4uKTamXonPs
sudo apt install festival

## tts french francais
sudo apt install espeak

echo "Bonjour" | espeak -vfr

---

# Some keycode for key mapping
https://www.tcl.tk/man/tcl8.4/TkCmd/keysyms.htm

# Really cool terminal emulator
https://github.com/Swordfish90/cool-retro-term
```bash
wget https://github.com/Swordfish90/cool-retro-term/releases/download/1.1.1/Cool-Retro-Term-1.1.1-x86_64.AppImage
chmod a+x Cool-Retro-Term-1.1.1-x86_64.AppImage
./Cool-Retro-Term-1.1.1-x86_64.AppImage
```

# Show the history of comand in bash
history 

# ffmpeg
If you wish to compress your videos before uploading them to YouTube, you can use FFmpeg:

ffmpeg -i input -c:v libx264 -crf 21 -preset faster -pix_fmt yuv420p -maxrate 5000K -bufsize 5000K -vf 'scale=if(gte(iw\,ih)\,min(1920\,iw)\,-2):if(lt(iw\,ih)\,min(1920\,ih)\,-2)' -movflags +faststart -c:a aac -b:a 160k output

## lbry format
ffmpeg -i input.mkv -c:v libx264 -crf 21 -preset faster -pix_fmt yuv420p -maxrate 5000K -bufsize 5000K -vf 'scale=if(gte(iw\,ih)\,min(1920\,iw)\,-2):if(lt(iw\,ih)\,min(1920\,ih)\,-2)' -movflags +faststart -c:a aac -b:a 160k -max_muxing_queue_size 9999 output.mp4

---

# Download youtube video
sudo apt install youtube-dl
#youtube-dl can download the content of a chanel, playList or video with the url
#you can specify the destination with
youtube-dl -o 'outputDirectory/videoName' url

# Play audio file
play filename.format

# Record audio file
sudo apt install sox

# Terminal music player
1. sudo apt install cmus
2. sudo apt install moc 
> (to use moc the command is __mocp__)


# BASIC coding language shell
bwbasic

# pdf to text
pdftotext -layout input.pdf output.txt

# text to epub
ebook-convert input.txt output.epub

# epub to txt
ebook-convert input.epub output.txt
> (To read them from the terminal using the cat or less command.)

# odt to pdf
libreoffice --headless --convert-to pdf *.odt

# html to pdf
Install html to pdf
```bash
sudo apt-get install wkhtmltopdf
sudo ln -s /usr/bin/wkhtmltopdf /usr/local/bin/html2pdf
```
Use html to pdf
```bash
html2pdf source.html output.pdf
```
# open pdf 
```
evince
```
---



# what is my ip 
hostname -I | awk '{print $1}'

# Terminal text web browser
## web
- qutebrowser
- w3m

## gemini
- bollux

## Search engin
- https://wiby.me/

---

# windows manager
- awesome
[Awesome config](https://github.com/AmosNimos/awsom)
- i3

---

# sudoedit
sudoedit "/file/file.type"

# rc file are resouce file
> example /home/bashrc

exemple alisa py = "python3 programename.py"

# Change language ubuntu
Super+space change the language keyboard layout in ubuntu.

or 

setxkbmap us

# Rename a file
mv old-name new-name

# convert multiple spaces to a tabs of file content
sed 's/ \+ /\t/g' algo_strategy.py > algo_strategy1.py

# Fix sound... (Because sound break often)
sudo alsa force-reload

# Open the gui file manager at the current working directory of the terminal
xdg-open .

## Open new terminal from the current one
gnome-terminal

---

# Change gnome theme
gsettings set org.gnome.desktop.interface gtk-theme "Dracula"
gsettings set org.gnome.desktop.interface icon-theme "Dracula"
gsettings set org.gnome.desktop.wm.preferences theme "Dracula"
lxappearance

# to find app
sudo apt install synapse

Or

In the terminal type:
Whereis name_of_programme

> Don't forget to replace __name_of_programme__ with the actual name of the programe of file you are looking for.


## Nanorc
### (Configuration for the nano terminal text editor)
set tabsize 4
set linenumbers
set mouse

 cat vi
# Bash Usefull commands
- tail *file_name* (show the end of the file)
- head *file_name* (show the begening of the file)
- less *file_name* (show the content of the file)
- cat *file_name* (show the content of the file)
- vi (basic old shool text editor) 

> You can __Exit__ the __Vi__ and __Vim__ editor (without saving) by typing:

~~~
:q
~~~

- mkdir *directoryname* (create empty directory)
- touch *file_name* (create empty directory)
- rm *filename* (remove file)
- rmdir *directory_name* (remove empty directoryname)
- mkdir *directory_name* (Make a new directory)
- "something" > *file_name* (replace file content with "something")
- "something" >> *file_name* (append "something" at the end of file.format content)
- ls (list file in current directory)
- cd /path/to/directory (move to directory)
- cd (move to home directory)
- man (show manual of information about commandname)
- apropos (apropos command helps the user when they don't remember the exact command but knows a few keywords related to the command that define its uses or functionality.)
- mv *path_to/file_name* /path/to/another/directory (move file.format to directory)
- mv *old_name* *new_name* (rename oldname to newname)
- xkill (Click on a programme to force it to close)
- pwd (Print working directory)

- top (show running processes)
- ps (reports information on current running processes, outputting to standard output.)

> On my bashrc you have the fuction __hitman__ which use the __kill__ command.

- kill (kill running processes)

> On my bashrc you have the function __memory__ which use the __df__ command.

- df (disck free, display the amount of available disk space for file systems)

- du (allows a user to gain disk usage information quickly.)

- cp (copy files or group of files or directory.)


---

## Naming a file 

add the following to the name of a file you are creating from the terminal to append the current date __$(date +"(%m_%d_%Y)").__
Example:
~~~
filename_$(date +"%m_%d_%Y").txt
~~~

# Add acount to sudoers (sudo access)

su -

> Enter root password (if you don't have it, pray.)

cd /etc && echo "user_name ALL=(ALL)  ALL" >> /etc/sudoers

> (Don't forget to replace __user_name__ with your actuall user name.)

---

# Install .deb package

sudo dpkg -i [packagename].deb

---

# MOC MUSIC PLAYER THEME
> Theme alternatif : darkdot_theme transparent-background moca_theme darkdot_theme green_theme red_theme etc...
~~~
mkdir ./moc && cp /usr/share/doc/moc/examples/config.example ~/.moc/config && echo "Theme = /usr/share/moc/themes/darkdot_theme" >> ~/.moc/config
~~~

> To run command when you start the bash terminal you might need to append them in ~/.profile and check the Command/Run command as login shell preference.

--- 

# My 60% keyboard key modification
~~~
# Swap caps lock and escape
setxkbmap -option caps:swapescape

# Replace right shift with tilde 
xmodmap -e 'keycode 62 = asciitilde'
~~~

[Markdown Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)

### Threads Sites and Blog

A discussion on popular [Unix_commands](https://news.ycombinator.com/item?id=6360320)

Play Quake on your web browser on [Net_Quake](https://www.netquake.io/quake)
