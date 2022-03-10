import csv
from tabulate import tabulate as tb
import json
import os
from difflib import SequenceMatcher as SM

class Sequence:
    
    def __init__(self,gen,type):
        self.gen = gen
        self.type = type
    

    def print_type(self):
        return self.type    	

    def bagitiga(text):
    	return [text[i:i+3] for i in range(0,len(text),3)]
    	
    def bagitigaaja(self): #bagitiga tanpa meminta input
    	return [self.gen[i:i+3] for i in range(0,len(self.gen),3)]
    		
    def dna_to_code(cod):
    	phe = cod.count('ttt')+cod.count('ttc')#1
    	leu = cod.count('tta')+cod.count('ttg')+cod.count('ctt')+cod.count('ctc')+cod.count('cta')+cod.count('ctg')#2
    	ile = cod.count('att')+cod.count('atc')+cod.count('ata')#3
    	met = cod.count('atg')#4
    	val = cod.count('gtt')+cod.count('gtc')+cod.count('gta')+cod.count('gtg')#5
    	ser = cod.count('tct')+cod.count('tcc')+cod.count('tca')+cod.count('tcg')+cod.count('agt')+cod.count('agc')#6
    	pro = cod.count('cct')+cod.count('ccc')+cod.count('cca')+cod.count('ccg')#7
    	thr = cod.count('act')+cod.count('acc')+cod.count('aca')+cod.count('acg')#8
    	ala = cod.count('gct')+cod.count('gcc')+cod.count('gca')+cod.count('gcg')#9
    	tyr = cod.count('tat')+cod.count('tac')#10
    	his = cod.count('cat')+cod.count('cac')#11
    	gln = cod.count('caa')+cod.count('cag')#12
    	asn = cod.count('aat')+cod.count('aac')#13
    	lys = cod.count('aaa')+cod.count('aag')#14
    	asp = cod.count('gat')+cod.count('gac')#15
    	glu = cod.count('gaa')+cod.count('gag')#16
    	cys = cod.count('tgt')+cod.count('tgc')#17
    	trp = cod.count('tgg')#18
    	arg = cod.count('cgt')+cod.count('cgc')+cod.count('cga')+cod.count('cgg')+cod.count('aga')+cod.count('agg')#19
    	gly = cod.count('ggt')+cod.count('ggc')+cod.count('gga')+cod.count('ggg')#20
    
    	dna = {"Phe":(phe/len(cod))*100,"Leu":(leu/len(cod))*100,"Ile":( ile/len(cod))*100,"Met":(met/len(cod))*100,"Val" :( val/len(cod))*100,"Ser":( ser/len(cod))*100,"Pro":(pro/len(cod))*100,"Thr":(thr/len(cod))*100,"Ala":(ala/len(cod))*100,"Tyr":(tyr/len(cod))*100,"His":(his/len(cod))*100,"Gln":(gln/len(cod))*100,"Asn":(asn/len(cod))*100,"Lys":(lys/len(cod))*100,"Asp":(asp/len(cod))*100,"Glu":(glu/len(cod))*100,"Cys":(cys/len(cod))*100,"Trp":(trp/len(cod))*100,"Arg":(arg/len(cod))*100,"Gly":(gly/len(cod))*100,"Length":len(cod),"description":""}
    	self.seqtype = "dna"
    	return dna
    
    def rna_to_code(cod):
    	
    	phe = cod.count('uuu')+cod.count('uuc')#1
    	leu = cod.count('uua')+cod.count('uug')+cod.count('cuu')+cod.count('cuc')+cod.count('cua')+cod.count('cug')#2
    	ile = cod.count('auu')+cod.count('auc')+cod.count('aua')#3
    	met = cod.count('aug')#4
    	val = cod.count('guu')+cod.count('guc')+cod.count('gua')+cod.count('gug')#5
    	ser = cod.count('ucu')+cod.count('ucc')+cod.count('uca')+cod.count('ucg')+cod.count('agu')+cod.count('agc')#6
    	pro = cod.count('ccu')+cod.count('ccc')+cod.count('cca')+cod.count('ccg')#7
    	thr = cod.count('acu')+cod.count('acc')+cod.count('aca')+cod.count('acg')#8
    	ala = cod.count('gcu')+cod.count('gcc')+cod.count('gca')+cod.count('gcg')#9
    	tyr = cod.count('uau')+cod.count('uac')#10
    	his = cod.count('cau')+cod.count('cac')#11
    	gln = cod.count('caa')+cod.count('cag')#12
    	asn = cod.count('aau')+cod.count('aac')#13
    	lys = cod.count('aaa')+cod.count('aag')#14
    	asp = cod.count('gau')+cod.count('gac')#15
    	glu = cod.count('gaa')+cod.count('gag')#16
    	cys = cod.count('ugu')+cod.count('ugc')#17
    	trp = cod.count('ugg')#18
    	arg = cod.count('cgu')+cod.count('cgc')+cod.count('cga')+cod.count('cgg')+cod.count('aga')+cod.count('agg')#19
    	gly = cod.count('ggu')+cod.count('ggc')+cod.count('gga')+cod.count('ggg')#20
    	
    	rna = {"Phe":(phe/len(cod))*100,"Leu":(leu/len(cod))*100,"Ile":( ile/len(cod))*100,"Met":(met/len(cod))*100,"Val" :( val/len(cod))*100,"Ser":( ser/len(cod))*100,"Pro":(pro/len(cod))*100,"Thr":(thr/len(cod))*100,"Ala":(ala/len(cod))*100,"Tyr":(tyr/len(cod))*100,"His":(his/len(cod))*100,"Gln":(gln/len(cod))*100,"Asn":(asn/len(cod))*100,"Lys":(lys/len(cod))*100,"Asp":(asp/len(cod))*100,"Glu":(glu/len(cod))*100,"Cys":(cys/len(cod))*100,"Trp":(trp/len(cod))*100,"Arg":(arg/len(cod))*100,"Gly":(gly/len(cod))*100,"Length":len(cod),"description":""}
    	self.seqtype = "rna"
    	return rna
    
    def decomp_amino_acid(self):
    	gen = Sequence.bagitiga(self.gen.lower())	
    	if(self.type == "rna"):
                
    		return Sequence.rna_to_code(gen)
    	else:
                
    		return Sequence.dna_to_code(gen)
    
    def bagilagi(text):
    	txt = []
    	for i in range(0,3):
    		txt.append(text[i])
    	return txt
    def codon2(text):
    	cc = []
    	#teks = ""
    	#if(len(text) % 3 != 0):
    		#pan = len(text)-(len(text)%3)
    		#teks = text[:pan]
    	ll = Sequence.bagitiga(text)
    	for i in ll:
    		hh = Sequence.bagilagi(i)
    		cc.append(hh)
    	return cc
    def codon3(text):
    	cc = []
    	teks = ""
    	if(len(text) % 3 != 0):
    		pan = len(text)-(len(text)%3)
    		teks = text[:pan]
    	ll = Sequence.bagitiga(teks)
    	for i in ll:
    		hh = Sequence.bagilagi(i)
    		cc.append(hh)
    	return cc
    def dna_extract_nucleutide(codon):
    	cod = codon.lower()
    	bb2 = Sequence.bagitiga(cod)
    	bb3 = Sequence.codon2(bb2)
    	a1,t1,g1,c1,a2,t2,g2,c2,a3,t3,g3,c3 = 0,0,0,0,0,0,0,0,0,0,0,0
    	for i in range(0,len(bb3)):
    		a1 += bb3[i][0].count("a")
    		t1 += bb3[i][0].count("t")
    		g1 += bb3[i][0].count("g")
    		c1 += bb3[i][0].count("c")
    		a2 += bb3[i][1].count("a")
    		t2 += bb3[i][1].count("t")
    		g2 += bb3[i][1].count("g")
    		c2 += bb3[i][1].count("c")
    		a3 += bb3[i][2].count("a")
    		t3 += bb3[i][2].count("t")
    		g3 += bb3[i][2].count("g")
    		c3 += bb3[i][2].count("c")
    	result = {"a1" : (a1/len(cod))*100,"t1" : (t1/len(cod))*100,"g1" : (g1/len(cod))*100,"c1" : (c1/len(cod))*100,"a2" : (a2/len(cod))*100,"t2" : (t2/len(cod))*100,"g2" : (g2/len(cod))*100,"c2" : (c2/len(cod))*100,"a3" : (a3/len(cod))*100,"t3" : (t3/len(cod))*100,"g3" : (g3/len(cod))*100,"c3" : (c3/len(cod))*100,"description":""}
        
    	return result
    def rna_extract_nucleutide(codon):
    	cod = codon.lower()
    	bb2 = Sequence.bagitiga(cod)
    	bb3 = Sequence.codon3(cod)
    	a1,u1,g1,c1,a2,u2,g2,c2,a3,u3,g3,c3 = 0,0,0,0,0,0,0,0,0,0,0,0
    	for i in range(0,len(bb3)):
    		a1 += bb3[i][0].count("a")
    		u1 += bb3[i][0].count("u")
    		g1 += bb3[i][0].count("g")
    		c1 += bb3[i][0].count("c")
    		a2 += bb3[i][1].count("a")
    		u2 += bb3[i][1].count("u")
    		g2 += bb3[i][1].count("g")
    		c2 += bb3[i][1].count("c")
    		a3 += bb3[i][2].count("a")
    		u3 += bb3[i][2].count("u")
    		g3 += bb3[i][2].count("g")
    		c3 += bb3[i][2].count("c")
    	result = {"a1" : (a1/len(cod))*100,"u1" : (u1/len(cod))*100,"g1" : (g1/len(cod))*100,"c1" : (c1/len(cod))*100,"a2" : (a2/len(cod))*100,"u2" : (u2/len(cod))*100,"g2" : (g2/len(cod))*100,"c2" : (c2/len(cod))*100,"a3" : (a3/len(cod))*100,"u3" : (u3/len(cod))*100,"g3" : (g3/len(cod))*100,"c3" : (c3/len(cod))*100,"description":""}
                
    	return result
    	
    def decomp_nucleutide(self):
    	gen = self.gen.lower()
    	if(self.type == "rna"):
                
    		return Sequence.rna_extract_nucleutide(gen)
    	else:
                
    		return Sequence.dna_extract_nucleutide(gen)


    def protein_extract(self):
        gen = self.gen.lower()
        cod = [gen[i:i+1] for i in range(0,len(gen),1)]
        if(self.type == "protein"):
            for j in range(0,len(cod)):
                phe = cod.count('f')
                leu = cod.count('l')
                ile = cod.count('i')
                met = cod.count('m')
                val = cod.count('v')
                ser = cod.count('s')
                pro = cod.count('p')
                thr = cod.count('t')
                ala = cod.count('a')
                tyr = cod.count('y')
                his = cod.count('h')
                gln = cod.count('q')
                asn = cod.count('n')
                lys = cod.count('k')
                asp = cod.count('d')
                glu = cod.count('e')
                cys = cod.count('c')
                trp = cod.count('w')
                arg = cod.count('r')
                gly = cod.count('g')
    	
            protein = {"Phe":(phe/len(cod))*100,"Leu":(leu/len(cod))*100,"Ile":( ile/len(cod))*100,"Met":(met/len(cod))*100,"Val" :( val/len(cod))*100,"Ser":( ser/len(cod))*100,"Pro":(pro/len(cod))*100,"Thr":(thr/len(cod))*100,"Ala":(ala/len(cod))*100,"Tyr":(tyr/len(cod))*100,"His":(his/len(cod))*100,"Gln":(gln/len(cod))*100,"Asn":(asn/len(cod))*100,"Lys":(lys/len(cod))*100,"Asp":(asp/len(cod))*100,"Glu":(glu/len(cod))*100,"Cys":(cys/len(cod))*100,"Trp":(trp/len(cod))*100,"Arg":(arg/len(cod))*100,"Gly":(gly/len(cod))*100,"Length":len(cod),"description":""}
            
            return protein
        else:
            return "this function only for protein data"

    def gen_to_csv(pp,namefile,seqtype):
         csv_columns1 = ["Phe","Leu","Ile","Met","Val","Ser","Pro","Thr","Ala","Tyr","His","Gln","Asn","Lys","Asp","Glu","Cys","Trp","Arg","Gly","Length","description"]
         csv_columns2 = ["a1","t1","g1","c1","a2","t2","g2","c2","a3","t3","g3","c3","description"]
         csv_columns3 = ["a1","u1","g1","c1","a2","u2","g2","c2","a3","u3","g3","c3","description"]

         if(seqtype == "atgc"):
             csv_columns = csv_columns2
         elif(seqtype == "augc"):
             csv_columns = csv_columns3
         else:
             csv_columns = csv_columns1

         csv_file = str(namefile).strip()+'.csv'.strip()
         try:
            with open(csv_file, 'w') as csvfile:
              writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
              writer.writeheader()
              for data in pp:
                writer.writerow(data)
            return "Success export to csv"
         except IOError:
            return "I/O error"

