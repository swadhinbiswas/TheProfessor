from typing import Optional, List
from uuid import UUID
from models.plagermodel import Plager
from  schemas.plagur import PlagerBase,OutPlager,UpdatePlager

class PlagerService:
  @staticmethod
  async def create_plager(plager:PlagerBase)->Plager:
    plager_in=Plager(
      file_name=plager.file_name,
      title=plager.title,
      owner=plager.owner,
      description=plager.description,
      word_file_link=plager.word_file_link
      
      
    )
    await plager_in.save()
    return plager_in
  
  @staticmethod
  async def get_plager()->List[Plager]:
    return await Plager.all().to_list()
  
  @staticmethod
  async def get_plager_by_title(title:str)->Plager:
    return await Plager.find_one(Plager.title==title)
  
  @staticmethod
  async def get_plager_by_owner(owner:str)->Plager:
    return await Plager.find_one(Plager.owner==owner)
  

  

  
    