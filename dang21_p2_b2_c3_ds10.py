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
from decimal import Decimal, ROUND_HALF_UP

def bt_dang21_p2_b2_c3_ds10(self):
    def format_dec(val):
        s = str(val).rstrip('0').rstrip('.')
        if s == '':
            s = '0'
        return s.replace('.', ',')
    
    # Random các thông số cho bài toán
    while True:
        n_A = random.choice([15, 20, 25])
        n_B = random.choice([25, 30, 35])
        n_old = n_A + n_B
        n_new = random.choice([10, 15, 20])
        n_total = n_old + n_new
        
        p_A = random.randint(40, 48)
        p_B = p_A + random.randint(4, 8)
        
        total_old = n_A * p_A + n_B * p_B
        # Năng suất trung bình của công nhân cũ (đẹp: chia hết cho 2 khi chia n_old)
        if (total_old * 2) % n_old == 0:
            p_old_dec = Decimal(str(total_old)) / Decimal(str(n_old))
            
            # Chọn năng suất trung bình toàn bộ nhà máy p_total nguyên, lớn hơn p_old_dec
            p_total = int(p_old_dec) + random.randint(1, 3)
            total_all = n_total * p_total
            total_new = total_all - total_old
            
            # Kiểm tra năng suất trung bình công nhân mới nguyên và hợp lý
            if total_new > 0 and total_new % n_new == 0:
                p_new = total_new // n_new
                
                # Chọn mức tăng năng suất delta_A của công nhân phân xưởng A sao cho n_A * delta_A chia hết cho n_total
                valid_deltas = [d for d in range(2, 7) if (n_A * d) % n_total == 0]
                if valid_deltas and 50 <= p_new <= 65:
                    delta_A = random.choice(valid_deltas)
                    p_all_after = p_total + (n_A * delta_A) // n_total
                    break
    
    p_old_str = format_dec(p_old_dec)
    
    # Tạo dữ liệu nhiễu
    wrong_total_old = total_old + random.choice([-100, 100])
    wrong_p_old_dec = Decimal(str(p_A + p_B)) / Decimal('2')
    if wrong_p_old_dec == p_old_dec:
        wrong_p_old_dec = p_old_dec + Decimal('0.5')
    wrong_p_old_str = format_dec(wrong_p_old_dec)
    wrong_p_new = p_new + random.choice([-2, 2])
    wrong_p_all_after = p_total + delta_A
    
    # Nội dung câu hỏi
    noidungcauhoi = ('''Một nhà máy có hai phân xưởng A và B cùng sản xuất một loại linh kiện. \\\\
    $\\bullet$ Phân xưởng A có $%s$ công nhân, năng suất trung bình là $%s$ sản phẩm/ngày. \\\\
    $\\bullet$ Phân xưởng B có $%s$ công nhân, năng suất trung bình là $%s$ sản phẩm/ngày. \\\\
    Sau đó, nhà máy tuyển thêm $%s$ công nhân mới vào làm việc chung để nâng năng suất trung bình của toàn bộ $%s$ công nhân lên mức $%s$ sản phẩm/ngày.''' % (n_A, p_A, n_B, p_B, n_new, n_total, p_total))
    
    ######################################################################## Nhận biết ############################################
    
    # Các đáp án
    nb_da_1_d = '\\True Tổng số sản phẩm làm ra trong một ngày của phân xưởng A và phân xưởng B là $%s$ sản phẩm' % (total_old)
    nb_da_1_s = 'Tổng số sản phẩm làm ra trong một ngày của phân xưởng A và phân xưởng B là $%s$ sản phẩm' % (wrong_total_old)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_nb_1 = [nb_da_1]
    
    # Nội dung lời giải
    prod_A = n_A * p_A
    prod_B = n_B * p_B
    loigiai_nb_1 = ('''Số sản phẩm phân xưởng A làm ra trong một ngày là: $%s \\cdot %s = %s$ (sản phẩm). \\\\ Số sản phẩm phân xưởng B làm ra trong một ngày là: $%s \\cdot %s = %s$ (sản phẩm). \\\\ Tổng số sản phẩm làm ra trong một ngày của cả hai phân xưởng là: $%s + %s = %s$ (sản phẩm).''' % (n_A, p_A, prod_A, n_B, p_B, prod_B, prod_A, prod_B, total_old))
    
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
    th_da_1_d = '\\True Năng suất trung bình của $%s$ công nhân cũ (gồm cả hai phân xưởng A và B) là $%s$ sản phẩm/ngày' % (n_old, p_old_str)
    th_da_1_s = 'Năng suất trung bình của $%s$ công nhân cũ (gồm cả hai phân xưởng A và B) là $%s$ sản phẩm/ngày' % (n_old, wrong_p_old_str)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_th_1 = [th_da_1]
    
    # Nội dung lời giải
    loigiai_th_1 = ('''Năng suất trung bình của $%s$ công nhân cũ là: $\\overline{x}_{\\text{cũ}} = \\dfrac{%s}{%s} = %s$ (sản phẩm/ngày).''' % (n_old, total_old, n_old, p_old_str))
    
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
    vd_da_1_d = '\\True Năng suất trung bình của $%s$ công nhân mới tuyển là $%s$ sản phẩm/ngày' % (n_new, p_new)
    vd_da_1_s = 'Năng suất trung bình của $%s$ công nhân mới tuyển là $%s$ sản phẩm/ngày' % (n_new, wrong_p_new)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vd_1 = [vd_da_1]
    
    # Nội dung lời giải
    loigiai_vd_1 = ('''Tổng số sản phẩm của toàn bộ $%s$ công nhân làm ra trong một ngày là: $%s \\cdot %s = %s$ (sản phẩm). \\\\ Tổng số sản phẩm của $%s$ công nhân mới tuyển làm ra trong một ngày là: $%s - %s = %s$ (sản phẩm). \\\\ Năng suất trung bình của $%s$ công nhân mới tuyển là: $\\overline{x}_{\\text{mới}} = \\dfrac{%s}{%s} = %s$ (sản phẩm/ngày).''' % (n_total, n_total, p_total, total_all, n_new, total_all, total_old, total_new, n_new, total_new, n_new, p_new))
    
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
    vdc_da_1_d = '\\True Nếu mỗi công nhân cũ của phân xưởng A tăng năng suất thêm $%s$ sản phẩm/ngày (giữ nguyên năng suất của phân xưởng B và $%s$ công nhân mới), thì năng suất trung bình của toàn nhà máy đạt $%s$ sản phẩm/ngày' % (delta_A, n_new, p_all_after)
    vdc_da_1_s = 'Nếu mỗi công nhân cũ của phân xưởng A tăng năng suất thêm $%s$ sản phẩm/ngày (giữ nguyên năng suất của phân xưởng B và $%s$ công nhân mới), thì năng suất trung bình của toàn nhà máy đạt $%s$ sản phẩm/ngày' % (delta_A, n_new, wrong_p_all_after)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vdc_1 = [vdc_da_1]
    
    # Nội dung lời giải
    inc_prod = n_A * delta_A
    total_after = total_all + inc_prod
    loigiai_vdc_1 = ('''Khi mỗi công nhân của phân xưởng A tăng năng suất thêm $%s$ sản phẩm/ngày thì tổng số sản phẩm của toàn nhà máy trong một ngày tăng thêm là: $%s \\cdot %s = %s$ (sản phẩm). \\\\ Tổng số sản phẩm mới của toàn nhà máy là: $%s + %s = %s$ (sản phẩm). \\\\ Vậy năng suất trung bình mới của toàn nhà máy là: $\\overline{x} = \\dfrac{%s}{%s} = %s$ (sản phẩm/ngày).''' % (delta_A, n_A, delta_A, inc_prod, total_all, inc_prod, total_after, total_after, n_total, p_all_after))
    
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