class File:
    def __init__(self,file_,type_,data_):
        self.file_ = file_
        self.type_ = type_
        self.data_ = data_
        self.desc = []
        self.Gen = []
        self.result = []
        self.typeresult = [0]

        if(self.type_ == "fasta"):
            x = open(self.file_,'r')

            aa = x.readlines()
            a = []
            for k in aa:
                a.append(k.lower().replace("\n",""))
            gen = []
            x.close()
            a[len(a)-1] = ">"
            for i in a:
                if(i.count(">") > 0):
                    self.desc.append(i)
                    a.remove(i)
                    sen = ""
                    for word in gen:
                        sen += str(word)
                    self.Gen.append(sen)
                    del gen[0:len(gen)]
                else:
                    gen.append(i)
            self.Gen.remove("")
            self.desc.remove(">")
        

    def _desc(self):
        return self.desc

    def _gen(self):
        return self.Gen

    def extract_to_nucl(self):
        #result = []
        if(self.data_ == "dna"):
            self.typeresult[0] = "atgc"
            for ii in self.Gen:
                Genom = Sequence(ii.lower(),"dna")
                genom_result = Genom.decomp_nucleutide()
                self.result.append(genom_result)
                locat = self.Gen.index(ii);self.result[locat]['description'] = self.desc[locat]
            
        elif(self.data_ == "rna"):
            self.typeresult[0] = "augc"
            for ii in self.Gen:
                Genom = Sequence(ii.lower(),"rna")
                genom_result = Genom.decomp_nucleutide()
                self.result.append(genom_result)
                locat = self.Gen.index(ii);self.result[locat]['description'] = self.desc[locat]
            
        else:
            return "Type Incorrect"
        
        return self.result

    def extract_to_amino(self):
        #result = []
        if(self.data_ == "dna" or self.data_ == "rna"):
            for ii in self.Gen:
                Genom = Sequence(ii,self.data_)
                genom_result = Genom.decomp_amino_acid()
                self.result.append(genom_result)
                locat = self.Gen.index(ii);self.result[locat]['description'] = self.desc[locat]
            self.typeresult = "amino"
        elif(self.data_ == "protein"):
            for ii in self.Gen:
                Genom = Sequence(ii,self.data_)
                genom_result = Genom.protein_extract()
                self.result.append(genom_result)
                locat = self.Gen.index(ii);self.result[locat]['description'] = self.desc[locat]
            self.typeresult = "amino"
        else:
            return "Type Incorrect"
            
        return self.result

    def exportCsv(self,name):
        hh = Sequence.gen_to_csv(self.result,name,self.typeresult[0])
        if(hh == "Success export to csv"):
            return "Success export"+str(self.typeresult[0])+" to csv"

    def show(self):
        return tb(self.result, headers='keys', tablefmt='fancy_grid')

    def exportJson(self,name):
        namefile = str(name).strip()+'.json'.strip()
        with open(namefile, "w") as outfile:
            json.dump(self.result, outfile)
        return "Exporting to JSON Finnish"

    def mergeFiles(nameFile,typeFiles):
        command = "cat *."+typeFiles+" > " + nameFile +"."+typeFiles
        os.system(command)
        return "Merge Files Finish"

    def splitFiles(self,nameFiles,typeFile):
        for i in range(0,len(self.Gen)):
        	teks = self.desc[i]+"\n"+self.Gen[i]+"\n"
        	name = nameFiles+"_"+str(i)+"."+typeFile
        	files_op = open(name,"w")
        	files_op.write(teks)
        	files_op.close()
        	print(name+" export finished")
        return "All Split Files Finished"

    def similarityRatio(gen):
    	Genes = [None]
    	for i in gen:
    		Genes.append(i)
    	similar = SM(Genes).ratio()
    	return similar
class About:

    def __version__():
        return "Version\t: 0.0.01(Alpha Version)"

    def __about__():
        return "Bioinformatics Project\n\nBy : Heru Triana\n"

    def __logo__():
        print("  ___            _    _              ___       ")
        print(" | _ \ _ _  ___ | |_ (_) _ _   __ _ | _ \ _  _ ")
        print(" |  _/| '_|/ _ \|  _|| || ' \ / _` ||  _/| || |")
        print(" |_|  |_|  \___/ \__||_||_||_|\__,_||_|   \_, |")
        print("                                          |__/ ")
    def __all__():
        About.__logo__()
        print(About.__about__())
        print(About.__version__())







