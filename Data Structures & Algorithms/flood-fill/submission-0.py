class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        if sr>=len(image) or sc>=len(image[0]) or sr<0 or sc<0:
            return image
        a=image[sr][sc]
        if a==color:
            return image
        image[sr][sc]=color
        if sr-1<len(image) and sc<len(image[0]) and image[sr-1][sc]==a:
            self.floodFill(image,sr-1,sc,color)
        if sr+1<len(image) and sc<len(image[0]) and image[sr+1][sc]==a:
            self.floodFill(image,sr+1,sc,color)
        if sr<len(image) and sc-1<len(image[0]) and image[sr][sc-1]==a:
            self.floodFill(image,sr,sc-1,color)
        if sr<len(image) and sc+1<len(image[0]) and image[sr][sc+1]==a:
            self.floodFill(image,sr,sc+1,color)
        return image                



        