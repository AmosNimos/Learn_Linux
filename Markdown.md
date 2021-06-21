# Requirements
1. sudo apt-get install pandoc texlive-latex-base texlive-fonts-recommended texlive-extra-utils texlive-latex-extra
2. sudo apt install markdown
3. sudo apt update 
4. sudo apt upgrade

# Markdown to pdf
```bash
pandoc README.md -o README.pdf
```
# Markdown to epub

```bash
pandoc README.md -o README.epub
```

!!! Be sure to have correct Markdown formating if you whant this to work. !!!

# Markdown to html
```bash
markdown README.md > README.html
```
## Sources
[Source 1](https://blog.podkalicki.com/markdown-to-pdf-quick-howto-for-linux-ubuntu/)
[Source 2](https://linux.die.net/man/1/markdown)
