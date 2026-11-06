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


def bt_dang2_p2_b3_c3_ds10(self):
            # Khai báo biến
            lisdang=['1','2']
            dang=random.choice(lisdang)

            if dang=='2':
                # Giá trị và tần số
                k1=randint(1,10)
                k2=randint(1,10)
                k3=randint(1,10)
                k4=randint(1,10)

                x1=randint(1,20)
                x2=x1+k1
                x3=x2+k2
                x4=x3+k3
                x5=x4+k4

                m1=randint(1,20)
                m2=randint(1,20)
                m3=randint(1,20)
                m4=randint(1,20)
                m5=randint(1,20)

                # Tính tổng tần số
                n = m1 + m2 + m3 + m4 + m5

                # Đảm bảo tổng n là lẻ
                if n % 2 == 0:
                    m1 += 1  # Điều chỉnh để n thành lẻ
                    n = m1 + m2 + m3 + m4 + m5  # Cập nhật n

                # Số TB
                h1=(m1*x1+m2*x2+m3*x3+m4*x4+m5*x5)/n
                xtb = Decimal(float(h1)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

                # Tính tần số tích lũy
                cumulative_frequencies = [m1, m1 + m2, m1 + m2 + m3, m1 + m2 + m3 + m4, n]

                # Tìm vị trí trung vị
                median_pos = (n + 1) // 2  # Vị trí trung vị trong danh sách tích lũy

                # Xác định giá trị tại vị trí trung vị
                median_value = None
                for i, cum_freq in enumerate(cumulative_frequencies):
                    if cum_freq >= median_pos:
                        median_value = [x1, x2, x3, x4, x5][i]
                        break

                # Tính trung vị
                median = median_value

                # Tính Q1 và Q3
                q1_pos = (n + 1) // 4  # Vị trí Q1
                q3_pos = 3 * (n + 1) // 4  # Vị trí Q3

                q1 = None
                q3 = None

                # Xác định giá trị Q1 và Q3 dựa trên tần số tích lũy
                for i, cum_freq in enumerate(cumulative_frequencies):
                    if q1 is None and cum_freq >= q1_pos:
                        q1 = [x1, x2, x3, x4, x5][i]
                    if q3 is None and cum_freq >= q3_pos:
                        q3 = [x1, x2, x3, x4, x5][i]

                # Tính Mốt (Mo)
                freq_list = [m1, m2, m3, m4, m5]
                mo = [x1, x2, x3, x4, x5][freq_list.index(max(freq_list))]

                # Phương sai
                phsai=Rational(m1*(x1-h1)**2+m2*(x2-h1)**2+m3*(x3-h1)**2+m4*(x4-h1)**2+m5*(x5-h1)**2,n)
                dlech=sqrt(phsai)

                s2=Decimal(float(phsai)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
                dl=Decimal(float(dlech)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

                # Nội dung câu hỏi
                noidungcauhoi = ('Cho bảng số liệu sau \n'
                                '''\\begin{center}
                                \\begin{tabular}{|c|c|c|c|c|c|}
                                    \\hline
                                    Giá trị & \\, $%s$ \\, & \\, $%s$ \\, & \\, $%s$ \\, & \\, $%s$ \\, & \\, $%s$ \\,  \\\\
                                    \\hline
                                    Tần số & $%s$ & $%s$ & $%s$ & $%s$ & $%s$ \\\\
                                    \\hline
                                \\end{tabular}
                                \\end{center}'''

                                %(latex(x1),latex(x2),latex(x3),latex(x4),latex(x5),
                                latex(m1),latex(m2),latex(m3),latex(m4),latex(m5),
                                ))

                ######################################################################## Nhận biết ############################################
                # Các đáp án
                nb_da_1_d = '\\True Khoảng biến thiên của dãy số liệu là $R=%s$' %(latex(x5-x1))
                nb_da_1_s = 'Khoảng biến thiên của dãy số liệu là $R=%s$' %(latex(x5-x1+1))
                list_nb_da_1=[nb_da_1_d,nb_da_1_s]
                nb_da_1=random.choice(list_nb_da_1)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_nb_1 = [nb_da_1]

                # Nội dung lời giải
                loigiai_nb_1 = ('Khoảng biến thiên của mẫu số liệu là $R=%s-%s=%s$$zz$'
                        %(latex(x5),latex(x1),latex(x5-x1)
                        ))

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
                th_da_1_d = '\\True Phương sai của dãy số liệu (làm tròn đến hàng phần trăm) là $s^2=%s$' %(latex(s2))
                th_da_1_s = 'Phương sai của dãy số liệu (làm tròn đến hàng phần trăm) là $s^2=%s$' %(latex(s2+1))
                list_th_da_1=[th_da_1_d,th_da_1_s]
                th_da_1=random.choice(list_th_da_1)


                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_th_1 = [th_da_1]

                # Nội dung lời giải
                loigiai_th_1 = loigiai=('Tổng tần số là $n=%s+%s+%s+%s+%s=%s$$zz$\\\\ \n'
                        'Số trung bình là $\\bar{x}=\\dfrac{%s \\cdot %s+%s \\cdot %s+%s \\cdot %s+%s \\cdot %s+%s \\cdot %s}{%s}=%s$$zz$ \\\\ \n'
                        'Phương sai của mẫu số liệu là \\\\ \n'
                        '$s^2=\\dfrac{%s\\left( %s-%s \\right)^2+%s\\left( %s-%s \\right)^2+%s\\left( %s-%s \\right)^2+%s\\left( %s-%s \\right)^2+%s\\left( %s-%s \\right)^2}{%s}$\\\\ \n'
                        '$=%s$$zz$'
                        %(latex(m1),latex(m2),latex(m3),latex(m4),latex(m5),latex(n),
                        latex(m1),latex(x1),latex(m2),latex(x2),latex(m3),latex(x3),latex(m4),latex(x4),latex(m5),latex(x5),latex(n),latex(xtb),
                        latex(m1),latex(x1),latex(xtb),latex(m2),latex(x2),latex(xtb),latex(m3),latex(x3),latex(xtb),latex(m4),latex(x4),latex(xtb),latex(m5),latex(x5),latex(xtb),latex(n),latex(s2)

                        ))


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
                vd_da_1_d = '\\True Độ lệch chuẩn của dãy số liệu (làm tròn đến hàng phần trăm) là $s=%s$' %(latex(dl))
                vd_da_1_s = 'Độ lệch chuẩn của dãy số liệu (làm tròn đến hàng phần trăm) là $s=%s$' %(latex(dl+1))
                list_vd_da_1=[vd_da_1_d,vd_da_1_s]
                vd_da_1=random.choice(list_vd_da_1)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_vd_1 = [vd_da_1]

                # Nội dung lời giải
                loigiai_vd_1 = (
                        'Số trung bình là $\\bar{x}=\\dfrac{%s \\cdot %s+%s \\cdot %s+%s \\cdot %s+%s \\cdot %s+%s \\cdot %s}{%s}=%s$$zz$ \\\\ \n'
                        'Phương sai của mẫu số liệu là \\\\ \n'
                        '$s^2=\\dfrac{%s\\left( %s-%s \\right)^2+%s\\left( %s-%s \\right)^2+%s\\left( %s-%s \\right)^2+%s\\left( %s-%s \\right)^2+%s\\left( %s-%s \\right)^2}{%s}$\\\\ \n'
                        '$=%s$$zz$ \\\\ \n'
                        'Độ lệch chuẩn của mẫu số liệu là \\\\ \n'
                        '$s=\\sqrt{%s}=%s$$zz$'
                        %(
                        latex(m1),latex(x1),latex(m2),latex(x2),latex(m3),latex(x3),latex(m4),latex(x4),latex(m5),latex(x5),latex(n),latex(xtb),
                        latex(m1),latex(x1),latex(xtb),latex(m2),latex(x2),latex(xtb),latex(m3),latex(x3),latex(xtb),latex(m4),latex(x4),latex(xtb),latex(m5),latex(x5),latex(xtb),latex(n),latex(s2),
                        latex(s2),latex(dl)
                        ))

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
                vdc_da_1_d = '\\True Khoảng tứ phân vị của dãy số liệu là $\\Delta_Q=%s$' %(latex(q3-q1))
                vdc_da_1_s = 'Khoảng tứ phân vị của dãy số liệu là $\\Delta_Q=%s$' %(latex(q3-q1-1))
                list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
                vdc_da_1=random.choice(list_vdc_da_1)


                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_vdc_1 = [vdc_da_1]

                # Nội dung lời giải
                loigiai_vdc_1 = (
                        'Gọi $x_1, x_2, ..., x_{%s}$ là dãy số liệu được xắp xếp theo thứ tự không giảm$zz$ \\\\ \n'
                        'Khi đó trung vị của mẫu số liệu là $M_e=x_{%s}=%s$$zz$ \\\\ \n'
                        'Tứ phân vị thứ nhất là $Q_1=%s$$zz$ \\\\ \n'
                        'Tứ phân vị thứ ba là $Q_3=%s$$zz$ \\\\ \n'
                        'Khoảng tứ phân vị là $\\Delta_Q=%s-%s=%s$$zz$'
                        %(
                        latex(n),
                        latex(Rational(n+1,2)),
                        latex(median),
                        latex(q1),
                        latex(q3),
                        latex(q3),latex(q1),latex(q3-q1)
                        ))

                # Đưa các lời giải vào danh sách lời giải
                list_vdc_2 = [loigiai_vdc_1]

                # Kết hợp các đáp án và lời giải vào cùng một danh sách
                combined_vdc = list(zip(list_vdc_1, list_vdc_2))

                # Xáo trộn danh sách kết hợp
                random.shuffle(combined_vdc)

                # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
                shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            if dang=='1':
                # Giá trị và tần số
                k1=randint(1,10)
                k2=randint(1,10)
                k3=randint(1,10)
                k4=randint(1,10)

                x1=randint(1,20)
                x2=x1+k1
                x3=x2+k2
                x4=x3+k3
                x5=x4+k4

                m1=randint(1,20)
                m2=randint(1,20)
                m3=randint(1,20)
                m4=randint(1,20)
                m5=randint(1,20)

                # Tính tổng tần số
                n = m1 + m2 + m3 + m4 + m5

                # Đảm bảo tổng n là chẵn
                if n % 2 != 0:
                    m1 += 1  # Điều chỉnh để n thành chẵn
                    n = m1 + m2 + m3 + m4 + m5  # Cập nhật n

                # Số TB
                h1=(m1*x1+m2*x2+m3*x3+m4*x4+m5*x5)/n
                xtb = Decimal(float(h1)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

                # Tính tần số tích lũy
                cumulative_frequencies = [m1, m1 + m2, m1 + m2 + m3, m1 + m2 + m3 + m4, n]

                # Tìm hai vị trí trung vị
                lower_mid_pos = n // 2       # Vị trí đầu tiên
                upper_mid_pos = lower_mid_pos + 1  # Vị trí thứ hai

                lower_mid_value = None
                upper_mid_value = None

                # Tìm giá trị tương ứng cho hai vị trí
                for i, cum_freq in enumerate(cumulative_frequencies):
                    if lower_mid_value is None and cum_freq >= lower_mid_pos:
                        lower_mid_value = [x1, x2, x3, x4, x5][i]
                    if upper_mid_value is None and cum_freq >= upper_mid_pos:
                        upper_mid_value = [x1, x2, x3, x4, x5][i]

                # Tính trung vị
                median = (lower_mid_value + upper_mid_value) / 2

                # Tính toán Q1 và Q3
                q1_pos = n // 4  # Vị trí Q1
                q3_pos = 3 * n // 4  # Vị trí Q3

                q1 = None
                q3 = None

                # Xác định giá trị Q1 và Q3 dựa trên tần số tích lũy
                for i, cum_freq in enumerate(cumulative_frequencies):
                    if q1 is None and cum_freq >= q1_pos:
                        q1 = [x1, x2, x3, x4, x5][i]
                    if q3 is None and cum_freq >= q3_pos:
                        q3 = [x1, x2, x3, x4, x5][i]

                # Tính Mốt (Mo)
                freq_list = [m1, m2, m3, m4, m5]
                mo = [x1, x2, x3, x4, x5][freq_list.index(max(freq_list))]

                # Phương sai
                phsai=Rational(m1*(x1-h1)**2+m2*(x2-h1)**2+m3*(x3-h1)**2+m4*(x4-h1)**2+m5*(x5-h1)**2,n)
                dlech=sqrt(phsai)

                s2=Decimal(float(phsai)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
                dl=Decimal(float(dlech)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

                # Nội dung câu hỏi
                noidungcauhoi = ('Cho bảng số liệu sau \n'
                                '''\\begin{center}
                                \\begin{tabular}{|c|c|c|c|c|c|}
                                    \\hline
                                    Giá trị & \\, $%s$ \\, & \\, $%s$ \\, & \\, $%s$ \\, & \\, $%s$ \\, & \\, $%s$ \\,  \\\\
                                    \\hline
                                    Tần số & $%s$ & $%s$ & $%s$ & $%s$ & $%s$ \\\\
                                    \\hline
                                \\end{tabular}
                                \\end{center}'''

                                %(latex(x1),latex(x2),latex(x3),latex(x4),latex(x5),
                                latex(m1),latex(m2),latex(m3),latex(m4),latex(m5),
                                ))

                ######################################################################## Nhận biết ############################################
                # Các đáp án
                nb_da_1_d = '\\True Khoảng biến thiên của dãy số liệu là $R=%s$' %(latex(x5-x1))
                nb_da_1_s = 'Khoảng biến thiên của dãy số liệu là $R=%s$' %(latex(x5-x1+1))
                list_nb_da_1=[nb_da_1_d,nb_da_1_s]
                nb_da_1=random.choice(list_nb_da_1)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_nb_1 = [nb_da_1]

                # Nội dung lời giải
                loigiai_nb_1 = ('Khoảng biến thiên của mẫu số liệu là $R=%s-%s=%s$$zz$'
                        %(latex(x5),latex(x1),latex(x5-x1)
                        ))

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
                th_da_1_d = '\\True Phương sai của dãy số liệu (làm tròn đến hàng phần trăm) là $s^2=%s$' %(latex(s2))
                th_da_1_s = 'Phương sai của dãy số liệu (làm tròn đến hàng phần trăm) là $s^2=%s$' %(latex(s2+1))
                list_th_da_1=[th_da_1_d,th_da_1_s]
                th_da_1=random.choice(list_th_da_1)


                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_th_1 = [th_da_1]

                # Nội dung lời giải
                loigiai_th_1 = ('Tổng tần số là $n=%s+%s+%s+%s+%s=%s$$zz$\\\\ \n'
                        'Số trung bình là $\\bar{x}=\\dfrac{%s \\cdot %s+%s \\cdot %s+%s \\cdot %s+%s \\cdot %s+%s \\cdot %s}{%s}=%s$$zz$ \\\\ \n'
                        'Phương sai của mẫu số liệu là \\\\ \n'
                        '$s^2=\\dfrac{%s\\left( %s-%s \\right)^2+%s\\left( %s-%s \\right)^2+%s\\left( %s-%s \\right)^2+%s\\left( %s-%s \\right)^2+%s\\left( %s-%s \\right)^2}{%s}$\\\\ \n'
                        '$=%s$$zz$'
                        %(latex(m1),latex(m2),latex(m3),latex(m4),latex(m5),latex(n),
                        latex(m1),latex(x1),latex(m2),latex(x2),latex(m3),latex(x3),latex(m4),latex(x4),latex(m5),latex(x5),latex(n),latex(xtb),
                        latex(m1),latex(x1),latex(xtb),latex(m2),latex(x2),latex(xtb),latex(m3),latex(x3),latex(xtb),latex(m4),latex(x4),latex(xtb),latex(m5),latex(x5),latex(xtb),latex(n),latex(s2)

                        ))


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
                vd_da_1_d = '\\True Độ lệch chuẩn của dãy số liệu (làm tròn đến hàng phần trăm) là $s=%s$' %(latex(dl))
                vd_da_1_s = 'Độ lệch chuẩn của dãy số liệu (làm tròn đến hàng phần trăm) là $s=%s$' %(latex(dl+1))
                list_vd_da_1=[vd_da_1_d,vd_da_1_s]
                vd_da_1=random.choice(list_vd_da_1)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_vd_1 = [vd_da_1]

                # Nội dung lời giải
                loigiai_vd_1 = (
                        'Số trung bình là $\\bar{x}=\\dfrac{%s \\cdot %s+%s \\cdot %s+%s \\cdot %s+%s \\cdot %s+%s \\cdot %s}{%s}=%s$$zz$ \\\\ \n'
                        'Phương sai của mẫu số liệu là \\\\ \n'
                        '$s^2=\\dfrac{%s\\left( %s-%s \\right)^2+%s\\left( %s-%s \\right)^2+%s\\left( %s-%s \\right)^2+%s\\left( %s-%s \\right)^2+%s\\left( %s-%s \\right)^2}{%s}$\\\\ \n'
                        '$=%s$$zz$ \\\\ \n'
                        'Độ lệch chuẩn của mẫu số liệu là \\\\ \n'
                        '$s=\\sqrt{%s}=%s$$zz$'
                        %(
                        latex(m1),latex(x1),latex(m2),latex(x2),latex(m3),latex(x3),latex(m4),latex(x4),latex(m5),latex(x5),latex(n),latex(xtb),
                        latex(m1),latex(x1),latex(xtb),latex(m2),latex(x2),latex(xtb),latex(m3),latex(x3),latex(xtb),latex(m4),latex(x4),latex(xtb),latex(m5),latex(x5),latex(xtb),latex(n),latex(s2),
                        latex(s2),latex(dl)
                        ))

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
                vdc_da_1_d = '\\True Khoảng tứ phân vị của dãy số liệu là $\\Delta_Q=%s$' %(latex(q3-q1))
                vdc_da_1_s = 'Khoảng tứ phân vị của dãy số liệu là $\\Delta_Q=%s$' %(latex(q3-q1-1))
                list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
                vdc_da_1=random.choice(list_vdc_da_1)


                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_vdc_1 = [vdc_da_1]
                # Nội dung lời giải
                loigiai_vdc_1 = (
                        'Gọi $x_1, x_2, ..., x_{%s}$ là dãy số liệu được xắp xếp theo thứ tự không giảm$zz$ \\\\ \n'
                        'Khi đó trung vị của mẫu số liệu là $M_e=\\dfrac{x_{%s}+x_{%s}}{2}=%s$$zz$ \\\\ \n'
                        'Tứ phân vị thứ nhất là $Q_1=%s$$zz$ \\\\ \n'
                        'Tứ phân vị thứ ba là $Q_3=%s$$zz$ \\\\ \n'
                        'Khoảng tứ phân vị là $\\Delta_Q=%s-%s=%s$$zz$'
                        %(
                        latex(n),
                        latex(Rational(n,2)),latex(Rational(n,2)+1),
                        latex(median),
                        latex(q1),
                        latex(q3),
                        latex(q3),latex(q1),latex(q3-q1)
                        ))

                # Đưa các lời giải vào danh sách lời giải
                list_vdc_2 = [loigiai_vdc_1]

                # Kết hợp các đáp án và lời giải vào cùng một danh sách
                combined_vdc = list(zip(list_vdc_1, list_vdc_2))

                # Xáo trộn danh sách kết hợp
                random.shuffle(combined_vdc)

                # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
                shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
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
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('.', ',').replace('$zz$', '.').replace('\\left[', '').replace('\\right]', '').replace(',0$', '$')
            return content

