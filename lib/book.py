#!/usr/bin/env python3

class Book:
    def __init__(self,title,page_count):
        self.title=title
        self.page_count=self.check_int(page_count)
        
    def check_int(self,page_count):
        if isinstance(page_count,int):
            return page_count
        else:
            print("page_count must be an integer")
            return None
    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
    pass
    
        