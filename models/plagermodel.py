from typing import Any, Optional,List
from datetime import datetime
from uuid import UUID,uuid4
from beanie import Document, Indexed

class Plager(Document):
    id: UUID = Indexed(default_factory=uuid4)
    file_name: Optional[str] = None
    title: Optional[str] = None
    owner: List[str] = []
    plagarism_persent: Optional[str] = None
    plagur: Optional[bool]=False
    
    created_at: Optional[datetime] = datetime.now()
    updated_at: Optional[datetime] = datetime.now()
    description: Optional[str] = None
    word_file_link: Optional[str] = None
    
    def __repr__(self):
        return f"<Plagar {self.file_name}>",f"<Plagar {self.title}>",f"<Plagar {self.owner}>",f"<Plagar {self.plagarism}>"
    
    def __str__(self):
        return self.file_name,self.title,self.owner,self.plagarism
    
    def __eq__(self, other: Any) -> bool:
        if isinstance(other, Plager):
            return self.title == other.title
        return False
    
    def __hash__(self)->int:
        return hash(self.id)
    
    @property
    def get_title(self)->str:
        return self.title
    def get_description(self)->str:
        return self.description
    def plagarism(self)->str:
        return self.plagarism
    
    @classmethod
    async def get_plagar(self,title:str)->"Plager":
        return await Plager.find_one(self.title == title)
    async def get_plagar_by_owner(self,owner:str)->"Plager":
        return await Plager.find_one(self.owner == owner)
    async def get_plagar_by_plagarism(self,plagarism:str)->"Plager":
        return await Plager.find_one(self.plagarism == plagarism)
    
    class Collection:
        name = "Plagar"
    
    