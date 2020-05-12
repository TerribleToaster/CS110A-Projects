#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat April 12 12:46:37 2020

@author: clintonpotter

This program downloads a website using the request module and parses it using the beautiful soup module.
It then finds all the hyperlinks on the website and prints them out. If an error is returned it will print
"This link is broken" then the error and website.
"""
def linkchecker(site):


	import requests, bs4
	res = requests.get(site)
	#downloads site info
	website = bs4.BeautifulSoup(res.text,'html.parser')
	#stores site as variable

	for link in website.find_all('a'):
	#finds all <a> references in html and returns them
		site = link.get('href')
		#stores the href value from the <a>'s'
		if site[0:5] != "https":
		#checks if it is a proper website link, if not it passes
			pass
		else:
			reqs = requests.get(site)
			#downloads site info
			try:
				reqs.raise_for_status()
				#tests code for error
			except Exception as exc:
				print('This link is broken: %s' % (exc))
				#if code returns error it prints error
			else:
				print(site)
				#if no error prints site.



linkchecker("https://blog.fluidui.com/top-404-error-page-examples/")


