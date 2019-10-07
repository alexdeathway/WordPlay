from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,"index.html")   
def analyzed(request):
    #return HttpResponse("haa bhai mil gayi value")
    removepunc=request.POST.get("removepunc","off")
    print(removepunc)
    extraspaceremover=request.POST.get("extraspaceremover","off")
    extralineremover=request.POST.get("extralineremover","off")
    allcaps=request.POST.get("allcaps","off")
    charcount=request.POST.get("charcount","off")
    djtext=request.POST.get('text','Default')
    analyzedtext=""
    action=[]
    print(djtext)
    if (removepunc=="on" or extraspaceremover=="on" or extralineremover=="on" or allcaps=="on" or charcount=="on"):
        if  removepunc=="on":
            #punctuations="a,b,c"
            punctuations = r"""!()-[]{};:'"\,<>./?@#$%^&*_~"""
            for char  in djtext: 
                if char not in punctuations:
                    analyzedtext+=char    
            djtext=analyzedtext
            analyzedtext=""
            action.append("Punctuations Removed")
        if extraspaceremover == "on":
            for charindex in range(0,len(djtext)-1):
                if not(djtext[charindex]==" " and djtext[charindex+1]==" "):
                    analyzedtext+=djtext[charindex]
            djtext=analyzedtext
            analyzedtext=" "
            action.append(" Extra Space Remover")
        if  extralineremover=="on":
            for char in djtext:
                if char !="\n":
                    analyzedtext+=char
            djtext=analyzedtext
            analyzedtext=""
            action.append("Extra Line removed")                      
        if  allcaps=="on":
            for cha in djtext:
                analyzedtext+=cha.upper()
            djtext=analyzedtext
            analyzedtext=""
            action.append("All Capital")  
        if  charcount=="on":
            charcount=0
            for char in djtext:
                if (char !=" " or char !="\n") or char!=" ":
                    charcount+=1
            #djtext=charcount
            action.append("Character Count")  
        param={"analyzedtext":djtext,"action":action}    
        return render(request,"Analyzed.html",param)                  
    else:
        return HttpResponse("Error!")
         
    

            
    
