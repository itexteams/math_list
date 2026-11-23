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

def bt_dang16_p2_b2_c3_ds10(self):
    # Random các thông số cho bài toán
    n = random.choice([8, 10, 12, 15, 20])
    while True:
        x_bar = random.randint(10, 25)
        m_e = random.randint(10, 25)
        m_o = random.randint(10, 25)
        if len({x_bar, m_e, m_o}) == 3:
            break
    
    c_add = random.randint(2, 6)
    k_mul = random.randint(2, 4)
    
    # Tính các giá trị mới
    new_x_bar = x_bar + c_add
    new_m_e = m_e + c_add
    new_m_o = m_o + c_add
    mul_m_e = m_e * k_mul
    
    # Giá trị nhiễu
    wrong_x_bar = x_bar + c_add + random.choice([-1, 1])
    wrong_m_o = m_o + c_add + random.choice([-1, 1])
    wrong_mul_m_e = m_e + k_mul
    
    # Nội dung câu hỏi
    noidungcauhoi = ('''Cho mẫu số liệu gốc gồm $%s$ giá trị $x_1, x_2, \\ldots, x_{%s}$ có số trung bình $\\overline{x} = %s$, trung vị $M_e = %s$ và mốt $M_o = %s$. Người ta cộng thêm $%s$ đơn vị vào mỗi giá trị của mẫu số liệu để được mẫu mới.''' % (n, n, x_bar, m_e, m_o, c_add))
    
    ######################################################################## Nhận biết ############################################
    
    # Các đáp án
    nb_da_1_d = '\\True Số trung bình của mẫu số liệu mới là $%s$' % (new_x_bar)
    nb_da_1_s = 'Số trung bình của mẫu số liệu mới là $%s$' % (wrong_x_bar)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_nb_1 = [nb_da_1]
    
    # Nội dung lời giải
    loigiai_nb_1 = ('''Khi cộng thêm $%s$ đơn vị vào mỗi giá trị của mẫu số liệu gốc thì số trung bình cũng tăng thêm $%s$ đơn vị. \\\\ Vậy số trung bình của mẫu số liệu mới là $\\overline{x}_{\\text{mới}} = \\overline{x} + %s = %s + %s = %s$.''' % (c_add, c_add, c_add, x_bar, c_add, new_x_bar))
    
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
    th_da_1_d = '\\True Trung vị của mẫu số liệu mới là $%s$' % (new_m_e)
    th_da_1_s = 'Trung vị của mẫu số liệu mới vẫn giữ nguyên là $%s$' % (m_e)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_th_1 = [th_da_1]
    
    # Nội dung lời giải
    loigiai_th_1 = ('''Khi cộng thêm $%s$ đơn vị vào mỗi giá trị của mẫu số liệu gốc thì thứ tự các phần tử không thay đổi và mỗi giá trị đều tăng thêm $%s$ đơn vị nên trung vị cũng tăng thêm $%s$ đơn vị. \\\\ Vậy trung vị của mẫu số liệu mới là $M_{e\\text{ mới}} = M_e + %s = %s + %s = %s$.''' % (c_add, c_add, c_add, c_add, m_e, c_add, new_m_e))
    
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
    vd_da_1_d = '\\True Mốt của mẫu số liệu mới là $%s$' % (new_m_o)
    vd_da_1_s = 'Mốt của mẫu số liệu mới là $%s$' % (wrong_m_o)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vd_1 = [vd_da_1]
    
    # Nội dung lời giải
    loigiai_vd_1 = ('''Khi cộng thêm $%s$ đơn vị vào mỗi giá trị của mẫu số liệu gốc thì tần số xuất hiện của các giá trị tương ứng không đổi và giá trị có tần số lớn nhất tăng thêm $%s$ đơn vị. \\\\ Vậy mốt của mẫu số liệu mới là $M_{o\\text{ mới}} = M_o + %s = %s + %s = %s$.''' % (c_add, c_add, c_add, m_o, c_add, new_m_o))
    
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
    vdc_da_1_d = '\\True Nếu nhân mỗi giá trị của mẫu số liệu gốc với $%s$ (thay vì cộng $%s$), thì trung vị của mẫu mới là $%s$' % (k_mul, c_add, mul_m_e)
    vdc_da_1_s = 'Nếu nhân mỗi giá trị của mẫu số liệu gốc với $%s$ (thay vì cộng $%s$), thì trung vị của mẫu mới là $%s$' % (k_mul, c_add, wrong_mul_m_e)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vdc_1 = [vdc_da_1]
    
    # Nội dung lời giải
    loigiai_vdc_1 = ('''Khi nhân mỗi giá trị của mẫu số liệu gốc với số dương $%s$ thì thứ tự không giảm của dãy số liệu được giữ nguyên và giá trị trung vị được nhân lên $%s$ lần. \\\\ Vậy trung vị của mẫu số liệu mới là $M_{e\\text{ mới}} = %s \\cdot M_e = %s \\cdot %s = %s$.''' % (k_mul, k_mul, k_mul, k_mul, m_e, mul_m_e))
    
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