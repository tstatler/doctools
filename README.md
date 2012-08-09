DocTools
========

This repository contains build scripts, configuration files, and other miscellany related
to building the Titanium docs for JsDuck.

To build the docs, you must have a local clone of this repo, the titanium_mobile repo, and
the Titanium-flavored JsDuck repo.

## Initial Setup

1.   Clone all three repos, preferably into the same parent folder (for example, ~/work).

2.   Set the TI_ROOT environment variable to the parent directory of all three repos.

       TI_ROOT=~/work
        export TI_ROOT

     If the repos are in different locations, or use non-default names, you can set
     environment variables for each repo. See `deploy.sh`.

3.   Make sure you have Ruby installed, and install JsDuck's dependencies: 

        gem install compass
        gem install rdiscount
        gem install json
    
4.  Make sure you have python installed and install pyyaml and Pygments. 

        easy_install pyyaml
        easy_install Pygments

5.  Export the wiki docs as an Eclise Help archive. Extract the archive and rename the
    folder to ${DOCTOOLS_DIR}/htmlguides.

6.  If the jsduck_generator has not yet been added to Titanium mobile, obtain a copy of 
    it and place it in the `titanium_mobile/apidoc/generators` folder.

7.  Here goes nothing! Try building the docs:

        sh deploy.sh

8.  If all goes well, open dist/index.html and see how it looks.

