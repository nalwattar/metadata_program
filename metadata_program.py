import sys 
import Bio.SeqIO
import csv
import subprocess

class SequenceMetadata(object):

    #Initialiser

    def __init__(self, idNumber, organism, accessionNumber):
    	self.idNumber = idNumber
    	self.organism = organism
    	self.accessionNumber = accessionNumber
        
    def __str__(self):
    	return '(\'%s\',\'%s\',\'%s\')' % (self.idNumber, self.organism, self.accessionNumber)

    def makeRowDict(self):
    	return {'idNumber': self.idNumber, 'organism': self.organism, 'accessionNumber': self.accessionNumber}
        
    
def readMetadata(gbFnameList):
    sequenceMetadataList = []
    for gbFname in gbFnameList:
        record = Bio.SeqIO.read(gbFname, 'genbank')
        sequenceMetadata = SequenceMetadata(record.id, record.annotations['organism'], record.annotations['accessions'][0])
        sequenceMetadataList.append(sequenceMetadata)
    return sequenceMetadataList

def test_readMetadata():
    test = readMetadata(sys.argv[2:])
    print(test)
    
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
	sequenceMetadata = SequenceMetadata()
	sequenceMetadataList.append(sequenceMetadata)
	with open(sys.argv[1], 'w') as csvFile:
		writeMetadataToCsv(sequenceMetadataList, csvFile)

test_readMetadata()
sys.exit(1)
