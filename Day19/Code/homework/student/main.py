import show_menu 
import student_info 


def main():
    L = []
    while True:
        #打印菜单
        #show_menu()
        show_menu.menu()

        s = input('请选择:')
        if s == '1':
            L = student_info.input_student()
             
        elif s == '2':
            student_info.print_student(L)

        elif s == '3':
            student_info.delete_student(L)

        elif s =='4':
            student_info.modify_student(L)

        elif s == '5':
            student_info.max_min_score(L)
             
        elif s == '6':
            student_info.min_max_score(L)

        elif s == '7':
            student_info.max_min_age(L)

        elif s =='8':
            student_info.min_max_age(L)

        elif s == '9':
            L = student_info.student_read()

        elif s == '10':
            student_info.student_write(L)     
        
        elif s == "q":
            break
print(main())