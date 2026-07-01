# #to make a finance app by the use of python
# print('welcome.we are gonna track your expence.')
# print('===========MENU============')
# print('1) add your expence')
# print('2) view all the expenses')
# print('3) view total spending')
# print('4) exit')
# print('choose the number to perform any of these action from (1-4) ')
# expenses=[]
# while True:
#     option=int(input('enter your option:- '))
#     if(option==1):
#         date=(input('enter the date:- '))
#         cate=input('enter the category:- ')
#         amt=float(input('enter amount:- ')) 
#         des=str(input('description:- '))

#         expense={
#             'date': date,
#             'category': cate,
#             'description': des,
#             'amount': amt,
#         }
#         expenses.append(expense)
#         print('your expense is added is sucessfully.')
        

#     elif(option==2):
#         if(len(expenses)== 0):
#             print('no expense till now.')
#         else:
#             print('total expenses done till now ')
#             count=1 
#             for i in expenses:
#                 print(f'number {count}:- {i ['date']}', {i ['category']} , {i ['description']} , {i ['amount']})
#                 count= count+1
            

#     elif(option==3):
#         totalamt=0
#         for i in expenses:
#             totalamt= totalamt+ i['amount']
        
#         print('\n the total amount spent till now is :- ', totalamt)
       
    
#     elif(option==4):
#         print('thanku for using us')
#         break
    
#     else:
#         print('invalid option entered.')
