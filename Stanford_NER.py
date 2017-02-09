import nltk
import os

java_path = "C:/Program Files/Java/jre1.8.0_111/bin/java.exe" 
os.environ['JAVAHOME'] = java_path

from nltk.tag.stanford import StanfordNERTagger
st = StanfordNERTagger('C:\pentaho_projects\quick_try_outs\content\public\Python-NLTK\stanford-ner-2014-06-16\classifiers\english.all.3class.distsim.crf.ser.gz',
'C:\pentaho_projects\quick_try_outs\content\public\Python-NLTK\stanford-ner-2014-06-16\stanford-ner.jar')

with open('sample.txt', 'r') as f:
	sample = f.read()
	#print (sample)
	output = st.tag(sample.split())
	print (output)