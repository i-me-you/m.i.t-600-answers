# 6.0001/6.00 Problem Set 5 - RSS Feed Filter
# Name:i-me-you
# Collaborators:google\ none
# Time:n/a
# =============================================================================
# comeback for testing and seeing it work
# =============================================================================
import feedparser
import string
import time
import threading
from project_util import translate_html
import mtTkinter as tk
from mtTkinter import *
from datetime import datetime
import pytz


#-----------------------------------------------------------------------

#======================
# Code for retrieving and parsing
# Google and Yahoo News feeds
# Do not change this code
#======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        description = translate_html(entry.description)
        pubdate = translate_html(entry.published)

        try:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %Z")
            pubdate.replace(tzinfo=pytz.timezone("GMT"))
          #  pubdate = pubdate.astimezone(pytz.timezone('EST'))
          #  pubdate.replace(tzinfo=None)
        except ValueError:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %z")

        newsStory = NewsStory(guid, title, description, link, pubdate)
        ret.append(newsStory)
    return ret

#======================
# Data structure design
#======================

# Problem 1

# =============================================================================
#  NewsStory
# =============================================================================
class NewsStory(object):
    def __init__(self, guid, title, description, link, pubdate):
        self.guid = guid
        self.title = title
        self.description = description
        self.link = link
        self.pubdate = pubdate
    
    def get_guid(self):
        return self.guid
    
    def get_title(self):
        return self.title
    
    def get_description(self):
        return self.description
    
    def get_link(self):
        return self.link
    
    def get_pubdate(self):
        return self.pubdate
        


#======================
# Triggers
#======================

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        # DO NOT CHANGE THIS!
        raise NotImplementedError

# PHRASE TRIGGERS

# Problem 2
# =============================================================================
# PhraseTrigger
# =============================================================================
class PhraseTrigger(Trigger):
    def __init__(self, phrase):
        Trigger.__init__(self)
        self.phrase = phrase
        
#    def __str__(self):
#        return str(self.phrase)
    
    def is_phrase_in(self, text):
        '''returns true if whole 'phrase' is present in its entirety and appears
        consecutively in text
        false otherwise'''  
        phrase_copy = str(self.phrase)
        text_copy = str(text)

        ##making both lowercase
        phrase_copy = phrase_copy.lower()
        text_copy = text_copy.lower()

        ##changing punctuations to spaces
        for char in string.punctuation:
            if char in phrase_copy:
                phrase_copy = phrase_copy.replace(char,' ')
            if char in text_copy:
                text_copy = text_copy.replace(char, ' ')

        ##making phrase_copy and text_copy a list to get each individual element
        phrase_copy = phrase_copy.split()
        text_copy = text_copy.split()

        ##joining them back to remove spaces
        phrase_copy = ' '.join(phrase_copy)
        text_copy = ' '.join(text_copy)
                                           ##OLUWA THANK YOU FOR HELPING ME SOLVE THIS FUNCTION
        for char in text_copy.split():    ##INCASE IT IS CONTAINED IN OTHER WORDS
            for item in phrase_copy.split():
                if (item in char) and (len(char) > len(item)):
                    return False
        return phrase_copy in text_copy
    
    
# Problem 3                                                ##SUPERCLASS
# =============================================================================
# TitleTrigger    
# =============================================================================
class TitleTrigger(PhraseTrigger):          
    '''fires anytime a new's item's title contains a given phrase'''

    def __init__(self, title):     
        super().__init__(self)
        self.title = title            ##news title attribute
#
    def __str__(self):
        return str(self.title)

    def evaluate(self, news):   
        return self.is_phrase_in(news.get_title())     


         
# Problem 4
# =============================================================================
# DescriptionTrigger
# =============================================================================
        

class DescriptionTrigger(PhraseTrigger):
    '''fires when a new's item's description contains a given phrase'''

    def __init__(self, description):
        super().__init__(self)
        self.description = description
        
    def __str__(self):
        return str(self.description)
        
    def evaluate(self, news):
        return self.is_phrase_in(news.get_description())

