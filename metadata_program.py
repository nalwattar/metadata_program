import sys 
import Bio.SeqIO
import csv

class SequenceMetadata(object):

    #Initialiser

    def __init__(self, idNumber, organism, accessionNumber):
    	self.idNumber = idNumber
    	self.organism = organism
    	self.accessionNumber = accessionNumber
        
    def __str__(self):
    	return '(\'%s\',\'%s\',\'%s\')' % (self.idNumber, self.organism, self.accessionNumber)

    def parseGenbankFile(self):
    	with open(sys.argv[2], 'r') as genbankFile:
    	    seqIO.parse(genbankFile, 'genbank')
    	    return sequenceMetadata.idNumber, sequenceMetadata.organism, sequenceMetadata.accession
    
    def makeRowDict(self):
    	return {'idNumber': self.idNumber, 'organism': self.organism, 'accessionNumber': self.accessionNumber}
        
    
def writeMetadataToCsv(sequenceMetadataList, csvFile):
    sequenceMetadataFieldnameList = ['idNumber', 'organism', 'accessionNumber']
    writer = csv.DictWriter(csvFile, fieldnames = sequenceMetadataFieldnameList, restval='no info available')
    writer.writeheader()
    for sequenceMetadata in sequenceMetadataList:
        print('loop is running')
        writer.writerow(sequenceMetadata.makeRowDict())

        
sequenceMetadataList = []
sequenceMetadata = SequenceMetadata('1234', 'palm', '5678')
sequenceMetadataList.append(sequenceMetadata)

with open(sys.argv[1], 'w') as csvFile:
    writeMetadataToCsv(sequenceMetadataList, csvFile)
