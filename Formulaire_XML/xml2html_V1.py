# -*- coding: utf8 -*-

from pylab import *

# Bibliothèques minidom : lecture du XML
from xml.dom.minidom import *

# Bibiliothèques Pigments : coloration synthaxique des codes
from pygments import highlight
from pygments.lexers import PythonLexer,CLexer,ScilabLexer
from pygments.formatters import HtmlFormatter

#Pour convertir les formules latex en svg :
#import os
#os.system("~/bin/latex2svg '$a^c$' eq1.svg")

# debug
import pdb

def unescape(s):
     # Fonction permettant de traduire le code html (comme &amp;)
     # en vrai caractères pour les programmes
     s = s.replace("&lt;", "<")
     s = s.replace("&gt;", ">")
     s = s.replace("&amp;", "&")
     s = s.replace("&quot;", "\"")
     return s
   
#=================
# Fonctions de traitement de chaque case du tableau

def traite_python(noeud_python,fic):
      global No_exemple
      module=""
      for noeud_module in noeud_python.getElementsByTagName("module"):
	module=noeud_module.toxml(encoding='utf-8')[8:-9]
      fic.write("<td title=\"{}\">\n".format(module))
      #fic.write("</tt>")
      for lien in noeud_python.getElementsByTagName("lien"):
	fic.write("<a href=\"{}\"><img style=\"border:0; float:right;\" src=\"{}\" alt=\"?\"></a>".format(lien.toxml(encoding='utf-8')[6:-7],"style/FAQ-icon.png"))
      # Chaque exemple fait l'objet d'un icone et d'un fichier html dans le dossier exemples
      for exemple in noeud_python.getElementsByTagName("exemple"):
	No_exemple+=1
	fic.write("<a href=\"{}\"><img style=\"border:0; float:right;\" src=\"{}\" alt=\"?\"></a>".format("exemples/ex{:d}.html".format(No_exemple),"style/Add-icon.png"))
	traite_exemple(exemple,"exemples/ex{:d}.html".format(No_exemple),"python")
      code=noeud_python.getElementsByTagName("code_python")[0].toxml(encoding='utf-8')[13:-14]
      code=unescape(code)
      fic.write(highlight(code, PythonLexer(encoding='utf-8'), HtmlFormatter(encoding='utf-8')))
      fic.write("</td>\n")


def traite_scilab(noeud_scilab,fic):
      global No_exemple
      module=""
      for noeud_module in noeud_scilab.getElementsByTagName("module"):
	module=noeud_module.toxml(encoding='utf-8')[8:-9]
      fic.write("<td title=\"{}\">\n".format(module))
      #fic.write("</tt>")
      for lien in noeud_scilab.getElementsByTagName("lien"):
	fic.write("<a href=\"{}\"><img style=\"border:0; float:right;\" src=\"{}\" alt=\"?\"></a>".format(lien.toxml(encoding='utf-8')[6:-7],"style/FAQ-icon.png"))
      # Chaque exemple fait l'objet d'un icone et d'un fichier html dans le dossier exemples
      for exemple in noeud_scilab.getElementsByTagName("exemple"):
	No_exemple+=1
	fic.write("<a href=\"{}\"><img style=\"border:0; float:right;\" src=\"{}\" alt=\"?\"></a>".format("exemples/ex{:d}.html".format(No_exemple),"style/Add-icon.png"))
	traite_exemple(exemple,"exemples/ex{:d}.html".format(No_exemple),"scilab")
      code=noeud_scilab.getElementsByTagName("code_scilab")[0].toxml(encoding='utf-8')[13:-14]
      code=unescape(code)
      fic.write(highlight(code, ScilabLexer(encoding='utf-8'), HtmlFormatter(encoding='utf-8')))
      fic.write("</td>\n")


def traite_C(noeud_C,fic):
      global No_exemple
      module=""
      for noeud_module in noeud_C.getElementsByTagName("module"):
	module=noeud_module.toxml(encoding='utf-8')[8:-9]
      fic.write("<td title=\"{}\">\n".format(module))
      #fic.write("</tt>")
      for lien in noeud_C.getElementsByTagName("lien"):
	fic.write("<a href=\"{}\"><img style=\"border:0; float:right;\" src=\"{}\" alt=\"?\"></a>".format(lien.toxml(encoding='utf-8')[6:-7],"style/FAQ-icon.png"))
      # Chaque exemple fait l'objet d'un icone et d'un fichier html dans le dossier exemples
      for exemple in noeud_C.getElementsByTagName("exemple"):
	No_exemple+=1
	fic.write("<a href=\"{}\"><img style=\"border:0; float:right;\" src=\"{}\" alt=\"?\"></a>".format("exemples/ex{:d}.html".format(No_exemple),"style/Add-icon.png"))
	traite_exemple(exemple,"exemples/ex{:d}.html".format(No_exemple),"C")
      code=noeud_C.getElementsByTagName("code_C")[0].toxml(encoding='utf-8')[8:-9]
      code=unescape(code)
      fic.write(highlight(code, CLexer(encoding='utf-8'), HtmlFormatter(encoding='utf-8')))
      fic.write("</td>\n")

