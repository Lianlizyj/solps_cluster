#!bin/bash

# step 0
path=`pwd`;
echo ${path};
cp $path/../bb/* .;

# step 1 delete the postfix('.stencil')
cp b2.neutrals.parameters.stencil b2.neutrals.parameters;
#cp b2.boundary.parameters.stencil b2.boundary.parameters;
cp b2ah.dat.stencil b2ah.dat

# step 2 modify the input files
	# b2mn.dat
	
	# step 1
	
