import google.generativeai as genai
from sympy.abc import x, y, z, t
import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QMessageBox
)
from pdf2image import convert_from_path
from math import degrees
import openpyxl
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font
from openpyxl.utils import get_column_letter
from sympy import simplify, collect
from itertools import combinations
import itertools
from PyQt5.QtCore import QSettings
import sys
import os
import platform
import subprocess
import hashlib
import time
from datetime import datetime, timedelta
# Bổ sung các widget và core cho Splash Screen
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QLabel, QLineEdit, 
    QPushButton, QComboBox, QCheckBox, QTextEdit, QVBoxLayout, 
    QHBoxLayout, QGridLayout, QMessageBox, QColorDialog,
    QSplashScreen, QProgressBar  # <-- BỔ SUNG 2 CÁI NÀY
)
from PyQt5.QtCore import Qt, QSettings, QThread, pyqtSignal  # <-- BỔ SUNG QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QTreeWidget, QTreeWidgetItem, QTextEdit, QLabel, 
    QSpacerItem, QSizePolicy, QStackedWidget, QPushButton, QCheckBox, QSpinBox,
    QScrollArea  # <-- Thêm mục này vào đây
)
from PyQt5.QtWidgets import QCheckBox
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt, QPropertyAnimation, pyqtProperty
from functools import wraps
import re
import uuid
import json, base64
from datetime import datetime
from nacl.signing import VerifyKey
from nacl.encoding import HexEncoder
from nacl.exceptions import BadSignatureError
### CÔNG CỤ
import sys
import numpy as np
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QDialog, 
    QVBoxLayout, QHBoxLayout, QTabWidget, QWidget, 
    QLabel, QSlider, QDoubleSpinBox, QGroupBox
)
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D  # Cần cho 3D


