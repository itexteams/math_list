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

def bt_dang17_p2_b2_c3_ds10(self):
    def format_list_num(lst):
        return '; '.join('$' + str(v) + '$' for v in lst)
    
    # Random dữ liệu cho Tổ 1 và Tổ 2 (mỗi tổ 7 công nhân)
    # Yêu cầu:
    # - Cùng giá trị trung bình M (ví dụ từ 20 đến 25)
    # - Tổ 1 đồng đều hơn Tổ 2 (biên độ nhỏ hơn, trung vị bằng M, mốt bằng M xuất hiện 3 lần)
    # - Tổ 2 phân tán hơn (biên độ lớn hơn, mốt bằng M xuất hiện 2 lần, trung vị bằng M)
    while True:
        M = random.randint(20, 25)
        # Tạo Tổ 1: [M-2, M-1, M, M, M, M+1, M+2] -> tổng = 7M, trung vị = M, mốt = M (tần số 3), R = 4
        t1_sorted = [M - 2, M - 1, M, M, M, M + 1, M + 2]
        
        # Tạo Tổ 2: phân tán hơn, tổng = 7M, mốt = M (tần số 2), trung vị = M
        d1 = random.randint(3, 5)
        d2 = random.randint(2, d1 - 1)
        d3 = random.randint(4, 6)
        d4 = d1 + d2 - d3
        if d4 >= 1 and d4 != d3 and len({M - d1, M - d2, M, M + d4, M + d3}) == 5:
            t2_sorted = sorted([M - d1, M - d2, M, M, M + d4, M + d3, M])
            # Kiểm tra trung vị Tổ 2 (index 3) có bằng M không
            if t2_sorted[3] == M:
                t1_data = t1_sorted.copy()
                t2_data = t2_sorted.copy()
                random.shuffle(t1_data)
                random.shuffle(t2_data)
                if t1_data != t1_sorted and t2_data != t2_sorted:
                    break
    
    tong_t1 = sum(t1_data)
    tong_t2 = sum(t2_data)
    med_t1 = t1_sorted[3]
    med_t2 = t2_sorted[3]
    range_t1 = t1_sorted[-1] - t1_sorted[0]
    range_t2 = t2_sorted[-1] - t2_sorted[0]
    
    str_t1_data = format_list_num(t1_data)
    str_t2_data = format_list_num(t2_data)
    str_t1_sorted = format_list_num(t1_sorted)
    str_t2_sorted = format_list_num(t2_sorted)
    
    # Giá trị nhiễu
    wrong_M = M + random.choice([-1, 1])
    wrong_mode = M + random.choice([-2, 2])
    
    # Nội dung câu hỏi
    noidungcauhoi = ('''Năng suất lao động (sản phẩm/ngày) của $7$ công nhân Tổ $1$ và $7$ công nhân Tổ $2$ được ghi lại như sau: \\\\
    $\\bullet$ Tổ $1$: %s. \\\\
    $\\bullet$ Tổ $2$: %s.''' % (str_t1_data, str_t2_data))
    
    ######################################################################## Nhận biết ############################################
    
    # Các đáp án
    nb_da_1_d = '\\True Năng suất trung bình của hai tổ bằng nhau và cùng bằng $%s$ sản phẩm/ngày' % (M)
    nb_da_1_s = 'Năng suất trung bình của hai tổ bằng nhau và cùng bằng $%s$ sản phẩm/ngày' % (wrong_M)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_nb_1 = [nb_da_1]
    
    # Nội dung lời giải
    tong_t1_str = ' + '.join(str(v) for v in t1_data)
    tong_t2_str = ' + '.join(str(v) for v in t2_data)
    loigiai_nb_1 = ('''Năng suất trung bình của Tổ $1$ là: $\\overline{x}_1 = \\dfrac{%s}{7} = \\dfrac{%s}{7} = %s$ (sản phẩm/ngày). \\\\ Năng suất trung bình của Tổ $2$ là: $\\overline{x}_2 = \\dfrac{%s}{7} = \\dfrac{%s}{7} = %s$ (sản phẩm/ngày). \\\\ Vậy năng suất trung bình của hai tổ bằng nhau và cùng bằng $%s$ sản phẩm/ngày.''' % (tong_t1_str, tong_t1, M, tong_t2_str, tong_t2, M, M))
    
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
    th_da_1_d = '\\True Trung vị năng suất của Tổ $1$ bằng trung vị năng suất của Tổ $2$'
    th_da_1_s = 'Trung vị năng suất của Tổ $1$ lớn hơn trung vị năng suất của Tổ $2$'
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_th_1 = [th_da_1]
    
    # Nội dung lời giải
    loigiai_th_1 = ('''Sắp xếp mẫu số liệu của Tổ $1$ theo thứ tự không giảm ta được: %s. Vì cỡ mẫu $n = 7$ nên trung vị của Tổ $1$ là số thứ $4$, tức là $M_{e1} = %s$. \\\\ Sắp xếp mẫu số liệu của Tổ $2$ theo thứ tự không giảm ta được: %s. Vì cỡ mẫu $n = 7$ nên trung vị của Tổ $2$ là số thứ $4$, tức là $M_{e2} = %s$. \\\\ Vậy trung vị năng suất của Tổ $1$ bằng trung vị năng suất của Tổ $2$ (cùng bằng $%s$ sản phẩm/ngày).''' % (str_t1_sorted, med_t1, str_t2_sorted, med_t2, M))
    
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
    vd_da_1_d = '\\True Mốt của cả hai tổ đều bằng $%s$ sản phẩm/ngày' % (M)
    vd_da_1_s = 'Mốt của cả hai tổ đều bằng $%s$ sản phẩm/ngày' % (wrong_mode)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vd_1 = [vd_da_1]
    
    # Nội dung lời giải
    loigiai_vd_1 = ('''Trong mẫu số liệu của Tổ $1$, giá trị $%s$ xuất hiện nhiều nhất với tần số là $3$ nên $M_{o1} = %s$. \\\\ Trong mẫu số liệu của Tổ $2$, giá trị $%s$ xuất hiện nhiều nhất với tần số là $2$ nên $M_{o2} = %s$. \\\\ Vậy mốt của cả hai tổ đều bằng $%s$ sản phẩm/ngày.''' % (M, M, M, M, M))
    
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
    vdc_da_1_d = '\\True Năng suất của Tổ $1$ đồng đều hơn Tổ $2$'
    vdc_da_1_s = 'Năng suất của Tổ $2$ đồng đều hơn Tổ $1$'
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vdc_1 = [vdc_da_1]
    
    # Nội dung lời giải
    loigiai_vdc_1 = ('''Khoảng biến thiên năng suất của Tổ $1$ là $R_1 = %s - %s = %s$ (sản phẩm/ngày). \\\\ Khoảng biến thiên năng suất của Tổ $2$ là $R_2 = %s - %s = %s$ (sản phẩm/ngày). \\\\ Vì $R_1 < R_2$ ($%s < %s$) và các giá trị của Tổ $1$ tập trung sát giá trị trung bình $%s$ hơn nên năng suất của Tổ $1$ đồng đều hơn Tổ $2$.''' % (t1_sorted[-1], t1_sorted[0], range_t1, t2_sorted[-1], t2_sorted[0], range_t2, range_t1, range_t2, M))
    
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