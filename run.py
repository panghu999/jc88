import lianzhong_api #line:1
import requests ,time ,os ,random ,re ,json #line:2
from base64 import b64decode #line:3
from selenium .webdriver .chrome .options import Options #line:4
from selenium .webdriver import ActionChains #line:5
from selenium import webdriver #line:6
from selenium .webdriver .support .wait import WebDriverWait #line:7
from selenium .webdriver .support import expected_conditions as EC #line:8
from selenium .webdriver .common .by import By #line:9
import cv2 as cv #line:10
TG_BOT_TOKEN =''#line:11
TG_USER_ID =''#line:12
if "TG_BOT_TOKEN"in os .environ and os .environ ["TG_BOT_TOKEN"]and "TG_USER_ID"in os .environ and os .environ ["TG_USER_ID"]:#line:13
        TG_BOT_TOKEN =os .environ ["TG_BOT_TOKEN"]#line:14
        TG_USER_ID =os .environ ["TG_USER_ID"]#line:15
        print ("Telegram 推送打开")#line:16
def get_email ():#line:17
    OO000O0000O0O0O00 =random .randint (11 ,999 )#line:18
    OOOO0OOO00O0OO0O0 =random .randint (0 ,200 )#line:19
    OO00O00O0000O000O ='varytmp+{}uu{}d@gmail.com'.format (OO000O0000O0O0O00 ,OOOO0OOO00O0OO0O0 )#line:20
    return OO00O00O0000O000O #line:21
def p_main (O00O0OOOO0O000000 ,OO000OO00OO00O00O ,OOOOOO000OO00O000 ):#line:22
            OOOOO0OO0000OOOO0 ='https://jc88.me/share?userid='+OOOOOO000OO00O000 #line:23
            OO0OOOO000O0O000O =get_email ()#line:24
            print (OO0OOOO000O0O000O )#line:25
            O0O0OO00OO00O0O00 =Options ()#line:26
            O0O0OO00OO00O0O00 =webdriver .ChromeOptions ()#line:27
            O0O0OO00OO00O0O00 .add_argument ('--headless')#line:29
            O0O0OO00OO00O0O00 .add_argument ('--disable-gpu')#line:30
            O0O0OO00OO00O0O00 .add_argument ("--no-sandbox")#line:32
            O0O0O0000O0O0O00O =webdriver .Chrome (options =O0O0OO00OO00O0O00 )#line:33
            O0O0O0000O0O0O00O .get (OOOOO0OO0000OOOO0 )#line:35
            O0O0O0000O0O0O00O .implicitly_wait (10 )#line:36
            time .sleep (1 )#line:37
            O0O0O0000O0O0O00O .find_element_by_xpath ('//*[@id="app"]/section/main/div/div/div[2]/form/div[1]/div[2]/div/span/span/input').send_keys (OO0OOOO000O0O000O )#line:40
            O000O0O000OO0000O =O0O0O0000O0O0O00O .find_element_by_xpath ('//*[@id="app"]/section/main/div/div/div[2]/form/div[2]/div[2]/div/span/span/span/span/img').get_attribute ('src')#line:45
            O000O0O000OO0000O =O000O0O000OO0000O .split (",")[-1 ]#line:47
            O000O0O000OO0000O =O000O0O000OO0000O .replace ("%0A",'\n')#line:48
            O00OOOOO0O00O00OO =b64decode (O000O0O000OO0000O )#line:49
            with open ('./captcha.gif','wb')as O000OO0OOOO0OOOO0 :#line:50
                O000OO0OOOO0OOOO0 .write (O00OOOOO0O00O00OO )#line:51
                O000OO0OOOO0OOOO0 .close ()#line:52
            time .sleep (2 )#line:53
            O0O000OO0O0OOO00O ='./captcha.gif'#line:55
            O0O00OOOOO00O000O =lianzhong_api .main (O00O0OOOO0O000000 ,OO000OO00OO00O00O ,O0O000OO0O0OOO00O ,'http://v1-http-api.jsdama.com/api.php?mod=php&act=upload','','','1008','6d2c0d7fd993356644f952329275796f')#line:57
            O00OOOO000O0OO00O =O0O00OOOOO00O000O .json ()['data']['val']#line:59
            OOOOOOOOOO0OO00O0 =O0O00OOOOO00O000O .json ()['data']['id']#line:60
            print ('图片已识别:'+O00OOOO000O0OO00O )#line:61
            O0O0O0000O0O0O00O .find_element_by_xpath ('//*[@id="app"]/section/main/div/div/div[2]/form/div[2]/div[2]/div/span/span/span/input').send_keys (O00OOOO000O0OO00O )#line:64
            time .sleep (1 )#line:66
            O0O0O0000O0O0O00O .find_element_by_xpath ('//*[@id="app"]/section/main/div/div/div[2]/form/div[3]/div[2]/div/span/span/span/span/button').click ()#line:68
            time .sleep (10 )#line:70
            os .remove (O0O000OO0O0OOO00O )#line:72
            O0OO00OO0O00OO00O =get_num (OO0OOOO000O0O000O )#line:74
            print (O0OO00OO0O00OO00O )#line:75
            print ('验证码已识别：'+O0OO00OO0O00OO00O [0 ])#line:76
            O0O0O0000O0O0O00O .find_element_by_xpath ('//*[@id="app"]/section/main/div/div/div[2]/form/div[3]/div[2]/div/span/span/span/input').send_keys (O0OO00OO0O00OO00O [0 ])#line:79
            O0O0O0000O0O0O00O .find_element_by_xpath ('//*[@id="app"]/section/main/div/div/div[2]/form/div[4]/div[2]/div/span/span/input').send_keys ('qwer1234')#line:83
            time .sleep (1 )#line:85
            O0O0O0000O0O0O00O .find_element_by_xpath ('//*[@id="app"]/section/main/div/div/div[2]/div/p[1]/button').click ()#line:86
            print ('正在点击注册完成！')#line:87
            time .sleep (2 )#line:88
            tx_code (O0O0O0000O0O0O00O )#line:89
            time .sleep (4 )#line:90
            if O0O0O0000O0O0O00O .current_url =='https://jc88.me/home':#line:91
                telegram_bot ("jc88",'微信公众号 柠檬玩机交流 邀请成功！')#line:92
                O0O0O0000O0O0O00O .quit ()#line:93
            else :#line:94
                telegram_bot ("jc88",'微信公众号 柠檬玩机交流 邀请失败')#line:95
                print ('微信公众号 柠檬玩机交流 邀请失败！')#line:96
