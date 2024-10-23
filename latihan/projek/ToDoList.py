
class Task:
    def __init__(self,title,due_data,kategori):
        self.title=title
        self.due_data=due_data
        self.kategori=kategori
        self.is_completed=False

    def mark_as_completed(self):
        self.is_completed=True

    def __str__(self):
        status="selesai" if self.is_completed else "belum selesai"
        return f"judul: {self.title}, batas waktu: {self.due_data}, kategori: {self.kategori}, status: {status}"
        
class ToDoList:
    def __init__(self):
        self.tasks=[]
    
    def add_task(self,task):
        self.tasks.append(task)
        print(f'tugas "{task.title}"berhasil ditambahkan.')

    def remove_task(self,title):
        for task in self.tasks:
            if task.title == title:
                self.tasks.remove(task)
                print(f'tugas "{title}"berhasil dihapus.')
                return
        print(f'tugas dengan judul "{title}" tidak ditemukan.')
    
    def mark_task_as_completed(self,title):
        for task in self.tasks:
            if task.title == title:
                task.mark_as_completed()
                print(f'"tugas "{title}" ditandai dengan selesai.')
                return
        print(f'"tugas dengan judul "{title}" tidak ditemukan.')
        
    def display_tasks(self,filter_category=None):
        if not self.tasks:
            print("tidak ada tugas yang tersedia.")
        else:
            for task in self.tasks:
              if filter_category is None or task.kategori == filter_category:
                    print(task)

def add_task_manually(todo_list):
        title=input("masukan judul tugas:")
        due_date=input("masukan batas waktu tugas (yyy-mm-dd):")
        category=input("masukan kategori tugas:")

        task=Task(title,due_date,category)
        todo_list.add_task(task)

todo_list=ToDoList()
while True:
    print("\nMenu")
    print("1.tambah tugas")
    print("2.tampilkan semua tugas")
    print("3.tampiilkan tugas berdasarkan kategori")
    print("4.tandai tugas sebagai selesai")
    print("5.hapus tugas")
    print("6.keluar")

    choice=input("pilih opsi (1/2/3/4/5/6):")
    if choice == "1":
        add_task_manually(todo_list)
    elif choice == "2":
        print("\ndaftar tugas:")
        todo_list.display_tasks()
    elif choice == "3":
        category=input("masukan kategori yang ditampilkan:")
        print(f"\ndaftar tugas kategori{category}:")
        todo_list.display_tasks(filter_category = category)
    elif choice == "4":
        title=input("masukan judul tugas yang ingin ditandai sebagai selesai:")
        todo_list.mark_task_as_completed(title)
    elif choice == "5":
        title=input("masukan judul yang ingin dihapus:")
        todo_list.remove_task(title)
    elif choice == "6":
        print("keluar program.")
        break
    else:
        print("opsi tidak valid,silahkan coba lagi!")
                
