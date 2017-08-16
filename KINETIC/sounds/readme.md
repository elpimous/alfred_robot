Marytts install for ubuntu (tested on 16.04)
============================================

install :

	follow : https://github.com/scbickle/maryspeak
	I personnaly replaced '/opt' by '/usr/bin'

	open ~/.bash_aliases
	feed with : alias maryspeak='java -cp "/usr/bin/marytts-5.1/lib/*" -Dmary.base=/usr/bin/marytts-5.1 maryspeak.Maryspeak'


play :

	start marytts server : /usr/bin/marytts-5.1/bin$ ./marytts-server.sh
	run Alfred_talk.py,  to speek a sentence

Enjoy.

	elpimous12@orange.fr ----- Aout 2017
	------------------------------------
