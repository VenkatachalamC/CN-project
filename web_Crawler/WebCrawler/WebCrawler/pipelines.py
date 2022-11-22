

from itemadapter import ItemAdapter
import sqlite3

#Storing the crawled datas into database
class WebcrawlerPipeline():

    def __init__(self):
        self.make_conn()
        self.create_table()

    #creating a tabe
    def create_table(self):
        self.cur.execute('''DROP TABLE IF EXISTS book_details''')
        self.cur.execute('''create table book_details( title text,price text,Author text,image_link text)''')

    #making connection with the database
    def make_conn(self):
        self.con=sqlite3.connect('details.db')
        self.cur=self.con.cursor()

    #processing the yielded items
    def process_item(self, item, spider):
        self.insert_values(item)
        return item

    #inserting values into the database
    def insert_values(self,item):
        #Executing the insert command
        self.con.execute('''insert into book_details values(?,?,?,?)''', (item['title'] , item['price'] , item['Author'],item['image_urls'] ) )
        self.con.commit()

