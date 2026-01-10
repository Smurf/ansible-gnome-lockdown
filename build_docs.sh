if [ ! -d .venv ]
then
	python -m venv .venv
fi

source .venv/bin/activate
rm -rf docs/build
antsibull-docs sphinx-init --use-current --dest-dir docs smurf.gnome_lockdown
cd docs
pip install -r requirements.txt
./build.sh
