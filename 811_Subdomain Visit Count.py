# -*- coding: utf-8 -*-
"""
811. Subdomain Visit Count
Created on Fri May 11 10:14:16 2018
@author: FT
"""

class Solution:
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        DominDic = {}
        for web in cpdomains:
            webtime = int(web.split()[0])
            webadd = web.split()[1]
            while(len(webadd.split("."))>1):
                if(webadd not in DominDic):
                    DominDic[webadd] = webtime
                else:
                    DominDic[webadd] += webtime
                webadd = webadd.replace(webadd.split(".")[0]+".","").strip(".")
            if(webadd not in DominDic):
                DominDic[webadd] = webtime
            else:
                DominDic[webadd] += webtime
        answer = []
        for k,v in DominDic.items():
            answer.append(str(v)+" "+k)
#        print(answer)
        return answer
        
s = Solution()
add = ["9001 discuss.leetcode.com"]
addr = ["4781 hal.net","3742 kmi.ca","7602 fai.fly.com","8927 qpf.gqi.org","6183 gtu.org","7371 yvs.co","6661 xuf.network","9066 yvr.co","4070 rhf.uyy.org","4283 etj.tnr.com","3443 rif.ibf.team","5030 ixi.com","5908 yvs.ca","5789 wph.us","1614 gxj.network","8109 zyh.jfz.network","8435 tpr.irv.network","9848 gbq.ca","4632 gqi.co","7102 gxj.net","2490 dbr.cgl.net","8422 tnw.zqk.team","2018 uuy.network","2358 vbo.com","7372 buf.co","3698 fzx.org","7792 kwd.com","6693 uno.ytn.net","2948 cpl.ser.network","9722 npa.uyy.us","219 yls.network","486 asz.ca","5431 znq.us","8238 vos.ajl.net","1342 fff.ca","2228 cso.gdw.org","2090 zon.vbo.com","7031 zqk.us","2984 okv.us","1052 ocf.com","6148 hwu.com","813 oms.zfz.us","2546 uuy.com","1592 hwu.ca","6253 okv.team","4596 uuy.com","7437 dzg.wsv.network","7970 fly.us","961 jtg.us","962 xec.jfz.co","610 tid.team","7281 nkw.org","5870 yes.gtu.network","1165 llh.okv.us","7084 ser.com","5510 oca.hwu.org","4454 ork.yvs.network","8670 iux.us","5526 oth.wsv.team","2905 wiz.wqv.org","1917 arm.ulz.com","451 pfz.wsv.network","8271 yjt.org","24 gxz.net","7323 msc.nva.com","4837 pfx.ibf.network","529 qay.team","3311 kwd.us","5803 wsv.co","834 hly.hlr.network","5959 yvs.us","6251 hlr.co","2936 vzd.dfa.network","8546 zqy.us","483 bix.ytn.co","2226 oqr.gbq.org","7600 zqk.ca","2612 hbu.cwn.net","430 oxv.bhp.com","9954 srz.vbo.team","3925 hoh.com","5647 ses.ltq.org","1476 gdw.us","1535 ajl.network","5253 bom.yvs.team","8864 thk.net","7029 ser.co","8694 gxk.tfm.co","5255 rbb.fff.com","8491 xzz.ser.co","7181 hnl.net","5919 axj.fff.org","4088 mqy.asz.org","4954 bec.okv.com","8943 dak.wqv.network","5556 jtg.com","1458 xov.epf.co","2868 uwm.yjt.com","6474 tfm.net","2045 tid.co"]
s.subdomainVisits(add)