#=================
# Fonction de traitement des fichiers exemples

def traite_exemple(noeud_exemple,nom_fichier,code):
  fic_exemple=open(nom_fichier,"w")
  fic2=open("style/head_exemple.html","r") # On lit le <head> du dossier style
  head=fic2.readlines()
  fic2.close()
  fic_exemple.writelines(head)
  for node in noeud_exemple.childNodes:
    #print node.nodeName
    #pdb.set_trace()
    if all(array(node.nodeName)!=array(["code_python","code_scilab","code_C"])): # Si le noeud n'est pas un code
      #print node.toxml(encoding='utf-8')
      #print node.nodeName
      fic_exemple.write(node.toxml(encoding='utf-8'))  # on recopie le noeud à l'identique
    else:            # Si le noeud est un code, coloration syntaxique
      if (node.nodeName=="code_python"):
        #pdb.set_trace()
        code=node.toxml(encoding='utf-8')[13:-14]
        code=unescape(code)
        fic_exemple.write(highlight(code, PythonLexer(encoding='utf-8'), HtmlFormatter(encoding='utf-8')))
      if (node.nodeName=="code_scilab"):
        #pdb.set_trace()
        code=node.toxml(encoding='utf-8')[13:-14]
        code=unescape(code)
        fic_exemple.write(highlight(code, ScilabLexer(encoding='utf-8'), HtmlFormatter(encoding='utf-8')))
      if (node.nodeName=="code_C"):
        #pdb.set_trace()
        code=node.toxml(encoding='utf-8')[8:-9]
        code=unescape(code)
        fic_exemple.write(highlight(code, CLexer(encoding='utf-8'), HtmlFormatter(encoding='utf-8')))
  #fic_exemple.write(noeud_exemple.toxml(encoding='utf-8')[9:-10])
  fic_exemple.close()



#======================================================
#  Début de programme
#======================================================


fic=open("style/head.html","r") # On lit le <head> du dossier style
head=fic.readlines()
fic.close()

dom1 = parse('formulaire.xml')  # Lecture du fichier xml

fic=open("formulaire.html","w") # On ouvre le fichier html à écrire
fic.writelines(head)            # On recopie le <head> du dossier style

No_exemple=0  # Compteur d'exemples pour numéroter les fichiers html

body=dom1.getElementsByTagName("body")

# Lecture des noeuds les uns après les autres.
# Les noeuds sont recopiés (texte et titres), sauf s'il s'agit d'un tableau, auquel cas il y a une mise en forme spéciale.
for node in body[0].childNodes:
  #print node.nodeName
  if node.nodeName!="tableau": # Si le noeud n'est pas un tableau
    #print node.toxml(encoding='utf-8')
    fic.write(node.toxml(encoding='utf-8'))  # on recopie le noeud à l'identique
  else:            # Si le noeud est un tableau
    # on débute le tableau et on met la ligne de titre
    fic.write("<table>\n<tr><th>Description</th><th>Python</th><th>Scilab</th><th>C</th></tr>\n")
    parite=False
    for ligne in node.getElementsByTagName("ligne"):
      parite= not parite
      if parite:
        fic.write("<tr class=\"odd\">\n")
      else:
        fic.write("<tr class=\"even\">\n")
      
      fic.write("<td>\n")
      fic.write(ligne.getElementsByTagName("description")[0].toxml(encoding='utf-8')[13:-14])
      fic.write("</td>\n")
      
      # Ecriture des 3 cases avec code highlight et les icones d'aide et d'exemple
      traite_python(ligne.getElementsByTagName("python")[0],fic)
      traite_scilab(ligne.getElementsByTagName("scilab")[0],fic)
      traite_C(ligne.getElementsByTagName("C")[0],fic)

      
      fic.write("</tr>")  # On clot la ligne
    # on clot le tableau
    fic.write("</table>\n")
    

fic.close()