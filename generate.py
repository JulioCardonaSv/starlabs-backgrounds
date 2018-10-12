#!/usr/bin/python2

import os, commands, sys, glob

class Wallpaper:
	def __init__ (self, name):
		self.name = name
		self.filename = None
		self.artist = None

directory = os.getcwd()
wallpaperDirectory = "./backgrounds/starlabs"

CODENAME = "StarLabs"
wallpapers = []

# MAKE GNOME/MATE Wallpapers
os.system("sed \"s/cinnamon-wp/gnome-wp/\" cinnamon-background-properties/%s.xml > gnome-background-properties/%s.xml" % (CODENAME.lower(), CODENAME.lower()))
os.system("sed \"s/cinnamon-wp/mate-wp/\" cinnamon-background-properties/%s.xml > mate-background-properties/%s.xml" % (CODENAME.lower(), CODENAME.lower()))

#MAKE Xfce Wallpapers

for root, dirs, files in os.walk(wallpaperDirectory):
	for basename in files:
		os.system("ln -s /usr/share/backgrounds/%s/%s xfce4-backdrops/%s" % (CODENAME.lower(), basename, basename))

os.chdir("xfce4-backdrops")
os.system("rename 's/^/%s_/' *" % CODENAME.lower())
os.chdir("..")

# MAKE KDE Wallpapers
with open ("cinnamon-background-properties/%s.xml" % CODENAME.lower(), "r") as metadata_file:
	for line in metadata_file:
		line = line.strip()
		if line.startswith("<name>"):
			name = line.replace("<name>", "").replace("</name>", "")
			wallpaper = Wallpaper(name)
			wallpapers.append(wallpaper)
		elif line.startswith("<filename>"):
			wallpaper.filename = line.replace("<filename>", "").replace("</filename>", "")
		elif line.startswith("<artist>"):
			wallpaper.artist = line.replace("<artist>", "").replace("</artist>", "")

os.system("rm -rf kde-wallpapers/*")
os.chdir("kde-wallpapers")
for wallpaper in wallpapers:
	print "WALL: ", wallpaper.name
	os.system("mkdir -p '%s'/contents/images" % (wallpaper.name))
	wallpaper.filepath = wallpaper.filename.replace ("/usr/share", "%s") % (directory)
	os.system("convert %s -resize 400x250 '%s'/contents/screenshot.jpg" % (wallpaper.filepath, wallpaper.name))
	dimensions = commands.getoutput("identify %s | awk {'print $3'}" % wallpaper.filepath)
	if not "x" in dimensions:
		print "Erroneous dimensions: %s for %s" % (dimensions, wallpaper.path)
		sys.exit(1)
	suffix = "jpg"
	if (wallpaper.filename.endswith(".png")):
		suffix = "png"
	os.system("ln -s %s '%s'/contents/images/%s.%s" % (wallpaper.filename, wallpaper.name, dimensions, suffix))
	os.system("sed \"s/NAME/%s/g; s/ARTIST/%s/g\" ../kde-desktop.template > '%s/metadata.desktop'" % (wallpaper.name, wallpaper.artist, wallpaper.name))