def bt_dang11_p2_b2_c2_ds11(self):
    # Khai báo biến
    P = randint(80, 110) * 10
    d_val = randint(4, 6) * 10
    
    u1 = P
    u2 = P - d_val
    u2_sai = u2 + randint(1, 3) * 10
    
    d_true = -d_val
    d_false = d_val
    
    k3 = 3
    price_k3 = P - k3 * d_val
    T3 = price_k3 - randint(1, 3) * 10
    
    half_P = P / 2
    if half_P.is_integer():
        half_P_str = str(int(half_P))
    else:
        half_P_str = str(half_P).replace('.', ',')
    
    val_n = (P - half_P) / d_val
    if val_n.is_integer():
        val_n_str = str(int(val_n))
    else:
        val_n_str = str(round(val_n, 2)).replace('.', ',')
    
    N_min = math.floor(val_n) + 1
    N_sai = N_min - randint(1, 2)
    
    # Nội dung câu hỏi
    noidungcauhoi = ('''Giá của một chiếc xe ô tô lúc mới mua là %s triệu đồng. Cứ sau mỗi năm sử dụng, giá của chiếc xe ô tô giảm %s triệu đồng. Gọi $u_1 = %s$ và $u_{n+1}$ là giá của chiếc ô tô sau $n$ năm sử dụng ($n \\ge 1$).'''
                     % (latex(P), latex(d_val), latex(P)))
    
    ########################################################################
    # Nhận biết ############################################
    # Các đáp án
    nb_da_1_d = '\\True Giá của chiếc ô tô sau $1$ năm sử dụng là $%s$ triệu đồng' % (latex(u2))
    nb_da_1_s = 'Giá của chiếc ô tô sau $1$ năm sử dụng là $%s$ triệu đồng' % (latex(u2_sai))
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_nb_1 = [nb_da_1]
    
    # Nội dung lời giải
    if '\\True' in nb_da_1:
        loigiai_nb_1 = ('''Giá của chiếc ô tô sau $1$ năm sử dụng là $u_2 = u_1 - %s = %s - %s = %s$ (triệu đồng).'''
                        % (latex(d_val), latex(P), latex(d_val), latex(u2)))
    else:
        loigiai_nb_1 = ('''Giá của chiếc ô tô sau $1$ năm sử dụng là $u_2 = u_1 - %s = %s - %s = %s \\ne %s$ (triệu đồng).'''
                        % (latex(d_val), latex(P), latex(d_val), latex(u2), latex(u2_sai)))
    
    # Đưa các lời giải vào danh sách lời giải
    list_nb_2 = [loigiai_nb_1]
    
    # Kết hợp các đáp án và lời giải vào cùng một danh sách
    combined_nb = list(zip(list_nb_1, list_nb_2))
    
    # Xáo trộn danh sách kết hợp
    random.shuffle(combined_nb)
    
    # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    
    ########################################################################
    # Thông hiểu ############################################
    # Các đáp án
    th_da_1_d = '\\True Dãy số $(u_n)$ là cấp số cộng với công sai $d = %s$' % (latex(d_true))
    th_da_1_s = 'Dãy số $(u_n)$ là cấp số cộng với công sai $d = %s$' % (latex(d_false))
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_th_1 = [th_da_1]
    
    # Nội dung lời giải
    if '\\True' in th_da_1:
        loigiai_th_1 = ('''Vì giá của chiếc ô tô mỗi năm giảm %s triệu đồng nên $u_{n+1} - u_n = -%s$, do đó dãy số $(u_n)$ là một cấp số cộng với công sai $d = -%s$.'''
                        % (latex(d_val), latex(d_val), latex(d_val)))
    else:
        loigiai_th_1 = ('''Vì giá của chiếc ô tô mỗi năm giảm %s triệu đồng nên $u_{n+1} - u_n = -%s$, do đó công sai của cấp số cộng là $d = -%s \\ne %s$.'''
                        % (latex(d_val), latex(d_val), latex(d_val), latex(d_false)))
    
    # Đưa các lời giải vào danh sách lời giải
    list_th_2 = [loigiai_th_1]
    
    # Kết hợp các đáp án và lời giải vào cùng một danh sách
    combined_th = list(zip(list_th_1, list_th_2))
    
    # Xáo trộn danh sách kết hợp
    random.shuffle(combined_th)
    
    # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ########################################################################
    # Vận dụng ############################################
    # Các đáp án
    vd_da_1_d = '\\True Giá của chiếc ô tô sau %s năm sử dụng lớn hơn %s triệu đồng' % (latex(k3), latex(T3))
    vd_da_1_s = 'Giá của chiếc ô tô sau %s năm sử dụng nhỏ hơn %s triệu đồng' % (latex(k3), latex(T3))
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vd_1 = [vd_da_1]
    
    # Nội dung lời giải
    if '\\True' in vd_da_1:
        loigiai_vd_1 = ('''Giá của chiếc ô tô sau %s năm sử dụng là $u_{%s} = u_1 - %s \\cdot %s = %s - %s = %s$ (triệu đồng). \\\\
Vì %s > %s nên giá của chiếc ô tô sau %s năm sử dụng lớn hơn %s triệu đồng.'''
                        % (latex(k3), latex(k3 + 1), latex(k3), latex(d_val), latex(P), latex(k3 * d_val), latex(price_k3),
                           latex(price_k3), latex(T3), latex(k3), latex(T3)))
    else:
        loigiai_vd_1 = ('''Giá của chiếc ô tô sau %s năm sử dụng là $u_{%s} = u_1 - %s \\cdot %s = %s - %s = %s$ (triệu đồng). \\\\
Vì %s > %s nên khẳng định giá của chiếc ô tô sau %s năm sử dụng nhỏ hơn %s triệu đồng là sai.'''
                        % (latex(k3), latex(k3 + 1), latex(k3), latex(d_val), latex(P), latex(k3 * d_val), latex(price_k3),
                           latex(price_k3), latex(T3), latex(k3), latex(T3)))
    
    # Đưa các lời giải vào danh sách lời giải
    list_vd_2 = [loigiai_vd_1]
    
    # Kết hợp các đáp án và lời giải vào cùng một danh sách
    combined_vd = list(zip(list_vd_1, list_vd_2))
    
    # Xáo trộn danh sách kết hợp
    random.shuffle(combined_vd)
    
    # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ########################################################################
    # Vận dụng cao ############################################
    # Các đáp án
    vdc_da_1_d = '\\True Sau ít nhất %s năm sử dụng thì giá của chiếc ô tô nhỏ hơn một nửa giá trị ban đầu của nó' % (latex(N_min))
    vdc_da_1_s = 'Sau ít nhất %s năm sử dụng thì giá của chiếc ô tô nhỏ hơn một nửa giá trị ban đầu của nó' % (latex(N_sai))
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vdc_1 = [vdc_da_1]
    
    # Nội dung lời giải
    if '\\True' in vdc_da_1:
        loigiai_vdc_1 = ('''Một nửa giá trị ban đầu của chiếc ô tô là $\\frac{%s}{2} = %s$ (triệu đồng). \\\\
Giá của chiếc ô tô sau $n$ năm sử dụng là $P_n = %s - %s n$ (triệu đồng). \\\\
Để giá của chiếc ô tô nhỏ hơn một nửa giá trị ban đầu, ta có: \\\\
$%s - %s n < %s \\Leftrightarrow %s n > %s - %s \\Leftrightarrow %s n > %s \\Leftrightarrow n > %s$. \\\\
Vì $n \\in \\mathbb{N}^*$ nên $n \\ge %s$. \\\\
Vậy sau ít nhất %s năm sử dụng thì giá của chiếc ô tô nhỏ hơn một nửa giá trị ban đầu của nó.'''
                        % (latex(P), half_P_str,
                           latex(P), latex(d_val),
                           latex(P), latex(d_val), half_P_str, latex(d_val), latex(P), half_P_str, latex(d_val), str(round(P - half_P, 2)).replace('.', ','), val_n_str,
                           latex(N_min), latex(N_min)))
    else:
        loigiai_vdc_1 = ('''Một nửa giá trị ban đầu của chiếc ô tô là $\\frac{%s}{2} = %s$ (triệu đồng). \\\\
Giá của chiếc ô tô sau $n$ năm sử dụng là $P_n = %s - %s n$ (triệu đồng). \\\\
Để giá của chiếc ô tô nhỏ hơn một nửa giá trị ban đầu, ta có: \\\\
$%s - %s n < %s \\Leftrightarrow %s n > %s - %s \\Leftrightarrow %s n > %s \\Leftrightarrow n > %s$. \\\\
Vì $n \\in \\mathbb{N}^*$ nên $n \\ge %s$, do đó số năm ít nhất phải là %s chứ không phải %s.'''
                        % (latex(P), half_P_str,
                           latex(P), latex(d_val),
                           latex(P), latex(d_val), half_P_str, latex(d_val), latex(P), half_P_str, latex(d_val), str(round(P - half_P, 2)).replace('.', ','), val_n_str,
                           latex(N_min), latex(N_min), latex(N_sai)))
    
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
    
    # Cập nhật lại lời giải tương ứng với mệnh đề được chốt
    if '\\True' in nb_da_1:
        loigiai_nb_1 = ('''Giá của chiếc ô tô sau $1$ năm sử dụng là $u_2 = u_1 - %s = %s - %s = %s$ (triệu đồng).'''
                        % (latex(d_val), latex(P), latex(d_val), latex(u2)))
    else:
        loigiai_nb_1 = ('''Giá của chiếc ô tô sau $1$ năm sử dụng là $u_2 = u_1 - %s = %s - %s = %s \\ne %s$ (triệu đồng).'''
                        % (latex(d_val), latex(P), latex(d_val), latex(u2), latex(u2_sai)))
                        
    if '\\True' in th_da_1:
        loigiai_th_1 = ('''Vì giá của chiếc ô tô mỗi năm giảm %s triệu đồng nên $u_{n+1} - u_n = -%s$, do đó dãy số $(u_n)$ là một cấp số cộng với công sai $d = -%s$.'''
                        % (latex(d_val), latex(d_val), latex(d_val)))
    else:
        loigiai_th_1 = ('''Vì giá của chiếc ô tô mỗi năm giảm %s triệu đồng nên $u_{n+1} - u_n = -%s$, do đó công sai của cấp số cộng là $d = -%s \\ne %s$.'''
                        % (latex(d_val), latex(d_val), latex(d_val), latex(d_false)))
                        
    if '\\True' in vd_da_1:
        loigiai_vd_1 = ('''Giá của chiếc ô tô sau %s năm sử dụng là $u_{%s} = u_1 - %s \\cdot %s = %s - %s = %s$ (triệu đồng). \\\\
Vì %s > %s nên giá của chiếc ô tô sau %s năm sử dụng lớn hơn %s triệu đồng.'''
                        % (latex(k3), latex(k3 + 1), latex(k3), latex(d_val), latex(P), latex(k3 * d_val), latex(price_k3),
                           latex(price_k3), latex(T3), latex(k3), latex(T3)))
    else:
        loigiai_vd_1 = ('''Giá của chiếc ô tô sau %s năm sử dụng là $u_{%s} = u_1 - %s \\cdot %s = %s - %s = %s$ (triệu đồng). \\\\
Vì %s > %s nên khẳng định giá của chiếc ô tô sau %s năm sử dụng nhỏ hơn %s triệu đồng là sai.'''
                        % (latex(k3), latex(k3 + 1), latex(k3), latex(d_val), latex(P), latex(k3 * d_val), latex(price_k3),
                           latex(price_k3), latex(T3), latex(k3), latex(T3)))
                        
    if '\\True' in vdc_da_1:
        loigiai_vdc_1 = ('''Một nửa giá trị ban đầu của chiếc ô tô là $\\frac{%s}{2} = %s$ (triệu đồng). \\\\
Giá của chiếc ô tô sau $n$ năm sử dụng là $P_n = %s - %s n$ (triệu đồng). \\\\
Để giá của chiếc ô tô nhỏ hơn một nửa giá trị ban đầu, ta có: \\\\
$%s - %s n < %s \\Leftrightarrow %s n > %s - %s \\Leftrightarrow %s n > %s \\Leftrightarrow n > %s$. \\\\
Vì $n \\in \\mathbb{N}^*$ nên $n \\ge %s$. \\\\
Vậy sau ít nhất %s năm sử dụng thì giá của chiếc ô tô nhỏ hơn một nửa giá trị ban đầu của nó.'''
                        % (latex(P), half_P_str,
                           latex(P), latex(d_val),
                           latex(P), latex(d_val), half_P_str, latex(d_val), latex(P), half_P_str, latex(d_val), str(round(P - half_P, 2)).replace('.', ','), val_n_str,
                           latex(N_min), latex(N_min)))
    else:
        loigiai_vdc_1 = ('''Một nửa giá trị ban đầu của chiếc ô tô là $\\frac{%s}{2} = %s$ (triệu đồng). \\\\
Giá của chiếc ô tô sau $n$ năm sử dụng là $P_n = %s - %s n$ (triệu đồng). \\\\
Để giá của chiếc ô tô nhỏ hơn một nửa giá trị ban đầu, ta có: \\\\
$%s - %s n < %s \\Leftrightarrow %s n > %s - %s \\Leftrightarrow %s n > %s \\Leftrightarrow n > %s$. \\\\
Vì $n \\in \\mathbb{N}^*$ nên $n \\ge %s$, do đó số năm ít nhất phải là %s chứ không phải %s.'''
                        % (latex(P), half_P_str,
                           latex(P), latex(d_val),
                           latex(P), latex(d_val), half_P_str, latex(d_val), latex(P), half_P_str, latex(d_val), str(round(P - half_P, 2)).replace('.', ','), val_n_str,
                           latex(N_min), latex(N_min), latex(N_sai)))
    
    # Gán lại vào list
    list_nb_1 = [nb_da_1]
    list_th_1 = [th_da_1]
    list_vd_1 = [vd_da_1]
    list_vdc_1 = [vdc_da_1]
    
    list_nb_2 = [loigiai_nb_1]
    list_th_2 = [loigiai_th_1]
    list_vd_2 = [loigiai_vd_1]
    list_vdc_2 = [loigiai_vdc_1]
    
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
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\n\\choiceTFn \n'
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