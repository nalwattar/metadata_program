import sys 
from Bio import SeqIO
import csv

class SequenceMetadata(object):

    #Initialiser

    def __init__(self, idNumber, organism, accessionNumber):
    	self.idNumber = idNumber
    	self.organism = organism
    	self.accessionNumber = accessionNumber
        
    def __str__(self):
    	return '(\'%s\',\'%s\',\'%s\')' % (self.idNumber, self.organism, self.accessionNumber)

    def accessAnnotations(self):
    	for record in SeqIO.parse(sys.argv[2],'gb'):
    		self.idNumber = record.id
    		self.organism = record.annotations['organism']
    		self.accessionNumber = record.annotations['accession']

    def makeRowDict(self):
    	return {'idNumber': self.idNumber, 'organism': self.organism, 'accessionNumber': self.accessionNumber}
        
    
def writeMetadataToCsv(sequenceMetadataList, csvFile):
    sequenceMetadataFieldnameList = ['idNumber', 'organism', 'accessionNumber']
    writer = csv.DictWriter(csvFile, fieldnames = sequenceMetadataFieldnameList, restval='no info available')
    writer.writeheader()
    for sequenceMetadata in sequenceMetadataList:
        print('loop is running')
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
	sequenceMetadata = SequenceMetadata(self.idNumber, self.organism, self.accessionNumber)
	sequenceMetadataList.append(sequenceMetadata)
	with open(sys.argv[1], 'w') as csvFile:
		writeMetadataToCsv(sequenceMetadataList, csvFile)
runWriteMetadataToCsv()