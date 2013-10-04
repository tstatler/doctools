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

if [ ! "$ALLOY" ]; then
    if [ "$TI_ROOT" ]; then
        ALLOY=${TI_ROOT}/alloy
    else
        echo "No alloy dir \$ALLOY and \$TI_ROOT not defined. Exiting."
        exit 1
    fi
fi

alloyDirs="${ALLOY}/Alloy/lib ${ALLOY}/docs/apidoc
	$(find $ALLOY/widgets -type d -name controllers)
	$(find $ALLOY/Alloy/builtins -maxdepth 1 -type f ! -name moment.js)"

ruby ${JSDUCK}/bin/jsduck --external "void,Callback,Backbone.Collection,Backbone.Model,Backbone.Events" --export full --pretty-json -o - $alloyDirs > ${DOCTOOLS}/build/alloy.json
python ${DOCTOOLS}/jsduck2json/jsduck2json.py ${DOCTOOLS}/build/alloy.json ${DOCTOOLS}/build/api.json
echo "Done! File generated at: $DOCTOOLS/build/api.json"
