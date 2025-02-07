# Problem: Subdomain Visit Count - https://leetcode.com/problems/subdomain-visit-count

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        ans = []
        res = defaultdict(int)
        for item in cpdomains:
            hey = item.split()
            bye = hey[1].split('.')
            for i in range(len(bye)):
                hel = ".".join(bye[i:])
                res[hel]+= int(hey[0])
        for key, value in res.items(): 
            ans.append(f'{value} {key}')
        return ans