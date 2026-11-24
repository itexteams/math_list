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


def bt_dang25_p2_b3_c3_ds10(self):
    def fmt_num(val):
        if isinstance(val, Rational):
            if val.q == 1:
                return str(val.p)
            else:
                f = float(val)
                s = str(round(f, 5)).rstrip('0').rstrip('.')
                return s.replace('.', ',')
        elif isinstance(val, float):
            s = str(round(val, 5)).rstrip('0').rstrip('.')
            return s.replace('.', ',')
        return str(val)
    
    def fmt_1dec(val):
        s = '%.1f' % float(val)
        return s.replace('.', ',')
    
    # Khối lượng chuẩn mỗi bao (kg)
    std_mass = random.choice([25, 40, 50])
    
    # Tạo dữ liệu ngẫu nhiên gồm 10 bao gạo sao cho:
    # - Khối lượng trung bình bằng đúng std_mass
    # - Độ lệch chuẩn s > 0,15 kg (tức phương sai s^2 > 0,0225) và s <= 0,2 kg (tức s^2 <= 0,04)
    # Để các giá trị đẹp đến 1 chữ số thập phân, ta random độ lệch theo phần mười kg (tổng bằng 0)
    while True:
        diffs_tenths = [random.choice([-3, -2, -1, 0, 0, 1, 2, 3]) for _ in range(9)]
        last_diff = -sum(diffs_tenths)
        if -4 <= last_diff <= 4:
            diffs_tenths.append(last_diff)
            sum_sq_tenths = sum(d**2 for d in diffs_tenths)
            # s^2 = sum_sq_tenths / (10 * 100) = sum_sq_tenths / 1000
            # Cần 0.0225 < s^2 <= 0.04 <=> 22.5 < sum_sq_tenths <= 40
            if 23 <= sum_sq_tenths <= 39:
                random.shuffle(diffs_tenths)
                data_rat = [Rational(std_mass) + Rational(d, 10) for d in diffs_tenths]
                var_val = Rational(sum_sq_tenths, 1000)
                s_float = math.sqrt(float(var_val))
                break
    
    # Giá trị sai cho phương án b
    var_wrong = var_val + Rational(4, 1000)
    
    # Chuỗi hiển thị dãy số liệu (giữ định dạng 1 chữ số thập phân như ảnh mẫu: 49,8; 50,0; ...)
    data_str = '; \\quad '.join(fmt_1dec(v) for v in data_rat)
    sum_str = ' + '.join(fmt_1dec(v) for v in data_rat)
    sq_diff_str = ' + '.join('(%s - %s)^2' % (fmt_1dec(v), str(std_mass)) for v in data_rat)
    s_approx_str = fmt_num(round(s_float, 3))
    
    # Nội dung câu hỏi
    noidungcauhoi = ('''Một dây chuyền đóng gói gạo tự động quy định khối lượng chuẩn mỗi bao là $%s\\text{ kg}$. Kiểm tra ngẫu nhiên $10$ bao gạo, ta thu được khối lượng (đơn vị: $\\text{kg}$):
    \\begin{center}
    $%s$
    \\end{center}''' % (str(std_mass), data_str))
    
    ######################################################################## Nhận biết ###########################################
    
    # Các đáp án
    nb_da_1_d = '\\True Khối lượng trung bình của $10$ bao gạo đạt đúng mức chuẩn $%s\\text{ kg}$' % (str(std_mass))
    nb_da_1_s = 'Khối lượng trung bình của $10$ bao gạo không đạt mức chuẩn $%s\\text{ kg}$' % (str(std_mass))
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_nb_1 = [nb_da_1]
    
    # Nội dung lời giải
    loigiai_nb_1 = ('''Khối lượng trung bình của $10$ bao gạo là:
    $$\\overline{x} = \\dfrac{%s}{10} = %s \\text{ (kg)}.$$
    Vậy khối lượng trung bình của $10$ bao gạo đạt đúng mức chuẩn $%s\\text{ kg}$.''' % (
        sum_str, str(std_mass), str(std_mass)
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
    th_da_1_d = '\\True Phương sai của mẫu số liệu là $%s$' % (fmt_num(var_val))
    th_da_1_s = 'Phương sai của mẫu số liệu là $%s$' % (fmt_num(var_wrong))
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_th_1 = [th_da_1]
    
    # Nội dung lời giải
    loigiai_th_1 = ('''Phương sai của mẫu số liệu là:
    $$s^2 = \\dfrac{1}{10}\\left[%s\\right] = %s.$$''' % (
        sq_diff_str, fmt_num(var_val)
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
    vd_da_1_d = '\\True Độ lệch chuẩn của mẫu số liệu lớn hơn $0,15\\text{ kg}$'
    vd_da_1_s = 'Độ lệch chuẩn của mẫu số liệu nhỏ hơn $0,15\\text{ kg}$'
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vd_1 = [vd_da_1]
    
    # Nội dung lời giải
    loigiai_vd_1 = ('''Độ lệch chuẩn của mẫu số liệu là:
    $$s = \\sqrt{s^2} = \\sqrt{%s} \\approx %s \\text{ (kg)}.$$
    Vì $%s > 0,15$ nên độ lệch chuẩn của mẫu số liệu lớn hơn $0,15\\text{ kg}$.''' % (
        fmt_num(var_val), s_approx_str, s_approx_str
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
    vdc_da_1_d = '\\True Dây chuyền được đánh giá là hoạt động ổn định nếu độ lệch chuẩn không vượt quá $0,2\\text{ kg}$. Với kết quả trên, dây chuyền này đạt yêu cầu'
    vdc_da_1_s = 'Dây chuyền được đánh giá là hoạt động ổn định nếu độ lệch chuẩn không vượt quá $0,2\\text{ kg}$. Với kết quả trên, dây chuyền này không đạt yêu cầu'
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vdc_1 = [vdc_da_1]
    
    # Nội dung lời giải
    loigiai_vdc_1 = ('''Ta có độ lệch chuẩn của mẫu số liệu là $s \\approx %s\\text{ kg} < 0,2\\text{ kg}$. \\\\
    Vậy với kết quả kiểm tra trên, dây chuyền đóng gói gạo này hoạt động ổn định và đạt yêu cầu.''' % (
        s_approx_str
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

