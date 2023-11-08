from math import ceil


class PaginationHelper:

    # The constructor takes in an array of items and an integer indicating
    # how many items fit within a single page
    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page

    # returns the number of items within the entire collection
    def item_count(self):
        return len(self.collection)

    # returns the number of pages
    def page_count(self):
        pages = len(self.collection) / self.items_per_page
        return ceil(pages)

    # returns the number of items on the given page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self, page_index):
        if page_index in range(self.page_count()):
            if page_index == self.page_count() - 1:
                return len(self.collection) - self.items_per_page * (self.page_count() - 1)
            return self.items_per_page
        else:
            return -1

    # determines what page an item at the given index is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self, item_index):
        if item_index in range(len(self.collection)):
            return (item_index) // self.items_per_page
        return -1

