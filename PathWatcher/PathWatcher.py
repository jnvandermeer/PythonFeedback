import os
import easygui
import re

class PathWatcher(object):
    """
    A (hopefully) extremely simple pathwatcher. It doesn't
    watch for updated files. That's more fancy and requires
    inotify for linux, or that ReadDirectoryChanges in Windows.
    I *MIGHT* implement this in this class if it's necessary and if
    I can't find it anywhere else (which is not likely)
    See: http://timgolden.me.uk/python/win32_how_do_i/watch_directory_for_changes.html
    Some functionality to select for filename patterns will probably
    also come a bit later!!

    NOTE -- if you call isAdded while things are removed, then calling
    isRemoved next will say False. the isAdded updates the list!
    """


    def __init__(self,*args):

        if not args:
            # popup a windows and ask for it!
            path_to_watch=easygui.diropenbox()
            file_regex=easygui.textbox(msg='Enter Regular Expression', title = 'regex')
            file_regex=file_regex[:-1]
        else:
            path_to_watch=args[0]
            file_regex=args[1]
            
        # store it in the instance..
        self.file_regex = file_regex
        self.path_to_watch = path_to_watch
        self.before = dict ([(f, None) for f in os.listdir (self.path_to_watch)])



    def getPath(self):
        return self.path_to_watch

    def isChanged(self):

        before = self.before
        after = dict ([(f, None) for f in os.listdir (self.path_to_watch)])
        added = [f for f in after if not f in before]
        removed = [f for f in before if not f in after]

        # store for later! --add the base path to it, also:
        self.added=[]
        self.removed=[]
        for item in added:
            self.added.append(os.path.join(self.path_to_watch,item))
        for item in removed:
            self.removed.append(os.path.join(self.path_to_watch,item))
            
        # apply our regex checker -- make sure that it checks the extensions!!
        self.REStringFilter()
        
        if self.added: print "Added: ", ", ".join (self.added)
        if self.removed: print "Removed: ", ", ".join (self.removed)

        self.before = after

        if self.added or self.removed:
            return True
        return False



    def REStringFilter(self):
        """
        takes in a list of strings, returns anther list of strings
        where each element passes a regex check.
        ... could also be performed by the 'map' method...
        """

        def REHelper(inlist, regex):
            newList=[]
            for item in inlist:
                if re.match(regex,item):
                    newList.append(item)
            return newList

        self.added=REHelper(self.added,self.file_regex)
        self.removed=REHelper(self.removed,self.file_regex)
        

    # some other helper functions, i don't really case if things are removed, just if they
    # are added...    
    def isAdded(self):
        self.isChanged()
        if self.added:
            return True
        return False

    def isRemoved(self):
        self.isChanged()
        if self.removed:
            return True
        return False

        

    
    
    
