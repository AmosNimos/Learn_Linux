[Debian setup](https://github.com/AmosNimos/debian-based-setup)

[Bash terminal](https://github.com/AmosNimos/bashrc)

[vim](https://github.com/AmosNimos/VIM)

# Bash terminal cursor movement tips
http://teohm.com/blog/shortcuts-to-move-faster-in-bash-command-line/

> Move to the end on a line ctrl-e move to the beginning of a line ctrl-a.

> ("meta key" is the "alt key")

---

# tts (text to speech)
https://www.youtube.com/watch?v=4uKTamXonPs
sudo apt install festival

## tts french francais
sudo apt install espeak

echo "bonjour" | espeak -vfr

---

# gui __selection__ to a command
sudo apt install xsel

# some key code for key mapping
https://www.tcl.tk/man/tcl8.4/TkCmd/keysyms.htm

# really cool terminal emulator
https://github.com/Swordfish90/cool-retro-term
```bash
wget https://github.com/Swordfish90/cool-retro-term/releases/download/1.1.1/Cool-Retro-Term-1.1.1-x86_64.AppImage
chmod a+x Cool-Retro-Term-1.1.1-x86_64.AppImage
./Cool-Retro-Term-1.1.1-x86_64.AppImage
```

# show the history of comand in bash
history 

# mpv
mpv can open entire folder and you use the "enter key to skip to the next video"

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

# Bash Usefull commands
- tail filename.format (show the end of the file)
- head filename.format (show the begening of the file)
- less fielname.format (show the begening of the file)
- mkdir directoryname (create empty directory)
- touch filename.format (create empty directory)
- rm filename (remove file)
- rmdir directoryname (remove empty directoryname)
- "something" > file.format (replace file content with "something")
- "something" >> file.format (append "something" at the end of file.format content)
- ls (list file in current directory)
- cd /path/to/directory (move to directory)
- cd (move to home directory)
- man commandname (show manual of information about commandname)
- mv /path/to/file.format /path/to/another/directory (move file.format to directory)
- mv oldname.format newname.format (rename oldname to newname)
- xkill (Click on a programme to force it to close)

---

# Add acount to sudoers (sudo access)

su -

> Enter root password (if you don't have it, pray.)

cd /etc && echo "user_name ALL=(ALL)  ALL" >> /etc/sudoers

> (Don't forget to replace __user_name__ with your actuall user name.)

---

# Install .deb package

sudo dpkg -i [packagename].deb

# Create a bootable linux distro flash drive isntaller 

- Download Iso file

> Suggestion: 
> If "Nvidia hardware" Then: Install Ubuntu LTS; Else: Install Debian LTS;

- sudo lsblk 
- Phisically plug usb device to your computer hardware.
- sudo lsblk 
- Find the name of the __usb port__ by comparing both lsblk output
- sudo umount /dev/__NameOfUsbPort__
- sudo dd bs=4M if=__PathToYOurIsoFile__ of=/dev/sdb status=progress oflag=sync
- Wait for it to be installed.
- Then disconnect the phisical usb drive from your computer hardware, and reconnect it to see if the change have been made.

> All this could be automated by a shell file.

[Markdown Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)
