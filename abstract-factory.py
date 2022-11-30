class Python():   
   def Type(self):   
      return "Dasar-dasar Bahasa Pemrograman Python"  
  
   def __str__(self):   
      return "Python"  
  
  
class Java():     
   def Type(self):   
      return "Bahasa Pemrograman Java Dasar"  
  
   def __str__(self):   
      return "Java"  
  
  
class R():     
   def Type(self):   
      return "Kelas Bahasa Pemrograman R"  
  
   def __str__(self):   
      return "R"  
  
  
# main method   
if __name__ == "__main__":   
   p = Python() # object for Python   
   j = Java() # object for java   
   r = R() # object for R  
  
   print(f'Nama Kursus: {r} dan tipenya: {r.Type()}')   
   print(f'Nama Kursus: {j} dan tipenya: {j.Type()}')   
   print(f'Nama Kursus: {p} dan tipenya: {p.Type()}')   