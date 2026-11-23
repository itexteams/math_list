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

def bt_dang20_p2_b2_c3_ds10(self):
    def format_list_num(lst):
        return '; '.join('$' + str(v) + '$' for v in lst)
    
    # Random 9 giá trị cố định tăng dần (trong đó mode_val xuất hiện 2 lần, outlier là giá trị lớn đột biến)
    # Điều kiện:
    # - Tổng 11 số chia hết cho 11 để số trung bình mean_val nguyên
    # - Tổng a + b = sum_ab lẻ hoặc được chọn sao cho tồn tại duy nhất cặp (a, b) với a <= b (hoặc có điều kiện chặt để suy ra a, b duy nhất)
    # Cụ thể theo mẫu gốc: 2; 4; 6; 7; 7; 8; 9; 10; 22; a; b. Trung bình = 8 => tổng = 88, 9 số đầu tổng = 75 => a + b = 13.
    # Để có duy nhất một mốt là 7: trong 9 số đã có hai số 7, và các số 2, 4, 6, 8, 9, 10, 22 đều xuất hiện 1 lần.
    # Nếu a, b không có số nào bằng 7 thì a, b phải khác nhau và không trùng với {2, 4, 6, 8, 9, 10, 22} -> với a + b = 13 (a <= b):
    # Các cặp (a, b) tự nhiên với a <= b và a + b = 13: (0,13), (1,12), (2,11), (3,10), (4,9), (5,8), (6,7).
    # Lưu ý ở mẫu gốc câu b ghi "Giá trị của a và b lần lượt là a = 6 và b = 7" (tức mốt 7 xuất hiện 3 lần, hoặc đề ngầm hiểu a, b thuộc tập các số đã có).
    # Để bài toán chặt chẽ và chuẩn xác 100%, ta thiết kế sao cho:
    # Chọn mode_val (ví dụ 7 hoặc 8), xuất hiện 2 lần trong 9 số đầu; 7 số còn lại phân biệt.
    # Chọn sum_ab = 2 * mode_val - 1 (ví dụ mode_val = 7 => sum_ab = 13, hoặc mode_val = 8 => sum_ab = 15)
    # Và ràng buộc thêm a >= x3 (số thứ 3) để giới hạn miền giá trị của a, b sao cho cặp (a, b) với b = mode_val là duy nhất!
    while True:
        mode_val = random.choice([7, 8, 9])
        x1 = mode_val - random.randint(4, 5)
        x2 = mode_val - random.randint(2, 3)
        x3 = mode_val - 1
        x4 = mode_val
        x5 = mode_val
        x6 = mode_val + 1
        x7 = mode_val + 2
        x8 = mode_val + 3
        outlier = mode_val + random.randint(13, 18)
        
        known_9 = [x1, x2, x3, x4, x5, x6, x7, x8, outlier]
        sum_9 = sum(known_9)
        
        # Chọn a_val = x3 = mode_val - 1 và b_val = mode_val => a_val + b_val = 2*mode_val - 1
        a_val = mode_val - 1
        b_val = mode_val
        sum_ab = a_val + b_val
        
        total_11 = sum_9 + sum_ab
        if x1 >= 1 and total_11 % 11 == 0:
            mean_val = total_11 // 11
            # Dãy đầy đủ 11 phần tử
            full_sorted = sorted(known_9 + [a_val, b_val])
            med_val = full_sorted[5]
            # Số nhân viên có số hợp đồng lớn hơn trung vị med_val
            count_bonus = sum(1 for v in full_sorted if v > med_val)
            if med_val == mode_val and count_bonus == 5:
                break
    
    str_known_9 = format_list_num(known_9)
    str_full_sorted = format_list_num(full_sorted)
    
    # Giá trị nhiễu
    wrong_sum_ab = sum_ab + random.choice([-1, 1])
    wrong_a = a_val - 1
    wrong_b = b_val + 1
    wrong_med = mean_val
    wrong_count_bonus = sum(1 for v in full_sorted if v > mean_val)
    if wrong_count_bonus == count_bonus:
        wrong_count_bonus = count_bonus - 1
    
    # Nội dung câu hỏi
    noidungcauhoi = ('''Số hợp đồng ký được trong quý I của $11$ nhân viên phòng kinh doanh được thống kê như sau (trong đó có hai nhân viên mới vào làm nên số liệu được kí hiệu là $a$ và $b$, với $a, b \\in \\mathbb{N}$ và $%s \\le a \\le b$): \\\\ %s; $a$; $b$. \\\\ Biết rằng số hợp đồng trung bình mỗi nhân viên ký được là $%s$ hợp đồng và mẫu số liệu trên có duy nhất một mốt là $%s$.''' % (x3, str_known_9, mean_val, mode_val))
    
    ######################################################################## Nhận biết ############################################
    
    # Các đáp án
    nb_da_1_d = '\\True Tổng số hợp đồng của hai nhân viên mới là $a + b = %s$' % (sum_ab)
    nb_da_1_s = 'Tổng số hợp đồng của hai nhân viên mới là $a + b = %s$' % (wrong_sum_ab)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_nb_1 = [nb_da_1]
    
    # Nội dung lời giải
    tong_9_str = ' + '.join(str(v) for v in known_9)
    loigiai_nb_1 = ('''Vì số hợp đồng trung bình mỗi nhân viên ký được là $%s$ hợp đồng nên tổng số hợp đồng của cả $11$ nhân viên là $11 \\cdot %s = %s$ (hợp đồng). \\\\ Ta có: $%s + a + b = %s \\Leftrightarrow %s + a + b = %s \\Leftrightarrow a + b = %s$.''' % (mean_val, mean_val, total_11, tong_9_str, total_11, sum_9, total_11, sum_ab))
    
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
    th_da_1_d = '\\True Giá trị của $a$ và $b$ lần lượt là $a = %s$ và $b = %s$' % (a_val, b_val)
    th_da_1_s = 'Giá trị của $a$ và $b$ lần lượt là $a = %s$ và $b = %s$' % (wrong_a, wrong_b)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_th_1 = [th_da_1]
    
    # Nội dung lời giải
    loigiai_th_1 = ('''Vì $a, b \\in \\mathbb{N}$, $%s \\le a \\le b$ và $a + b = %s$ nên chỉ có cặp số duy nhất thỏa mãn là $a = %s$ và $b = %s$. \\\\ Khi đó trong mẫu số liệu có giá trị $%s$ xuất hiện nhiều nhất với tần số bằng $3$ nên mẫu số liệu có duy nhất một mốt là $%s$ (thỏa mãn đề bài).''' % (x3, sum_ab, a_val, b_val, mode_val, mode_val))
    
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
    vd_da_1_d = '\\True Trung vị của mẫu số liệu đã cho là $%s$ hợp đồng' % (med_val)
    vd_da_1_s = 'Trung vị của mẫu số liệu đã cho là $%s$ hợp đồng' % (wrong_med)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vd_1 = [vd_da_1]
    
    # Nội dung lời giải
    loigiai_vd_1 = ('''Với $a = %s$ và $b = %s$, sắp xếp mẫu số liệu gồm $11$ giá trị theo thứ tự không giảm ta được: %s. \\\\ Vì cỡ mẫu $n = 11$ là số lẻ nên trung vị của mẫu số liệu là giá trị đứng ở vị trí thứ $\\dfrac{11 + 1}{2} = 6$ trong dãy đã sắp xếp. \\\\ Vậy trung vị của mẫu số liệu là $M_e = %s$ hợp đồng.''' % (a_val, b_val, str_full_sorted, med_val))
    
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
    vdc_da_1_d = '\\True Giám đốc quyết định thưởng cho những nhân viên có số hợp đồng lớn hơn số đặc trưng đại diện phù hợp nhất của mẫu số liệu (tránh bị ảnh hưởng bởi nhân viên xuất sắc ký được $%s$ hợp đồng). Khi đó có $%s$ nhân viên được nhận thưởng' % (outlier, count_bonus)
    vdc_da_1_s = 'Giám đốc quyết định thưởng cho những nhân viên có số hợp đồng lớn hơn số đặc trưng đại diện phù hợp nhất của mẫu số liệu (tránh bị ảnh hưởng bởi nhân viên xuất sắc ký được $%s$ hợp đồng). Khi đó có $%s$ nhân viên được nhận thưởng' % (outlier, wrong_count_bonus)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vdc_1 = [vdc_da_1]
    
    # Nội dung lời giải
    bonus_vals_str = ', '.join('$' + str(v) + '$' for v in full_sorted if v > med_val)
    loigiai_vdc_1 = ('''Do mẫu số liệu có giá trị đột biến là $%s$ nên số đặc trưng đại diện phù hợp nhất để tránh bị ảnh hưởng bởi giá trị bất thường này là trung vị $M_e = %s$. \\\\ Trong mẫu số liệu, các nhân viên có số hợp đồng lớn hơn $%s$ gồm $%s$ nhân viên (với số hợp đồng lần lượt là %s). \\\\ Vậy có $%s$ nhân viên được nhận thưởng.''' % (outlier, med_val, med_val, count_bonus, bonus_vals_str, count_bonus))
    
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