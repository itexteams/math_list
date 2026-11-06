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


def bt_dang49_p2_b2_c4_ds12(self):
            # Khai báo biến
            # Hàm chuyển đổi số thập phân sang định dạng có dấu phẩy
            def to_dec(val):
                return "{:.2f}".format(float(val)).replace('.', ',')

            # Khai báo biến (Random số bi xanh và đỏ)
            x_bi = random.randint(4, 7) # Số bi xanh
            y_bi = random.randint(5, 8) # Số bi đỏ
            N = x_bi + y_bi

            # Tính toán các xác suất trước để truyền vào chuỗi
            # a) Nhận biết
            P_A = Rational(x_bi, N)
            val_a = to_dec(P_A)
            val_a_s = to_dec(Rational(y_bi, N))
            if val_a_s == val_a:
                val_a_s = to_dec(P_A + Rational(1, 10))

            # b) Thông hiểu
            tu_b = math.comb(x_bi, 2)
            mau_b = math.comb(N-1, 2)
            P_B1_g_Abar = Rational(tu_b, mau_b)
            val_b = to_dec(P_B1_g_Abar)

            P_B1_g_A = Rational(math.comb(x_bi-1, 2), mau_b)
            val_b_s = to_dec(P_B1_g_A)
            if val_b_s == val_b:
                val_b_s = to_dec(P_B1_g_Abar + Rational(1, 10))

            # c) Vận dụng
            P_Abar = Rational(y_bi, N)
            P_B2_g_Abar = Rational(math.comb(x_bi, 1) * math.comb(y_bi-1, 1), math.comb(N-1, 2))
            P_c = P_Abar * P_B2_g_Abar
            val_c = to_dec(P_c)
            val_c_s = to_dec(P_c + Rational(5, 100))

            # d) Vận dụng cao
            P_B3_g_A = 1 - P_B1_g_A
            P_B3_g_Abar = 1 - P_B1_g_Abar
            P_B3 = P_A * P_B3_g_A + P_Abar * P_B3_g_Abar
            P_d = (P_Abar * P_B3_g_Abar) / P_B3
            val_d = to_dec(P_d)
            val_d_s = to_dec(1 - P_d)
            if val_d_s == val_d:
                val_d_s = to_dec(P_d + Rational(1, 10))

            # Nội dung câu hỏi
            noidungcauhoi = ('''Một hộp có chứa $%s$ viên bi màu xanh và $%s$ viên bi màu đỏ (các viên bi có cùng kích thước và khối lượng, được đánh số khác nhau). Bạn An lấy ngẫu nhiên 1 viên bi từ trong hộp và không hoàn lại, Sau đó bạn Bình lấy ngẫu nhiên 2 viên bi từ trong hộp (Các kết quả tính được ở các ý đều làm tròn đến hàng phần trăm).''' % (x_bi, y_bi))

            ######################################################################## Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True Xác suất để bạn An lấy được 1 viên bi màu xanh là $%s$' % val_a
            nb_da_1_s = 'Xác suất để bạn An lấy được 1 viên bi màu xanh là $%s$' % val_a_s
            list_nb_da_1=[nb_da_1_d,nb_da_1_s]
            nb_da_1=random.choice(list_nb_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('''Gọi $A$ là biến cố: "Bạn An lấy được 1 viên bi màu xanh". \\\\
            Gọi $B_1$ là biến cố: "Bạn Bình lấy được 2 viên xanh". \\\\
            Gọi $B_2$ là biến cố: "Bạn Bình lấy được 1 viên xanh và 1 viên bi đỏ". \\\\
            Gọi $B_3$ là biến cố: "Bạn Bình lấy được ít nhất một viên bi màu đỏ". \\\\
            Xác suất để bạn An lấy được 1 viên bi màu xanh là: $P(A) = \\frac{C_{%s}^1}{C_{%s}^1} = %s \\approx %s$.''' % (x_bi, N, latex(P_A), val_a))

            # Đưa các lời giải vào danh sách lời giải
            list_nb_2 = [loigiai_nb_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_nb = list(zip(list_nb_1, list_nb_2))
            random.shuffle(combined_nb)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ######################################################################## Thông hiểu ############################################
            # Các đáp án
            th_da_1_d = '\\True Xác suất để bạn Bình lấy được 2 viên bi màu xanh, biết rằng bạn An đã lấy được 1 viên bi màu đỏ là $%s$' % val_b
            th_da_1_s = 'Xác suất để bạn Bình lấy được 2 viên bi màu xanh, biết rằng bạn An đã lấy được 1 viên bi màu đỏ là $%s$' % val_b_s
            list_th_da_1=[th_da_1_d,th_da_1_s]
            th_da_1=random.choice(list_th_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('''Vì An đã lấy 1 viên đỏ ($\\overline{A}$ đã xảy ra), trong hộp còn lại: $%s$ xanh, $%s$ đỏ (tổng $%s$ viên). \\\\
            Xác suất Bình lấy 2 xanh từ $%s$ viên còn lại là: $P(B_1 | \\overline{A}) = \\frac{C_{%s}^2}{C_{%s}^2} = %s \\approx %s$.''' % (x_bi, y_bi - 1, N - 1, N - 1, x_bi, N - 1, latex(P_B1_g_Abar), val_b))

            # Đưa các lời giải vào danh sách lời giải
            list_th_2 = [loigiai_th_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_th = list(zip(list_th_1, list_th_2))
            random.shuffle(combined_th)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## Vận dụng ############################################
            # Các đáp án
            vd_da_1_d = '\\True Xác suất để bạn An lấy được 1 viên bi màu đỏ và bạn Bình lấy được 1 viên bi màu xanh và 1 viên bi màu đỏ là $%s$' % val_c
            vd_da_1_s = 'Xác suất để bạn An lấy được 1 viên bi màu đỏ và bạn Bình lấy được 1 viên bi màu xanh và 1 viên bi màu đỏ là $%s$' % val_c_s
            list_vd_da_1=[vd_da_1_d,vd_da_1_s]
            vd_da_1=random.choice(list_vd_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('''Ta có: $P(\\overline{A}) = 1 - P(A) = %s$. \\\\
            Sau khi An lấy 1 viên bi đỏ, hộp còn $%s$ viên bi xanh và $%s$ viên bi đỏ. \\\\
            Khi đó: $P(B_2 | \\overline{A}) = \\frac{C_{%s}^1 \\cdot C_{%s}^1}{C_{%s}^2} = %s$. \\\\
            Vậy: $P(\\overline{A} \\cap B_2) = %s \\cdot %s = %s \\approx %s$.''' % (latex(P_Abar), x_bi, y_bi - 1, x_bi, y_bi - 1, N - 1, latex(P_B2_g_Abar), latex(P_Abar), latex(P_B2_g_Abar), latex(P_c), val_c))

            # Đưa các lời giải vào danh sách lời giải
            list_vd_2 = [loigiai_vd_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vd = list(zip(list_vd_1, list_vd_2))
            random.shuffle(combined_vd)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## Vận dụng cao ############################################
            # Các đáp án
            vdc_da_1_d = '\\True Biết rằng bạn Bình lấy được ít nhất một viên bi màu đỏ, xác suất bạn An lấy được một viên bi màu đỏ là $%s$' % val_d
            vdc_da_1_s = 'Biết rằng bạn Bình lấy được ít nhất một viên bi màu đỏ, xác suất bạn An lấy được một viên bi màu đỏ là $%s$' % val_d_s
            list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
            vdc_da_1=random.choice(list_vdc_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = ('''Ta có: $P(B_3 | A) = 1 - P(B_1 | A) = 1 - \\frac{C_{%s}^2}{C_{%s}^2} = %s$. \\\\
            $P(B_3 | \\overline{A}) = 1 - P(B_1 | \\overline{A}) = 1 - \\frac{C_{%s}^2}{C_{%s}^2} = %s$. \\\\
            $\\Rightarrow P(B_3) = P(A) \\cdot P(B_3 | A) + P(\\overline{A}) \\cdot P(B_3 | \\overline{A}) = %s \\cdot %s + %s \\cdot %s = %s$. \\\\
            Vậy $P(\\overline{A} | B_3) = \\frac{P(\\overline{A} \\cap B_3)}{P(B_3)} = \\frac{P(\\overline{A}) \\cdot P(B_3 | \\overline{A})}{P(B_3)} = \\frac{%s \\cdot %s}{%s} = %s \\approx %s$.''' % (
                x_bi - 1, N - 1, latex(P_B3_g_A),
                x_bi, N - 1, latex(P_B3_g_Abar),
                latex(P_A), latex(P_B3_g_A), latex(P_Abar), latex(P_B3_g_Abar), latex(P_B3),
                latex(P_Abar), latex(P_B3_g_Abar), latex(P_B3), latex(P_d), val_d
            ))

            # Đưa các lời giải vào danh sách lời giải
            list_vdc_2 = [loigiai_vdc_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
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
                       '\\begin{ex}\n'+
                       str(noidungcauhoi)+ '\n'+
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
                       '\\end{ex}\n\\end{minipage} \n\n')
            return content

