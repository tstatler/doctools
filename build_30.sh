outdir=$TI_ROOT/doctools/dist/titanium/3.0
cd $TI_ROOT/titanium_mobile 
git checkout 3_1_X 
git pull appcelerator 3_1_X
cd $TI_ROOT/alloy
git checkout 1_1_X
git pull appcelerator 1_1_X
cd $TI_ROOT/doctools
rm -rf $outdir
sh deploy.sh -o alloy -o modules -g htmlguides-latest -d $outdir prod
rm -rf ~/Sites/titanium/3.0
rm -rf ~/Sites/titanium/landing/index.html
cp -rf $outdir ~/Sites/titanium/3.0
cp $TI_ROOT/appc_web_docs/titanium/landing/index.html ~/Sites/titanium/landing/index.html
