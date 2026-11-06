import sys
from PyQt5.QtWidgets import QApplication, QColorDialog, QMainWindow, QSplitter, QTreeWidget, QSpacerItem, QSizePolicy, QTreeWidgetItem, QCheckBox, QFileDialog, QVBoxLayout, QTextEdit, QPushButton, QWidget, QLabel, QLineEdit, QDialog, QAction, QMessageBox, QScrollBar, QHeaderView, QMenu, QGridLayout
from sympy import *
from sympy.abc import x
import sympy as sp
from sympy import symbols,sqrt,evaluate,Subs,latex, Rational, expand, simplify, integrate
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
from sympy import symbols, Eq, solve
import numpy as np
from PyQt5.QtGui import QIcon
from math import factorial
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTextDocument
from subprocess import run, CalledProcessError
import shutil
from PyQt5.QtWidgets import QProgressBar
from docx import Document
from PyQt5 import QtGui
import re
import pandas as pd
from PyQt5.QtGui import QPixmap
import subprocess
import platform
import json
from decimal import Decimal, ROUND_HALF_UP
from PyQt5.QtWidgets import QComboBox, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QSpinBox, QTreeWidget, QTreeWidgetItem, QCheckBox, QTextEdit, QPushButton, QHBoxLayout
from random import randint, choice, shuffle
from sympy import latex
from fractions import Fraction
from collections import Counter
from random import sample
import shutil
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
import qrcode
import json
import glob
import os
import platform
import subprocess
import hashlib
import base64
from datetime import datetime, timedelta
from PyQt5.QtWidgets import (QApplication, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox)
from sympy import symbols, solve, Lt
#from PyQt5.QtWebEngineWidgets import QWebEngineView
#from PyQt5.QtCore import QUrl
#from sympy import latex
import re
import pyperclip
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

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


