def transcribe(codon):
  gen = ""
  for i in codon:
    if(i == 't'):
      gen += 'a'
    if(i == 'c'):
      gen += 'g'
    if(i == 'a'):
      gen += 'u'
    if(i == 'g'):
      gen += 'c'
  return gen

def translation(codon):
  gen = ""
  for cod in codon:
    if (cod == 'ttt' or cod == 'ttc'):
      gen += 'f'
    if(cod == 'tta' or cod == 'ttg' or cod == 'ctt' or cod == 'ctc' or cod == 'cta' or cod == 'ctg'):
      gen += 'l'
    if(cod == 'att' or cod == 'atc' or cod == 'ata'):
      gen += 'i'
    if(cod == 'atg'):
      gen += 'm'
    if(cod == 'gtt' or cod == 'gtc' or cod == 'gta' or cod == 'gtg'):
      gen += 'v'
    if(cod == 'tct' or cod == 'tcc' or cod == 'tca' or cod == 'tcg' or cod == 'agt' or cod == 'agc'):
      gen += 's'
    if(cod == 'cct' or cod == 'ccc' or cod == 'cca' or cod == 'ccg'):
      gen += 'p'
    if(cod == 'act' or cod == 'acc' or cod == 'aca' or cod == 'acg'):
      gen += 't'
    if(cod == 'gct' or cod == 'gcc' or cod == 'gca' or cod == 'gcg'):
      gen += 'a'
    if(cod == 'tat' or cod == 'tac'):
      gen += 'y'
    if(cod == 'cat' or cod == 'cac'):
      gen += 'h'
    if(cod == 'caa' or cod == 'cag'):
      gen += 'q'
    if(cod == 'aat' or cod == 'aac'):
      gen += 'n'
    if(cod == 'aaa' or cod == 'aag'):
      gen += 'k'
    if(cod == 'gat' or cod == 'gac'):
      gen += 'd'
    if(cod == 'gaa' or cod == 'gag'):
      gen += 'e'
    if(cod == 'tgt' or cod == 'tgc'):
      gen += 'c'
    if(cod == 'tgg'):
      gen += 'w'
    if(cod == 'cgt' or cod == 'cgc' or cod == 'cga' or cod == 'cgg' or cod == 'aga' or cod == 'agg'):
      gen += 'r'
    if(cod == 'ggt' or cod == 'ggc' or cod == 'gga' or cod == 'ggg'):
      gen += 'g'
    if (cod == 'uuu' or cod == 'uuc'):
      gen += 'f'
    if(cod == 'uua' or cod == 'uug' or cod == 'cuu' or cod == 'cuc' or cod == 'cua' or cod == 'cug'):
      gen += 'l'
    if(cod == 'auu' or cod == 'auc' or cod == 'aua'):
      gen += 'i'
    if(cod == 'aug'):
      gen += 'm'
    if(cod == 'guu' or cod == 'guc' or cod == 'gua' or cod == 'gug'):
      gen += 'v'
    if(cod == 'ucu' or cod == 'ucc' or cod == 'uca' or cod == 'ucg' or cod == 'agu' or cod == 'agc'):
      gen += 's'
    if(cod == 'ccu' or cod == 'ccc' or cod == 'cca' or cod == 'ccg'):
      gen += 'p'
    if(cod == 'acu' or cod == 'acc' or cod == 'aca' or cod == 'acg'):
      gen += 't'
    if(cod == 'gcu' or cod == 'gcc' or cod == 'gca' or cod == 'gcg'):
      gen += 'a'
    if(cod == 'uau' or cod == 'uac'):
      gen += 'y'
    if(cod == 'cau' or cod == 'cac'):
      gen += 'h'
    if(cod == 'caa' or cod == 'cag'):
      gen += 'q'
    if(cod == 'aau' or cod == 'aac'):
      gen += 'n'
    if(cod == 'aaa' or cod == 'aag'):
      gen += 'k'
    if(cod == 'gau' or cod == 'gac'):
      gen += 'd'
    if(cod == 'gaa' or cod == 'gag'):
      gen += 'e'
    if(cod == 'ugu' or cod == 'ugc'):
      gen += 'c'
    if(cod == 'ugg'):
      gen += 'w'
    if(cod == 'cgu' or cod == 'cgc' or cod == 'cga' or cod == 'cgg' or cod == 'aga' or cod == 'agg'):
      gen += 'r'
    if(cod == 'ggu' or cod == 'ggc' or cod == 'gga' or cod == 'ggg'):
      gen += 'g'
  return gen

g = ['atg','ggt','tat']
print(translation(g))