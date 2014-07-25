pushd $TI_ROOT/appc_web_docs/titanium
git rm -rf 3.0
cp -r $TI_ROOT/doctools/dist/titanium/3.0 .
git add 3.0
pushd data/solr
cp $TI_ROOT/doctools/dist/titanium/data/solr/* .
popd
popd
