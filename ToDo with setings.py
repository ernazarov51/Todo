todos: list['ToDo']=[]
users: list['User']=[]
class CRUD:
    def sequance_id(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass

    def create(self):
        pass

    def get_all(self):
        pass
class User(CRUD):
    def __init__(self,id=None,fullname=None,username=None,password=None): 
        self.id=id
        self.fullname=fullname
        self.username=username
        self.password=password


    def sequance_id(self):
        if users:
            last_id=users[-1].id
            next_id=last_id+1
            return next_id
        else:
            return 1

    def isvalid(self):
        for user in users:
            if user.username==self.username:
                return False,'usernamedan avval ro\'yxatdan o\'tilgan!'
            if len(self.password)<1:
                return False,'Parol Yaroqsiz!'
        return True,'Muvaffaqiyatli!'

    def islogin(self):
        for user in users:
            if self.username==user.username and self.password==user.password:
                return True,user
        return False,'username yoki parol!'

    def save(self):
        users.append(self)
        
class ToDo(CRUD):
    def __init__(self,id=None,title=None,description=None,execute_at=None,user_id=None):
        self.id=id
        self.title=title
        self.description=description
        self.execute_at=execute_at
        self.user_id=user_id

    def sequance_id(self):
        if todos:
            last_id=todos[-1].id
            next_id=last_id+1
            return next_id
        else:
            return 1
    def create(self):
        todos.append(self)

    def update(self,attribute,value):
        for todo in todos:
            if attribute=='title':
                todo.title=value
            elif attribute=='description':
                todo.description=value
            elif attribute=='time':
                todo.execute_at=value
            else:
                return 'Unday attribut topilmadi!'
        return 'Succes!'
    def delete(self,id,current_user):
        for todo in todos:
            if todo.id==id and todo.user_id==current_user.id:
                todos.remove(todo)
                return 'Succes!'

    def get_all(self,current_user:User):
        currentodo=[]
        for todo in todos:
            if todo.user_id==current_user.id:
                currentodo.append(todo)
        return currentodo


class UI:
    def main(self):
        print('\n====================================================================================\n')
        menu='''
        1) Registr
        2) Login
        0) exit
        '''
        match input(menu):
            case '1':
                self.registr()

            case '2':
                self.login()

            case'0':
                return
            case _:
                self.main()

    def registr(self):
        print('\n====================================================================================\n')
        user={
        'id':User().sequance_id(),
        'fullname':input('Fullname: '),
        'username':input('Username: '),
        'password':input('Password: ')
        }
        user=User(**user)
        isbool,message=user.isvalid()
        if isbool==True:
            user.save()
            print(message)
            self.main()
            return
        else:
            print(message)
            self.main()
            return



    def login(self):
        print('\n====================================================================================\n')
        user={
        'username':input('Username: '),
        'password':input('Password: ')
        }
        user=User(**user)
        isbool,responce=user.islogin()
        if isbool==True:
            print(f'Xush kelibsiz {responce.fullname}')
            self.account(responce)
            return
        else:
            print(responce)
            self.main()
            return

    def account(self,current_user:User):
        print('\n====================================================================================\n')
        menu='''
        1) Todo
        2) Settings
        0) Back
        '''
        match input(menu):
            case '1':
                self.todo_menu(current_user)
            case '2':
                Settings().main(current_user)
            case '0':
                self.main()
            case _:
                self.main()

    def todo_menu(self,current_user:User):
        print('\n====================================================================================\n')
        menu='''
        1) Create
        2) Delete
        3) Update
        4) Get all
        0) Back
        '''
        match input(menu):
            case '1':
                print('\n====================================================================================\n')
                data={
                'id':ToDo().sequance_id(),
                'title':input('Title: '),
                'description':input('Description: '),
                'execute_at':input('Moment: '),
                'user_id':current_user.id
                }
                data=ToDo(**data)
                data.create()
                self.todo_menu(current_user)
                return

            case '2':
                print('\n====================================================================================\n')
                id=int(input('ID: '))
                ToDo().delete(id,current_user)
                print('Todo ochirildi!')
                self.todo_menu(current_user)
                return

            case '3':
                print('\n====================================================================================\n')
                attribute=input('Attribute title/description/time :')
                value=input('Qiymat: ')
                ToDo().update(attribute,value)
                self.todo_menu(current_user)
                return

            case'4':
                s=ToDo().get_all(current_user)
                if len(s)==0:
                    print('\n====================================================================================\n')
                    print('TODO topilmadi!')
                for todo in ToDo().get_all(current_user):
                    print('\n')
                    print(f'ID: {todo.id}')
                    print(f'Title: {todo.title}')
                    print(f'Description: {todo.description}')
                    print(f'Moment: {todo.execute_at}')
                self.todo_menu(current_user)
                return

            case '0':
                self.account(current_user)
                return
            case _:
                self.main()
class Settings:
    def main(self, current_user:User):
        print('\n====================================================================================\n')
        menu="""
        1) About
        2) Change account data
        3) Delete account
        0) <-- Back
        """
        match input(menu):
            case '1':
                self.about(current_user)
            case '2':
                print('\n====================================================================================\n')
                attribute=input('Attribute fullname/password :')
                value=input('Enter the value: ')
                self.change(attribute,value,current_user)
                self.main(current_user)
                return
            case '3':
                self.deleteccount(current_user)
            case '0':
                UI().account(current_user)
                return

    def about(self,current_user:User):
        print('\n====================================================================================\n')
        data=f"""
        ID: {current_user.id}
        Fullname: {current_user.fullname}
        Username: {current_user.username}
        Password: {current_user.password}
        """
        print(data)
        input('Click enter for back to settings!')
        self.main(current_user)
        

    def change(self,attribute,value,current_user:User):
        print('\n====================================================================================\n')
        for user in users:
            if attribute=='fullname':
                user.fullname=value
            elif attribute=='password':
                user.password=value
        return 'Succes!'

    def deleteccount(self,current_user:User):
        print('\n====================================================================================\n')
        print('Account o\'chirilsinmi? Y/n')
        key=input(">>>")
        if key=='n':
            print('Bekor qilindi!')
            self.main(current_user)
            return
        else:
            print('Processing...')
            for user in users:
                if user.username==current_user.username:
                    users.remove(current_user)
            for todo in todos:
                if todo.user_id==current_user.id:
                    todos.remove(todo)
            UI().main()
            return


UI().main()
print(todos)
"""
Finally
"""