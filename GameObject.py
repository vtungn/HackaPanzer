class GameObject:

    def __init__(self, game, position):   
        self.game = game  
        self.game.add_object(self)
        
        self.position = position

    def LoadContent(self):
        pass
        
    def UpdateKeyPress(self, event):
        pass

    def Update(self, event):
        pass

    def Draw(self,screen):
        pass