def telegram_bot (O0OOOO00O00O0OOO0 ,O000O00OO0OO00000 ):#line:97
    print ("\n")#line:98
    OO0O0OOOO0OO00O0O =TG_BOT_TOKEN #line:99
    O0O00O0O000O0O0O0 =TG_USER_ID #line:100
    if "TG_BOT_TOKEN"in os .environ and "TG_USER_ID"in os .environ :#line:101
        OO0O0OOOO0OO00O0O =os .environ ["TG_BOT_TOKEN"]#line:102
        O0O00O0O000O0O0O0 =os .environ ["TG_USER_ID"]#line:103
    if not OO0O0OOOO0OO00O0O or not O0O00O0O000O0O0O0 :#line:104
        print ("Telegram推送的tg_bot_token或者tg_user_id未设置!!\n取消推送")#line:105
        return #line:106
    print ("Telegram 推送开始")#line:107
    O00O00OO0OO00OO0O ={"chat_id":O0O00O0O000O0O0O0 ,"text":O0OOOO00O00O0OOO0 +'\n\n'+O000O00OO0OO00000 ,"disable_web_page_preview":"true"}#line:109
    O0OOOO0OOO0000O00 =requests .post (url ='https://api.telegram.org/bot%s/sendMessage'%(OO0O0OOOO0OO00O0O ),data =O00O00OO0OO00OO0O )#line:111
    print (O0OOOO0OOO0000O00 .text )#line:112
def get_num (O00OO0O0OOOOO000O ):#line:113
    global Driver #line:114
    OO0000000O000O0OO ={'Cookie':'csrf_gmailnator_cookie=9283eccf4672e233327c1d07cbde2fbe; __gads=ID=808c92a03a3667c7-2268f1463cc6007d:T=1614844196:RT=1614845007:S=ALNI_MaEB-hZfUPTo6kHkEmOBLzPe4nqTQ; cto_bundle=AGHOXV9XSVpTNzY3TlRHbldjMDY5RFhQTlU4Y2J1cUpIWGNLVU0xa3ZiWGRKV1duNHo5cXpJYSUyQm5mZ0ROVDJBRFlIa211cG85JTJCOElMV0ZGQUIzVCUyRjg4NTdQZmZSSW9xMzZmMVY5dXdXeDViUUFYeG51SWNibEhqZGxqWGU5NjBQZHpxMg; _ga=GA1.2.1618068840.1614844229; _gid=GA1.2.103981802.1614844229; ci_session=15d382f04f7b998cecd0f9158bfe3db2c8f32629; __cfduid=d1f9a21dd34e5060cfd24ea55f37149961614844181'}#line:117
    O0O0O000O00OOO000 ={'csrf_gmailnator_token':'9283eccf4672e233327c1d07cbde2fbe','action':'LoadMailList','Email_address':O00OO0O0OOOOO000O }#line:119
    try :#line:120
        OO0O0O0O000O000OO =requests .post (url ='https://www.gmailnator.com/mailbox/mailboxquery',data =O0O0O000O00OOO000 ,headers =OO0000000O000O0OO ).text #line:121
        OO00O0O00OO0000OO =re .findall (r'(?<=messageid\\/#).+(?=\\">\\n\\t\\t\\t\\t\\t<table class=\\"message_container)',OO0O0O0O000O000OO )[0 ]#line:122
        O0O0O0O00000OOO0O ={'csrf_gmailnator_token':'9283eccf4672e233327c1d07cbde2fbe','action':'get_message','message_id':OO00O0O00OO0000OO ,'email':'varytmp'}#line:124
        OOO0O0O000OOOOO0O =requests .post (url ='https://www.gmailnator.com/mailbox/get_single_message/',headers =OO0000000O000O0OO ,data =O0O0O0O00000OOO0O ).json ()#line:125
        OO0OO00O0O000OO00 =OOO0O0O000OOOOO0O ['content']#line:127
        OO00OO0000O0OO0O0 =re .findall (r'(?<=验证码为 <b>).+(?=</b>，有效)',OO0OO00O0O000OO00 )#line:129
        return OO00OO0000O0OO0O0 #line:130
    except Exception as OOOOOOOO0000OOOOO :#line:131
        print (OOOOOOOO0000OOOOO )#line:132
