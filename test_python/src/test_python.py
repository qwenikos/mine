__author__ = "nikos"
__date__ = "$Dec 11, 2015 11:18:45 PM$"
def filter1(filename):
#    print filename
    goon=False
    genes_counter=0
    stranded_counter=0
    genes_tsl1_counter=0
    antistranded_counter=0
    unique_onlycount=0;
    rec_count=0;
    ndict={}
    ndict_dup={}
    f = open(filename, 'r')
    first_line=f.readline()
    
#    print first_line
#    return
    for line in f:
        goon=True
        rec_count+=1;
        col1,col2,col3,col4,col5,col6,col7,col8=line.rstrip().split(",")
        gene_id=col1 
        trans_id=col2
        chrom=col3
        gene_start=col4
        gene_end=col5
        strand=col6
        tss=col7
        tsl=col8
        genes_counter+=1;
        if tsl=='tsl1' and goon:
            genes_tsl1_counter+=1;
            goon=True
        else:
            goon=False
        if strand=='-1' and goon:
                if tss==gene_end:
                    stranded_counter+=1
                    goon=True
                else:
                    goon=False
        if strand=='1' and goon:
            if tss==gene_start:
                antistranded_counter+=1
                goon=True
            else:
                goon=False
                
        if gene_id in ndict_dup and goon:  #for removing over dublicates TSS
            ndict_dup[gene_id]+=1
            goon=False
        elif gene_id in ndict:
            ndict_dup[gene_id]=1
            del ndict[gene_id]
            unique_onlycount-=1
            goon=False
        if goon:
            ndict[gene_id]=[trans_id,chrom,gene_start,gene_end,strand,tss,tsl]
            unique_onlycount+=1
    
#    print '------------'
    print_data=False
    if print_data:
        print first_line.rstrip()
        for keys in ndict:
            print keys+','+ndict[keys][0]+','+ndict[keys][1]+','+ndict[keys][2]+','+ndict[keys][3]+','+ndict[keys][4]+','+ndict[keys][5]+','+ndict[keys][6]
   
    statistics=True
    if statistics:
        print 'filename= '+filename
        print 'total genes in ensemble export= '+str(genes_counter )        
        print 'genes after tsl1 filter= '+str(genes_tsl1_counter)
        print 'stranded with same start= '+str(stranded_counter)
        print 'anti stranded  with same start= '+str(antistranded_counter)
        print 'total  with same start= '+str(antistranded_counter+stranded_counter)
        print 'total  after duplicates removed= '+str(unique_onlycount)
        unique_onlycount
        
    return ndict
#main program
linc_file_name='/home/nikos/biothesis/data/ensemble_linc_genes.csv'
protein_coding_file_name='/home/nikos/biothesis/data/ensemble_protein_coding_gene.csv'
linc_test='/home/nikos/biothesis/data/linc_test.csv'
filename=linc_file_name
filtered_dict=filter1(filename)
filtered_dict_tuple={}
print filtered_dict['ENSMUSG00000095110']
for keys in filtered_dict:
    filtered_dict_tuple[keys]=tuple(filtered_dict[keys])
import operator
sorted_x = sorted(filtered_dict_tuple.items(), key=operator.itemgetter(4))   
print sorted_x

 
        
    
    
    
    
  