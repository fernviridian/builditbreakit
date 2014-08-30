sudo apt-get install python-virtualenv
virtualenv env
. env/bin/activate
pip install pysqlcipher
echo "Run '. env/bin/activate' in your shell before logread or logappend."