def tx_code (OOOOO00000OO0OOOO ):#line:133
    ""#line:134
    OOOOO00000OO0OOOO .implicitly_wait (10 )#line:135
    OOOOO00000OO0OOOO .switch_to .frame ("tcaptcha_iframe")#line:136
    time .sleep (0.5 )#line:138
    O0OOOO00OO0OOOOOO =OOOOO00000OO0OOOO .find_element_by_xpath ('//img[@id="slideBg"]').get_attribute ('src')#line:139
    print (O0OOOO00OO0OOOOOO )#line:140
    if save_img (O0OOOO00OO0OOOOOO ):#line:141
        O0O00OOO0OO000OO0 =get_pos ()#line:142
        O0OO0OO00OOO0000O =get_track (O0O00OOO0OO000OO0 )#line:143
        time .sleep (0.5 )#line:144
        O0O0O0O0O00O0OOOO =OOOOO00000OO0OOOO .find_element_by_xpath ('// *[ @ id = "tcaptcha_drag_thumb"]')#line:145
        ActionChains (OOOOO00000OO0OOOO ).click_and_hold (on_element =O0O0O0O0O00O0OOOO ).perform ()#line:146
        time .sleep (0.2 )#line:147
        print ('轨迹',O0OO0OO00OOO0000O )#line:148
        for OO00O0O00O0OO0OO0 in O0OO0OO00OOO0000O :#line:149
            ActionChains (OOOOO00000OO0OOOO ).move_by_offset (xoffset =OO00O0O00O0OO0OO0 ,yoffset =0 ).perform ()#line:150
        time .sleep (1 )#line:151
        ActionChains (OOOOO00000OO0OOOO ).release (on_element =O0O0O0O0O00O0OOOO ).perform ()#line:152
        time .sleep (5 )#line:153
        return True #line:155
    else :#line:156
        print ('缺口图片捕获失败')#line:157
        return False #line:158
def save_img (O0000O00OOO0O000O ):#line:160
    ""#line:161
    try :#line:162
        OOOO00OOO0O00OO0O =requests .get (O0000O00OOO0O000O ).content #line:163
        with open ('bg.jpeg','wb')as O00O00OO0O000O0O0 :#line:164
            O00O00OO0O000O0O0 .write (OOOO00OOO0O00OO0O )#line:165
        return True #line:166
    except :#line:167
        return False #line:168
