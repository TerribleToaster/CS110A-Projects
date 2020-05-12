#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat April 12 12:46:37 2020

@author: clintonpotter

Intakes the Titanic data set from https://vincentarelbundock.github.io/Rdatasets/datasets.html
and calculates the following:
Survival/Death by gender
Survival/Death  by class
Survival/Death by age
"""
from pathlib import Path 
import os
import pprint

titanicFile = open('/Users/clintonpotter/Desktop/Assignment 7/Titanic.csv') #opens file from directory
Manifest = titanicFile.read() #assigns Manifest to list object
Manifest = Manifest.replace('"',"") #removes the '' from strings in list, this makes data look nicer
titanicFile.close()

def manifestBuilder(Manifest):
	tKeys = Manifest.split('\n')[0].split(',') #builds new key list, spliting only the first line [0] and 
	# then spliting every object in that line by ','.
	dictManifest = {}
	for row in range(1,33):
		# for loop running through each index of data with the intent of building a dictionary from lists
		tvalue = Manifest.split('\n')[row].split(',') #splits each row into list of values
		dictManifest[tKeys[0]] = dictManifest.get(tKeys[0],[]) + [tvalue[0]] #assigns first key to first value in list
		dictManifest[tKeys[1]] = dictManifest.get(tKeys[1],[]) + [tvalue[1]]
		dictManifest[tKeys[2]] = dictManifest.get(tKeys[2],[]) + [tvalue[2]]
		dictManifest[tKeys[3]] = dictManifest.get(tKeys[3],[]) + [tvalue[3]]
		dictManifest[tKeys[4]] = dictManifest.get(tKeys[4],[]) + [tvalue[4]]
		dictManifest[tKeys[5]] = dictManifest.get(tKeys[5],[]) + [tvalue[5]]
	return dictManifest

def genderSurvival(dictManifest):
	maleSurvivors = 0
	maleDeaths = 0
	fSurvivors = 0
	fDeaths = 0
	gsurvivalDict = {}
	for value in range(len(dictManifest[''])): #runs through all indices
		if dictManifest["Sex"][value] == 'Male' and dictManifest["Survived"][value] == 'Yes':
			#if the survivor entry listed the Sex as Male and Survived as Yes
			maleSurvivors = int(dictManifest["Freq"][value]) + maleSurvivors
			#takes Freq value and adds it to maleSurvivors
		elif dictManifest["Sex"][value] == 'Male' and dictManifest["Survived"][value] == 'No':
			maleDeaths = int(dictManifest["Freq"][value]) + maleDeaths

		elif dictManifest["Sex"][value] == 'Female' and dictManifest["Survived"][value] == 'Yes':
			fSurvivors = int(dictManifest["Freq"][value]) + fSurvivors
		
		elif dictManifest["Sex"][value] == 'Female' and dictManifest["Survived"][value] == 'No':
			fDeaths = int(dictManifest["Freq"][value]) + fDeaths
	gsurvivalDict = {'Males': [maleSurvivors, maleDeaths], 'Females': [fSurvivors, fDeaths]}
	return gsurvivalDict

def classSurvival(dictManifest):
	crewSurvivors = 0
	crewDeaths = 0
	firstSurvivors = 0
	firstDeaths = 0
	secondSurvivors = 0
	secondDeaths = 0
	thirdSurvivors = 0
	thirdDeaths = 0
	cSurvivalDict = {}
	for value in range(len(dictManifest[''])): #runs through all indices
		if dictManifest["Class"][value] == 'Crew' and dictManifest["Survived"][value] == 'Yes':
			#if the survivor entry listed the Sex as Male and Survived as Yes
			crewSurvivors = int(dictManifest["Freq"][value]) + crewSurvivors
			#takes Freq value and adds it to maleSurvivors
		elif dictManifest["Class"][value] == 'Crew' and dictManifest["Survived"][value] == 'No':
			crewDeaths = int(dictManifest["Freq"][value]) + crewDeaths

		elif dictManifest["Class"][value] == '1st' and dictManifest["Survived"][value] == 'Yes':
			firstSurvivors = int(dictManifest["Freq"][value]) + firstSurvivors

		elif dictManifest["Class"][value] == '1st' and dictManifest["Survived"][value] == 'No':
			firstDeaths = int(dictManifest["Freq"][value]) + firstDeaths

		elif dictManifest["Class"][value] == '2nd' and dictManifest["Survived"][value] == 'Yes':
			secondSurvivors = int(dictManifest["Freq"][value]) + secondSurvivors

		elif dictManifest["Class"][value] == '2nd' and dictManifest["Survived"][value] == 'No':
			secondDeaths = int(dictManifest["Freq"][value]) + secondDeaths

		elif dictManifest["Class"][value] == '3rd' and dictManifest["Survived"][value] == 'Yes':
			thirdSurvivors = int(dictManifest["Freq"][value]) + thirdSurvivors

		elif dictManifest["Class"][value] == '3rd' and dictManifest["Survived"][value] == 'No':
			thirdDeaths = int(dictManifest["Freq"][value]) + thirdDeaths
	cSurvivalDict = {'Crew': [crewSurvivors, crewDeaths], '1st': [firstSurvivors, firstDeaths], '2nd': [secondSurvivors, secondDeaths], '3rd': [thirdSurvivors, thirdDeaths]}
	return cSurvivalDict

def ageSurvival(dictManifest):
	childSurvivors = 0
	childDeaths = 0
	adultSurvivors = 0
	adultDeaths = 0
	aSurvivalDict = {}
	for value in range(len(dictManifest[''])): #runs through all indices
		if dictManifest["Age"][value] == 'Child' and dictManifest["Survived"][value] == 'Yes':
			childSurvivors = int(dictManifest["Freq"][value]) + childSurvivors

		elif dictManifest["Age"][value] == 'Child' and dictManifest["Survived"][value] == 'No':
			childDeaths = int(dictManifest["Freq"][value]) + childDeaths

		elif dictManifest["Age"][value] == 'Adult' and dictManifest["Survived"][value] == 'Yes':
			adultSurvivors = int(dictManifest["Freq"][value]) + adultSurvivors
		
		elif dictManifest["Age"][value] == 'Adult' and dictManifest["Survived"][value] == 'No':
			adultDeaths = int(dictManifest["Freq"][value]) + adultDeaths
	aSurvivalDict = {'Child': [childSurvivors, childDeaths], 'Adult': [adultSurvivors, adultDeaths]}
	return aSurvivalDict

dictManifest = manifestBuilder(Manifest)

genderSurvivalDict = genderSurvival(dictManifest)
classSurvivalDict = classSurvival(dictManifest)
ageSurvivalDict = ageSurvival(dictManifest)
#pprint.pprint(genderSurvivalDict)
#print(classSurvivalDict)


glist = []
clist = []
alist = []
masterlist = []
glist = [(k, v) for k, v in genderSurvivalDict.items()] 
clist = [(k, v) for k, v in classSurvivalDict.items()] 
alist = [(k, v) for k, v in ageSurvivalDict.items()] 
masterlist = glist + clist + alist
print("('Category', [Survived, Died]")
pprint.pprint(masterlist)


