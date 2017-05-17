#!/usr/bin/python

import os
import sys

ifile1 = open("Q8N6T7.final","r")
ifile2 = open("Q8N6T7.out.pfam","r")

seq = ifile2.readlines()
seq = [i.rstrip("\n") for i in seq]
qu= range(0,len(seq),2)
hi = range(1,len(seq),2)
pair = list(zip(qu,hi))

d = {}
for (i,j) in pair:
    que = seq[i]
    hit = seq[j]
    que = que.split()
    hit = hit.split()
    que_pre = que[0].find("|")
    que_suf = que[0].find("|",que_pre+1)
    que_pro = que[0][(que_pre+1):que_suf]
    que_pos = que[0].find("/")
    que_range = que[0][(que_pos+1):]

    hit_pre = hit[0].find("|")
    hit_suf = hit[0].find("|",hit_pre+1)
    hit_pro = hit[0][(hit_pre+1):hit_suf]
    hit_pos = hit[0].find("/")
    hit_range = hit[0][(hit_pos+1):]
    d[(que_pro,que_range,hit_pro,hit_range)] = (que[1],hit[1])


firstline = ifile1.readline()
for line in ifile1:
    line = line.rstrip("\n")
    l = line.split("\t")

    query_pre = l[0].find("|")
    query_suf = l[0].find("|",query_pre+1)
    query_pro = l[0][(query_pre+1):query_suf]
    hsp_query_range = l[18]+"-"+l[19]

    hit_pre = l[3].find("|")
    hit_suf = l[3].find("|",hit_pre+1)
    hit_pro = l[3][(hit_pre+1):hit_suf]
    hsp_hit_range = l[21]+"-"+l[22]

    hit_des = l[5].split(" ")
    first = hit_des[1].find(":")
    fi_re = hit_des[1][(first+1):]
    last = hit_des[3].find(":")
    la_re = hit_des[3][(last+1):]
    pdb_fir = str(int(fi_re)+int(l[21])-1)
    pdb_las = str(int(fi_re)+int(l[22])-1)
    pdb_id = hit_pro[:-1]
    pdb_chain = hit_pro[-1]

    if (query_pro,hsp_query_range,hit_pro,hsp_hit_range) in d:
        ofile = open(query_pro+"_"+hsp_query_range+"_"+hit_pro+"_"+pdb_fir+"-"+pdb_las+".ali","w")
        ofile.write(">P1;"+hit_pro+"\n")
        ofile.write("structure:"+pdb_id+":"+pdb_fir+":"+pdb_chain+":"+pdb_las+":"+pdb_chain+"\n")
        template = d[(query_pro,hsp_query_range,hit_pro,hsp_hit_range)][1]
        tem_len = len(template)
        tim = tem_len/75+1
        for i in range(1,tim+1):
            if i == tim:
                print >> ofile,template[:]+"*"
            else:
                print >> ofile,template[:75]
                template = template[75:]

            
        ofile.write(">P1;"+query_pro+"\n")
        ofile.write("sequence:"+query_pro+":"+l[18]+":"+" " +":"+l[19]+":"+" "+"\n")
        query_seq = d[(query_pro,hsp_query_range,hit_pro,hsp_hit_range)][0]
        que_len = len(query_seq)
        time = que_len/75+1
        for i in range(1,time+1):
            if i == time:
                print >> ofile,query_seq[:]+"*"
            else:
                print >> ofile,query_seq[:75]
                query_seq = query_seq[75:]

        ofile.close()


ifile1.close()
ifile2.close()


    
    





   

