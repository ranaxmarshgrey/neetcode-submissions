class Solution:
    def ladderLength(self, beginword: str, endword: str, wordlist: List[str]) -> int:
        if endword not in wordlist:
            return 0
        
        nei=collections.defaultdict(list)
        wordlist.append(beginword)
        for word in wordlist:
            for j in range(len(word)):
                pattern=word[:j]+"*"+word[j+1:]
                nei[pattern].append(word)
        visit=set([beginword])
        q=deque([beginword])
        res=1
        while q:
            for i in range(len(q)):
                word=q.popleft()
                if word==endword:
                    return res
                for j in range(len(word)):
                    pattern=word[:j]+"*"+word[j+1:]
                    for neiword in nei[pattern]:
                        if neiword not in visit:
                            visit.add(neiword)
                            q.append(neiword)



            res+=1

        return 0