# TIME TRIGGERS

# Problem 5
# =============================================================================
# TimeTrigger
# =============================================================================
# Constructor:
#        Input: Time has to be in EST and in the format of "%d %b %Y %H:%M:%S".
#        Convert time from string to a datetime before saving it as an attribute.

class TimeTrigger(Trigger):
    '''Trigger based on when newstory is published'''

    def __init__(self, time):
        Trigger.__init__(self)
        time = datetime.strptime(time, '%d %b %Y %H:%M:%S')     #converting to datetime
        time = time.replace(tzinfo = pytz.timezone("EST"))     #adding timezone
        self.time = time
        
# Problem 6
# =============================================================================
#  BeforeTrigger and AfterTrigger
# =============================================================================
class BeforeTrigger(TimeTrigger):
    '''fires when a news story is published strictly before the trigger's time'''

    def __init__(self, time):
        TimeTrigger.__init__(self, time)
        

    def evaluate(self, news):      ## #comparing trigger time and newsstory time

        trigger_time = self.time.replace(tzinfo = None)      ###removing timezones
        newstime = news.get_pubdate()
        newstime = newstime.replace(tzinfo = None)
        if trigger_time > newstime:
            return True
        else:
            return False



class AfterTrigger(TimeTrigger):
    '''Fires when a news story is published strictly after the trigger's time'''
    def __init__(self, time):
        TimeTrigger.__init__(self, time)
        
        
    def evaluate(self, news):

        trigger_time = self.time.replace(tzinfo = None)  #removing timezone
        newstime = news.get_pubdate()
        newstime = newstime.replace(tzinfo = None)
        if newstime > trigger_time:
            return True
        else:
            return False

        
# COMPOSITE TRIGGERS

# Problem 7
# =============================================================================
# NotTrigger
# =============================================================================
class NotTrigger(Trigger):
    '''inverts the output of another Triggr and returns it'''
    def __init__(self, Trigga):                    #went gangsta yo
        Trigger.__init__(self)
        self.trigga = Trigga            #takes in a trigger as a constructor to the class
    
    def evaluate(self, news):       #returns not Trigger.evaluate(newsitem)
        return not self.trigga.evaluate(news)

# Problem 8
# =============================================================================
#  AndTrigger
# =============================================================================
class AndTrigger(Trigger):
    '''fires if two triggers (which are constructors to the class)
    should Fire'''
    def __init__(self, Trigga1, Trigga2):
        Trigger.__init__(self)
        self.Trigga1 = Trigga1
        self.Trigga2 = Trigga2
        
    def evaluate(self, news):             #if both trigga's are true return true else false
        if (self.Trigga1.evaluate(news)) and (self.Trigga2.evaluate(news)):
            return True
        else:
            return False

# Problem 9
# =============================================================================
#  OrTrigger
# =============================================================================
class OrTrigger(Trigger):
    '''Fires if any/both of the two triggers (which are constructors to the class)
    should fire'''
    def __init__(self, Trigga1, Trigga2):
        Trigger.__init__(self)
        self.Trigga1 = Trigga1
        self.Trigga2 = Trigga2
        
    def evaluate(self, news):
        if (self.Trigga1.evaluate(news)) or (self.Trigga2.evaluate(news)):
            return True
        else:
            return False

#======================
# Filtering
#======================

