class site:
    def __init__(self,url:str):
        self.url=url
        self.next=None
        self.prev=None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.hpg=site(homepage)
        self.cur=self.hpg


    def visit(self, url: str) -> None:
        a=site(url)
        self.cur.next=a
        a.prev=self.cur
        self.cur = a
        
        

    def back(self, steps: int) -> str:
        while self.cur.prev and steps>0:
            self.cur=self.cur.prev
            steps-=1
        return self.cur.url    
        

    def forward(self, steps: int) -> str:
        while self.cur.next and steps>0:
            self.cur=self.cur.next
            steps-=1
        return self.cur.url