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


def bt_dang25_p2_b1_c4_ds12(self):
            # Khai báo biến
            def format_dec(val):
                """Hàm định dạng số thập phân làm tròn 2 chữ số, sử dụng dấu phẩy"""
                return f"{val:.2f}".replace('.', ',')

            # Khai báo biến
            x = symbols('x')

            # Vòng lặp sinh số liệu cho bài toán
            while True:
                # Random số lượng bi trong từng hộp
                r1, y1 = random.randint(3, 6), random.randint(3, 5)
                r2, y2 = random.randint(2, 4), random.randint(2, 4)
                r3, y3 = random.randint(2, 4), random.randint(2, 4)

                n1 = r1 + y1
                n2 = r2 + y2
                n3 = r3 + y3

                # Số tổ hợp mẫu
                c2_n2_1 = math.comb(n2 + 1, 2)
                c3_n3_2 = math.comb(n3 + 2, 3)

                # ================= Tính Toán =================
                # Mệnh đề A: Lấy 1 bi vàng từ hộp I
                p_A = Fraction(y1, n1)
                val_a = round(float(p_A), 2)

                # Mệnh đề B: 2 bi khác màu từ hộp II
                p_1R1Y_given_R = Fraction(math.comb(r2 + 1, 1) * math.comb(y2, 1), c2_n2_1)
                p_1R1Y_given_Y = Fraction(math.comb(r2, 1) * math.comb(y2 + 1, 1), c2_n2_1)
                p_B = Fraction(r1, n1) * p_1R1Y_given_R + Fraction(y1, n1) * p_1R1Y_given_Y
                val_b = round(float(p_B), 2)

                # Mệnh đề C: Cả 3 bi màu đỏ từ hộp III
                # Trường hợp 1: Nhận bi Đỏ từ hộp I
                p_2R_given_R = Fraction(math.comb(r2 + 1, 2), c2_n2_1)
                p_2Y_given_R = Fraction(math.comb(y2, 2), c2_n2_1)

                term_R_2R = p_2R_given_R * Fraction(math.comb(r3 + 2, 3), c3_n3_2)
                term_R_1R1Y = p_1R1Y_given_R * Fraction(math.comb(r3 + 1, 3), c3_n3_2)
                term_R_2Y = p_2Y_given_R * Fraction(math.comb(r3, 3), c3_n3_2)
                sum_R = term_R_2R + term_R_1R1Y + term_R_2Y

                # Trường hợp 2: Nhận bi Vàng từ hộp I
                p_2R_given_Y = Fraction(math.comb(r2, 2), c2_n2_1)
                p_2Y_given_Y = Fraction(math.comb(y2 + 1, 2), c2_n2_1)

                term_Y_2R = p_2R_given_Y * Fraction(math.comb(r3 + 2, 3), c3_n3_2)
                term_Y_1R1Y = p_1R1Y_given_Y * Fraction(math.comb(r3 + 1, 3), c3_n3_2)
                term_Y_2Y = p_2Y_given_Y * Fraction(math.comb(r3, 3), c3_n3_2)
                sum_Y = term_Y_2R + term_Y_1R1Y + term_Y_2Y

                p_C = Fraction(r1, n1) * sum_R + Fraction(y1, n1) * sum_Y

                if p_C == 0: 
                    continue
                val_c = round(float(p_C), 2)

                # Mệnh đề D: 3 bi đỏ vốn thuộc về 3 hộp khác nhau
                p_ZY = Fraction(r1, n1) * Fraction(r2, c2_n2_1) * Fraction(r3, c3_n3_2)
                p_D = p_ZY / p_C
                val_d = round(float(p_D), 2)

                break

            # Nội dung câu hỏi
            noidungcauhoi = ('''Có ba hộp đựng bi: Hộp I có %s bi đỏ và %s bi vàng, hộp II có %s bi đỏ và %s bi vàng, hộp III có %s bi đỏ và %s bi vàng. Lấy ngẫu nhiên một viên bi từ hộp I bỏ sang hộp II, rồi lấy ngẫu nhiên hai viên bi từ hộp II bỏ sang hộp III. Cuối cùng lấy ngẫu nhiên ba viên bi từ hộp III (Kết quả tính được ở các ý dưới đây đều làm tròn đến hàng phần trăm).'''
                             % (r1, y1, r2, y2, r3, y3))

            ######################################################################## Nhận biết ############################################
            nb_da_1_d = '\\True Xác suất để lấy được 1 bi vàng từ hộp I bằng $%s$' % format_dec(val_a)
            nb_da_1_s = 'Xác suất để lấy được 1 bi vàng từ hộp I bằng $%s$' % format_dec(val_a + random.choice([0.11, -0.05, 0.08]))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)
            list_nb_1 = [nb_da_1]

            loigiai_nb_1 = ('''Xác suất để lấy được một bi vàng từ hộp I bằng $\\frac{%s}{%s} \\approx %s$ nên mệnh đề này %s.'''
                            % (y1, n1, format_dec(val_a), "đúng" if "\\True" in nb_da_1 else "sai"))
            list_nb_2 = [loigiai_nb_1]

            combined_nb = list(zip(list_nb_1, list_nb_2))
            random.shuffle(combined_nb)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ######################################################################## Thông hiểu ############################################
            th_da_1_d = '\\True Xác suất để lấy được 2 bi khác màu từ hộp II bằng $%s$' % format_dec(val_b)
            th_da_1_s = 'Xác suất để lấy được 2 bi khác màu từ hộp II bằng $%s$' % format_dec(val_b + random.choice([-0.12, 0.15, 0.07]))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)
            list_th_1 = [th_da_1]

            # Sơ đồ cây TikZ - Đã được làm rộng ra và tối ưu hiển thị chữ
            tikz_tree = (
                "\\begin{center}\n"
                "\\begin{tikzpicture}[grow=right, sloped, level 1/.style={sibling distance=5cm, level distance=4.5cm}, level 2/.style={sibling distance=2.2cm, level distance=5.5cm}, every node/.style={scale=0.9}, line width=1pt]\n"
                "\\node {Hộp I (" + str(r1) + " đ - " + str(y1) + " v)}\n"
                "  child {node {Hộp II (" + str(r2) + " đ - " + str(y2+1) + " v)}\n"
                "    child {node[right] {Hộp III (2v)} edge from parent node[below] {$\\frac{" + str(math.comb(y2+1, 2)) + "}{" + str(c2_n2_1) + "}$}}\n"
                "    child {node[right] {Hộp III (1đ - 1v)} edge from parent node[fill=white, inner sep=2pt] {$\\frac{" + str(math.comb(r2, 1)*math.comb(y2+1, 1)) + "}{" + str(c2_n2_1) + "}$}}\n"
                "    child {node[right] {Hộp III (2đ)} edge from parent node[above] {$\\frac{" + str(math.comb(r2, 2)) + "}{" + str(c2_n2_1) + "}$}}\n"
                "    edge from parent node[below, pos=0.6] {$\\frac{" + str(y1) + "}{" + str(n1) + "}$}\n"
                "  }\n"
                "  child {node {Hộp II (" + str(r2+1) + " đ - " + str(y2) + " v)}\n"
                "    child {node[right] {Hộp III (2v)} edge from parent node[below] {$\\frac{" + str(math.comb(y2, 2)) + "}{" + str(c2_n2_1) + "}$}}\n"
                "    child {node[right] {Hộp III (1đ - 1v)} edge from parent node[fill=white, inner sep=2pt] {$\\frac{" + str(math.comb(r2+1, 1)*math.comb(y2, 1)) + "}{" + str(c2_n2_1) + "}$}}\n"
                "    child {node[right] {Hộp III (2đ)} edge from parent node[above] {$\\frac{" + str(math.comb(r2+1, 2)) + "}{" + str(c2_n2_1) + "}$}}\n"
                "    edge from parent node[above, pos=0.6] {$\\frac{" + str(r1) + "}{" + str(n1) + "}$}\n"
                "  };\n"
                "\\end{tikzpicture}\n"
                "\\end{center}\n"
            )

            loigiai_th_1 = ('''Ta có sơ đồ cây như hình bên dưới:\\\\ \n%s\n
            Gọi $X$ là biến cố lấy được hai bi khác màu từ hộp II thì khi đó ta có:\\\\ 
            $P(X) = \\frac{%s}{%s} \\cdot \\frac{%s}{%s} + \\frac{%s}{%s} \\cdot \\frac{%s}{%s} = \\frac{%s}{%s} \\approx %s$ nên mệnh đề này %s.'''
                % (tikz_tree, r1, n1, p_1R1Y_given_R.numerator, p_1R1Y_given_R.denominator, 
                   y1, n1, p_1R1Y_given_Y.numerator, p_1R1Y_given_Y.denominator, 
                   p_B.numerator, p_B.denominator, format_dec(val_b), "đúng" if "\\True" in th_da_1 else "sai"))
            list_th_2 = [loigiai_th_1]

            combined_th = list(zip(list_th_1, list_th_2))
            random.shuffle(combined_th)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## Vận dụng ############################################
            vd_da_1_d = '\\True Xác suất để lấy được cả 3 bi màu đỏ từ hộp III bằng $%s$' % format_dec(val_c)
            vd_da_1_s = 'Xác suất để lấy được cả 3 bi màu đỏ từ hộp III bằng $%s$' % format_dec(val_c + random.choice([0.02, 0.05, -0.01]))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)
            list_vd_1 = [vd_da_1]

            def term_str(prob_box2, r_box3):
                if math.comb(r_box3, 3) == 0: return ""
                return f"\\frac{{{prob_box2.numerator}}}{{{prob_box2.denominator}}} \\cdot \\frac{{C^3_{{{r_box3}}}}}{{C^3_{{{n3+2}}}}}"

            terms_R = []
            if math.comb(r3+2, 3) > 0: terms_R.append(term_str(p_2R_given_R, r3+2))
            if math.comb(r3+1, 3) > 0: terms_R.append(term_str(p_1R1Y_given_R, r3+1))
            if math.comb(r3, 3) > 0: terms_R.append(term_str(p_2Y_given_R, r3))

            terms_Y = []
            if math.comb(r3+2, 3) > 0: terms_Y.append(term_str(p_2R_given_Y, r3+2))
            if math.comb(r3+1, 3) > 0: terms_Y.append(term_str(p_1R1Y_given_Y, r3+1))
            if math.comb(r3, 3) > 0: terms_Y.append(term_str(p_2Y_given_Y, r3))

            inner_R = " + ".join(filter(None, terms_R))
            inner_Y = " + ".join(filter(None, terms_Y))

            loigiai_vd_1 = ('''Gọi $Y$ là biến cố lấy được cả ba bi đỏ từ hộp III, ta có:\\\\
            $P(Y) = \\frac{%s}{%s} \\left( %s \\right) + \\frac{%s}{%s} \\left( %s \\right) = \\frac{%s}{%s} \\approx %s$ nên mệnh đề này %s.'''
                % (r1, n1, inner_R, y1, n1, inner_Y, p_C.numerator, p_C.denominator, format_dec(val_c), "đúng" if "\\True" in vd_da_1 else "sai"))
            list_vd_2 = [loigiai_vd_1]

            combined_vd = list(zip(list_vd_1, list_vd_2))
            random.shuffle(combined_vd)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## Vận dụng cao ############################################
            vdc_da_1_d = '\\True Biết rằng 3 bi được lấy từ hộp III màu đỏ, xác suất để 3 bi đó vốn thuộc về 3 hộp khác nhau bằng $%s$' % format_dec(val_d)
            vdc_da_1_s = 'Biết rằng 3 bi được lấy từ hộp III màu đỏ, xác suất để 3 bi đó vốn thuộc về 3 hộp khác nhau bằng $%s$' % format_dec(val_d + random.choice([0.13, -0.08, 0.04]))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)
            list_vdc_1 = [vdc_da_1]

            loigiai_vdc_1 = ('''Gọi $Z$ là biến cố: "Lấy từ hộp III ba viên bi mà mỗi bi thuộc về mỗi hộp I, II, III trước đó".\\\\
            Ta có: $P(Z|Y) = \\frac{{P(ZY)}}{{P(Y)}} = \\frac{{\\frac{%s}{%s} \\cdot \\frac{{1 \\cdot %s}}{{C^2_{%s}}} \\cdot \\frac{{1 \\cdot 1 \\cdot %s}}{{C^3_{%s}}}}}{{ \\frac{%s}{%s} }} = \\frac{%s}{%s} \\approx %s$ nên mệnh đề này %s.'''
                % (r1, n1, r2, n2+1, r3, n3+2, p_C.numerator, p_C.denominator, p_D.numerator, p_D.denominator, format_dec(val_d), "đúng" if "\\True" in vdc_da_1 else "sai"))
            list_vdc_2 = [loigiai_vdc_1]

            combined_vdc = list(zip(list_vdc_1, list_vdc_2))
            random.shuffle(combined_vdc)
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Đảm bảo bài có từ 1 đến 3 câu đúng
            while True:
                nb_da_1 = random.choice(list_nb_da_1)
                th_da_1 = random.choice(list_th_da_1)
                vd_da_1 = random.choice(list_vd_da_1)
                vdc_da_1 = random.choice(list_vdc_da_1)

                answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                true_count = count_true_answers(answers)

                if 1 <= true_count <= 3:
                    break

            # Xuất câu hỏi với đáp án và lời giải
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+
                str(noidungcauhoi)+ '\n' +
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

