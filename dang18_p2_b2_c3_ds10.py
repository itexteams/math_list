import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTreeWidget, QTreeWidgetItem, QCheckBox, QFileDialog, QVBoxLayout, QTextEdit, QPushButton, QWidget, QLabel, QLineEdit, QDialog, QAction, QMessageBox
from sympy import *
from sympy.abc import x
import sympy as sp
from sympy import symbols, sqrt, evaluate, Subs, latex, Rational
import random
import math
from sympy import Rational
from fractions import Fraction as frac
from random import randint
from PyQt5.QtGui import QTextCursor
from PyQt5.QtGui import QFont
import hashlib
import uuid
import os
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox

def bt_dang18_p2_b2_c3_ds10(self):
    # Random 5 số nguyên tăng dần: a1 < a2 < a3 < a4 < a5 (x nằm giữa a2 và a3)
    while True:
        a1 = random.randint(2, 5)
        a2 = a1 + random.randint(2, 4)
        # Khoảng cách giữa a2 và a3 ít nhất bằng 4 để có các giá trị nguyên x nằm hẳn bên trong
        a3 = a2 + random.randint(4, 6)
        a4 = a3 + random.randint(2, 4)
        a5 = a4 + random.randint(2, 4)
        
        sum_known = a1 + a2 + a3 + a4 + a5
        # Chọn giá trị x_mean nằm trong (a2, a3) sao cho (sum_known + x_mean) chia hết cho 6
        valid_x_mean = [v for v in range(a2 + 1, a3) if (sum_known + v) % 6 == 0]
        
        # Chọn giá trị x_med nằm trong (a2, a3) sao cho (x_med + a3) chẵn (để trung vị nguyên) và khác x_mean
        valid_x_med = [v for v in range(a2 + 1, a3) if (v + a3) % 2 == 0 and v not in valid_x_mean]
        
        if valid_x_mean and valid_x_med:
            x_mean = random.choice(valid_x_mean)
            mean_val = (sum_known + x_mean) // 6
            
            x_med = random.choice(valid_x_med)
            med_val = (x_med + a3) // 2
            break
    
    # Dãy số hiển thị trong đề bài
    str_data = '$%s$; $%s$; $x$; $%s$; $%s$; $%s$' % (a1, a2, a3, a4, a5)
    str_data_x_med = '$%s$; $%s$; $%s$; $%s$; $%s$; $%s$' % (a1, a2, x_med, a3, a4, a5)
    
    # Giá trị nhiễu
    wrong_x_mean = x_mean + random.choice([-1, 1])
    wrong_x_med = x_med + random.choice([-1, 1])
    
    # Nội dung câu hỏi
    noidungcauhoi = ('''Cho mẫu số liệu đã được sắp xếp theo thứ tự không giảm gồm $6$ số: %s.''' % (str_data))
    
    ######################################################################## Nhận biết ############################################
    
    # Các đáp án
    nb_da_1_d = '\\True Điều kiện của $x$ là $%s \\le x \\le %s$' % (a2, a3)
    nb_da_1_s = 'Điều kiện của $x$ là $%s < x < %s$' % (a2, a3)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_nb_1 = [nb_da_1]
    
    # Nội dung lời giải
    loigiai_nb_1 = ('''Vì mẫu số liệu đã được sắp xếp theo thứ tự không giảm nên số đứng sau lớn hơn hoặc bằng số đứng trước. \\\\ Do đó điều kiện của $x$ là $%s \\le x \\le %s$.''' % (a2, a3))
    
    # Đưa các lời giải vào danh sách lời giải
    list_nb_2 = [loigiai_nb_1]
    
    # Kết hợp các đáp án và lời giải vào cùng một danh sách
    combined_nb = list(zip(list_nb_1, list_nb_2))
    
    # Xáo trộn danh sách kết hợp
    random.shuffle(combined_nb)
    
    # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    
    ######################################################################## Thông hiểu ############################################
    
    # Các đáp án
    th_da_1_d = '\\True Nếu số trung bình của mẫu số liệu bằng $%s$ thì $x = %s$' % (mean_val, x_mean)
    th_da_1_s = 'Nếu số trung bình của mẫu số liệu bằng $%s$ thì $x = %s$' % (mean_val, wrong_x_mean)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_th_1 = [th_da_1]
    
    # Nội dung lời giải
    total_6 = mean_val * 6
    loigiai_th_1 = ('''Số trung bình của mẫu số liệu bằng $%s$ nên ta có: $\\dfrac{%s + %s + x + %s + %s + %s}{6} = %s \\Leftrightarrow %s + x = %s \\Leftrightarrow x = %s$ (thỏa mãn điều kiện $%s \\le x \\le %s$).''' % (mean_val, a1, a2, a3, a4, a5, mean_val, sum_known, total_6, x_mean, a2, a3))
    
    # Đưa các lời giải vào danh sách lời giải
    list_th_2 = [loigiai_th_1]
    
    # Kết hợp các đáp án và lời giải vào cùng một danh sách
    combined_th = list(zip(list_th_1, list_th_2))
    
    # Xáo trộn danh sách kết hợp
    random.shuffle(combined_th)
    
    # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ######################################################################## Vận dụng ############################################
    
    # Các đáp án
    vd_da_1_d = '\\True Nếu trung vị của mẫu số liệu bằng $%s$ thì $x = %s$' % (med_val, x_med)
    vd_da_1_s = 'Nếu trung vị của mẫu số liệu bằng $%s$ thì $x = %s$' % (med_val, wrong_x_med)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vd_1 = [vd_da_1]
    
    # Nội dung lời giải
    two_med = med_val * 2
    loigiai_vd_1 = ('''Mẫu số liệu có cỡ mẫu $n = 6$ là số chẵn nên trung vị của mẫu số liệu là trung bình cộng của hai giá trị đứng ở vị trí thứ $3$ và thứ $4$, tức là $M_e = \\dfrac{x + %s}{2}$. \\\\ Theo đề bài $M_e = %s \\Leftrightarrow \\dfrac{x + %s}{2} = %s \\Leftrightarrow x + %s = %s \\Leftrightarrow x = %s$ (thỏa mãn điều kiện $%s \\le x \\le %s$).''' % (a3, med_val, a3, med_val, a3, two_med, x_med, a2, a3))
    
    # Đưa các lời giải vào danh sách lời giải
    list_vd_2 = [loigiai_vd_1]
    
    # Kết hợp các đáp án và lời giải vào cùng một danh sách
    combined_vd = list(zip(list_vd_1, list_vd_2))
    
    # Xáo trộn danh sách kết hợp
    random.shuffle(combined_vd)
    
    # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ######################################################################## Vận dụng cao ############################################
    
    # Các đáp án
    vdc_da_1_d = '\\True Với $x = %s$, mẫu số liệu không có mốt' % (x_med)
    vdc_da_1_s = 'Với $x = %s$, mẫu số liệu có mốt là $M_o = %s$' % (x_med, x_med)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vdc_1 = [vdc_da_1]
    
    # Nội dung lời giải
    loigiai_vdc_1 = ('''Với $x = %s$, mẫu số liệu trở thành: %s. \\\\ Nhận thấy cả $6$ giá trị trong mẫu số liệu đều phân biệt và mỗi giá trị chỉ xuất hiện đúng $1$ lần nên mẫu số liệu không có mốt.''' % (x_med, str_data_x_med))
    
    # Đưa các lời giải vào danh sách lời giải
    list_vdc_2 = [loigiai_vdc_1]
    
    # Kết hợp các đáp án và lời giải vào cùng một danh sách
    combined_vdc = list(zip(list_vdc_1, list_vdc_2))
    
    # Xáo trộn danh sách kết hợp
    random.shuffle(combined_vdc)
    
    # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
    shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)
    
    def count_true_answers(answers):
        return sum('\\True' in ans for ans in answers)
    
    # Lặp đến khi đáp án có từ 1 đến 3 đúng
    while True:
        nb_da_1 = random.choice(list_nb_da_1)
        th_da_1 = random.choice(list_th_da_1)
        vd_da_1 = random.choice(list_vd_da_1)
        vdc_da_1 = random.choice(list_vdc_da_1)
    
        answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
        true_count = count_true_answers(answers)
        
        if 1 <= true_count <= 3:
            break
    
    # Gán lại vào list
    list_nb_1 = [nb_da_1]
    list_th_1 = [th_da_1]
    list_vd_1 = [vd_da_1]
    list_vdc_1 = [vdc_da_1]
    
    combined_nb = list(zip(list_nb_1, list_nb_2))
    combined_th = list(zip(list_th_1, list_th_2))
    combined_vd = list(zip(list_vd_1, list_vd_2))
    combined_vdc = list(zip(list_vdc_1, list_vdc_2))
    
    random.shuffle(combined_nb)
    random.shuffle(combined_th)
    random.shuffle(combined_vd)
    random.shuffle(combined_vdc)
    
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)
    
    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    content = ('\\begin{minipage}{\\textwidth} \n'
    '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
    '\\choiceTFn \n'
    '{'+str(shuffled_answers_nb[0])+'}\n'
    '{'+str(shuffled_answers_th[0])+'}\n'
    '{'+str(shuffled_answers_vd[0])+'}\n'
    '{'+str(shuffled_answers_vdc[0])+'}\n'
    '\\loigiai{ \n'
    '\\begin{enumEX}[a)]{1} \n'
    '\\item '+str(shuffled_solutions_nb[0])+'\n'
    '\\item '+str(shuffled_solutions_th[0])+'\n'
    '\\item '+str(shuffled_solutions_vd[0])+'\n'
    '\\item '+str(shuffled_solutions_vdc[0])+'\n'
    '\\end{enumEX}} \n'
    '\\end{ex}\n \\end{minipage}\n\n')
    return content