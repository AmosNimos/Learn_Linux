# How to do math calculation in the nash terminal

> There are several solutions listed (shell, awk, dc, perl, python, etc.).

A function may be defined with any option (gawk seems to be the most flexible to use):

~~~
c () { local in="$(echo " $*" | sed -e 's/\[/(/g' -e 's/\]/)/g')";
       gawk -M -v PREC=201 -M 'BEGIN {printf("%.60g\n",'"${in-0}"')}' < /dev/null
     }
~~~

And use it like:
~~~
$ c 236- 192
44
~~~

## Shell

The simplest calc in CLI is the CLI (shell) itself (If IFS is default):

~~~
$ echo $(( 22 + 333 ))
355

~~~

Spaces could be omitted:
~~~
$ echo $((22*333))
7326
~~~

As it is part of POSIX almost all shells have it. And it includes most of C language math functionality (except that zsh has a different precedence, set C_PRECEDENCES to restore it to a compatible value):
~~~
$ echo $((22*333^2))
7324
~~~

And some shells have most of the C language math syntax (including comma):
~~~
$ echo $((a=22,b=333,c=a*b,c))
7326
~~~

But it is only integer math (and usually less than 263 in present day OSes) in some shells:
~~~
$ echo $((1234/3))
411

$ zsh -c 'echo $((2**63))'
-9223372036854775808
~~~

Some shells could do floating math:
~~~
$ ksh -c 'echo $((1234/3.0))'
411.333333333333333

$ ksh -c 'echo $((12345678901234567890123/3.0))'
4.11522630041152263e+21
Avoid zsh (zcalc has similar problems):

$ zsh -c 'echo $((12345678901234567890123 + 1))'
zsh:1: number truncated after 22 digits: 12345678901234567890123 + 1
-1363962815083169259
I recommend you to avoid expr, it needs weird escapes sometimes:

$ expr 22 \* 333
7326
~~~

## bc
> At the next level is (also POSIX)bc (cousin of RPN dc)

$ echo '22*333' | bc
7326

$ echo '22 333 * p' | dc
7326
The dc was (historically) used to implement bc and got excluded from POSIX in 2017.

Shorter if your shell supports it:

~~~
$ bc <<<'22*333'
7326
Or even:

$ <<<'22*333' bc
7326
Both are arbitrary precision calculators with some internal math functions:

$ bc <<<2^200
1606938044258990275541962092341162602522202993782792835301376

$ echo 's(3.1415/2)' | bc -l        # sine function
.99999999892691403749

~~~

## awk

After those really basic calc tools, you need to go up to other languages

~~~ 
$ awk "BEGIN {print (22*33)/7}"
103.714

$ perl -E "say 22*33/7"
103.714285714286

$ python3 -c "print(22*33/7)"
103.71428571428571

$ php -r 'echo 22*33/7,"\n";'
103.71428571429
~~~

## function

You may define a function of any of the above options:

~~~
c () 
{ 
    local in="$(echo " $*" | sed -e 's/\[/(/g' -e 's/\]/)/g')";
    gawk -M -v PREC=201 -M 'BEGIN {printf("%.60g\n",'"${in-0}"')}' < /dev/null
}
~~~

And use:

~~~
$ c 22* 33 /7                   # spaces or not, it doesn't matter.
103.714285714285714285714285714285714285714285714285714285714
~~~


The original source of this documentation is on [stackexchange](https://unix.stackexchange.com/questions/480121/simple-command-line-calculator), This answer was given by user [ImHere](https://unix.stackexchange.com/users/232326/imhere).
