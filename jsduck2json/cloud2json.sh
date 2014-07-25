if [ ! "$JSDUCK" ]; then
    if [ "$TI_ROOT" ]; then
        JSDUCK=${TI_ROOT}/jsduck
    else
        echo "No JSDuck dir \$JSDUCK and \$TI_ROOT not defined. Exiting."
        exit 1
    fi
fi

if [ ! "$DOCTOOLS" ]; then
    if [ "$TI_ROOT" ]; then
        DOCTOOLS=${TI_ROOT}/doctools
    else
        echo "No doctools dir \$DOCTOOLS and \$TI_ROOT not defined. Exiting."
        exit 1
    fi
fi

srcDirs="$TI_ROOT/cloud_docs/"

case "$1" in
	javadoc)
		OUTPUT="$TI_ROOT/aps_sdk/utilities/apidoc/android.json"
		SCRIPT="cloud2javadoc.py"
		;;
	appledoc)
		OUTPUT="$TI_ROOT/aps_sdk/utilities/apidoc/ios.json"
		SCRIPT="cloud2appledoc.py"
		;;
	solr)
		OUTPUT="$DOCTOOLS/dist/cloud_solr.json"
		SCRIPT="cloud2solr.py"
		;;
    *)
        OUTPUT="$DOCTOOLS/dist/api.json"
        SCRIPT="cloud2solr.py"

esac

ruby ${JSDUCK}/bin/jsduck --rest --export full --meta-tags $DOCTOOLS/meta --pretty-json -o - $srcDirs > ${DOCTOOLS}/build/cloud.json
## Remove warning messages
sed -i '' 's/Warning: Skipping tag summary//g' ${DOCTOOLS}/build/cloud.json
sed -i '' 's/Warning: Skipping tag base-url//g' ${DOCTOOLS}/build/cloud.json
sed -i '' 's/Warning: Skipping tag pseudo//g' ${DOCTOOLS}/build/cloud.json

python ${DOCTOOLS}/jsduck2json/${SCRIPT} ${DOCTOOLS}/build/cloud.json ${OUTPUT}
echo "Done! File generated at: $OUTPUT"
