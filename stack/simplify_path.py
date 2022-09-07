class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        sstr = ''
        for i in path + '/':
            if i == '/':
                if sstr =='..':
                    if stack:
                        stack.pop()
                        sstr = ''
                elif sstr !='' and sstr !='.':
                    stack.append(sstr)
                sstr = ''
            else:
                sstr+= i
        return '/' + '/'.join(stack)
            
        