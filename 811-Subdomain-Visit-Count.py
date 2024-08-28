class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        adj = defaultdict(int)
        for cpdomain in cpdomains:
            rep, domain = cpdomain.split()
            rep = int(rep)
            domain_parts = domain.split(".")
            subdomains = [".".join(domain_parts[i:]) for i in range(len(domain_parts))]
            for subdomain in subdomains:
                if subdomain not in adj:
                    adj[subdomain] = rep
                else:
                    adj[subdomain] += rep
        res = []
        for key, value in adj.items():
            temp = str(value) + " " + key
            res.append(temp)
        return res
