import zipfile
import re

def docx(f):
  docx =  zipfile.ZipFile(f)
  content = docx.read('word/document.xml').decode('utf-8')
  cleaned = re.sub('<(.|\n)*?>','',content)
  return cleaned