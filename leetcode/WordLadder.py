__author__ = 'Brown'
class Solution(object):
    def ladderLength(self,beginWord,endWord,wordList):
        if wordList==[] or beginWord==endWord:
            return 0
        wordList.append(endWord)
        queue=[(beginWord,1)]
        while queue:
            curr=queue.pop(0)
            curr_word=curr[0]
            curr_len=curr[1]
            if curr_word==endWord: return curr_len
            for i in range(len(beginWord)):
                part1=beginWord[:i];part2=beginWord[i+1:]
                for letter in 'abcdefghijklmnopqrstuvwxyz':
                    if letter!=curr[i]:
                        tmp=part1+letter+part2
                        if tmp in wordList:
                            queue.append((tmp,curr_len+1))
                            wordList.remove(tmp)
                            break
        return 0