def get_pos ():#line:171
    ""#line:174
    O0OOOOOO00O00O00O =cv .imread ('bg.jpeg')#line:175
    OOOO0000O000OO00O =cv .GaussianBlur (O0OOOOOO00O00O00O ,(5 ,5 ),0 )#line:176
    O00O0000O0OOO0000 =cv .Canny (OOOO0000O000OO00O ,200 ,400 )#line:177
    OOO0O000O0O0OOOOO ,OO0OOOOO00OO00O0O =cv .findContours (O00O0000O0OOO0000 ,cv .RETR_EXTERNAL ,cv .CHAIN_APPROX_SIMPLE )#line:178
    for OO00O0OOOOOOO0OO0 ,OO0OOO0O0OO0OO0OO in enumerate (OOO0O000O0O0OOOOO ):#line:179
        O0OO0OO0O00OOO00O =cv .moments (OO0OOO0O0OO0OO0OO )#line:180
        if O0OO0OO0O00OOO00O ['m00']==0 :#line:181
            O0O0000OOOOO00OOO =O0OO000O0O00000O0 =0 #line:182
        else :#line:183
            O0O0000OOOOO00OOO ,O0OO000O0O00000O0 =O0OO0OO0O00OOO00O ['m10']/O0OO0OO0O00OOO00O ['m00'],O0OO0OO0O00OOO00O ['m01']/O0OO0OO0O00OOO00O ['m00']#line:184
        if 6000 <cv .contourArea (OO0OOO0O0OO0OO0OO )<8000 and 370 <cv .arcLength (OO0OOO0O0OO0OO0OO ,True )<390 :#line:185
            if O0O0000OOOOO00OOO <400 :#line:186
                continue #line:187
            O00OO0OOO000O0O00 ,OOOOO0OO00O0OOO00 ,O00OO0000OOO00O00 ,O0O0OOOO00O0OOO00 =cv .boundingRect (OO0OOO0O0OO0OO0OO )#line:188
            cv .rectangle (O0OOOOOO00O00O00O ,(O00OO0OOO000O0O00 ,OOOOO0OO00O0OOO00 ),(O00OO0OOO000O0O00 +O00OO0000OOO00O00 ,OOOOO0OO00O0OOO00 +O0O0OOOO00O0OOO00 ),(0 ,0 ,255 ),2 )#line:189
            print ('【缺口识别】 {x}px'.format (x =O00OO0OOO000O0O00 /2 ))#line:191
            return O00OO0OOO000O0O00 /2 #line:192
    return 0 #line:193
def get_track (OOOO0O0OO00O0OO00 ):#line:196
    ""#line:198
    OOOO0O0OO00O0OO00 -=37 #line:199
    O000O00OO0OO0O00O =0 #line:201
    O0OOO00000O00OO0O =0.2 #line:203
    O0OOOOO0OO00OOO0O =[]#line:205
    O00OOOOOO0O000O00 =0 #line:207
    O000OOO0O000000OO =OOOO0O0OO00O0OO00 *7 /8 #line:209
    OOOO0O0OO00O0OO00 +=10 #line:211
    while O00OOOOOO0O000O00 <OOOO0O0OO00O0OO00 :#line:213
        if O00OOOOOO0O000O00 <O000OOO0O000000OO :#line:214
            OO000OOOOOOO00OOO =random .randint (2 ,4 )#line:216
        else :#line:217
            OO000OOOOOOO00OOO =-random .randint (3 ,5 )#line:218
        O0O00O0O00O0O0OO0 =O000O00OO0OO0O00O #line:221
        OOO00000O0OO00O00 =O0O00O0O00O0O0OO0 *O0OOO00000O00OO0O +0.5 *OO000OOOOOOO00OOO *(O0OOO00000O00OO0O **2 )#line:223
        O00OOOOOO0O000O00 +=OOO00000O0OO00O00 #line:225
        O0OOOOO0OO00OOO0O .append (round (OOO00000O0OO00O00 ))#line:227
        O000O00OO0OO0O00O =O0O00O0O00O0O0OO0 +OO000OOOOOOO00OOO *O0OOO00000O00OO0O #line:230
    for OO00O0OOO0OO00OOO in range (4 ):#line:233
        O0OOOOO0OO00OOO0O .append (-random .randint (2 ,3 ))#line:234
    for OO00O0OOO0OO00OOO in range (4 ):#line:235
        O0OOOOO0OO00OOO0O .append (-random .randint (1 ,3 ))#line:236
    return O0OOOOO0OO00OOO0O #line:237
def move_to (O0O0OOO0OO0O000O0 ):#line:239
    ""#line:240
    pass #line:241
def main ():#line:244
    O0000000OO0000O00 =os .environ ["xiaohg"]#line:245
    OOOOOO0OO0O0OO000 =os .environ ["Psp19940912.."]#line:246
    O00O0O0O0OO00OO00 =os .environ ["WEZN37"]#line:247
    O0O0OOO0O00000O00 =lianzhong_api .get_points (O0000000OO0000O00 ,OOOOOO0OO0O0OO000 )#line:248
    O0O0OOO0O00000O00 =O0O0OOO0O00000O00 .json ()['data']#line:249
    print ('剩余点数：'+str (O0O0OOO0O00000O00 ))#line:250
    if int (O0O0OOO0O00000O00 )<=2 :#line:251
        print ('点数不足！！')#line:252
        time .sleep (5 )#line:253
        telegram_bot ("p++",'点数不足！')#line:254
        exit ()#line:255
    else :#line:256
        print ('start')#line:257
        p_main (O0000000OO0000O00 ,OOOOOO0OO0O0OO000 ,O00O0O0O0OO00OO00 )#line:258
if __name__ =='__main__':#line:261
    main ()#line:262
