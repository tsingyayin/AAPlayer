#官方文档HL鹰语转SPOL0.6.0

import sys
import os
import random
import time
import math

def HLtoSPOL():
  print("官方资源文件转SPOL程序")
  print("请输入需要转换的资源文件的名称")
  while True:
    filename=input("Userinput→")
    try:
        file=open(filename+".txt","r",encoding="UTF-8")
    except IOError:
        print("找不到文件",filename)
    else:
        print("已经找到文件",filename)
        break

  try:
    os.remove(r".\\story\\"+filename+".spol")
  except Exception:
    None
  else:
    None

  Spolfile=open(".\\story\\"+filename+".spol","w+",encoding="UTF-8")
  Spolraw=[]
  Spolraw+=["/SPOL0.6.0"+"\n"]
  Spolraw+=[":"+filename+":"+filename+":罗德岛走廊:罗德岛"+"\n"]

  Cachefile=open(".\\arknights\\cache\\"+filename+".shl","w+",encoding="UTF-8")
  Cacheraw=[]
  InDecision=0
  Inblock=0

  bgsetlst={"image":"","screenadapt":"","fadetime":"","block":""}
  blockersetlst={"a":"0","r":"0","g":"0","b":"0","fadetime":"","block":"true",}
  decisionrawlst={"options":[],"alues":[]}
  avgsetlst={"name":"","name2":""," focus":"1"}
  blockersetlst={"a":"0","r":"0","g":"0","b":"0","fadetime":"","block":"true",}
  branchsetlst={"references":[]}

#逐行转换循环
  for lineraw in file.readlines():
    line=lineraw[:-1]
    if line[:5]!="[name":
        line=line.replace(" ","")
    line=line.replace("Dr.{@nickname}","Doctor")
    line=line.replace("{@Nickname}","Doctor")
    Cacheraw+=[line+"\n"]

    if line[1:9]=="Decision":
        InDecision=1
        inforaw=line[line.index("(")+1:line.index(")")]
        inforawlst=inforaw.split(",v")
        decisionrawlst={"options":[],"alues":[]}

        for i in inforawlst:
            decisionrawlst[i.split("=")[0]]+=i.split("=")[1][1:-1].split(";")

        decisionspolstr=""
        for i in range(0,len(decisionrawlst["alues"])):
            try:
                if len(decisionrawlst["options"])==1:
                    decisionspolstr+="|||"+decisionrawlst["alues"][i]+":"+decisionrawlst["options"][0]
                elif len(decisionrawlst["options"])!=1:
                    decisionspolstr+="|||"+decisionrawlst["alues"][i]+":"+decisionrawlst["options"][i]
            except Exception:
                decisionspolstr="|||1:！！！这个分支点无法被正常解释！！！"
                InDecision=0
                break
            else:
                None

        Spolraw+=[decisionspolstr+"\n"]
        continue



    if line=="[stopmusic]":
        Spolraw+=["{}"+"\n"]

    elif line=="[Character]":
        Spolraw+=[">>>:"+"\n"]
        avgsetlst={"name":"","name2":"","focus":"1"}

    elif line=="[Background]":
        bgsetlst={"image":"","screenadapt":"","fadetime":"","block":""}
        Spolraw+=["[黑场]"+"\n"]

    elif line[1:11]=="Background":
        inforaw=line[line.index("(")+1:line.index(")")]
        inforawlst=inforaw.split(",")
        bgsetlst={"image":"","screenadapt":"","fadetime":"","block":""}
        for i in inforawlst:
            bgsetlst[i.split("=")[0]]=i.split("=")[1]
        Spolraw+=["["+bgsetlst["image"][1:-1]+",,,"+bgsetlst["fadetime"]+"]"+"\n"]

    elif line[1:8]=="Blocker":
        inforaw=line[line.index("(")+1:line.index(")")]
        inforawlst=inforaw.split(",")
        blockersetlst={"a":"0","r":"0","g":"0","b":"0","fadetime":"","block":"true",}
        for i in inforawlst:
            blockersetlst[i.split("=")[0]]=i.split("=")[1]
        if blockersetlst["a"]=="1":
            Spolraw+=["["+"黑场"+",,,"+blockersetlst["fadetime"]+"]"+"\n"]
            Inblock=1
        elif blockersetlst["a"]=="0":
            Spolraw+=["["+bgsetlst["image"][1:-1]+",,,"+blockersetlst["fadetime"]+"]"+"\n"]
            Inblock=0

    elif line[1:10]=="Character":
        inforaw=line[line.index("(")+1:line.index(")")]
        inforawlst=inforaw.split(",")
        avgsetlst={"name":"","name2":"","focus":"1"}

        for i in inforawlst:
            avgsetlst[i.split("=")[0]]=i.split("=")[1]


    elif line[1:5]=="name":
        nameraw=line[line.index("=")+2:line.index("]")-1]
        wordraw=line[line.index("]")+1:]
        wordraw=wordraw.replace(" ","") #这里有个空格替换
        if avgsetlst["name2"]=="":
            if Inblock==0:
                Spolraw+=[">>>"+avgsetlst["name"][1:-1]+":"+nameraw+":"+wordraw+"\n"]
            elif Inblock==1:
                Spolraw+=[">>>:"+nameraw+":"+wordraw+"\n"]
        elif avgsetlst["name2"]!="":
            if avgsetlst["focus"]=="1":
                if Inblock==0:
                    Spolraw+=[">>>"+avgsetlst["name"][1:-1]+":"+nameraw+":"+wordraw+">>>"+avgsetlst["name2"][1:-1]+":"+"\n"]
                elif Inblock==1:
                    Spolraw+=[">>>:"+nameraw+":"+wordraw+">>>:"+"\n"]
            elif avgsetlst["focus"]=="2":
                if Inblock==0:
                    Spolraw+=[">>>"+avgsetlst["name"][1:-1]+":"+">>>"+avgsetlst["name2"][1:-1]+":"+nameraw+":"+wordraw+"\n"]
                elif Inblock==1:
                    Spolraw+=[">>>:"+">>>:"+nameraw+":"+wordraw+"\n"]

    elif line[1:10]=="Predicate":
        inforaw=line[line.index("(")+1:line.index(")")]
        inforawlst=inforaw.split(",")
        branchsetlst={"references":[]}

        for i in inforawlst:
            branchsetlst[i.split("=")[0]]+=i.split("=")[1][1:-1].split(";")

        if branchsetlst["references"]==decisionrawlst["alues"]:
            Spolraw+=["|||"+"\n"]
            InDecision=0

        else:
            Spolraw+=["||"+branchsetlst["references"][0]+"\n"]
            continue

    elif line[1:6]=="Delay":
        Spolraw+=[">>>:"+"(,"+line[line.index("=")+1:-2]+")"+"\n"]

    elif line[0]!="[":
        Spolraw+=[">>>:"+line+"\n"]

    

    if InDecision==1:
        Spolraw[-1]="|"+Spolraw[-1]

  Cachefile.writelines(Cacheraw)
  Cachefile.close()

  Spolfile.writelines(Spolraw)
  Spolfile.close()

  print("转换完毕")
  return
