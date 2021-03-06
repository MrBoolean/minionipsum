import sublime, sublime_plugin, random, re

class MinionIpsumCommand(sublime_plugin.TextCommand):

    def run(self, edit, paragraphNumber = 1):

        bananaArray = ["pepete","aaaaaah","uuuhhh","jiji","hahaha","jeje","wiiiii","bananaaaa","bappleees","potatoooo","para tu","la bodaaa","poulet tikka masala","daa","hana dul sae","belloo!","poopayee","tank yuuu!","me want bananaaa!","underweaaar","bee do bee do bee do","tulaliloo","ti aamoo!","tatata bala tu","baboiii","po kass","gelatooo","butt","chasy"]

        regions = self.view.sel()

        for region in regions:  
            
            if not region.empty():  
                selection = self.view.substr(sublime.Region(region.begin()-20, region.end()))
                last = re.search("\d+", selection).group(0)
                text = self.generateFullText(int(last), bananaArray)
            else: 
                text = self.generateFullText(paragraphNumber, bananaArray)

        self.view.insert(edit, self.view.sel()[0].begin(), text)

    def generateFullText(self, paragraphNumber, wordsArray):

        FullText = ""
        FullText = self.generateParagraph(wordsArray)   

        for num in range(1, paragraphNumber):
            FullText=FullText+self.generateParagraph(wordsArray);  
    
        return FullText

    def generateParagraph(self, wordsArray):

        oneParagraph = ""
        linesNumber = random.randrange(5,10)
        oneParagraph = self.generateLine(wordsArray)

        for num in range(1, linesNumber):
            oneParagraph = oneParagraph + self.generateLine(wordsArray)   

        return oneParagraph+"\n\n"

    def generateLine(self, wordsArray):

        oneLine = ""
        wordsNumber = random.randrange(5,10)
        wordsArrayLength = len(wordsArray)
        wordRandomIndex = random.randrange(5, wordsArrayLength);
        firstLine = True

        if(firstLine):
            oneLine = "Minions ipsum"
            firstLine=False
        else:
            oneLine=wordsArray[wordRandomIndex];
        
        for num in range(0, wordsArrayLength):
            wordRandomIndex = random.randrange(num, len(wordsArray));       
            wordRandom = wordsArray[wordRandomIndex]

            oneLine=oneLine + ' ' + wordRandom;   

        return oneLine