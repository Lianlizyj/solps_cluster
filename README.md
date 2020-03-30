# Solps_cluster
## Scriprs for solps in linux
---
- exp: create sequence from user input;
	e.g. exp 1 2 3 5 7
- tt: create case cluster for parameter scannning
	callback: tt
- rtime: return the average time of case runing
	callback: rtime
- m2scp: shortcuts for scp
- myscp: sjortcuts for scp
- most_data: create data for analysis by b2plot
- scan: a loop tool for case scanning
- bb: copy base input file to a base case, which is the source for tt
- fcpd : copy a file to all of the directory in a common father path,which you sepcified
	e.g. fcpd file_name dir_name(absolute path) 
- ups and ups2: plot a case upstream profiles. ups2 can create figure for two different case for comparing
	e.g. bash ups (in a case file)
	e.g. bash ups2 case_a/ case_b (in the father path of case,which you want to known)
	tips: gv ups.eps ;gv ups2.eps
- gn and gn2: plot case downstream profiles, which is similar to ups and ups2
	e.g. bash gn
	e.g. bash gn2 case_a/ gn2_b/
	tips: if you want to check the profiles, gv base.eps and gv base2.eps corespondingly
- spt: b2plot script for sputering 
- 2D_OT: b2plot scripts for case analysis
---




