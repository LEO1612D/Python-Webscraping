from bs4 import BeautifulSoup

with open('home.html','r') as html_file:

    content = html_file.read()

    soup = BeautifulSoup(content, 'lxml')


    #find search for one tag, findall for all of the tags stored in list

    # tags = soup.findAll('h5')

    # print(tags)

    # for data in tags:
    #     print(data.text)

    #---------------------------------------------------------------------

    #Grab all the course cards

    course_cards = soup.find_all('div',class_='card')

    for course in course_cards:
        print("{} is {}".format(course.h5.text,course.a.text.split()[-1]))
        # print(f'{course.h5.text} costs {course.a.text.split()[-1]}')

    
    # OUTPUT : 
    # Python for beginners is 20$
    # Python Web Development is 50$
    # Python Machine Learning is 100$


    