[Source](https://blog.podkalicki.com/markdown-to-pdf-quick-howto-for-linux-ubuntu/)
1. sudo apt-get install pandoc texlive-latex-base texlive-fonts-recommended texlive-extra-utils texlive-latex-extra
2. sudo apt update 
3. sudo apt upgrade

```bash
 pandoc README.md -o README.pdf
```

!!! Be sure to have correct Markdown formating if you whant this to work. !!!
