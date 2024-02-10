from beanie import Document, Indexed
from typing import List,Any

class ArticleModel(Document):
    title: str
    owner: List[str]
    filename:str
    content:str

    
    def __repr__(self) -> str:
        return f"ArticleModel(title={self.title}, owner={self.owner})"
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __eq__(self, other: Any) -> bool:
        if isinstance(other, ArticleModel):
            return self.title == other.title and self.owner == other.owner
        return False
    @property
    def get_title(self):
        return self.title       
    @property
    def get_all_text(self):
        return self.all_text
    @property
    def get_owner(self):
        return self.owner
    @property
    def set_title(self, title):
        self.title = title
        
    @classmethod
    async def get_article_by_title(cls, title: str):
        return await cls.get(title=title)
    async def get_article_by_owner(cls, owner: str):
        return await cls.get(owner=owner)
    async def get_article_by_text(cls, all_text: str):
        return await cls.get(all_text=all_text)
    async def get_article_by_title_and_owner(cls, title: str, owner: str):
        return await cls.get(title=title, owner=owner)
    async def get_article_by_title_and_text(cls, title: str, all_text: str):
        return await cls.get(title=title, all_text=all_text)
    async def get_article_by_owner_and_text(cls, owner: str, all_text: str):
        return await cls.get(owner=owner, all_text=all_text)