# Problem 10
def filter_stories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances.

    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """
    # TODO: Problem 10
    # This is a placeholder
    # (we're just returning all the stories, with no filtering)
    newstory_list = []
    for char in stories:
        for item in triggerlist:
            if item.evaluate(char) == True:
                newstory_list.append(char)

#    return stories
    return newstory_list


#======================
# User-Specified Triggers
#======================
# Problem 11
def read_trigger_config(filename):
    """
    filename: the name of a trigger configuration file

    Returns: a list of trigger objects specified by the trigger configuration
        file.
    """
    # We give you the code to read in the file and eliminate blank lines and
    # comments. You don't need to know how it works for now!
    trigger_file = open(filename, 'r')
    lines = []
    for line in trigger_file:
        line = line.rstrip()
        if not (len(line) == 0 or line.startswith('//')):
            lines.append(line)
            
    # TODO: Problem 11
    # line is the list of lines that you need to parse and for which you need
    # to build triggers
    
#    print(lines) # for now, print it so you see what it contains!  |list
    triggerdict = {}
    made_triggers = []

    ##for normal triggers
    for item in lines:
        char = item.split(',')
        if char[1].lower() == 'title':                  
            triggerdict[char[0]] = TitleTrigger(char[2])
        elif char[1].lower() == 'description':
            triggerdict[char[0]] = DescriptionTrigger(char[2])
        elif char[1].lower() == 'after':
            triggerdict[char[0]] = AfterTrigger(char[2])
        elif  char[1].lower() == 'before':
            triggerdict[char[0]] = BeforeTrigger(char[2])
    
    ##for composite triggers and adding triggers to list
    for item in lines:
        char = item.split(',')
        if char[1].lower() == 'and' and (char[2] in triggerdict) and (char[3] in triggerdict):
            triggerdict[char[0]] = AndTrigger(triggerdict[char[2]], triggerdict[char[3]])
        elif char[1].lower() == 'or' and (char[2] in triggerdict) and (char[3] in triggerdict):
            triggerdict[char[0]] = OrTrigger(triggerdict[char[2]], triggerdict[char[3]])
        elif char[0].lower() == 'add':
            for item in char[1:]:
                made_triggers.append(triggerdict[item])
                

    return made_triggers

SLEEPTIME = 12 #seconds -- how often we poll

def main_thread(master):
    # A sample trigger list - you might need to change the phrases to correspond
    # to what is currently in the news
    try:
        t1 = TitleTrigger("election")
        t2 = DescriptionTrigger("Trump")
        t3 = DescriptionTrigger("Clinton")
        t4 = AndTrigger(t2, t3)
        triggerlist = [t1, t4]

        # Problem 11
        # TODO: After implementing read_trigger_config, uncomment this line 
        triggerlist = read_trigger_config('triggers.txt')
        
        # HELPER CODE - you don't need to understand this!
        # Draws the popup window that displays the filtered stories
        # Retrieves and filters the stories from the RSS feeds
        frame = Frame(master)
        frame.pack(side=BOTTOM)
        scrollbar = Scrollbar(master)
        scrollbar.pack(side=RIGHT,fill=Y)

        t = "Google & Yahoo Top News"
        title = StringVar()
        title.set(t)
        ttl = Label(master, textvariable=title, font=("Helvetica", 18))
        ttl.pack(side=TOP)
        cont = Text(master, font=("Helvetica",14), yscrollcommand=scrollbar.set)
        cont.pack(side=BOTTOM)
        cont.tag_config("title", justify='center')
        button = Button(frame, text="Exit", command=root.destroy)
        button.pack(side=BOTTOM)
        guidShown = []
        def get_cont(newstory):
            if newstory.get_guid() not in guidShown:
                cont.insert(END, newstory.get_title()+"\n", "title")
                cont.insert(END, "\n---------------------------------------------------------------\n", "title")
                cont.insert(END, newstory.get_description())
                cont.insert(END, "\n*********************************************************************\n", "title")
                guidShown.append(newstory.get_guid())

        while True:

            print("Polling . . .", end = ' ')
            # Get stories from Google's Top Stories RSS news feed
            stories = process("http://news.google.com/news?output=rss")

            # Get stories from Yahoo's Top Stories RSS news feed
            stories.extend(process("http://news.yahoo.com/rss/topstories"))

            stories = filter_stories(stories, triggerlist)

            list(map(get_cont, stories))
            scrollbar.config(command=cont.yview)


            print("Sleeping...")
            time.sleep(SLEEPTIME)

    except Exception as e:
        print(e)

#
if __name__ == '__main__':
    root = tk.Tk()
    root.title("Some RSS parser")
    t = threading.Thread(target=main_thread, args=(root,))
    t.start()
    root.mainloop()
