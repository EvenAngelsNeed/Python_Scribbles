
### Creating a virtual environment: ###

----------

<br>

**Windows - Using CMD:**

If not already installed:
 
	pip3 install virtualenv
<br>

Change to or start in the parent folder.

Create a virtual environment:

*(Use your preferred name for test_venv.)*


	python3 -m venv test_venv

<br>

Activate environment:
 
	test_venv\Scripts\activate

<br>

*Or in Git bash use:*
 
	test_venv\Scripts\. activate

<br>

If you want to install some packages:

	pip3 install Flask

<br>

Check packages installed correctly:

	pip3 freeze

<br>

Change directory and work in the virtual environment:

	cd test_venv

<br>


Finally deactivate the virtual environment:


	deactivate

<br>