def bt_dang26_p2_b1_c4_ds12(self):

            # Khai báo biến
            # --- CÁC HÀM HỖ TRỢ XỬ LÝ ĐỊNH DẠNG ---
            def tex_frac(f):
                if f.denominator == 1:
                    return str(f.numerator)
                return "\\frac{%s}{%s}" % (f.numerator, f.denominator)

            def dec_str(f):
                # Làm tròn đến 1 chữ số thập phân và đổi dấu chấm thành dấu phẩy
                val = round(float(f), 1)
                return str(val).replace('.', ',')

            def exact_dec_str(f):
                # In ra số thập phân chính xác (dùng cho các xác suất chẵn như 0.25, 0.5)
                s = str(float(f))
                if s.endswith('.0'):
                    s = s[:-2]
                return s.replace('.', ',')

            # --- KHAI BÁO BIẾN (RANDOM) ---
            N = 10
            n1 = random.randint(3, 5)
            n2 = random.randint(2, 4)
            n3 = N - n1 - n2

            # Tập các cặp xác suất đẹp để đảm bảo số liệu tính toán không bị lẻ tuần hoàn
            pool = [
                (frac(1, 4), 40), (frac(1, 2), 40), (frac(3, 4), 40),
                (frac(1, 5), 50), (frac(2, 5), 50), (frac(3, 5), 50),
                (frac(1, 2), 20), (frac(1, 4), 20)
            ]

            p1, S1 = random.choice(pool)
            p2, S2 = random.choice(pool)
            p3, S3 = random.choice(pool)

            t1, u1 = int(p1 * S1), int((1 - p1) * S1)
            t2, u2 = int(p2 * S2), int((1 - p2) * S2)
            t3, u3 = int(p3 * S3), int((1 - p3) * S3)

            p_t1, p_u1 = frac(t1, S1), frac(u1, S1)
            p_t2, p_u2 = frac(t2, S2), frac(u2, S2)
            p_t3, p_u3 = frac(t3, S3), frac(u3, S3)

            # Tính các trọng số xuất hiện
            P_T = n1 * p_t1 + n2 * p_t2 + n3 * p_t3
            P_U = n1 * p_u1 + n2 * p_u2 + n3 * p_u3

            # Tính xác suất chọn từ các nhóm
            P_A1 = n1 * p_t1 / P_T
            P_A2 = n2 * p_t2 / P_T
            P_A3 = n3 * p_t3 / P_T

            P_B1 = n1 * p_u1 / P_U
            P_B2 = n2 * p_u2 / P_U
            P_B3 = n3 * p_u3 / P_U

            # Biến cố C
            P_C_bar = P_A1 * P_B1 + P_A2 * P_B2 + P_A3 * P_B3
            P_C = 1 - P_C_bar

            # Kết quả các mệnh đề
            val_a = p_t3
            val_b = P_A2 * P_B1 / P_C
            val_c = (P_B3 * P_A1 + P_B3 * P_A2) / P_C
            val_d = (P_A1 * P_B2 + P_A1 * P_B3) / P_C

            # Định dạng các kết quả chuẩn (đúng)
            fval_a = dec_str(val_a)
            fval_b = dec_str(val_b)
            fval_c = dec_str(val_c)
            fval_d = dec_str(val_d)

            # Định dạng các kết quả nhiễu (sai) - Tịnh tiến 0,1 để làm đáp án gây nhiễu
            fval_a_s = dec_str(val_a + frac(1,10) if val_a < frac(9,10) else val_a - frac(1,10))
            fval_b_s = dec_str(val_b + frac(1,10) if val_b < frac(9,10) else val_b - frac(1,10))
            fval_c_s = dec_str(val_c + frac(1,10) if val_c < frac(9,10) else val_c - frac(1,10))
            fval_d_s = dec_str(val_d + frac(1,10) if val_d < frac(9,10) else val_d - frac(1,10))


            # Nội dung câu hỏi
            noidungcauhoi = ('''Để chuẩn bị cho lễ duyệt binh kỷ niệm Ngày Quốc khánh, một khối duyệt binh danh dự gồm %s sĩ quan được thành lập bằng cách tuyển chọn ngẫu nhiên từ ba sư đoàn. Chọn %s sĩ quan từ một danh sách gồm %s sĩ quan cấp úy và %s sĩ quan cấp tá từ sư đoàn I. Chọn %s sĩ quan từ một danh sách gồm %s sĩ quan cấp úy và %s sĩ quan cấp tá từ sư đoàn II. Chọn %s sĩ quan từ một danh sách gồm %s sĩ quan cấp úy và %s sĩ quan cấp tá từ sư đoàn III. Từ khối %s sĩ quan này, ban chỉ huy chọn ra hai vị trí quan trọng: một khối trưởng (được chọn ngẫu nhiên từ các sĩ quan cấp tá có trong khối) và một sĩ quan cầm cờ (được chọn ngẫu nhiên từ các sĩ quan cấp úy có trong khối). Biết rằng hai sĩ quan được chọn vào hai vị trí này thuộc hai đơn vị khác nhau (Kết quả làm tròn đến hàng phần chục).''' 
                             % (N, n1, u1, t1, n2, u2, t2, n3, u3, t3, N))

            ######################################################################## Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True Xác suất để chọn một sĩ quan bất kỳ từ sư đoàn III là sỹ quan cấp tá bằng $%s$' % fval_a
            nb_da_1_s = 'Xác suất để chọn một sĩ quan bất kỳ từ sư đoàn III là sỹ quan cấp tá bằng $%s$' % fval_a_s
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('''Xác suất để chọn một sĩ quan bất kỳ từ sư đoàn III là sỹ quan cấp tá: $P(T|III)=\\frac{%s}{%s}=%s$.''' 
                            % (t3, S3, exact_dec_str(p_t3)))

            list_nb_2 = [loigiai_nb_1]
            combined_nb = list(zip(list_nb_1, list_nb_2))
            random.shuffle(combined_nb)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ######################################################################## Thông hiểu ############################################
            # Các đáp án
            th_da_1_d = '\\True Xác suất để chọn được khối trưởng thuộc sư đoàn II và sĩ quan cầm cờ thuộc sư đoàn I là $%s$' % fval_b
            th_da_1_s = 'Xác suất để chọn được khối trưởng thuộc sư đoàn II và sĩ quan cầm cờ thuộc sư đoàn I là $%s$' % fval_b_s
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('''Xác suất khối trưởng sư đoàn II ($A_2$) và cầm cờ sư đoàn I ($B_1$) với điều kiện $C$ là: \\\\
            $P(A_2 \\cap B_1 | C) = \\frac{P(A_2)P(B_1)}{P(C)} = \\frac{%s \\cdot %s}{%s} = %s \\approx %s$.''' %
            (tex_frac(P_A2), tex_frac(P_B1), tex_frac(P_C), tex_frac(P_A2 * P_B1 / P_C), fval_b))

            list_th_2 = [loigiai_th_1]
            combined_th = list(zip(list_th_1, list_th_2))
            random.shuffle(combined_th)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## Vận dụng ############################################
            # Các đáp án
            vd_da_1_d = '\\True Xác suất để sĩ quan cầm cờ thuộc sư đoàn III là $%s$' % fval_c
            vd_da_1_s = 'Xác suất để sĩ quan cầm cờ thuộc sư đoàn III là $%s$' % fval_c_s
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('''Xác suất để sĩ quan cầm cờ thuộc sư đoàn III là: \\\\
            $P(B_3 | C) = \\frac{P(B_3 \\cap A_1) + P(B_3 \\cap A_2)}{P(C)} = \\frac{%s \\left( %s + %s \\right)}{%s} = %s \\approx %s$.''' %
            (tex_frac(P_B3), tex_frac(P_A1), tex_frac(P_A2), tex_frac(P_C), tex_frac((P_B3 * P_A1 + P_B3 * P_A2)/P_C), fval_c))

            list_vd_2 = [loigiai_vd_1]
            combined_vd = list(zip(list_vd_1, list_vd_2))
            random.shuffle(combined_vd)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## Vận dụng cao ############################################
            # Các đáp án
            vdc_da_1_d = '\\True Xác suất để khối trưởng là sĩ quan của sư đoàn I là $%s$' % fval_d
            vdc_da_1_s = 'Xác suất để khối trưởng là sĩ quan của sư đoàn I là $%s$' % fval_d_s
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = ('''Xác suất để khối trưởng là sĩ quan của sư đoàn I là: \\\\
            $P(A_1 | C) = \\frac{P(A_1 \\cap B_2) + P(A_1 \\cap B_3)}{P(C)} = \\frac{%s \\left( %s + %s \\right)}{%s} = %s \\approx %s$.''' %
            (tex_frac(P_A1), tex_frac(P_B2), tex_frac(P_B3), tex_frac(P_C), tex_frac((P_A1 * P_B2 + P_A1 * P_B3)/P_C), fval_d))

            list_vdc_2 = [loigiai_vdc_1]
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))
            random.shuffle(combined_vdc)
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

            # Gán lại vào list sau khi đạt tỷ lệ True/False hợp lý
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

            # Khung lập luận chung (được nhúng một lần vào đầu lời giải)
            common_sol = ('''Gọi $T$ là biến cố một sĩ quan được chọn từ mỗi sư đoàn là cấp tá và $U$ là biến cố một sĩ quan được chọn từ mỗi sư đoàn là cấp úy. \\\\
            Sư đoàn I (chọn %s người) nên $P(T|I)=\\frac{%s}{%s}=%s$ và $P(U|I)=\\frac{%s}{%s}=%s$. \\\\
            Sư đoàn II (chọn %s người) nên $P(T|II)=\\frac{%s}{%s}=%s$ và $P(U|II)=\\frac{%s}{%s}=%s$. \\\\
            Sư đoàn III (chọn %s người) nên $P(T|III)=\\frac{%s}{%s}=%s$ và $P(U|III)=\\frac{%s}{%s}=%s$. \\\\
            Trong khối %s người được chọn, ta tính trọng số xuất hiện của cấp tá và cấp úy: \\\\
            Tổng xác suất chọn 1 cấp tá (Khối trưởng): $P(T)=%s \\cdot %s + %s \\cdot %s + %s \\cdot %s = %s$. \\\\
            Tổng xác suất chọn 1 cấp úy (Cầm cờ): $P(U)=%s \\cdot %s + %s \\cdot %s + %s \\cdot %s = %s$. \\\\
            Gọi các biến cố liên quan đến việc chọn 2 vị trí (khối trưởng và cầm cờ) như sau: \\\\
            Nhóm biến cố về khối trưởng (Sĩ quan cấp tá): \\\\
            Biến cố $A_1$ là biến cố khối trưởng thuộc sư đoàn I nên $P(A_1)=\\frac{%s \\cdot %s}{%s}=%s$. \\\\
            Biến cố $A_2$ là biến cố khối trưởng thuộc sư đoàn II nên $P(A_2)=\\frac{%s \\cdot %s}{%s}=%s$. \\\\
            Biến cố $A_3$ là biến cố khối trưởng thuộc sư đoàn III nên $P(A_3)=\\frac{%s \\cdot %s}{%s}=%s$. \\\\
            Nhóm biến cố về sĩ quan cầm cờ (Sĩ quan cấp úy): \\\\
            Biến cố $B_1$ là biến cố sĩ quan cầm cờ thuộc sư đoàn I nên $P(B_1)=\\frac{%s \\cdot %s}{%s}=%s$. \\\\
            Biến cố $B_2$ là biến cố sĩ quan cầm cờ thuộc sư đoàn II nên $P(B_2)=\\frac{%s \\cdot %s}{%s}=%s$. \\\\
            Biến cố $B_3$ là biến cố sĩ quan cầm cờ thuộc sư đoàn III nên $P(B_3)=\\frac{%s \\cdot %s}{%s}=%s$. \\\\
            Biến cố điều kiện bổ trợ là biến cố $C$ "Hai sĩ quan được chọn thuộc hai đơn vị khác nhau." \\\\
            Tính xác suất biến cố $C$. Trước hết ta tính $P(\\overline{C})$ (hai sĩ quan cùng đơn vị). \\\\
            $P(\\overline{C})=P(A_1 \\cap B_1)+P(A_2 \\cap B_2)+P(A_3 \\cap B_3)=%s \\cdot %s + %s \\cdot %s + %s \\cdot %s = %s$. \\\\
            $\\Rightarrow P(C)=1-P(\\overline{C})=%s$.''' % (
                n1, t1, S1, exact_dec_str(p_t1), u1, S1, exact_dec_str(p_u1),
                n2, t2, S2, exact_dec_str(p_t2), u2, S2, exact_dec_str(p_u2),
                n3, t3, S3, exact_dec_str(p_t3), u3, S3, exact_dec_str(p_u3),
                N,
                n1, exact_dec_str(p_t1), n2, exact_dec_str(p_t2), n3, exact_dec_str(p_t3), exact_dec_str(P_T),
                n1, exact_dec_str(p_u1), n2, exact_dec_str(p_u2), n3, exact_dec_str(p_u3), exact_dec_str(P_U),

                n1, exact_dec_str(p_t1), exact_dec_str(P_T), tex_frac(P_A1),
                n2, exact_dec_str(p_t2), exact_dec_str(P_T), tex_frac(P_A2),
                n3, exact_dec_str(p_t3), exact_dec_str(P_T), tex_frac(P_A3),

                n1, exact_dec_str(p_u1), exact_dec_str(P_U), tex_frac(P_B1),
                n2, exact_dec_str(p_u2), exact_dec_str(P_U), tex_frac(P_B2),
                n3, exact_dec_str(p_u3), exact_dec_str(P_U), tex_frac(P_B3),

                tex_frac(P_A1), tex_frac(P_B1), tex_frac(P_A2), tex_frac(P_B2), tex_frac(P_A3), tex_frac(P_B3), tex_frac(P_C_bar),
                tex_frac(P_C)
            ))

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+
                str(noidungcauhoi)+ 
                '\n\\choiceTFn \n'
               '{'+str(shuffled_answers_nb[0])+'}\n'
               '{'+str(shuffled_answers_th[0])+'}\n'
               '{'+str(shuffled_answers_vd[0])+'}\n'
               '{'+str(shuffled_answers_vdc[0])+'}\n'
                '\\loigiai{ \n' +
                str(common_sol) + 
                '\\begin{enumEX}[a)]{1} \n'
                '\\item '+str(shuffled_solutions_nb[0])+'\n'
                '\\item '+str(shuffled_solutions_th[0])+'\n'
                '\\item '+str(shuffled_solutions_vd[0])+'\n'
                '\\item '+str(shuffled_solutions_vdc[0])+'\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

