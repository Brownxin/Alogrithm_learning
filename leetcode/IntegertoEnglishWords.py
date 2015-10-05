__author__ = 'Brown'
class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        lv1='Zero One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split()
        lv2='Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()
        lv3='Hundred'
        lv4='Thousand Million Billion'.split()
        if num>=2**31-1:
            return 'Two Billion One Hundred Forty Seven Million Four Hundred Eighty Three Thousand Six Hundred Forty Seven'
        else:
            words=[]
            digit=0
            while num!=0:
                word=''
                token,num=num%1000,int(num/1000)
                if token>99:
                    word+=lv1[int(token/100)]+' '+lv3+' '
                    token=token%100
                if token>19:
                    word+=lv2[int(token/10)-2]+' '
                    token=token%10
                if token>0:
                    word+=lv1[token]+' '
                word=word.strip()
                if word!='':
                    if digit>0:
                        word+=' '+lv4[digit-1]
                    words+=word,
                digit+=1
            return ' '.join(words[::-1]) or 'Zero'