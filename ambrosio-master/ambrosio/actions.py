class Action(object):
    """Action to be carried on by Ambriosio """
    def __init__(self):
        super(Action, self).__init__()

    def do(self):
        pass

    def is_for_you(self, word):
        pass

class MusicPlayer(Action):
    """MusicPlayer for Ambrosio """
    def __init__(self):
        super(MusicPlayer, self).__init__()
        self.triggers = ["music","audio"] #Qualsevol paraula que comenci per aixo les executara el progama de audio

    def do(self,command):
            print "Will play music", " ".join(command)

    def is_for_you(self, word):
            if word in self.triggers:
                return True
            return False
