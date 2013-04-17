fail_on_error() {
    if [ $# -ne 2 ] ; then
        echo "Wrong number of arguments."
        exit 1
    fi
    if [ $1 -ne 0 ] ; then
        echo "Error: " $2
        exit 1
    fi
}
outdir=$TI_ROOT/doctools/dist/titanium/3.0
cd $TI_ROOT/titanium_mobile 
git checkout 3_1_X 
fail_on_error $? "Could not checkout titanium branch."
git pull appcelerator 3_1_X
fail_on_error $? "Pull failed on titanium branch."
cd $TI_ROOT/alloy
git checkout 1_1_X
fail_on_error $? "Could not checkout alloy branch."
git pull appcelerator 1_1_X
fail_on_error $? "Pull failed on alloy branch."
cd $TI_ROOT/doctools
rm -rf $outdir
sh deploy.sh -o alloy -o modules -g htmlguides-latest -d $outdir prod
fail_on_error $? "Deploy failed."
rm -rf ~/Sites/titanium/3.0
rm -rf ~/Sites/titanium/landing/index.html
cp -rf $outdir ~/Sites/titanium/3.0
cp $TI_ROOT/appc_web_docs/titanium/landing/index.html ~/Sites/titanium/landing/index.html
