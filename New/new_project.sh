cd $1
if [ -d "$2" ]; then
	echo "Project $2 already exists"
else
	echo "Creating Pauli Project at $1/$2 ..."
	mkdir $2
	cp -r /usr/local/lib/pauli_sdk/Template/* $2 
	echo "Project created successfully :D"
fi