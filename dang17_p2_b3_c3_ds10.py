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


def bt_dang17_p2_b3_c3_ds10(self):
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
    
    # Tạo dữ liệu ngẫu nhiên cho hai xạ thủ A và B trong 8 lần bắn
    # Sao cho điểm trung bình của hai xạ thủ bằng nhau và nguyên (8 hoặc 9)
    # Khoảng biến thiên của A nhỏ hơn B, phương sai của A nhỏ hơn B (A bắn ổn định hơn B)
    while True:
        mean_target = random.choice([8, 9])
        total_target = 8 * mean_target
        
        # Dữ liệu xạ thủ A (độ phân tán nhỏ)
        data_A = [random.randint(mean_target - 1, min(10, mean_target + 1)) for _ in range(7)]
        last_A = total_target - sum(data_A)
        if max(5, mean_target - 2) <= last_A <= 10:
            data_A.append(last_A)
        else:
            continue
            
        # Dữ liệu xạ thủ B (độ phân tán lớn hơn A)
        data_B = [random.randint(mean_target - 2, 10) for _ in range(7)]
        last_B = total_target - sum(data_B)
        if 5 <= last_B <= 10:
            data_B.append(last_B)
        else:
            continue
            
        R_A = max(data_A) - min(data_A)
        R_B = max(data_B) - min(data_B)
        
        var_A = sum((x_i - Rational(mean_target))**2 for x_i in data_A) / Rational(8)
        var_B = sum((x_i - Rational(mean_target))**2 for x_i in data_B) / Rational(8)
        
        if 0 < R_A < R_B and 0 < var_A < var_B:
            break
    
    std_A = sqrt(var_A)
    std_B = sqrt(var_B)
    
    # Giá trị sai cho các phương án
    mean_wrong = mean_target + random.choice([-1, 1]) if mean_target < 10 else mean_target - 1
    std_B_wrong = sqrt(var_B + Rational(1, 4))
    
    # Chuỗi hiển thị dãy điểm và tổng
    str_A = '; \\quad '.join(str(v) for v in data_A)
    str_B = '; \\quad '.join(str(v) for v in data_B)
    sum_A_str = ' + '.join(str(v) for v in data_A)
    sum_B_str = ' + '.join(str(v) for v in data_B)
    sq_A_str = ' + '.join('(%s - %s)^2' % (str(v), str(mean_target)) for v in data_A)
    sq_B_str = ' + '.join('(%s - %s)^2' % (str(v), str(mean_target)) for v in data_B)
    
    # Nội dung câu hỏi
    noidungcauhoi = ('''Thành tích bắn súng (tính theo điểm) của hai xạ thủ $A$ và $B$ trong $8$ lần bắn được ghi lại như sau:
    \\begin{itemize}
    \\item Xạ thủ $A$: $%s$
    \\item Xạ thủ $B$: $%s$
    \\end{itemize}''' % (str_A, str_B))
    
    ######################################################################## Nhận biết ###########################################
    
    # Các đáp án
    nb_da_1_d = '\\True Điểm trung bình của hai xạ thủ là bằng nhau và đều bằng $%s$ điểm' % (str(mean_target))
    nb_da_1_s = 'Điểm trung bình của hai xạ thủ là bằng nhau và đều bằng $%s$ điểm' % (str(mean_wrong))
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_nb_1 = [nb_da_1]
    
    # Nội dung lời giải
    loigiai_nb_1 = ('''Điểm trung bình của xạ thủ $A$ là:
    $$\\overline{x}_A = \\dfrac{%s}{8} = %s \\text{ (điểm)}.$$
    Điểm trung bình của xạ thủ $B$ là:
    $$\\overline{x}_B = \\dfrac{%s}{8} = %s \\text{ (điểm)}.$$
    Vậy điểm trung bình của hai xạ thủ là bằng nhau và đều bằng $%s$ điểm.''' % (
        sum_A_str, str(mean_target),
        sum_B_str, str(mean_target),
        str(mean_target)
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
    th_da_1_d = '\\True Khoảng biến thiên điểm số của xạ thủ $A$ nhỏ hơn của xạ thủ $B$'
    th_da_1_s = 'Khoảng biến thiên điểm số của xạ thủ $A$ lớn hơn của xạ thủ $B$'
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_th_1 = [th_da_1]
    
    # Nội dung lời giải
    loigiai_th_1 = ('''Khoảng biến thiên điểm số của xạ thủ $A$ là $R_A = %s - %s = %s$. \\\\
    Khoảng biến thiên điểm số của xạ thủ $B$ là $R_B = %s - %s = %s$. \\\\
    Vì $%s < %s$ nên khoảng biến thiên điểm số của xạ thủ $A$ nhỏ hơn của xạ thủ $B$.''' % (
        str(max(data_A)), str(min(data_A)), str(R_A),
        str(max(data_B)), str(min(data_B)), str(R_B),
        str(R_A), str(R_B)
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
    vd_da_1_d = '\\True Độ lệch chuẩn của xạ thủ $A$ bằng $%s$, còn của xạ thủ $B$ bằng $%s$' % (latex(std_A), latex(std_B))
    vd_da_1_s = 'Độ lệch chuẩn của xạ thủ $A$ bằng $%s$, còn của xạ thủ $B$ bằng $%s$' % (latex(std_A), latex(std_B_wrong))
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vd_1 = [vd_da_1]
    
    # Nội dung lời giải
    loigiai_vd_1 = ('''Phương sai điểm số của xạ thủ $A$ là:
    $$s_A^2 = \\dfrac{1}{8}\\left[%s\\right] = %s.$$
    Suy ra độ lệch chuẩn của xạ thủ $A$ là $s_A = \\sqrt{%s} = %s$. \\\\
    Phương sai điểm số của xạ thủ $B$ là:
    $$s_B^2 = \\dfrac{1}{8}\\left[%s\\right] = %s.$$
    Suy ra độ lệch chuẩn của xạ thủ $B$ là $s_B = \\sqrt{%s} = %s$.''' % (
        sq_A_str, latex(var_A), latex(var_A), latex(std_A),
        sq_B_str, latex(var_B), latex(var_B), latex(std_B)
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
    vdc_da_1_d = '\\True Xét về độ ổn định thành tích, xạ thủ $A$ bắn ổn định hơn xạ thủ $B$'
    vdc_da_1_s = 'Xét về độ ổn định thành tích, xạ thủ $B$ bắn ổn định hơn xạ thủ $A$'
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vdc_1 = [vdc_da_1]
    
    # Nội dung lời giải
    loigiai_vdc_1 = ('''Hai xạ thủ có cùng điểm trung bình là $%s$ điểm, nhưng độ lệch chuẩn điểm số của xạ thủ $A$ ($s_A = %s$) nhỏ hơn độ lệch chuẩn điểm số của xạ thủ $B$ ($s_B = %s$). \\\\
    Do đó xét về độ ổn định thành tích, xạ thủ $A$ bắn ổn định hơn xạ thủ $B$.''' % (
        str(mean_target), latex(std_A), latex(std_B)
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

