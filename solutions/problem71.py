class Solution:
    def simplifyPath(self, path: str) -> str:
        for i in range(5):
            path = path.replace("//", "/")
        
        stack_of_dirs = []
        splitted_dirs = path.split('/')
        for dir in splitted_dirs:
            if dir == "..":
                if len(stack_of_dirs) > 0:
                    stack_of_dirs.pop()
            elif dir == ".":
                continue
            else:
                stack_of_dirs.append(dir)
        path = ""
        for index, dir in enumerate(stack_of_dirs):
            if len(dir) == 0:
                stack_of_dirs.pop(index)
        for dir in stack_of_dirs:
            path += "/" + dir
        if len(path) == 0:
            path = "/"
        return path
    
s = Solution()
print(s.simplifyPath("/.../a/../b/c/../d/./"))