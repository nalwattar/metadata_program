import sys 
import Bio.SeqIO
import csv
import subprocess
import Bio.SeqRecord
import unittest
import os

class SequenceMetadata(object):

    #Initialiser

    def __init__(self, seqRecord):
        self.seqRecord = seqRecord

    def __str__(self):
    	return '(\'%s\',\'%s\',\'%s\')' % (self.seqRecord.id, self.seqRecord.annotations['organism'], self.seqRecord.annotations['accessions'][0], self.seq)

    def makeRowDict(self):
    	return {'idNumber': self.seqRecord.id, 'organism': self.seqRecord.annotations['organism'], 'accessionNumber': self.seqRecord.annotations['accessions'][0]}
        
    
def readMetadata(gbFnameList):
    sequenceMetadataList = []
    for gbFname in gbFnameList:
        #print(gbFname)
        record = Bio.SeqIO.read(gbFname, 'genbank')
        sequenceMetadata = SequenceMetadata(record)
        sequenceMetadataList.append(sequenceMetadata)
    return sequenceMetadataList

def test_readMetadata():
    test = readMetadata(sys.argv[3:])
    print(test)
    
def writeMetadataToCsv(sequencesList, csvFile):
    sequenceMetadataFieldnameList = ['idNumber', 'organism', 'accessionNumber']
    writer = csv.DictWriter(csvFile, fieldnames = sequenceMetadataFieldnameList, restval='no info available')
    writer.writeheader()
    for sequenceMetadata in sequencesList:
        #print('loop is running')
        writer.writerow(sequenceMetadata.makeRowDict())

def test_writeMetadataToCsv():
	sequenceMetadataList = []
	sequenceMetadata = SequenceMetadata('1234', 'palm', '5678')
	sequenceMetadataList.append(sequenceMetadata)
	with open(sys.argv[1], 'w') as csvFile:
		writeMetadataToCsv(sequenceMetadataList, csvFile)
#test_writeMetadataToCsv()

def runWriteMetadataToCsv():
	sequenceMetadataList = []
	sequenceMetadata = SequenceMetadata()
	sequenceMetadataList.append(sequenceMetadata)
	with open(sys.argv[1], 'w') as csvFile:
		writeMetadataToCsv(sequenceMetadataList, csvFile)

def mergeSequencesAndConvertToFasta(sequencesList, fastaFile):
    sequencesList = []
    for sequence in sequencesList:
        line = Bio.SeqIO.write(gbFname.seqRecord, fastaFile, 'fasta')
        sequencesList.append(sequence)
    return sequencesList

def pOpenForGuidetree(sequencesList, fastaFile):
	p = subprocess.Popen(['mafft', '--auto', '--reorder', '-'], stdin = subprocess.PIPE, stdout = subprocess.PIPE, universal_newlines = True)
	pid = os.fork()

	if pid >= 0:
		p.stdout.close()
		Bio.SeqIO.write(sequencesList, p.stdin, 'fasta')
		p.stdin.close()
		os.exit

	sequencesList = mergeSequencesAndConvertToFasta(sequencesList, fastaFile)
	records = list(Bio.SeqIO.parse(p.stdout, 'fasta'))
	#print(records)

#test_readMetadata()
#check arguments needed to run with
#if not exit/raise exception 
#if true put csv name into suitable variable and gb names into a suitable variable
sequencesList = readMetadata(sys.argv[3:])
#with open(sys.argv[1], 'w') as csvFile:
#	writeMetadataToCsv(sequencesList, csvFile)
#with open(sys.argv[2], 'w') as fastaFile:
#    mergeSequencesAndConvertToFasta(sequencesList, fastaFile)
#sys.exit(1)
mergeSequencesAndConvertToFasta(sequencesList, fastaFile)
#pOpenForGuidetree()
