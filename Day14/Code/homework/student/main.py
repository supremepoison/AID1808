import show_menu 
import student_info 


def main():
    global list
    while True:
        #打印菜单
        #show_menu()
        show_menu.menu()

        s = input('请选择:')
        if s == '1':
            list = student_info.input_student()
             
        elif s == '2':
            student_info.print_student(list)

        elif s == '3':
            student_info.delete_student()

        elif s =='4':
            student_info.modify_student()

        elif s == '5':
            student_info.max_min_score()
             
        elif s == '6':
            student_info.min_max_score()

        elif s == '7':
            student_info.max_min_age()

        elif s =='8':
            student_info.min_max_age()    
        
        elif s == "q":
            break
print(main())