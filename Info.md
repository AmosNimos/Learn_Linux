# Bash terminal cursor movement tips
http://teohm.com/blog/shortcuts-to-move-faster-in-bash-command-line/
> ("meta key" is the "alt key")

# tts
https://www.youtube.com/watch?v=4uKTamXonPs
sudo apt install festival
---

#tts french francais
sudo apt install espeak
echo "bonjour" | espeak -vfr

#pipe gui selection to a command
sudo apt install xsel

some key code for key mapping
https://www.tcl.tk/man/tcl8.4/TkCmd/keysyms.htm

# Code in basic, in the terminal, can also open .bas file.
bwbasic

really cool terminal emulator
https://github.com/Swordfish90/cool-retro-term

wget https://github.com/Swordfish90/cool-retro-term/releases/download/1.1.1/Cool-Retro-Term-1.1.1-x86_64.AppImage
chmod a+x Cool-Retro-Term-1.1.1-x86_64.AppImage
./Cool-Retro-Term-1.1.1-x86_64.AppImage

cd ~/Documents/files/deb 
./Cool-Retro-Term-1.1.1-x86_64.AppImage

#show the history of comand in bash
history 

mpv can open entire folder and you use the "enter key to skip to the next video"

If you wish to compress your videos before uploading them to YouTube, you can use FFmpeg:

ffmpeg -i input -c:v libx264 -crf 21 -preset faster -pix_fmt yuv420p -maxrate 5000K -bufsize 5000K -vf 'scale=if(gte(iw\,ih)\,min(1920\,iw)\,-2):if(lt(iw\,ih)\,min(1920\,ih)\,-2)' -movflags +faststart -c:a aac -b:a 160k output

# with calibre convert epub to txt to read them from the terminal using the cat or less command
ebook-convert input.epub output.txt


#download youtube video
sudo apt install youtube-dl
#youtube-dl can download the content of a chanel, playList or video with the url
#you can specify the destination with
youtube-dl -o 'outputDirectory/videoName' url

##Play audio file
play filename.format

##Record audio file
sudo apt install sox

##Terminal music player
moc 
# to use moc
mocp

cmus

#bash
move to the end on a line ^e move to the beginning of a line ^a.

#BASIC coding language shell
bwbasic

lbry format
ffmpeg -i input.mkv -c:v libx264 -crf 21 -preset faster -pix_fmt yuv420p -maxrate 5000K -bufsize 5000K -vf 'scale=if(gte(iw\,ih)\,min(1920\,iw)\,-2):if(lt(iw\,ih)\,min(1920\,ih)\,-2)' -movflags +faststart -c:a aac -b:a 160k -max_muxing_queue_size 9999 output.mp4

#pdf to text
pdftotext -layout input.pdf output.txt

#text to epub
ebook-convert input.txt output.epub

#what is my ip 
hostname -I | awk '{print $1}'

#ricing
#it mean making your own icon, customise your theme and shortcut and configuarion file.

##terminal browser
#web
qutebrowser
w3m

#gemini
bollux

#windows manager
i3
awesome

sudoedit
# sudoedit "/file/file.type"

#rc file are resouce file
#example /home/bashrc
alias new=old
#exemple alisa py = "python3 programename.py"

Super+space change the language keyboard layout.

#rename a file
mv old-name new-name

#convert multiple spaces to a tabs of file content
sed 's/ \+ /\t/g' algo_strategy.py > algo_strategy1.py

#fix sound...
sudo alsa force-reload

#open the gui file manager at the current working directory of the terminal
xdg-open .

#change theme
gsettings set org.gnome.desktop.interface gtk-theme "Dracula"
gsettings set org.gnome.desktop.interface icon-theme "Dracula"
gsettings set org.gnome.desktop.wm.preferences theme "Dracula"
lxappearance

#rendering engine?
picom from compton

#to find app
synapse
