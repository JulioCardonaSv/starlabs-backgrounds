all: generate

generate:
	python ./generate_other_wallpapers.py

clean:
	-rm ./gnome-background-properties/*
	-rm -r ./kde-wallpapers/*
	-rm ./mate-background-properties/*
	-rm ./xfce4-backdrops/*

install:
	-cp -r ./kde-wallpapers/* /usr/share/wallpapers/
	-cp -r ./backgrounds/* /usr/share/backgrounds/
	-cp -r ./cinnamon-background-properties /usr/share/
	-cp -r ./mate-background-properties /usr/share/
	-cp -r ./gnome-background-properties /usr/share/
	-cp ./xfce4-backdrops/* /usr/share/xfce4/backdrops/

uninstall:
	-rm -r /usr/share/wallpapers/Star\ Labs\ Systems\ -\ *
	-rm -r /usr/share/backgrounds/starlabs
	-rm /usr/share/cinnamon-background-properties/starlabs.xml
	-rm /usr/share/mate-background-properties/starlabs.xml
	-rm /usr/share/gnome-background-properties/starlabs.xml
	-rm /usr/share/xfce4/backdrops/starlabs_*.jpg
