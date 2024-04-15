import os

class HuffmanCoding:
    def init(self,path):
                self.path=path
                self.heap=[]
                self.codes={}

class HeapNode:
    def init():
        self.char=char
        self.Freq=Freq

        


    def FreqencyDict(text):
                ####
     Freqency=
               
     def MakeHeap(self,Freqency):
                ######
               
        
      def MergeCodes(self):
                 

         def MakeCodes(self):
                 

          def GetEncodedText(self,text):
                         

           def PaddEncodedText(self,encoded_text):
                              
                def GetByteArray(self,padding_encoded_text):
                                   

                  









                     def compress(self):
                        filename,file_extension= os.path.splitext(self.text)
                        output_path=filename+".bin"

                        with open(self.path, 'r')as file, open(output_path,'wb') as output:
                            text=file.read()
                            text=text.rstrip()

                            Freqency=FreqencyDict(text)

                            self.MakeHeap(Freqency)
                            self.MergeCodes()
                            self.MakeCodes()

                            encoded_text=EncodedText(text)
                            padding_encoded_text=PaddEncodedText(encoded_text)

                            b=self.GetByteArray(padding_encoded_text)
                            output.write(bytes(b))
                        print("Compression done successfulyy")
                        return output_path
                             
        
                
