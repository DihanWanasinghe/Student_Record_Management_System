# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion

# Any code taken from other sources is referenced within my code solu􀆟on.
# Student ID: w2054987
# Date: 10.12.2023

from graphics import *

outer_continue=False                                                        # variable used to continue the outer while loop
outer_break=False                                                           #  variable used to break the outer while loop
progress_count=0                                                            #line 5 -8 varibles are used to count the total of  each progression outcome
trailer_count=0
exclude_count=0
retriever_count=0

list_out=[]                                                                 #list for storing progression outcomes of each entry
list_cred=[]                                                                #list for storing  credits   of each entry


def list_text(list_out,list_cred):                                          #function for display the list and write/read from the text
    text_1 = open('text.txt', 'w')                                          #creating a new text file
    i=0
    for element in list_out:
        print(element, end=" - ")
        print(','.join(list_cred[i]))                                       #printing the list of preogression outcomes and corresponding credits
        text_1.write(element + ' - ')                                       # line 20-21 inputting the data to the text
        text_1.write(','.join(list_cred[i]) + '\n')

        i = i + 1
    text_1.close()
    text_1 = open(('text.txt'))
    print()
    for line in text_1:
        print(line, end='')                                                 #printing  the data from the text


def histo(progress_count,trailer_count,exclude_count,retriever_count):                           #histogram function
 total_outcomes = progress_count + trailer_count + exclude_count + retriever_count
 total_outcomes = str(total_outcomes)                                                            #line 34-38 converting int values of counting,total outcomes into str values
 progress_countst = str(progress_count)
 trailer_countst = str(trailer_count)
 exclude_countstr = str(exclude_count)
 retriever_countstr = str(retriever_count)
 mag=15                                                                                          #line 39 -40 variables used fro limittng the height of bars
 dec=1
 nums=[progress_count,trailer_count,exclude_count,retriever_count]                               #list of each int count variables
 max_num=max(nums)                                                                               #calculating which count bar would have the highest height

 win = GraphWin("Histogram",500,500)                                            #creating the window to draw graphics
 win.setBackground('white')

 txt = Text(Point(110, 10), "Histogram Results")                                      #the sentence at the top
 txt.draw(win)

 description=Text(Point(120,480),total_outcomes+" Outcomes in Total")                      #the sentence at the bottom
 description.draw(win)

 line=Line(Point(50,430),Point(465,430))                                             #bottom line of the histogram
 line.draw(win)

 while 430-max_num*mag<=25:                                                                     #calculating the ratio for the bars(to limit the max height)
      mag=mag-1
      if mag<=1:
       mag=1/dec
       dec=dec+1

 rect1=Rectangle(Point(70,430-progress_count*mag),Point(160,430))                      #'Progresss' bar texts regarding to it
 rect1.setFill('Green')
 rect1.setOutline('Black')
 text1=Text(Point(115,460),"Progress")
 text1.draw(win)
 rect1.draw(win)
 text12=Text(Point(115,430-progress_count*mag-10),""+progress_countst)
 text12.draw(win)

 rect2=Rectangle(Point(165,430-trailer_count*mag),Point(255,430))                      #'Trailer' bar  texts regarding to it
 rect2.setFill('Light Green')
 rect2.setOutline('Black')
 text2=Text(Point(210,460),"Trailer")
 text22 = Text(Point(210, 430 - trailer_count * mag - 10), "" + trailer_countst)
 text22.draw(win)
 text2.draw(win)
 rect2.draw(win)

 rect3 = Rectangle(Point(260,430-retriever_count*mag), Point(350, 430))                 #'Retriever' bar and texts regarding to it
 rect3.setFill('Yellow')
 rect3.setOutline('Black')
 text3=Text(Point(305,460),"Retriever")
 text32 = Text(Point(305, 430 - retriever_count * mag - 10), "" + retriever_countstr)
 text32.draw(win)
 text3.draw(win)
 rect3.draw(win)

 rect4 = Rectangle(Point(355,430-exclude_count*mag), Point(445, 430))                   #'Exclude' bar and texts regarding to it
 rect4.setFill('Red')
 rect4.setOutline('Black')
 text4=Text(Point(400,460),"Excluded")
 text42 = Text(Point(400, 430 - exclude_count * mag - 10), "" + exclude_countstr)
 text42.draw(win)
 text4.draw(win)
 rect4.draw(win)

 win.getMouse()
 win.close()

while True:

  user = str(input('Enter \'student\' if you are a student or enter \'staff\' if you are a staff member\n'))   #line 105-110 ,Identifying the user(staff or student)
  user = user.lower()
  if user=='student' or user=='staff':
      break
  else:
      print('Wrong Input')

while True:
      while True:
          try:
              pass_cred = int(input("Please enter the pass credits:"))                                        #Inputting valid  Pass credits
              if pass_cred % 20 != 0 or pass_cred > 120:
                  print("Out of Range")
              else:
                  break
          except ValueError:
              print("Integer required")

      while True:
          try:
              def_cred = int(input("Please enter the defer  credits:"))                                      #Inputting valid  Defer credits

              if def_cred % 20 != 0 or def_cred > 120:
                  print("Out of Range")
              else:
                  break
          except:
              print("Integer required")

      while True:
          try:
              fail_cred = int(input("Please enter the fail   credits:"))                                     #Inputting valid  Fail credits

              if fail_cred % 20 != 0 or fail_cred > 120:
                  print("Out of Range")
              else:
                  break
          except:
              print("Total Incorrect")

      if pass_cred + def_cred + fail_cred != 120:                                                             #Checking whether total credits are 120,else input the credits again
          print("Total Incorrect")
          continue
      elif pass_cred == 120:                                                                                  #line 148-159 deciding the progression outcome ,and counting how many times each possible progression outcome is displayed
          progress_out = "Progress"
          progress_count += 1
      elif pass_cred == 100:
          progress_out = "Progress(module trailer)"
          trailer_count += 1
      elif fail_cred >= 80:
          progress_out = "Exclude"
          exclude_count += 1
      elif (pass_cred <= 80 and pass_cred >= 20) or def_cred <= 120:
          progress_out = "Module retriever"
          retriever_count += 1

      print(progress_out)

      creds = [str(pass_cred), str(def_cred), str(fail_cred)]                                                  #inputting str values of each credit types to a list
      list_out.append(progress_out)                                                                            #append the progression outcome into a declared list variable
      list_cred.append(creds)                                                                                  #append the values of each credit type as a nested list into a declared list variable

      if user == 'staff':                                                                                      #checking whether user is a staff member
          print("Would you like to enter another set of data?")
          while True:
              more_ent = str(input('Enter \'y\' for yes or \'q\' to quit and view results:'))                  #check whether the staff memeber wants to input more records or not
              more_ent = more_ent.lower()

              if more_ent == "y":                                                                              #if the staff memeber has other data to input iterate the loop from the begiing
                  outer_continue = True
                  break
              elif more_ent == "q":                                                                            #if the staff member has finished
                  list_text(list_out, list_cred)                                                               #call out the function that dusplays list and lines in the text file
                  histo(progress_count, trailer_count, exclude_count, retriever_count)                         # inputting data  display the histogram

                  outer_break = True
                  break
              else:
                  print("Wrong Input")
      else:
        break

      if outer_break == True:                                                                                 #breaking the outer while loop
          break
      if outer_continue == True:                                                                              #iterating the outer while loop
          continue



