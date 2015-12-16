__author__ = "nikos"
__date__ = "$Dec 11, 2015 11:18:45 PM$"
import csv;
from collections import defaultdict, Counter
def test1():
 
    tuple1=(1,(2,3))
    tuple2=(1,(2,4))
    tuple3=(2,(4,6))
    tuple4=(1,(2,3))
    nlist=[tuple1,tuple2,tuple3,tuple4]

    print nlist[1][1]

    
#    if __name__ == "__main__":
#        i=10
#    dd="nikos";
#    if (i==10) :
#        print dd;
#    days=[1,2,3,4]
 
#    matrix=[[1,2,4],days]
#    females=set([1,2,3,4,4])
#    males=set([1,4,6,6,7,8])
#    print females &males  #set([1, 4])
#    print females  #set([1, 2, 3, 4])
#    ageDict={'homer':36,'marge':34,'lisa':8,'bart':10,12:2}
#    print(ageDict['lisa']) #8
#    print(ageDict[12]) #8
#    x='22'
#    y='78'
#    print(x+y)
    return


def filter1():
    linc_file_name='/home/nikos/biothesis/data/ensemble_linc_genes.csv'
    protein_coding_file_name='/home/nikos/biothesis/data/ensemble_protein_coding_gene.csv'
    with open (linc_file_name,'rb') as csvfile:
        filereader=csv.reader(csvfile,delimiter=',')
    #        row[0]=Ensembl Gene ID
    #        row[1]=Ensembl Transcript ID
    #        row[2]=Chromosome Name
    #        row[3]=Gene Start (bp)
    #        row[4] =Gene End (bp)
    #        row[5]=Strand
    #        row[6]=Transcription Start Site (TSS)
    #        row[7]=Transcript Support Level (TSL)

        genes_counter=0
        stranded_counter=0
        genes_tsl1_counter=0
        antistranded_counter=0
        for row in filereader:
            genes_counter+=1;
            if row[7]=='tsl1':
                genes_tsl1_counter+=1;
                if row[5]=='-1':
                    if row[6]==row[4]:
                           # print  row
                        stranded_counter+=1
                elif row[5]=='1':
                    if row[6]==row[3]:
                           # print row
                            antistranded_counter+=1

        print 'total genes in ensemble export= '+str(genes_counter )        
        print 'genes after tsl1 filter= '+str(genes_tsl1_counter)
        print 'stranded with same start= '+str(stranded_counter)
        print 'antistranded  with same start= '+str(antistranded_counter)
        print 'total  with same start= '+str(antistranded_counter+stranded_counter)
        return
def filter2():
    unique_onlycount=0;
    rec_count=0;
    linc_file_name='/home/nikos/biothesis/data/ensemble_linc_genes.csv'
    protein_coding_file_name='/home/nikos/biothesis/data/ensemble_protein_coding_gene.csv'
    map_genes = defaultdict(Counter)#a dict of counters to count 
                                                                                         #the repetitions by group
    f = open(linc_file_name, 'r')
    for line in f:
#        print line
        rec_count+=1;
        gene_id,trans_id,chrom,gene_start,gent_end,strand,tss,tsl = line.split(",")   
        #build the map (dict) indexed by the groups i.e. a key is  gene_id
        map_genes[(gene_id)][(trans_id,chrom,gene_start,gent_end,strand,tss,tsl)] += 1

    for (gene_id), counter in map_genes.items():
        if(len(counter)==1):
            unique_onlycount+=1;
            print gene_id
            trans_id,chrom,gene_start,gent_end,strand,tss,tsl = list(counter.keys())[0]
        # print all the repetitions
        for _ in range(counter[(gene_id)]):
            print(gene_id,trans_id,chrom,gene_start,gent_end,strand,tss,tsl)
            
    print unique_onlycount
    print rec_count
    return
def filter3():
    unique_onlycount=0;
    rec_count=0;
    nlist=[]
    linc_file_name='/home/nikos/biothesis/data/ensemble_linc_genes.csv'
    protein_coding_file_name='/home/nikos/biothesis/data/ensemble_protein_coding_gene.csv'
    map_genes = defaultdict(Counter)#a dict of counters to count 
                                                                                         #the repetitions by group
    f = open(linc_file_name, 'r')
    for line in f:
#        print line
        rec_count+=1;
        gene_id,trans_id,chrom,gene_start,gent_end,strand,tss,tsl = line.split(",")
        map_genes[(gene_id)][(trans_id,chrom,gene_start,gent_end,strand,tss,tsl)] +=1
        
        nlist.append([(gene_id),(trans_id,chrom,gene_start,gent_end,strand,tss,tsl)])
    
    for (gene_id), counter in map_genes.items():
        if(len(counter)==1):
            unique_onlycount+=1;
#            print gene_id
            trans_id,chrom,gene_start,gent_end,strand,tss,tsl = list(counter.keys())[0]
        # print all the repetitions
#            print(gene_id,trans_id,chrom,gene_start,gent_end,strand,tss,tsl)
    print nlist[2]
    print unique_onlycount
    print rec_count
    return
#test1()
#filter1()
#filter2()
filter3()
 
        
    
    
    
    
  