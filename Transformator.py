from itertools import islice

class Matrices:
  def __init__(self,df):
    self.df = df

  def mean(df):
    values = []
    for i in range(0,len(df)):
      values.append(df[i])
    return sum(values)/len(values)

  def Slice2d(listA, len_2d):
   res = iter(listA)
   return [list(islice(res,i)) for i in len_2d]

  def meanArray(self,n_sample):
    sizeArr = [n_sample,n_sample]
    mean_arr = []
    for i in range(0,len(self.df)):
      cc = []
      for j in self.df[i]:
        cc.append(self.df[i][j])
      mean_arr.append(Matrices.mean(cc))
    return Matrices.Slice2d(mean_arr,sizeArr)

  def mean_to_dict(self):
    mean_arr = []
    for i in range(0,len(self.df)):
      cc = []
      for j in self.df[i]:
        cc.append(self.df[i][j])
      mean_arr.append(Matrices.mean(cc))
      self.df[i]["mean"] = Matrices.mean(cc)
    return "finnish"