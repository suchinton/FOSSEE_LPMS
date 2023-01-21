#!/bin/sh

# script to generate binary and create appimagetool

chmod u+x ./appimagetool-x86_64.AppImage

#cleanup
rm FOSSEE_GUI.AppDir/usr/bin/Fossee & sleep 2

# binary creation
pyinstaller --onefile Fossee

#cleanup
cp dist/Fossee FOSSEE_GUI.AppDir/usr/bin/ & sleep 2
rm -r build/ & sleep 2
rm -r dist/ & sleep 2
rm Fossee.spec

#command="
ARCH=x86_64 ./appimagetool-x86_64.AppImage FOSSEE_GUI.AppDir/
#exec $command
