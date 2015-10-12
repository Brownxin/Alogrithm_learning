__author__ = 'Brown'
class Solution(object):
    def canFinish(self,numCourse,prerequististes):
        degrees=[0]*numCourse
        courses_map=[[] for i in range(numCourse)]
        for p in prerequististes:
            degrees[p[0]]+=1
            courses_map[p[1]].append(p[0])
        flag=True
        courses=set(range(numCourse))
        while flag and len(courses):
            removelist=[]
            flag=False
            for i in courses:
                if degrees[i]==0:
                    for x in courses_map[i]:
                        degrees[x]-=1
                    removelist.append(i)
                    flag=True
            for delete in removelist:
                courses.remove(delete)
        return len(courses)==0
