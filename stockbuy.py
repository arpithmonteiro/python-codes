class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        a=[]
    
        for i in range(len(prices)):
            for j in range(i,len(prices),1):
                if prices[i]<prices[j]:
                    a.append(prices[i]-prices[j])
        print(a)
        if len(a)==0:
            return 0
        x=min(a)
        return(abs(x))
            
