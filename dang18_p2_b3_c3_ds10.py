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


def bt_dang18_p2_b3_c3_ds10(self):
    def fmt_num(val):
        if isinstance(val, Rational):
            if val.q == 1:
                return str(val.p)
            else:
                f = float(val)
                s = str(round(f, 4)).rstrip('0').rstrip('.')
                return s.replace('.', ',')
        elif isinstance(val, float):
            s = str(round(val, 4)).rstrip('0').rstrip('.')
            return s.replace('.', ',')
        return str(val)
    
    # Tạo dữ liệu ngẫu nhiên gồm 9 ngày doanh thu (triệu đồng), trong đó có 1 giá trị bất thường lớn
    while True:
        base_val = random.randint(12, 16)
        normal_vals = [base_val + random.choice([-2, -1, 0, 0, 1, 1, 2, 3]) for _ in range(8)]
        sorted_8 = sorted(normal_vals)
        
        # Với 9 phần tử (đã sắp xếp x0..x8):
        # Trung vị Me = x4 (index 4)
        # Nửa dưới gồm 4 phần tử đầu (index 0..3): Q1 = (x1 + x2) / 2
        # Nửa trên gồm 4 phần tử sau (index 5..8): Q3 = (x6 + x7) / 2
        Q1_val = Rational(sorted_8[1] + sorted_8[2], 2)
        Q3_val = Rational(sorted_8[6] + sorted_8[7], 2)
        delta_Q = Q3_val - Q1_val
        
        if delta_Q >= 2:
            upper_fence = Q3_val + Rational(3, 2) * delta_Q
            lower_fence = Q1_val - Rational(3, 2) * delta_Q
            # Đảm bảo 8 giá trị đầu đều nằm trong khoảng thông thường
            if sorted_8[0] >= lower_fence and sorted_8[7] <= upper_fence:
                outlier_val = int(math.floor(float(upper_fence))) + random.randint(10, 20)
                sorted_data = sorted_8 + [outlier_val]
                # Xáo trộn ngẫu nhiên thứ tự hiển thị (nhưng không trùng với thứ tự đã sắp xếp)
                raw_data = sorted_data[:]
                random.shuffle(raw_data)
                if raw_data != sorted_data:
                    break
    
    Me_val = sorted_data[4]
    
    # Giá trị sai cho các phương án
    Me_wrong = Me_val + random.choice([-1, 1, 2])
    delta_Q_wrong = delta_Q + random.choice([-1, 1, 2])
    non_outlier_val = sorted_data[random.randint(1, 6)]
    
    # Chuỗi hiển thị dãy số liệu ban đầu và dãy đã sắp xếp
    raw_str = '; \\quad '.join(str(v) for v in raw_data)
    sorted_str = '; \\quad '.join(str(v) for v in sorted_data)
    
    # Nội dung câu hỏi
    noidungcauhoi = ('''Doanh thu (đơn vị: triệu đồng) của một cửa hàng tiện lợi trong $9$ ngày liên tiếp được thống kê như sau:
    \\begin{center}
    $%s$
    \\end{center}''' % (raw_str))
    
    ######################################################################## Nhận biết ###########################################
    
    # Các đáp án
    nb_da_1_d = '\\True Trung vị của mẫu số liệu là $M_e = %s$' % (str(Me_val))
    nb_da_1_s = 'Trung vị của mẫu số liệu là $M_e = %s$' % (str(Me_wrong))
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_nb_1 = [nb_da_1]
    
    # Nội dung lời giải
    loigiai_nb_1 = ('''Sắp xếp mẫu số liệu theo thứ tự không giảm ta được:
    $$%s.$$
    Vì cỡ mẫu là $n = 9$ (số lẻ) nên số trung vị của mẫu số liệu là giá trị chính giữa (số thứ $5$), tức là $M_e = %s$.''' % (
        sorted_str, str(Me_val)
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
    loigiai_th_1 = ('''Nửa số liệu bên trái gồm $4$ giá trị: $%s; %s; %s; %s$, suy ra tứ phân vị thứ nhất là:
    $$Q_1 = \\dfrac{%s + %s}{2} = %s.$$
    Nửa số liệu bên phải gồm $4$ giá trị: $%s; %s; %s; %s$, suy ra tứ phân vị thứ ba là:
    $$Q_3 = \\dfrac{%s + %s}{2} = %s.$$
    Vậy khoảng tứ phân vị của mẫu số liệu là:
    $$\\Delta_Q = Q_3 - Q_1 = %s - %s = %s.$$''' % (
        str(sorted_data[0]), str(sorted_data[1]), str(sorted_data[2]), str(sorted_data[3]),
        str(sorted_data[1]), str(sorted_data[2]), fmt_num(Q1_val),
        str(sorted_data[5]), str(sorted_data[6]), str(sorted_data[7]), str(sorted_data[8]),
        str(sorted_data[6]), str(sorted_data[7]), fmt_num(Q3_val),
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
    vd_da_1_d = '\\True Giá trị $%s$ là một giá trị bất thường của mẫu số liệu trên' % (str(outlier_val))
    vd_da_1_s = 'Giá trị $%s$ là một giá trị bất thường của mẫu số liệu trên' % (str(non_outlier_val))
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vd_1 = [vd_da_1]
    
    # Nội dung lời giải
    loigiai_vd_1 = ('''Ta có:
    $$Q_1 - 1,5 \\cdot \\Delta_Q = %s - 1,5 \\cdot %s = %s;$$
    $$Q_3 + 1,5 \\cdot \\Delta_Q = %s + 1,5 \\cdot %s = %s.$$
    Vì $%s > %s$ nên $%s$ là một giá trị bất thường của mẫu số liệu trên (còn các giá trị từ $%s$ đến $%s$ đều thuộc đoạn $[%s; %s]$ nên không phải giá trị bất thường).''' % (
        fmt_num(Q1_val), fmt_num(delta_Q), fmt_num(lower_fence),
        fmt_num(Q3_val), fmt_num(delta_Q), fmt_num(upper_fence),
        str(outlier_val), fmt_num(upper_fence), str(outlier_val),
        str(sorted_data[0]), str(sorted_data[7]), fmt_num(lower_fence), fmt_num(upper_fence)
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
    vdc_da_1_d = '\\True Để đại diện cho mức doanh thu thông thường của cửa hàng trong $9$ ngày này, ta nên dùng số trung vị thay vì số trung bình cộng'
    vdc_da_1_s = 'Để đại diện cho mức doanh thu thông thường của cửa hàng trong $9$ ngày này, ta nên dùng số trung bình cộng thay vì số trung vị'
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vdc_1 = [vdc_da_1]
    
    # Nội dung lời giải
    loigiai_vdc_1 = ('''Do mẫu số liệu có chứa giá trị bất thường rất lớn ($%s$) làm kéo lệch số trung bình cộng lên cao, nên để đại diện cho mức doanh thu thông thường của cửa hàng trong $9$ ngày này, ta nên dùng số trung vị thay vì số trung bình cộng.''' % (str(outlier_val)))
    
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

