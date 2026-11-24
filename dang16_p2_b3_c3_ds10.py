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


def bt_dang16_p2_b3_c3_ds10(self):
    def fmt_num(val):
        if isinstance(val, Rational):
            if val.q == 1:
                return str(val.p)
            else:
                f = float(val)
                s = str(round(f, 6)).rstrip('0').rstrip('.')
                return s.replace('.', ',')
        elif isinstance(val, float):
            s = str(round(val, 6)).rstrip('0').rstrip('.')
            return s.replace('.', ',')
        return str(val)
    
    # Tạo dữ liệu ngẫu nhiên cho bảng tần số 4 giá trị chiều cao và tổng tần số N = 20
    while True:
        h0 = random.randint(28, 31) * 5
        step = random.choice([5, 10])
        heights = [h0 + i * step for i in range(4)]
        
        # Random 4 tần số sao cho tổng bằng 20 và mỗi nhóm có ít nhất 2 cây
        n1 = random.randint(2, 5)
        n2 = random.randint(3, 6)
        n3 = random.randint(4, 8)
        n4 = 20 - (n1 + n2 + n3)
        
        if 2 <= n4 <= 6:
            freqs = [n1, n2, n3, n4]
            # Khai triển dãy số liệu 20 phần tử đã sắp xếp không giảm
            data = []
            for h, f in zip(heights, freqs):
                data.extend([h] * f)
            
            # Mẫu có 20 phần tử: nửa dưới 10 phần tử đầu (index 0..9), nửa trên 10 phần tử sau (index 10..19)
            Q1_val = Rational(data[4] + data[5], 2)
            Q3_val = Rational(data[14] + data[15], 2)
            delta_Q = Q3_val - Q1_val
            
            # Tính số trung bình cộng và phương sai
            mean_val = Rational(sum(h * f for h, f in zip(heights, freqs)), 20)
            var_val = sum(f * (h - mean_val)**2 for h, f in zip(heights, freqs)) / Rational(20)
            
            # Đảm bảo phương sai là số thập phân hữu hạn đẹp (mẫu số là ước của 10000)
            if delta_Q > 0 and 10000 % var_val.q == 0:
                break
    
    # Giá trị cắt ngọn giảm ở câu d
    k_cut = random.choice([3, 4, 5, 6])
    
    # Giá trị sai cho các phương án
    Q1_wrong = Q1_val + random.choice([-step, step])
    Q3_wrong = Q3_val + random.choice([-step, step])
    delta_Q_wrong = delta_Q + step
    var_wrong = var_val + Rational(5, 4)
    
    # Chuỗi hiển thị trong lời giải
    sum_freq_str = ' + '.join('%s \\cdot %s' % (str(f), str(h)) for h, f in zip(heights, freqs))
    var_term_str = ' + '.join('%s(%s - %s)^2' % (str(f), str(h), fmt_num(mean_val)) for h, f in zip(heights, freqs))
    
    # Nội dung câu hỏi
    noidungcauhoi = ('''Chiều cao (đơn vị: $\\text{cm}$) của $20$ cây giống trong một vườn ươm được thống kê ở bảng tần số sau:
    \\begin{center}
    \\begin{tabular}{|l|c|c|c|c|}
    \\hline
    \\textbf{Chiều cao ($\\text{cm}$)} & $%s$ & $%s$ & $%s$ & $%s$ \\\\
    \\hline
    \\textbf{Số cây} & $%s$ & $%s$ & $%s$ & $%s$ \\\\
    \\hline
    \\end{tabular}
    \\end{center}''' % (
        str(heights[0]), str(heights[1]), str(heights[2]), str(heights[3]),
        str(freqs[0]), str(freqs[1]), str(freqs[2]), str(freqs[3])
    ))
    
    ######################################################################## Nhận biết ###########################################
    
    # Các đáp án
    nb_da_1_d = '\\True Tứ phân vị thứ nhất $Q_1 = %s$ và tứ phân vị thứ ba $Q_3 = %s$' % (fmt_num(Q1_val), fmt_num(Q3_val))
    nb_da_1_s = 'Tứ phân vị thứ nhất $Q_1 = %s$ và tứ phân vị thứ ba $Q_3 = %s$' % (fmt_num(Q1_wrong), fmt_num(Q3_wrong))
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_nb_1 = [nb_da_1]
    
    # Nội dung lời giải
    loigiai_nb_1 = ('''Cỡ mẫu là $n = %s + %s + %s + %s = 20$. \\\\
    Sắp xếp chiều cao của $20$ cây giống theo thứ tự không giảm: $x_1; x_2; \\ldots; x_{20}$. \\\\
    Tứ phân vị thứ nhất $Q_1$ là trung vị của nửa số liệu bên trái ($x_1; x_2; \\ldots; x_{10}$), nên:
    $$Q_1 = \\dfrac{x_5 + x_6}{2} = \\dfrac{%s + %s}{2} = %s.$$
    Tứ phân vị thứ ba $Q_3$ là trung vị của nửa số liệu bên phải ($x_{11}; x_{12}; \\ldots; x_{20}$), nên:
    $$Q_3 = \\dfrac{x_{15} + x_{16}}{2} = \\dfrac{%s + %s}{2} = %s.$$''' % (
        str(freqs[0]), str(freqs[1]), str(freqs[2]), str(freqs[3]),
        str(data[4]), str(data[5]), fmt_num(Q1_val),
        str(data[14]), str(data[15]), fmt_num(Q3_val)
    ))
    
    # Đưa các lời giải vào danh sách lời giải
    list_nb_2 = [loigiai_nb_1]
    
    # Kết hợp các đáp án và lời giải vào cùng một danh sách
    combined_nb = list(zip(list_nb_1, list_nb_2))
    
    # Xáo trộn danh sách kết hợp
    random.shuffle(combined_nb)
    
    # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    
    ######################################################################## Thông hiểu ###########################################
    
    # Các đáp án
    th_da_1_d = '\\True Khoảng tứ phân vị của mẫu số liệu là $\\Delta_Q = %s$' % (fmt_num(delta_Q))
    th_da_1_s = 'Khoảng tứ phân vị của mẫu số liệu là $\\Delta_Q = %s$' % (fmt_num(delta_Q_wrong))
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_th_1 = [th_da_1]
    
    # Nội dung lời giải
    loigiai_th_1 = ('''Khoảng tứ phân vị của mẫu số liệu là:
    $$\\Delta_Q = Q_3 - Q_1 = %s - %s = %s.$$''' % (
        fmt_num(Q3_val), fmt_num(Q1_val), fmt_num(delta_Q)
    ))
    
    # Đưa các lời giải vào danh sách lời giải
    list_th_2 = [loigiai_th_1]
    
    # Kết hợp các đáp án và lời giải vào cùng một danh sách
    combined_th = list(zip(list_th_1, list_th_2))
    
    # Xáo trộn danh sách kết hợp
    random.shuffle(combined_th)
    
    # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ######################################################################## Vận dụng ###########################################
    
    # Các đáp án
    vd_da_1_d = '\\True Phương sai của mẫu số liệu là $s^2 = %s$' % (fmt_num(var_val))
    vd_da_1_s = 'Phương sai của mẫu số liệu là $s^2 = %s$' % (fmt_num(var_wrong))
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vd_1 = [vd_da_1]
    
    # Nội dung lời giải
    loigiai_vd_1 = ('''Chiều cao trung bình của $20$ cây giống là:
    $$\\overline{x} = \\dfrac{%s}{20} = %s \\text{ (cm)}.$$
    Phương sai của mẫu số liệu là:
    $$s^2 = \\dfrac{1}{20}\\left[%s\\right] = %s.$$''' % (
        sum_freq_str, fmt_num(mean_val), var_term_str, fmt_num(var_val)
    ))
    
    # Đưa các lời giải vào danh sách lời giải
    list_vd_2 = [loigiai_vd_1]
    
    # Kết hợp các đáp án và lời giải vào cùng một danh sách
    combined_vd = list(zip(list_vd_1, list_vd_2))
    
    # Xáo trộn danh sách kết hợp
    random.shuffle(combined_vd)
    
    # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ######################################################################## Vận dụng cao ###########################################
    
    # Các đáp án
    vdc_da_1_d = '\\True Nếu người ta cắt ngọn tất cả các cây sao cho mỗi cây giảm đi đúng $%s \\text{ cm}$ thì phương sai của mẫu số liệu mới không thay đổi' % (str(k_cut))
    vdc_da_1_s = 'Nếu người ta cắt ngọn tất cả các cây sao cho mỗi cây giảm đi đúng $%s \\text{ cm}$ thì phương sai của mẫu số liệu mới giảm đi $%s$ đơn vị' % (str(k_cut), str(k_cut**2))
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vdc_1 = [vdc_da_1]
    
    # Nội dung lời giải
    loigiai_vdc_1 = ('''Khi mỗi giá trị của mẫu số liệu đều giảm đi $%s \\text{ cm}$ thì số trung bình cộng của mẫu số liệu mới cũng giảm đi $%s \\text{ cm}$: $\\overline{x}' = \\overline{x} - %s$. \\\\
    Do đó độ lệch của mỗi giá trị so với số trung bình cộng không thay đổi: $(x_i - %s) - (\\overline{x} - %s) = x_i - \\overline{x}$. \\\\
    Vì vậy phương sai của mẫu số liệu mới không thay đổi.''' % (
        str(k_cut), str(k_cut), str(k_cut), str(k_cut), str(k_cut)
    ))
    
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
    '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
    '\\choiceTFn \n'
    '{' + str(shuffled_answers_nb[0]) + '}\n'
    '{' + str(shuffled_answers_th[0]) + '}\n'
    '{' + str(shuffled_answers_vd[0]) + '}\n'
    '{' + str(shuffled_answers_vdc[0]) + '}\n'
    '\\loigiai{ \n'
    '\\begin{enumEX}[a)]{1} \n'
    '\\item ' + str(shuffled_solutions_nb[0]) + '\n'
    '\\item ' + str(shuffled_solutions_th[0]) + '\n'
    '\\item ' + str(shuffled_solutions_vd[0]) + '\n'
    '\\item ' + str(shuffled_solutions_vdc[0]) + '\n'
    '\\end{enumEX}} \n'
    '\\end{ex}\n \\end{minipage}\n\n')
    return content

