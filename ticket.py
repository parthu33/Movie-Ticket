

class Movies():
        
        def __init__(self,movie_name):
              self.movie_name = movie_name
              
              
              

        def show(self):
                print('************   Welcome to RAM Cinemas    *************')
                print("****Those Movies are running in our Theater'**** ")
              
                val=''
                for key,val in movie_name.items():
                        print(f'{key}\t Tickets Available\t\t{val}')

    
        def book(self):
                
                try:
                        movieb_name =input('Enter the Movie you want to watch:').upper()
                        isfound=0
                        for key in movie_name.keys():         
                                if key == movieb_name: 
                                        isfound=1
                                        tickets_avail = movie_name[key]
                                        ticket_book = int(input('Enter the Ticket :'))
                                        if tickets_avail >= ticket_book:
                                                tickets_avail = tickets_avail - ticket_book
                                                print('Your Ticket has been booked')
                                                print( f'Available Tickets {tickets_avail}')
                                        else:
                                                print('Error!!')
                                        

                        if isfound==0:
                                print('Enter Valid Movie Name!!!!')
                except:
                        print('Something Wrong!! ')
        

movie_name = {'BEAST':200,'RRR':150,'KGF':140,'ET':56,'VALIMAI':50}
m = Movies(movie_name)
m.show()
m.book()






            
            
            
            
            
