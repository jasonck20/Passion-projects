import sqlite3

conn=sqlite3.connect("./movie.db")
c = conn.cursor()
c.executescript(''' 
drop table if exists includes;
drop table if exists lists;
drop table if exists retweets;
drop table if exists mentions;
drop table if exists hashtags;
drop table if exists tweets;
drop table if exists follows;
drop table if exists users;

create table users (
  usr         int,
  pwd	      text,
  name        text,
  email       text,
  city        text,
  timezone    float,
  primary key (usr)
);
create table follows (
  flwer       int,
  flwee       int,
  start_date  date,
  primary key (flwer,flwee),
  foreign key (flwer) references users,
  foreign key (flwee) references users
);
create table tweets (
  tid	      int,
  writer      int,
  tdate       date,
  text        text,
  replyto     int,
  primary key (tid),
  foreign key (writer) references users,
  foreign key (replyto) references tweets
);
create table hashtags (
  term        text,
  primary key (term)
);
create table mentions (
  tid         int,
  term        text,
  primary key (tid,term),
  foreign key (tid) references tweets,
  foreign key (term) references hashtags
);
create table retweets (
  usr         int,
  tid         int,
  rdate       date,
  primary key (usr,tid),
  foreign key (usr) references users,
  foreign key (tid) references tweets
);
create table lists (
  lname        text,
  owner        int,
  primary key (lname),
  foreign key (owner) references users
);
create table includes (
  lname       text,
  member      int,
  primary key (lname,member),
  foreign key (lname) references lists,
  foreign key (member) references users
);
''')

c.executescript('''
insert into users values (97, '1234' ,'Connor McDavid','cm@nhl.com','Edmonton',-7);
insert into users values (29, '1324','Leon Draisaitl','ld@nhl.com','Edmonton',-7);
insert into users values (5, '3412','Davood Rafiei','dr@ualberta.ca','Edmonton',-7);

insert into follows values (29,97,'2021-01-10');
insert into follows values (97,29,'2021-09-01');
insert into follows values (5,97,'2022-11-15');

insert into tweets values (1, 5,'2023-06-01','Looking for a good book to read. Just finished lone #survivor', null);
insert into tweets values (2, 97,'2023-02-12','#Edmonton #Oilers had a good game last night.',null);
insert into tweets values (3, 97,'2023-03-01','Go oliers!',2);
insert into tweets values (4, 5,'2023-03-02','yall got this',null);
insert into tweets values (5, 5,'2023-03-09','do you guys still play pokemon go?',null);
insert into tweets values (6, 5,'2022-12-09','anyone wanna go play football ?',null);
insert into tweets values (7, 29,'2022-12-10','Draisatl went crazy ',2);
               

insert into hashtags values ('survivor');
insert into hashtags values ('oilers');
insert into hashtags values ('edmonton');

insert into mentions values (12,'survivor');
insert into mentions values (13,'edmonton');
insert into mentions values (91,'oilers');

insert into retweets values (29,8,'2023-03-01');
insert into retweets values (29,2,'2023-03-02');

insert into lists values ('oilers players',5);
insert into lists values ('pc',5);
insert into lists values ('liberal',5);
insert into lists values ('ndp',5);

insert into includes values ('oilers players',97);
insert into includes values ('oilers players',29);

''')
conn.commit()


def find_tweets(text_to_find):
    # Function takes in text_to_find which is the user input
    # Searches the tweets table for text matching text_to_find
    # Prints the top 5 text that contains the text based on latest date
    search = "%"
    search += text_to_find
    search += "%"
    display_num = 5
    c.execute("select * from tweets where text like ? order by tdate DESC limit ?", (search, display_num, ))
    rows=c.fetchall()
    print(rows)
    display_more(search, display_num, display_num)

def display_more(search, display_num1, offset):
    request_more = input("5 more? (Y/N): ")
    if request_more == 'Y':
        c.execute("select * from tweets where text like ? order by tdate DESC limit ? offset ?", (search, display_num1, offset,  ))
        rows=c.fetchall()
        print(rows)
        display_more(search, display_num1, offset + 5)
    
    elif request_more == 'N':
        if display_num1 == offset:
            select_tweet(search, display_num1, 0)
        else:
            select_tweet(search, display_num1, offset - 5)

def select_tweet(text, limit, offset):
    c.execute("select * from tweets where text like ? order by tdate DESC limit ? offset ?", (text, limit, offset,  ))
    rows=c.fetchall()
    select = int(input("Select tweets 1-5?: "))
    select -= 1
    get_statistics(rows, select)

def get_statistics(rows, select):
    if len(rows) > select:
        tweet_id = rows[select][0]
        c.execute("select * from tweets where replyto = ?", (tweet_id, ))
        reps=c.fetchall()
        c.execute("select * from retweets r, tweets t where r.tid = t.tid")
        rets=c.fetchall()
        print("Tweet: ", rows[select][3])
        print('Number of Replies: ', len(reps))
        print('Number of Retweets: ', len(rets))



def main():
    look_for = input("Search tweet: ")
    find_tweets(look_for)


main()


