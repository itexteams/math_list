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


def bt_dang50_p2_b2_c4_ds12(self):
            # Khai báo biến
            # Hàm hỗ trợ định dạng số thập phân sử dụng dấu phẩy
            def format_dec(val):
                f_val = float(val)
                s = f"{f_val:.4f}".rstrip('0').rstrip('.')
                if s == '': s = '0'
                return s.replace('.', ',')

            # Khai báo biến
            # Lặp để tránh trường hợp xác suất 2 máy bằng nhau gây nhập nhằng cho câu d
            while True:
                q1 = random.randint(2, 6)
                q2 = random.randint(2, 6)
                n1 = random.choice([60, 80, 100, 120])
                n2 = random.choice([60, 80, 100, 120])
                if q1 != q2 and (q1 * n1) != (q2 * n2):
                    break

            N = n1 + n2

            p1_val = Rational(q1, 100)
            p2_val = Rational(q2, 100)

            # Xác suất sản phẩm tốt và phế phẩm
            p_B = Rational(n1, N) * (1 - p1_val) + Rational(n2, N) * (1 - p2_val)
            p_not_B = 1 - p_B

            # Xác suất điều kiện theo máy
            P_K1_given_not_B = (Rational(n1, N) * p1_val) / p_not_B
            P_K2_given_not_B = (Rational(n2, N) * p2_val) / p_not_B

            # Chuỗi định dạng cho đề bài
            str_p1 = f"0,0{q1}"
            str_p2 = f"0,0{q2}"
            str_p_not_k1 = format_dec(1 - q1/100)
            str_p_not_k2 = format_dec(1 - q2/100)

            # Nội dung câu hỏi
            noidungcauhoi = ('''Một loại sản phẩm do hai nhà máy số I, số II cùng sản xuất. Tỷ lệ phế phẩm của các nhà máy I, II lần lượt là $%s$ ; $%s$. Trong một lô sản phẩm để lẫn lộn $%s$ sản phẩm của nhà máy số I và $%s$ sản phẩm nhà máy số II. Một khách hàng lấy ngẫu nhiên 1 sản phẩm từ lô hàng đó.'''                  
                             %(str_p1, str_p2, n1, n2))

            ########################################################################
            # Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True Số phần tử của không gian mẫu là $%s$' %(N)
            nb_da_1_s = 'Số phần tử của không gian mẫu là $%s$' %(N + random.choice([10, 20, 30, 40]))
            list_nb_da_1=[nb_da_1_d,nb_da_1_s]
            nb_da_1=random.choice(list_nb_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('''Số phần tử của không gian mẫu là $n(\\Omega) = %s$.''' %(N))

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
            th_da_1_d = '\\True Xác suất để lấy được sản phẩm tốt là $\\frac{%s}{%s}$' %(p_B.p, p_B.q)  
            th_da_1_s = 'Xác suất để lấy được sản phẩm tốt là $\\frac{%s}{%s}$' %(p_B.p - random.choice([1, 2, 3]), p_B.q)   
            list_th_da_1=[th_da_1_d,th_da_1_s]
            th_da_1=random.choice(list_th_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('''Gọi $K_1$ là biến cố lấy được phế phẩm của nhà máy I.\\\\
            Gọi $K_2$ là biến cố lấy được phế phẩm của nhà máy II.\\\\
            Gọi $B$ là biến cố lấy được sản phẩm tốt: $P(K_1) = %s \\Rightarrow P(\\overline{K_1}) = %s$.\\\\
            $P(K_2) = %s \\Rightarrow P(\\overline{K_2}) = %s$.\\\\
            Xác suất để lấy được sản phẩm tốt là $P(B) = \\frac{C_{%s}^1}{C_{%s}^1} \\cdot %s + \\frac{C_{%s}^1}{C_{%s}^1} \\cdot %s = \\frac{%s}{%s} = %s$.'''       
                       %(str_p1, str_p_not_k1, str_p2, str_p_not_k2, n1, N, str_p_not_k1, n2, N, str_p_not_k2, p_B.p, p_B.q, format_dec(p_B)))

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
            vd_da_1_d = '\\True Xác suất để lấy được sản phẩm không tốt ở máy I là $\\frac{%s}{%s}$' %(P_K1_given_not_B.p, P_K1_given_not_B.q)  
            vd_da_1_s = 'Xác suất để lấy được sản phẩm không tốt ở máy I là $\\frac{%s}{%s}$' %(P_K1_given_not_B.p, P_K1_given_not_B.q + random.choice([1, 2]))  
            list_vd_da_1=[vd_da_1_d,vd_da_1_s]
            vd_da_1=random.choice(list_vd_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('''Xác suất để lấy được sản phẩm không tốt là $P(\\overline{B}) = 1 - \\frac{%s}{%s} = \\frac{%s}{%s} = %s$.\\\\
            Xác suất để lấy được sản phẩm không tốt ở máy I là \\\\
            $\\Rightarrow P(K_1 | \\overline{B}) = \\frac{P(K_1) P(\\overline{B}|K_1)}{P(\\overline{B})} = \\frac{C_{%s}^1 \\cdot %s}{C_{%s}^1 \\cdot %s} = %s \\approx %s$.'''  
                       %(p_B.p, p_B.q, p_not_B.p, p_not_B.q, format_dec(p_not_B), n1, str_p1, N, format_dec(p_not_B), latex(P_K1_given_not_B), format_dec(round(float(P_K1_given_not_B), 2))))

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
            # Tính toán để sinh mệnh đề logic động
            if P_K2_given_not_B < P_K1_given_not_B:
                vdc_da_1_d = '\\True Khả năng lấy được sản phẩm không tốt của máy II là thấp hơn máy I'
                vdc_da_1_s = 'Khả năng lấy được sản phẩm không tốt của máy II là cao hơn máy I'
                sosanh = 'thấp hơn'
            else:
                vdc_da_1_d = '\\True Khả năng lấy được sản phẩm không tốt của máy II là cao hơn máy I'
                vdc_da_1_s = 'Khả năng lấy được sản phẩm không tốt của máy II là thấp hơn máy I'
                sosanh = 'cao hơn'

            # Các đáp án
            list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
            vdc_da_1=random.choice(list_vdc_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = ('''Xác suất để lấy được sản phẩm không tốt ở máy II là \\\\
            $\\Rightarrow P(K_2 | \\overline{B}) = \\frac{P(K_2) P(\\overline{B}|K_2)}{P(\\overline{B})} = \\frac{C_{%s}^1 \\cdot %s}{C_{%s}^1 \\cdot %s} = %s \\approx %s$.\\\\
            Vậy khả năng lấy được sản phẩm không tốt ở máy II %s máy I.'''
                       %(n2, str_p2, N, format_dec(p_not_B), latex(P_K2_given_not_B), format_dec(round(float(P_K2_given_not_B), 2)), sosanh))

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

