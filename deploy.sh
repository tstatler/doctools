
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
python ./guides_parser.py --input "./htmlguides/toc.xml" --output "./build/guides"

compass compile ${JSDUCK}/template/resources/sass
ruby ${JSDUCK}/bin/jsduck --template ${JSDUCK}/template --config ./jsduck.config
cp -r "./htmlguides/images" "dist/images"
cp -r "./htmlguides/attachments" "dist/attachments"
cp -r "./htmlguides/css/common.css" "dist/resources/css/common.css"
cp ./resources/mock_video.png dist/resources/images/mock_video.png
cp ./resources/codestrong_logo_short.png dist/resources/images/codestrong_logo_short.png
