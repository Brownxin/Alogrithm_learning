__author__ = 'Brown'
class Solution(object):
    def findOrder(self,numCourses,prequisites):
        degrees=[0]*numCourses
        course_map=[[] for i in range(numCourses)]
        for p in prequisites:
            degrees[p[0]]+=1
            course_map[p[1]].append(p[0])
        courses=set(range(numCourses))
        res=[]
        flag=True
        while flag and len(courses):
            flag=False
            removelist=[]
            for i in courses:
                if degrees[i]==0:
                    for x in course_map[i]:
                        degrees[x]-=1
                    removelist.append(i)
                    flag=True
            for delete in removelist:
                res.append(delete)
                courses.remove(delete)
        if len(courses)==0:
            return res
        return []