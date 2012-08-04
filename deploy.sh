
if [ ! "$TI_DOCS" ]
then
    if [ "$TI_ROOT" ]
    then
        TI_DOCS=${TI_ROOT}/titanium_mobile/apidoc
    else
        echo "No doc root \$TI_DOCS and \$TI_ROOT not defined. Exiting."
        exit
    fi
fi
if [ ! "$JSDUCK" ]
then
    if [ "$TI_ROOT" ]
    then
        JSDUCK=${TI_ROOT}/jsduck
    else
        echo "No JSDuck dir \$JSDUCK and \$TI_ROOT not defined. Exiting."
        exit
    fi
fi

if [ ! "$DOCTOOLS" ]
then
    if [ "$TI_ROOT" ]
    then
        DOCTOOLS=${TI_ROOT}/doctools
    else
        echo "No doctools dir \$DOCTOOLS and \$TI_ROOT not defined. Exiting."
        exit
    fi
fi

python ${TI_DOCS}/docgen.py -f jsduck -o ./build
python ${JSDUCK}/guides_parser.py --input "./htmlguides/toc.xml" --output "./build/guides"

compass compile ${JSDUCK}/jsduck/template/resources/sass
ruby ${JSDUCK}/jsduck/bin/jsduck --config ./jsduck/jsduck.config
cp -r "${JSDUCK}/htmlguides/images" "dist/images"
cp -r "${JSDUCK}/htmlguides/attachments" "dist/attachments"
cp -r "${JSDUCK}/htmlguides/css/common.css" "dist/resources/css/common.css"
cp ${JSDUCK}/mock_video.png dist/resources/images/mock_video.png
cp ${JSDUCK}/codestrong_logo_short.png dist/resources/images/codestrong_logo_short.png
# cp -r "/landing" "dist/landing"
