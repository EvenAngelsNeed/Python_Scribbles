# tqdm
---

tqdm ('taqadum') is a progress bar for python scripts.

<br>

[Link to: tqdm documentation](https://tqdm.github.io/)

<br>

	pip3 install tqdm

<br>
Basic usage:

	import time
	import tqdm
	
	for i in tqdm.tqdm(range(20)):
	
		# Do some processing here.
		time.sleep(0.1)
		
		print("done!")


<br>

*Be aware that using the print() statement in a tqdm loop will break the bar visually. However you can use 'tqdm.tqdm.write("string")' instead. Printing will appear above the bar.*
<br>

Some more examples see test_tqdm.py

