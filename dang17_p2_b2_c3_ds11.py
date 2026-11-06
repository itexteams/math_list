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


def bt_dang17_p2_b2_c3_ds11(self):
            # Khai báo biến
            #lisdang=['1','2','3','4']
            lisdang=['2']
            dang=random.choice(lisdang)

            if dang=='4': #tổng chẵn - chia đôi hai bên lẻ
                # Khai báo biến
                lisv=[20,25,30,35,40]
                v = random.choice(lisv)

                # Vòng lặp để tạo tổng thỏa mãn điều kiện
                while True:
                    xe_values = random.sample(range(1,11), 5)
                    xe1, xe2, xe3, xe4, xe5 = xe_values
                    tong = xe1 + xe2 + xe3 + xe4 + xe5
                    tong1 = tong / 2

                    # Kiểm tra điều kiện thoát vòng lặp
                    if tong % 2 == 0 and tong1 % 2 != 0:
                        break

                # Chọn giá trị k ngẫu nhiên
                lisk=[1,2,3,4]
                k = random.choice(lisk)

                x1=Rational(v+v+k,2)
                x2=Rational(v+k+v+2*k,2)
                x3=Rational(v+2*k+v+3*k,2)
                x4=Rational(v+3*k+v+4*k,2)
                x5=Rational(v+4*k+v+5*k,2)

                nhom=randint(1,5)
                listanso=[xe1,xe2,xe3,xe4,xe5]

                xtb=Rational(xe1*x1+xe2*x2+xe3*x3+xe4*x4+xe5*x5,tong)

                # Tạo danh sách số liệu gốc
                data = []
                data.extend([v] * xe1)
                data.extend([v + k] * xe2)
                data.extend([v + 2 * k] * xe3)
                data.extend([v + 3 * k] * xe4)
                data.extend([v + 4 * k] * xe5)

                # Sắp xếp danh sách
                data.sort()

                # Tính toán vị trí Q1
                n = len(data)
                Q1_index = (n + 1) / 4

                if Q1_index.is_integer():
                    Q1 = data[int(Q1_index) - 1]
                else:
                    lower_index = int(Q1_index) - 1
                    upper_index = lower_index + 1
                    Q1 = (data[lower_index] + data[upper_index]) / 2

                # Tính toán vị trí Q2 (Median)
                Q2_index = (n + 1) / 2

                if Q2_index.is_integer():
                    Q2 = data[int(Q2_index) - 1]
                else:
                    lower_index = int(Q2_index) - 1
                    upper_index = lower_index + 1
                    Q2 = (data[lower_index] + data[upper_index]) / 2

                # Tính toán vị trí Q3
                Q3_index = 3 * (n + 1) / 4

                if Q3_index.is_integer():
                    Q3 = data[int(Q3_index) - 1]
                else:
                    lower_index = int(Q3_index) - 1
                    upper_index = lower_index + 1
                    Q3 = (data[lower_index] + data[upper_index]) / 2

                # Tạo danh sách các khoảng và tần số tương ứng
                intervals = [(v, v + k), (v + k, v + 2 * k), (v + 2 * k, v + 3 * k), (v + 3 * k, v + 4 * k), (v + 4 * k, v + 5 * k)]
                frequencies = [xe1, xe2, xe3, xe4, xe5]

                # Tìm khoảng chứa Q1, Q2 và Q3
                Q1_interval, Q2_interval, Q3_interval = None, None, None
                Q1_interval_index, Q2_interval_index, Q3_interval_index = None, None, None

                for i, (start, end) in enumerate(intervals):
                    if start <= Q1 < end:
                        Q1_interval = (start, end)
                        Q1_interval_index = i
                    if start <= Q2 < end:
                        Q2_interval = (start, end)
                        Q2_interval_index = i
                    if start <= Q3 < end:
                        Q3_interval = (start, end)
                        Q3_interval_index = i

                # Tính tổng tần số đến trước khoảng chứa Q1, Q2 và Q3
                total_freq_before_Q1 = sum(frequencies[:Q1_interval_index]) if Q1_interval_index is not None else 0
                total_freq_before_Q2 = sum(frequencies[:Q2_interval_index]) if Q2_interval_index is not None else 0
                total_freq_before_Q3 = sum(frequencies[:Q3_interval_index]) if Q3_interval_index is not None else 0

                # Tìm tần số tương ứng với khoảng chứa Q1, Q2 và Q3
                Q1_interval_frequency = frequencies[Q1_interval_index] if Q1_interval_index is not None else 0
                Q2_interval_frequency = frequencies[Q2_interval_index] if Q2_interval_index is not None else 0
                Q3_interval_frequency = frequencies[Q3_interval_index] if Q3_interval_index is not None else 0

                # Tính toán kết quả Q1, Q2 và Q3
                kqQ1 = Q1_interval[0] + Rational(1 * n / 4 - total_freq_before_Q1, Q1_interval_frequency) * (Q1_interval[1] - Q1_interval[0])
                kqQ2 = Q2_interval[0] + Rational(2 * n / 4 - total_freq_before_Q2, Q2_interval_frequency) * (Q2_interval[1] - Q2_interval[0])
                kqQ3 = Q3_interval[0] + Rational(3 * n / 4 - total_freq_before_Q3, Q3_interval_frequency) * (Q3_interval[1] - Q3_interval[0])

                # Kết quả
                kq = kqQ3 - kqQ1

                # Giả sử max_value đã được xác định từ xe1, xe2, xe3, xe4, xe5
                max_xe = max(xe1, xe2, xe3, xe4, xe5)

                # Tìm khoảng chứa max_xe
                if max_xe == xe1:
                    kh1 = v  
                    kh2 = v+k
                elif max_xe == xe2:
                    kh1 = v+k
                    kh2 = v+2*k
                elif max_xe == xe3:
                    kh1 = v+2*k
                    kh2 = v+3*k
                elif max_xe == xe4:
                    kh1 = v+3*k
                    kh2 = v+4*k
                elif max_xe == xe5:
                    kh1 = v+4*k
                    kh2 = v+5*k 


                # Gán giá trị trước và sau max_xe cho m và n
                if max_xe == xe1:
                    m = 0  # Không có giá trị trước
                    n1 = xe2
                elif max_xe == xe2:
                    m = xe1
                    n1 = xe3
                elif max_xe == xe3:
                    m = xe2
                    n1 = xe4
                elif max_xe == xe4:
                    m = xe3
                    n1 = xe5
                elif max_xe == xe5:
                    m = xe4
                    n1 = 0 # Không có giá trị sau

                mo=kh1+Rational(max_xe-m,max_xe-m+max_xe-n1)*(kh2-kh1)

                # Nội dung câu hỏi
                noidungcauhoi = ('Chiều cao (đơn vị: centimet) của các học sinh lớp 11B được cho trong bảng sau \n'            
                                '\\begin{center} \n'
                                '\\begin{tabular}{|c|c|} \n'
                                '\\hline \n'
                                'Chiều cao (cm) & Số học sinh \\\\ \n'
                                '\\hline \n'
                                '$[%s; %s)$ & $%s$ \\\\ \n'
                                '\\hline \n'
                                '$[%s, %s)$ & $%s$ \\\\ \n'
                                '\\hline \n'
                                '$[%s; %s)$ & $%s$ \\\\ \n'
                                '\\hline \n'
                                '$[%s; %s)$ & $%s$ \\\\ \n'
                                '\\hline \n'
                                '$[%s; %s)$ & $%s$ \\\\ \n'
                                '\\hline \n'
                                '& $n=%s$ \\\\ \n'
                                '\\hline \n'
                                '\\end{tabular} \n'
                                '\\end{center} \n'
                                %(
                                latex(v),latex(v+k),latex(xe1),
                                latex(v+k),latex(v+2*k),latex(xe2),
                                latex(v+2*k),latex(v+3*k),latex(xe3),
                                latex(v+3*k),latex(v+4*k),latex(xe4),
                                latex(v+4*k),latex(v+5*k),latex(xe5),
                                latex(tong),
                                ))

                ######################################################################## Nhận biết ############################################
                # Các đáp án
                nb_da_1_d = '\\True Giá trị đại diện của nhóm $[%s;%s)$ là $%s$' %(latex(v+2*k),latex(v+3*k),latex(xe3))
                nb_da_1_s = 'Giá trị đại diện của nhóm $[%s;%s)$ là $%s$' %(latex(v+2*k),latex(v+3*k),latex(1+xe3))
                list_nb_da_1=[nb_da_1_d,nb_da_1_s]
                nb_da_1=random.choice(list_nb_da_1)

                nb_da_2_d = '\\True Cỡ mẫu là $n=%s$' %(latex(tong))
                nb_da_2_s = 'Cỡ mẫu là $n=%s$' %(latex(tong-1))
                list_nb_da_2=[nb_da_2_d,nb_da_2_s]
                nb_da_2=random.choice(list_nb_da_2)

                nb_da_3_d = '\\True Tần số của nhóm $[%s;%s)$ là $m=%s$'%(latex(v+2*k),latex(v+3*k),latex(xe3))
                nb_da_3_s = 'Tần số của nhóm $[%s;%s)$ là $m=%s$'%(latex(v+2*k),latex(v+3*k),latex(1+xe3))
                list_nb_da_3=[nb_da_3_d,nb_da_3_s]
                nb_da_3=random.choice(list_nb_da_3)

                nb_da_4_d = '\\True Độ dài của nhóm $[%s;%s)$ là $%s$'%(latex(v+2*k),latex(v+3*k),latex(k))
                nb_da_4_s = 'Độ dài của nhóm $[%s;%s)$ là $%s$'%(latex(v+2*k),latex(v+3*k),latex(1+k))
                list_nb_da_4=[nb_da_4_d,nb_da_4_s]
                nb_da_4=random.choice(list_nb_da_4)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_nb_1 = [nb_da_1, nb_da_2,nb_da_3,nb_da_4]

                # Nội dung lời giải
                loigiai_nb_1 = ('Áp dụng công thức $x_i=\\dfrac{a_i+a_{i+1}}{2}$ với $i=1,2,3,4,5$, ta có \\\\ \n'
                                'Giá trị đại diện của nhóm $[%s;%s)$ là $%s$.'
                                %(latex(v+2*k),latex(v+3*k),latex(xe3)
                                ))
                loigiai_nb_2 = ('Cỡ mẫu là \\\\ \n'
                                '\\hspace*{1cm} $n=%s+%s+%s+%s+%s=%s$.'
                                %(latex(xe1),latex(xe2),latex(xe3),latex(xe4),latex(xe5),latex(tong)
                                ))
                loigiai_nb_3 = ('Tần số của nhóm $[%s;%s)$ là $m=%s$.'
                                %(latex(v+2*k),latex(v+3*k),latex(xe3)
                                ))
                loigiai_nb_4 = ('Độ dài của nhóm $[%s;%s)$ là $%s$.'
                                %(latex(v+2*k),latex(v+3*k),latex(k)
                                ))

                # Đưa các lời giải vào danh sách lời giải
                list_nb_2 = [loigiai_nb_1, loigiai_nb_2,loigiai_nb_3,loigiai_nb_4]

                # Kết hợp các đáp án và lời giải vào cùng một danh sách
                combined_nb = list(zip(list_nb_1, list_nb_2))

                # Xáo trộn danh sách kết hợp
                random.shuffle(combined_nb)

                # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
                shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

                ######################################################################## Thông hiểu ############################################
                # Các đáp án
                th_da_1_d = '\\True Số trung bình của mẫu số liệu là $\\bar{x}=%s$' %(latex(xtb))
                th_da_1_s = 'Số trung bình của mẫu số liệu là $\\bar{x}=%s$' %(latex(xtb+1))
                list_th_da_1=[th_da_1_d,th_da_1_s]
                th_da_1=random.choice(list_th_da_1)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_th_1 = [th_da_1]

                # Nội dung lời giải
                loigiai_th_1 = ('Cỡ mẫu là $n=%s+%s+%s+%s+%s=%s$. \\\\ \n'
                                'Giá trị đại điện của các nhóm là \\\\ \n'
                                '\\hspace*{1cm} $x_1=%s, x_2=%s, x_3=%s, x_4=%s, x_5=%s$. \\\\ \n'
                                'Số trung bình của mẫu số liệu là \\\\ \n'
                                '\\hspace*{1cm} $\\bar{x}=\\dfrac{%s \\cdot %s+%s \\cdot %s+%s \\cdot %s+%s \\cdot %s+%s \\cdot %s}{%s}=%s$.'
                                %(latex(xe1),latex(xe2),latex(xe3),latex(xe4),latex(xe5),latex(tong),
                                    latex(x1),latex(x2),latex(x3),latex(x4),latex(x5),
                                latex(xe1),latex(x1),latex(xe2),latex(x2),latex(xe3),latex(x3),latex(xe4),latex(x4),latex(xe5),latex(x5),latex(tong),latex(xtb)               
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
                vd_da_1_d = '\\True Mốt của mẫu số liệu là $M_o=%s$' %(latex(mo))
                vd_da_1_s = 'Mốt của mẫu số liệu là $M_o=%s$' %(latex(mo+1))
                list_vd_da_1=[vd_da_1_d,vd_da_1_s]
                vd_da_1=random.choice(list_vd_da_1)


                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_vd_1 = [vd_da_1]

                # Nội dung lời giải
                loigiai_vd_1 = ('Tần số lớn nhất là $%s$ nên nhóm chứa mốt là nhóm $[%s; %s)$. \\\\ \n'
                                'Ta có \\\\ \n'
                                '\\hspace*{1cm} $M_o=%s+\\dfrac{%s-%s}{(%s-%s)+(%s-%s)} \\cdot (%s-%s)=%s$.'
                                %(latex(max_xe),latex(kh1),latex(kh2),
                                latex(kh1),latex(max_xe),latex(m),latex(max_xe),latex(m),latex(max_xe),latex(n1),latex(kh2),latex(kh1),latex(mo)              
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
                vdc_da_1_d = '\\True Trung vị của mẫu số liệu là $M_e=%s$' %(latex(kqQ2))
                vdc_da_1_s = 'Trung vị của mẫu số liệu là $M_e=%s$' %(latex(1+kqQ2))
                list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
                vdc_da_1=random.choice(list_vdc_da_1)

                vdc_da_2_d = '\\True Tứ phân vị thứ nhất của mẫu số liệu là $Q_1=%s$' %(latex(kqQ1))
                vdc_da_2_s = 'Tứ phân vị thứ nhất của mẫu số liệu là $Q_1=%s$' %(latex(1+kqQ1))
                list_vdc_da_2=[vdc_da_2_d,vdc_da_2_s]
                vdc_da_2=random.choice(list_vdc_da_2)

                vdc_da_3_d = '\\True Tứ phân vị thứ ba của mẫu số liệu là $Q_3=%s$' %(latex(kqQ3))
                vdc_da_3_s = 'Tứ phân vị thứ ba của mẫu số liệu là $Q_3=%s$' %(latex(1+kqQ3))
                list_vdc_da_3=[vdc_da_3_d,vdc_da_3_s]
                vdc_da_3=random.choice(list_vdc_da_3)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_vdc_1 = [vdc_da_1,vdc_da_2,vdc_da_3]

                # Nội dung lời giải
                loigiai_vdc_1 = ('Cỡ mẫu $n=%s$. Giả sử $x_1, x_2, ..., x_{%s}$ là $%s$ số liệu và giả sử dãy số liệu gốc này được sắp xếp theo thứ tự không giảm. \\\\ \n'            
                            'Vì $n=%s$ nên trung vị của mẫu số liệu là $M_e=\\dfrac{x_{%s}+x_{%s}}{2}$ thuộc nhóm $[%s;%s)$. \\\\ \n'
                            '\\hspace*{1cm} Do đó, trung vị là \\\\ \n'
                            '\\hspace*{1cm} $M_e=%s+\\dfrac{\\frac{%s}{2}-%s}{%s} \\cdot %s=%s$.'
                            %(latex(tong),latex(tong),latex(tong),
                            latex(n),latex(n/2),latex(n/2+1),latex(Q2_interval[0]),latex(Q2_interval[1]),
                            latex(Q2_interval[0]),latex(n),latex(total_freq_before_Q2),latex(Q2_interval_frequency),latex(Q2_interval[1]-Q2_interval[0]),latex(kqQ2),        
                            ))
                loigiai_vdc_2 = ('Cỡ mẫu $n=%s$. Giả sử $x_1, x_2, ..., x_{%s}$ là $%s$ số liệu và giả sử dãy số liệu gốc này được sắp xếp theo thứ tự không giảm. \\\\ \n'
                        'Vì $n=%s$ nên tứ phân vị thứ nhất của mẫu số liệu là $x_{%s}$ thuộc nhóm $[%s;%s)$. \\\\ \n'
                        '\\hspace*{1cm} Do đó, tứ phân vị thứ nhất là \\\\ \n'
                        '\\hspace*{1cm} $Q_1=%s+\\dfrac{\\frac{%s}{4}-%s}{%s} \\cdot %s=%s$.'
                            %(latex(tong),latex(tong),latex(tong),               
                            latex(n),latex(n/4+1/2),latex(Q1_interval[0]),latex(Q1_interval[1]),
                            latex(Q1_interval[0]),latex(n),latex(total_freq_before_Q1),latex(Q1_interval_frequency),latex(Q1_interval[1]-Q1_interval[0]),latex(kqQ1),
                            ))
                loigiai_vdc_3 = ('Cỡ mẫu $n=%s$. Giả sử $x_1, x_2, ..., x_{%s}$ là $%s$ số liệu và giả sử dãy số liệu gốc này được sắp xếp theo thứ tự không giảm. \\\\ \n'             
                            'Vì $n=%s$ nên tứ phân vị thứ ba của mẫu số liệu là $x_{%s}$ thuộc nhóm $[%s;%s)$. \\\\ \n'
                            '\\hspace*{1cm} Do đó, tứ phân vị thứ ba là \\\\ \n'
                            '\\hspace*{1cm} $Q_3=%s+\\dfrac{\\frac{3 \\cdot %s}{4}-%s}{%s} \\cdot %s=%s$.'
                            %(latex(tong),latex(tong),latex(tong),                           
                            latex(n),latex(n/2+n/4+1/2),latex(Q3_interval[0]),latex(Q3_interval[1]),
                            latex(Q3_interval[0]),latex(n),latex(total_freq_before_Q3),latex(Q3_interval_frequency),latex(Q3_interval[1]-Q3_interval[0]),latex(kqQ3),                      
                            ))

                # Đưa các lời giải vào danh sách lời giải
                list_vdc_2 = [loigiai_vdc_1,loigiai_vdc_2,loigiai_vdc_3]

                # Kết hợp các đáp án và lời giải vào cùng một danh sách
                combined_vdc = list(zip(list_vdc_1, list_vdc_2))

                # Xáo trộn danh sách kết hợp
                random.shuffle(combined_vdc)

                # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
                shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            if dang=='3': #tổng chẵn - chia đôi hai bên chẵn
                # Khai báo biến
                lisv=[20,25,30,35,40]
                v = random.choice(lisv)

                # Vòng lặp để tạo tổng thỏa mãn điều kiện
                while True:
                    xe_values = random.sample(range(1,11), 5)
                    xe1, xe2, xe3, xe4, xe5 = xe_values
                    tong = xe1 + xe2 + xe3 + xe4 + xe5
                    tong1 = tong / 2

                    # Kiểm tra điều kiện thoát vòng lặp
                    if tong % 2 == 0 and tong1 % 2 == 0:
                        break 

                # Chọn giá trị k ngẫu nhiên
                lisk=[1,2,3,4]
                k = random.choice(lisk)

                x1=Rational(v+v+k,2)
                x2=Rational(v+k+v+2*k,2)
                x3=Rational(v+2*k+v+3*k,2)
                x4=Rational(v+3*k+v+4*k,2)
                x5=Rational(v+4*k+v+5*k,2)

                nhom=randint(1,5)
                listanso=[xe1,xe2,xe3,xe4,xe5]

                xtb=Rational(xe1*x1+xe2*x2+xe3*x3+xe4*x4+xe5*x5,tong)

                # Tạo danh sách số liệu gốc
                data = []
                data.extend([v] * xe1)
                data.extend([v + k] * xe2)
                data.extend([v + 2 * k] * xe3)
                data.extend([v + 3 * k] * xe4)
                data.extend([v + 4 * k] * xe5)

                # Sắp xếp danh sách
                data.sort()

                # Tính toán vị trí Q1
                n = len(data)
                Q1_index = (n + 1) / 4

                if Q1_index.is_integer():
                    Q1 = data[int(Q1_index) - 1]
                else:
                    lower_index = int(Q1_index) - 1
                    upper_index = lower_index + 1
                    Q1 = (data[lower_index] + data[upper_index]) / 2

                # Tính toán vị trí Q2 (Median)
                Q2_index = (n + 1) / 2

                if Q2_index.is_integer():
                    Q2 = data[int(Q2_index) - 1]
                else:
                    lower_index = int(Q2_index) - 1
                    upper_index = lower_index + 1
                    Q2 = (data[lower_index] + data[upper_index]) / 2

                # Tính toán vị trí Q3
                Q3_index = 3 * (n + 1) / 4

                if Q3_index.is_integer():
                    Q3 = data[int(Q3_index) - 1]
                else:
                    lower_index = int(Q3_index) - 1
                    upper_index = lower_index + 1
                    Q3 = (data[lower_index] + data[upper_index]) / 2

                # Tạo danh sách các khoảng và tần số tương ứng
                intervals = [(v, v + k), (v + k, v + 2 * k), (v + 2 * k, v + 3 * k), (v + 3 * k, v + 4 * k), (v + 4 * k, v + 5 * k)]
                frequencies = [xe1, xe2, xe3, xe4, xe5]

                # Tìm khoảng chứa Q1, Q2 và Q3
                Q1_interval, Q2_interval, Q3_interval = None, None, None
                Q1_interval_index, Q2_interval_index, Q3_interval_index = None, None, None

                for i, (start, end) in enumerate(intervals):
                    if start <= Q1 < end:
                        Q1_interval = (start, end)
                        Q1_interval_index = i
                    if start <= Q2 < end:
                        Q2_interval = (start, end)
                        Q2_interval_index = i
                    if start <= Q3 < end:
                        Q3_interval = (start, end)
                        Q3_interval_index = i

                # Tính tổng tần số đến trước khoảng chứa Q1, Q2 và Q3
                total_freq_before_Q1 = sum(frequencies[:Q1_interval_index]) if Q1_interval_index is not None else 0
                total_freq_before_Q2 = sum(frequencies[:Q2_interval_index]) if Q2_interval_index is not None else 0
                total_freq_before_Q3 = sum(frequencies[:Q3_interval_index]) if Q3_interval_index is not None else 0

                # Tìm tần số tương ứng với khoảng chứa Q1, Q2 và Q3
                Q1_interval_frequency = frequencies[Q1_interval_index] if Q1_interval_index is not None else 0
                Q2_interval_frequency = frequencies[Q2_interval_index] if Q2_interval_index is not None else 0
                Q3_interval_frequency = frequencies[Q3_interval_index] if Q3_interval_index is not None else 0

                # Tính toán kết quả Q1, Q2 và Q3
                kqQ1 = Q1_interval[0] + Rational(1 * n / 4 - total_freq_before_Q1, Q1_interval_frequency) * (Q1_interval[1] - Q1_interval[0])
                kqQ2 = Q2_interval[0] + Rational(2 * n / 4 - total_freq_before_Q2, Q2_interval_frequency) * (Q2_interval[1] - Q2_interval[0])
                kqQ3 = Q3_interval[0] + Rational(3 * n / 4 - total_freq_before_Q3, Q3_interval_frequency) * (Q3_interval[1] - Q3_interval[0])

                # Kết quả
                kq = kqQ3 - kqQ1

                # Giả sử max_value đã được xác định từ xe1, xe2, xe3, xe4, xe5
                max_xe = max(xe1, xe2, xe3, xe4, xe5)

                # Tìm khoảng chứa max_xe
                if max_xe == xe1:
                    kh1 = v  
                    kh2 = v+k
                elif max_xe == xe2:
                    kh1 = v+k
                    kh2 = v+2*k
                elif max_xe == xe3:
                    kh1 = v+2*k
                    kh2 = v+3*k
                elif max_xe == xe4:
                    kh1 = v+3*k
                    kh2 = v+4*k
                elif max_xe == xe5:
                    kh1 = v+4*k
                    kh2 = v+5*k 


                # Gán giá trị trước và sau max_xe cho m và n
                if max_xe == xe1:
                    m = 0  # Không có giá trị trước
                    n1 = xe2
                elif max_xe == xe2:
                    m = xe1
                    n1 = xe3
                elif max_xe == xe3:
                    m = xe2
                    n1 = xe4
                elif max_xe == xe4:
                    m = xe3
                    n1 = xe5
                elif max_xe == xe5:
                    m = xe4
                    n1 = 0 # Không có giá trị sau

                mo=kh1+Rational(max_xe-m,max_xe-m+max_xe-n1)*(kh2-kh1)

                # Nội dung câu hỏi
                noidungcauhoi = ('Chiều cao (đơn vị: centimet) của các học sinh lớp 11B được cho trong bảng sau \n'            
                                '\\begin{center} \n'
                                '\\begin{tabular}{|c|c|} \n'
                                '\\hline \n'
                                'Chiều cao (cm) & Số học sinh \\\\ \n'
                                '\\hline \n'
                                '$[%s; %s)$ & $%s$ \\\\ \n'
                                '\\hline \n'
                                '$[%s, %s)$ & $%s$ \\\\ \n'
                                '\\hline \n'
                                '$[%s; %s)$ & $%s$ \\\\ \n'
                                '\\hline \n'
                                '$[%s; %s)$ & $%s$ \\\\ \n'
                                '\\hline \n'
                                '$[%s; %s)$ & $%s$ \\\\ \n'
                                '\\hline \n'
                                '& $n=%s$ \\\\ \n'
                                '\\hline \n'
                                '\\end{tabular} \n'
                                '\\end{center} \n'
                                %(
                                latex(v),latex(v+k),latex(xe1),
                                latex(v+k),latex(v+2*k),latex(xe2),
                                latex(v+2*k),latex(v+3*k),latex(xe3),
                                latex(v+3*k),latex(v+4*k),latex(xe4),
                                latex(v+4*k),latex(v+5*k),latex(xe5),
                                latex(tong),
                                ))

                ######################################################################## Nhận biết ############################################
                # Các đáp án
                nb_da_1_d = '\\True Giá trị đại diện của nhóm $[%s;%s)$ là $%s$' %(latex(v+2*k),latex(v+3*k),latex(xe3))
                nb_da_1_s = 'Giá trị đại diện của nhóm $[%s;%s)$ là $%s$' %(latex(v+2*k),latex(v+3*k),latex(1+xe3))
                list_nb_da_1=[nb_da_1_d,nb_da_1_s]
                nb_da_1=random.choice(list_nb_da_1)

                nb_da_2_d = '\\True Cỡ mẫu là $n=%s$' %(latex(tong))
                nb_da_2_s = 'Cỡ mẫu là $n=%s$' %(latex(tong-1))
                list_nb_da_2=[nb_da_2_d,nb_da_2_s]
                nb_da_2=random.choice(list_nb_da_2)

                nb_da_3_d = '\\True Tần số của nhóm $[%s;%s)$ là $m=%s$'%(latex(v+2*k),latex(v+3*k),latex(xe3))
                nb_da_3_s = 'Tần số của nhóm $[%s;%s)$ là $m=%s$'%(latex(v+2*k),latex(v+3*k),latex(1+xe3))
                list_nb_da_3=[nb_da_3_d,nb_da_3_s]
                nb_da_3=random.choice(list_nb_da_3)

                nb_da_4_d = '\\True Độ dài của nhóm $[%s;%s)$ là $%s$'%(latex(v+2*k),latex(v+3*k),latex(k))
                nb_da_4_s = 'Độ dài của nhóm $[%s;%s)$ là $%s$'%(latex(v+2*k),latex(v+3*k),latex(1+k))
                list_nb_da_4=[nb_da_4_d,nb_da_4_s]
                nb_da_4=random.choice(list_nb_da_4)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_nb_1 = [nb_da_1, nb_da_2,nb_da_3,nb_da_4]

                # Nội dung lời giải
                loigiai_nb_1 = ('Áp dụng công thức $x_i=\\dfrac{a_i+a_{i+1}}{2}$ với $i=1,2,3,4,5$, ta có \\\\ \n'
                                'Giá trị đại diện của nhóm $[%s;%s)$ là $%s$.'
                                %(latex(v+2*k),latex(v+3*k),latex(xe3)
                                ))
                loigiai_nb_2 = ('Cỡ mẫu là \\\\ \n'
                                '\\hspace*{1cm} $n=%s+%s+%s+%s+%s=%s$.'
                                %(latex(xe1),latex(xe2),latex(xe3),latex(xe4),latex(xe5),latex(tong)
                                ))
                loigiai_nb_3 = ('Tần số của nhóm $[%s;%s)$ là $m=%s$.'
                                %(latex(v+2*k),latex(v+3*k),latex(xe3)
                                ))
                loigiai_nb_4 = ('Độ dài của nhóm $[%s;%s)$ là $%s$.'
                                %(latex(v+2*k),latex(v+3*k),latex(k)
                                ))

                # Đưa các lời giải vào danh sách lời giải
                list_nb_2 = [loigiai_nb_1, loigiai_nb_2,loigiai_nb_3,loigiai_nb_4]

                # Kết hợp các đáp án và lời giải vào cùng một danh sách
                combined_nb = list(zip(list_nb_1, list_nb_2))

                # Xáo trộn danh sách kết hợp
                random.shuffle(combined_nb)

                # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
                shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

                ######################################################################## Thông hiểu ############################################
                # Các đáp án
                th_da_1_d = '\\True Số trung bình của mẫu số liệu là $\\bar{x}=%s$' %(latex(xtb))
                th_da_1_s = 'Số trung bình của mẫu số liệu là $\\bar{x}=%s$' %(latex(xtb+1))
                list_th_da_1=[th_da_1_d,th_da_1_s]
                th_da_1=random.choice(list_th_da_1)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_th_1 = [th_da_1]

                # Nội dung lời giải
                loigiai_th_1 = ('Cỡ mẫu là $n=%s+%s+%s+%s+%s=%s$. \\\\ \n'
                                'Giá trị đại điện của các nhóm là \\\\ \n'
                                '\\hspace*{1cm} $x_1=%s, x_2=%s, x_3=%s, x_4=%s, x_5=%s$. \\\\ \n'
                                'Số trung bình của mẫu số liệu là \\\\ \n'
                                '\\hspace*{1cm} $\\bar{x}=\\dfrac{%s \\cdot %s+%s \\cdot %s+%s \\cdot %s+%s \\cdot %s+%s \\cdot %s}{%s}=%s$.'
                                %(latex(xe1),latex(xe2),latex(xe3),latex(xe4),latex(xe5),latex(tong),
                                    latex(x1),latex(x2),latex(x3),latex(x4),latex(x5),
                                latex(xe1),latex(x1),latex(xe2),latex(x2),latex(xe3),latex(x3),latex(xe4),latex(x4),latex(xe5),latex(x5),latex(tong),latex(xtb)               
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
                vd_da_1_d = '\\True Mốt của mẫu số liệu là $M_o=%s$' %(latex(mo))
                vd_da_1_s = 'Mốt của mẫu số liệu là $M_o=%s$' %(latex(mo+1))
                list_vd_da_1=[vd_da_1_d,vd_da_1_s]
                vd_da_1=random.choice(list_vd_da_1)


                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_vd_1 = [vd_da_1]

                # Nội dung lời giải
                loigiai_vd_1 = ('Tần số lớn nhất là $%s$ nên nhóm chứa mốt là nhóm $[%s; %s)$. \\\\ \n'
                                'Ta có \\\\ \n'
                                '\\hspace*{1cm} $M_o=%s+\\dfrac{%s-%s}{(%s-%s)+(%s-%s)} \\cdot (%s-%s)=%s$.'
                                %(latex(max_xe),latex(kh1),latex(kh2),
                                latex(kh1),latex(max_xe),latex(m),latex(max_xe),latex(m),latex(max_xe),latex(n1),latex(kh2),latex(kh1),latex(mo)              
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
                vdc_da_1_d = '\\True Trung vị của mẫu số liệu là $M_e=%s$' %(latex(kqQ2))
                vdc_da_1_s = 'Trung vị của mẫu số liệu là $M_e=%s$' %(latex(1+kqQ2))
                list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
                vdc_da_1=random.choice(list_vdc_da_1)

                vdc_da_2_d = '\\True Tứ phân vị thứ nhất của mẫu số liệu là $Q_1=%s$' %(latex(kqQ1))
                vdc_da_2_s = 'Tứ phân vị thứ nhất của mẫu số liệu là $Q_1=%s$' %(latex(1+kqQ1))
                list_vdc_da_2=[vdc_da_2_d,vdc_da_2_s]
                vdc_da_2=random.choice(list_vdc_da_2)

                vdc_da_3_d = '\\True Tứ phân vị thứ ba của mẫu số liệu là $Q_3=%s$' %(latex(kqQ3))
                vdc_da_3_s = 'Tứ phân vị thứ ba của mẫu số liệu là $Q_3=%s$' %(latex(1+kqQ3))
                list_vdc_da_3=[vdc_da_3_d,vdc_da_3_s]
                vdc_da_3=random.choice(list_vdc_da_3)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_vdc_1 = [vdc_da_1,vdc_da_2,vdc_da_3]

                # Nội dung lời giải
                loigiai_vdc_1 = ('Cỡ mẫu $n=%s$. Giả sử $x_1, x_2, ..., x_{%s}$ là $%s$ số liệu và giả sử dãy số liệu gốc này được sắp xếp theo thứ tự không giảm. \\\\ \n'            
                            'Vì $n=%s$ nên trung vị của mẫu số liệu là $M_e=\\dfrac{x_{%s}+x_{%s}}{2}$ thuộc nhóm $[%s;%s)$. \\\\ \n'
                            '\\hspace*{1cm} Do đó, trung vị là \\\\ \n'
                            '\\hspace*{1cm} $M_e=%s+\\dfrac{\\frac{%s}{2}-%s}{%s} \\cdot %s=%s$.'
                            %(latex(tong),latex(tong),latex(tong),
                            latex(n),latex(n/2),latex(n/2+1),latex(Q2_interval[0]),latex(Q2_interval[1]),
                            latex(Q2_interval[0]),latex(n),latex(total_freq_before_Q2),latex(Q2_interval_frequency),latex(Q2_interval[1]-Q2_interval[0]),latex(kqQ2),         
                            ))
                loigiai_vdc_2 = ('Cỡ mẫu $n=%s$. Giả sử $x_1, x_2, ..., x_{%s}$ là $%s$ số liệu và giả sử dãy số liệu gốc này được sắp xếp theo thứ tự không giảm. \\\\ \n'
                        'Vì $n=%s$ nên tứ phân vị thứ nhất của mẫu số liệu là $Q_1=\\dfrac{x_{%s}+x_{%s}}{2}$ thuộc nhóm $[%s;%s)$. \\\\ \n'
                        '\\hspace*{1cm} Do đó, tứ phân vị thứ nhất là \\\\ \n'
                        '\\hspace*{1cm} $Q_1=%s+\\dfrac{\\frac{%s}{4}-%s}{%s} \\cdot %s=%s$.'
                            %(latex(tong),latex(tong),latex(tong),               
                            latex(n),latex(n/4+1/2-1/2),latex(n/4+1/2+1/2),latex(Q1_interval[0]),latex(Q1_interval[1]),
                            latex(Q1_interval[0]),latex(n),latex(total_freq_before_Q1),latex(Q1_interval_frequency),latex(Q1_interval[1]-Q1_interval[0]),latex(kqQ1),
                            ))
                loigiai_vdc_3 = ('Cỡ mẫu $n=%s$. Giả sử $x_1, x_2, ..., x_{%s}$ là $%s$ số liệu và giả sử dãy số liệu gốc này được sắp xếp theo thứ tự không giảm. \\\\ \n'             
                            'Vì $n=%s$ nên tứ phân vị thứ ba của mẫu số liệu là $Q_3=\\dfrac{x_{%s}+x_{%s}}{2}$ thuộc nhóm $[%s;%s)$. \\\\ \n'
                            '\\hspace*{1cm} Do đó, tứ phân vị thứ ba là \\\\ \n'
                            '\\hspace*{1cm} $Q_3=%s+\\dfrac{\\frac{3 \\cdot %s}{4}-%s}{%s} \\cdot %s=%s$.'
                            %(latex(tong),latex(tong),latex(tong),                           
                            latex(n),latex(n/2+n/4+1/2-1/2),latex(n/2+n/4+1/2+1/2),latex(Q3_interval[0]),latex(Q3_interval[1]),
                            latex(Q3_interval[0]),latex(n),latex(total_freq_before_Q3),latex(Q3_interval_frequency),latex(Q3_interval[1]-Q3_interval[0]),latex(kqQ3),                        
                            ))

                # Đưa các lời giải vào danh sách lời giải
                list_vdc_2 = [loigiai_vdc_1,loigiai_vdc_2,loigiai_vdc_3]

                # Kết hợp các đáp án và lời giải vào cùng một danh sách
                combined_vdc = list(zip(list_vdc_1, list_vdc_2))

                # Xáo trộn danh sách kết hợp
                random.shuffle(combined_vdc)

                # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
                shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            if dang=='2': #tổng lẻ - chia đôi hai bên lẻ
                # Khai báo biến
                lisv=[20,25,30,35,40]
                v = random.choice(lisv)

                # Vòng lặp để tạo tổng thỏa mãn điều kiện
                while True:
                    xe_values = random.sample(range(1,11), 5)
                    xe1, xe2, xe3, xe4, xe5 = xe_values
                    tong = xe1 + xe2 + xe3 + xe4 + xe5
                    tong1 = (tong - 1) / 2

                    # Kiểm tra điều kiện thoát vòng lặp
                    if tong % 2 != 0 and tong1 % 2 != 0:
                        break  

                # Chọn giá trị k ngẫu nhiên
                lisk=[1,2,3,4]
                k = random.choice(lisk)

                x1=Rational(v+v+k,2)
                x2=Rational(v+k+v+2*k,2)
                x3=Rational(v+2*k+v+3*k,2)
                x4=Rational(v+3*k+v+4*k,2)
                x5=Rational(v+4*k+v+5*k,2)

                nhom=randint(1,5)
                listanso=[xe1,xe2,xe3,xe4,xe5]

                xtb=Rational(xe1*x1+xe2*x2+xe3*x3+xe4*x4+xe5*x5,tong)

                # Tạo danh sách số liệu gốc
                data = []
                data.extend([v] * xe1)
                data.extend([v + k] * xe2)
                data.extend([v + 2 * k] * xe3)
                data.extend([v + 3 * k] * xe4)
                data.extend([v + 4 * k] * xe5)

                # Sắp xếp danh sách
                data.sort()

                # Tính toán vị trí Q1
                n = len(data)
                Q1_index = (n + 1) / 4

                if Q1_index.is_integer():
                    Q1 = data[int(Q1_index) - 1]
                else:
                    lower_index = int(Q1_index) - 1
                    upper_index = lower_index + 1
                    Q1 = (data[lower_index] + data[upper_index]) / 2

                # Tính toán vị trí Q2 (Median)
                Q2_index = (n + 1) / 2

                if Q2_index.is_integer():
                    Q2 = data[int(Q2_index) - 1]
                else:
                    lower_index = int(Q2_index) - 1
                    upper_index = lower_index + 1
                    Q2 = (data[lower_index] + data[upper_index]) / 2

                # Tính toán vị trí Q3
                Q3_index = 3 * (n + 1) / 4

                if Q3_index.is_integer():
                    Q3 = data[int(Q3_index) - 1]
                else:
                    lower_index = int(Q3_index) - 1
                    upper_index = lower_index + 1
                    Q3 = (data[lower_index] + data[upper_index]) / 2

                # Tạo danh sách các khoảng và tần số tương ứng
                intervals = [(v, v + k), (v + k, v + 2 * k), (v + 2 * k, v + 3 * k), (v + 3 * k, v + 4 * k), (v + 4 * k, v + 5 * k)]
                frequencies = [xe1, xe2, xe3, xe4, xe5]

                # Tìm khoảng chứa Q1, Q2 và Q3
                Q1_interval, Q2_interval, Q3_interval = None, None, None
                Q1_interval_index, Q2_interval_index, Q3_interval_index = None, None, None

                for i, (start, end) in enumerate(intervals):
                    if start <= Q1 < end:
                        Q1_interval = (start, end)
                        Q1_interval_index = i
                    if start <= Q2 < end:
                        Q2_interval = (start, end)
                        Q2_interval_index = i
                    if start <= Q3 < end:
                        Q3_interval = (start, end)
                        Q3_interval_index = i

                # Tính tổng tần số đến trước khoảng chứa Q1, Q2 và Q3
                total_freq_before_Q1 = sum(frequencies[:Q1_interval_index]) if Q1_interval_index is not None else 0
                total_freq_before_Q2 = sum(frequencies[:Q2_interval_index]) if Q2_interval_index is not None else 0
                total_freq_before_Q3 = sum(frequencies[:Q3_interval_index]) if Q3_interval_index is not None else 0

                # Tìm tần số tương ứng với khoảng chứa Q1, Q2 và Q3
                Q1_interval_frequency = frequencies[Q1_interval_index] if Q1_interval_index is not None else 0
                Q2_interval_frequency = frequencies[Q2_interval_index] if Q2_interval_index is not None else 0
                Q3_interval_frequency = frequencies[Q3_interval_index] if Q3_interval_index is not None else 0

                # Tính toán kết quả Q1, Q2 và Q3
                kqQ1 = Q1_interval[0] + Rational(1 * n / 4 - total_freq_before_Q1, Q1_interval_frequency) * (Q1_interval[1] - Q1_interval[0])
                kqQ2 = Q2_interval[0] + Rational(2 * n / 4 - total_freq_before_Q2, Q2_interval_frequency) * (Q2_interval[1] - Q2_interval[0])
                kqQ3 = Q3_interval[0] + Rational(3 * n / 4 - total_freq_before_Q3, Q3_interval_frequency) * (Q3_interval[1] - Q3_interval[0])

                # Kết quả
                kq = kqQ3 - kqQ1

                # Giả sử max_value đã được xác định từ xe1, xe2, xe3, xe4, xe5
                max_xe = max(xe1, xe2, xe3, xe4, xe5)

                # Tìm khoảng chứa max_xe
                if max_xe == xe1:
                    kh1 = v  
                    kh2 = v+k
                elif max_xe == xe2:
                    kh1 = v+k
                    kh2 = v+2*k
                elif max_xe == xe3:
                    kh1 = v+2*k
                    kh2 = v+3*k
                elif max_xe == xe4:
                    kh1 = v+3*k
                    kh2 = v+4*k
                elif max_xe == xe5:
                    kh1 = v+4*k
                    kh2 = v+5*k 


                # Gán giá trị trước và sau max_xe cho m và n
                if max_xe == xe1:
                    m = 0  # Không có giá trị trước
                    n1 = xe2
                elif max_xe == xe2:
                    m = xe1
                    n1 = xe3
                elif max_xe == xe3:
                    m = xe2
                    n1 = xe4
                elif max_xe == xe4:
                    m = xe3
                    n1 = xe5
                elif max_xe == xe5:
                    m = xe4
                    n1 = 0 # Không có giá trị sau

                mo=kh1+Rational(max_xe-m,max_xe-m+max_xe-n1)*(kh2-kh1)

                # Nội dung câu hỏi
                noidungcauhoi = ('Chiều cao (đơn vị: centimet) của các học sinh lớp 11B được cho trong bảng sau \n'            
                                '\\begin{center} \n'
                                '\\begin{tabular}{|c|c|} \n'
                                '\\hline \n'
                                'Chiều cao (cm) & Số học sinh \\\\ \n'
                                '\\hline \n'
                                '$[%s; %s)$ & $%s$ \\\\ \n'
                                '\\hline \n'
                                '$[%s, %s)$ & $%s$ \\\\ \n'
                                '\\hline \n'
                                '$[%s; %s)$ & $%s$ \\\\ \n'
                                '\\hline \n'
                                '$[%s; %s)$ & $%s$ \\\\ \n'
                                '\\hline \n'
                                '$[%s; %s)$ & $%s$ \\\\ \n'
                                '\\hline \n'
                                '& $n=%s$ \\\\ \n'
                                '\\hline \n'
                                '\\end{tabular} \n'
                                '\\end{center} \n'
                                %(
                                latex(v),latex(v+k),latex(xe1),
                                latex(v+k),latex(v+2*k),latex(xe2),
                                latex(v+2*k),latex(v+3*k),latex(xe3),
                                latex(v+3*k),latex(v+4*k),latex(xe4),
                                latex(v+4*k),latex(v+5*k),latex(xe5),
                                latex(tong),
                                ))

                ######################################################################## Nhận biết ############################################
                # Các đáp án
                nb_da_1_d = '\\True Giá trị đại diện của nhóm $[%s;%s)$ là $%s$' %(latex(v+2*k),latex(v+3*k),latex(xe3))
                nb_da_1_s = 'Giá trị đại diện của nhóm $[%s;%s)$ là $%s$' %(latex(v+2*k),latex(v+3*k),latex(1+xe3))
                list_nb_da_1=[nb_da_1_d,nb_da_1_s]
                nb_da_1=random.choice(list_nb_da_1)

                nb_da_2_d = '\\True Cỡ mẫu là $n=%s$' %(latex(tong))
                nb_da_2_s = 'Cỡ mẫu là $n=%s$' %(latex(tong-1))
                list_nb_da_2=[nb_da_2_d,nb_da_2_s]
                nb_da_2=random.choice(list_nb_da_2)

                nb_da_3_d = '\\True Tần số của nhóm $[%s;%s)$ là $m=%s$'%(latex(v+2*k),latex(v+3*k),latex(xe3))
                nb_da_3_s = 'Tần số của nhóm $[%s;%s)$ là $m=%s$'%(latex(v+2*k),latex(v+3*k),latex(1+xe3))
                list_nb_da_3=[nb_da_3_d,nb_da_3_s]
                nb_da_3=random.choice(list_nb_da_3)

                nb_da_4_d = '\\True Độ dài của nhóm $[%s;%s)$ là $%s$'%(latex(v+2*k),latex(v+3*k),latex(k))
                nb_da_4_s = 'Độ dài của nhóm $[%s;%s)$ là $%s$'%(latex(v+2*k),latex(v+3*k),latex(1+k))
                list_nb_da_4=[nb_da_4_d,nb_da_4_s]
                nb_da_4=random.choice(list_nb_da_4)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_nb_1 = [nb_da_1, nb_da_2,nb_da_3,nb_da_4]

                # Nội dung lời giải
                loigiai_nb_1 = ('Áp dụng công thức $x_i=\\dfrac{a_i+a_{i+1}}{2}$ với $i=1,2,3,4,5$, ta có \\\\ \n'
                                'Giá trị đại diện của nhóm $[%s;%s)$ là $%s$.'
                                %(latex(v+2*k),latex(v+3*k),latex(xe3)
                                ))
                loigiai_nb_2 = ('Cỡ mẫu là \\\\ \n'
                                '\\hspace*{1cm} $n=%s+%s+%s+%s+%s=%s$.'
                                %(latex(xe1),latex(xe2),latex(xe3),latex(xe4),latex(xe5),latex(tong)
                                ))
                loigiai_nb_3 = ('Tần số của nhóm $[%s;%s)$ là $m=%s$.'
                                %(latex(v+2*k),latex(v+3*k),latex(xe3)
                                ))
                loigiai_nb_4 = ('Độ dài của nhóm $[%s;%s)$ là $%s$.'
                                %(latex(v+2*k),latex(v+3*k),latex(k)
                                ))

                # Đưa các lời giải vào danh sách lời giải
                list_nb_2 = [loigiai_nb_1, loigiai_nb_2,loigiai_nb_3,loigiai_nb_4]

                # Kết hợp các đáp án và lời giải vào cùng một danh sách
                combined_nb = list(zip(list_nb_1, list_nb_2))

                # Xáo trộn danh sách kết hợp
                random.shuffle(combined_nb)

                # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
                shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

                ######################################################################## Thông hiểu ############################################
                # Các đáp án
                th_da_1_d = '\\True Số trung bình của mẫu số liệu là $\\bar{x}=%s$' %(latex(xtb))
                th_da_1_s = 'Số trung bình của mẫu số liệu là $\\bar{x}=%s$' %(latex(xtb+1))
                list_th_da_1=[th_da_1_d,th_da_1_s]
                th_da_1=random.choice(list_th_da_1)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_th_1 = [th_da_1]

                # Nội dung lời giải
                loigiai_th_1 = ('Cỡ mẫu là $n=%s+%s+%s+%s+%s=%s$. \\\\ \n'
                                'Giá trị đại điện của các nhóm là \\\\ \n'
                                '\\hspace*{1cm} $x_1=%s, x_2=%s, x_3=%s, x_4=%s, x_5=%s$. \\\\ \n'
                                'Số trung bình của mẫu số liệu là \\\\ \n'
                                '\\hspace*{1cm} $\\bar{x}=\\dfrac{%s \\cdot %s+%s \\cdot %s+%s \\cdot %s+%s \\cdot %s+%s \\cdot %s}{%s}=%s$.'
                                %(latex(xe1),latex(xe2),latex(xe3),latex(xe4),latex(xe5),latex(tong),
                                    latex(x1),latex(x2),latex(x3),latex(x4),latex(x5),
                                latex(xe1),latex(x1),latex(xe2),latex(x2),latex(xe3),latex(x3),latex(xe4),latex(x4),latex(xe5),latex(x5),latex(tong),latex(xtb)               
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
                vd_da_1_d = '\\True Mốt của mẫu số liệu là $M_o=%s$' %(latex(mo))
                vd_da_1_s = 'Mốt của mẫu số liệu là $M_o=%s$' %(latex(mo+1))
                list_vd_da_1=[vd_da_1_d,vd_da_1_s]
                vd_da_1=random.choice(list_vd_da_1)


                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_vd_1 = [vd_da_1]

                # Nội dung lời giải
                loigiai_vd_1 = ('Tần số lớn nhất là $%s$ nên nhóm chứa mốt là nhóm $[%s; %s)$. \\\\ \n'
                                'Ta có \\\\ \n'
                                '\\hspace*{1cm} $M_o=%s+\\dfrac{%s-%s}{(%s-%s)+(%s-%s)} \\cdot (%s-%s)=%s$.'
                                %(latex(max_xe),latex(kh1),latex(kh2),
                                latex(kh1),latex(max_xe),latex(m),latex(max_xe),latex(m),latex(max_xe),latex(n1),latex(kh2),latex(kh1),latex(mo)              
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
                vdc_da_1_d = '\\True Trung vị của mẫu số liệu là $M_e=%s$' %(latex(kqQ2))
                vdc_da_1_s = 'Trung vị của mẫu số liệu là $M_e=%s$' %(latex(1+kqQ2))
                list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
                vdc_da_1=random.choice(list_vdc_da_1)

                vdc_da_2_d = '\\True Tứ phân vị thứ nhất của mẫu số liệu là $Q_1=%s$' %(latex(kqQ1))
                vdc_da_2_s = 'Tứ phân vị thứ nhất của mẫu số liệu là $Q_1=%s$' %(latex(1+kqQ1))
                list_vdc_da_2=[vdc_da_2_d,vdc_da_2_s]
                vdc_da_2=random.choice(list_vdc_da_2)

                vdc_da_3_d = '\\True Tứ phân vị thứ ba của mẫu số liệu là $Q_3=%s$' %(latex(kqQ3))
                vdc_da_3_s = 'Tứ phân vị thứ ba của mẫu số liệu là $Q_3=%s$' %(latex(1+kqQ3))
                list_vdc_da_3=[vdc_da_3_d,vdc_da_3_s]
                vdc_da_3=random.choice(list_vdc_da_3)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_vdc_1 = [vdc_da_1,vdc_da_2,vdc_da_3]

                # Nội dung lời giải
                loigiai_vdc_1 = ('Cỡ mẫu $n=%s$. Giả sử $x_1, x_2, ..., x_{%s}$ là $%s$ số liệu và giả sử dãy số liệu gốc này được sắp xếp theo thứ tự không giảm. \\\\ \n'            
                            'Vì $n=%s$ nên trung vị của mẫu số liệu là $M_e=x_{%s}$ thuộc nhóm $[%s;%s)$. \\\\ \n'
                            '\\hspace*{1cm} Do đó, trung vị là \\\\ \n'
                            '\\hspace*{1cm} $M_e=%s+\\dfrac{\\frac{%s}{2}-%s}{%s} \\cdot %s=%s$.'
                            %(latex(tong),latex(tong),latex(tong),
                            latex(n),latex((n+1)/2),latex(Q2_interval[0]),latex(Q2_interval[1]),
                            latex(Q2_interval[0]),latex(n),latex(total_freq_before_Q2),latex(Q2_interval_frequency),latex(Q2_interval[1]-Q2_interval[0]),latex(kqQ2),          
                            ))
                loigiai_vdc_2 = ('Cỡ mẫu $n=%s$. Giả sử $x_1, x_2, ..., x_{%s}$ là $%s$ số liệu và giả sử dãy số liệu gốc này được sắp xếp theo thứ tự không giảm. \\\\ \n'
                        'Vì $n=%s$ nên tứ phân vị thứ nhất của mẫu số liệu là $x_{%s}$ thuộc nhóm $[%s;%s)$. \\\\ \n'
                        '\\hspace*{1cm} Do đó, tứ phân vị thứ nhất là \\\\ \n'
                        '\\hspace*{1cm} $Q_1=%s+\\dfrac{\\frac{%s}{4}-%s}{%s} \\cdot %s=%s$.'
                            %(latex(tong),latex(tong),latex(tong),               
                            latex(n),latex(n/4+1/4),latex(Q1_interval[0]),latex(Q1_interval[1]),
                            latex(Q1_interval[0]),latex(n),latex(total_freq_before_Q1),latex(Q1_interval_frequency),latex(Q1_interval[1]-Q1_interval[0]),latex(kqQ1),
                            ))
                loigiai_vdc_3 = ('Cỡ mẫu $n=%s$. Giả sử $x_1, x_2, ..., x_{%s}$ là $%s$ số liệu và giả sử dãy số liệu gốc này được sắp xếp theo thứ tự không giảm. \\\\ \n'             
                            'Vì $n=%s$ nên tứ phân vị thứ ba của mẫu số liệu là $x_{%s}$ thuộc nhóm $[%s;%s)$. \\\\ \n'
                            '\\hspace*{1cm} Do đó, tứ phân vị thứ ba là \\\\ \n'
                            '\\hspace*{1cm} $Q_3=%s+\\dfrac{\\frac{3 \\cdot %s}{4}-%s}{%s} \\cdot %s=%s$.'
                            %(latex(tong),latex(tong),latex(tong),                           
                            latex(n),latex(3*n/4+3/4),latex(Q3_interval[0]),latex(Q3_interval[1]),
                            latex(Q3_interval[0]),latex(n),latex(total_freq_before_Q3),latex(Q3_interval_frequency),latex(Q3_interval[1]-Q3_interval[0]),latex(kqQ3),                         
                            ))

                # Đưa các lời giải vào danh sách lời giải
                list_vdc_2 = [loigiai_vdc_1,loigiai_vdc_2,loigiai_vdc_3]

                # Kết hợp các đáp án và lời giải vào cùng một danh sách
                combined_vdc = list(zip(list_vdc_1, list_vdc_2))

                # Xáo trộn danh sách kết hợp
                random.shuffle(combined_vdc)

                # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
                shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            if dang=='1': #tổng lẻ - chia đôi hai bên chẵn
                # Khai báo biến
                lisv=[20,25,30,35,40]
                v = random.choice(lisv)

                # Vòng lặp để tạo tổng thỏa mãn điều kiện
                while True:
                    xe_values = random.sample(range(1,11), 5)
                    xe1, xe2, xe3, xe4, xe5 = xe_values
                    tong = xe1 + xe2 + xe3 + xe4 + xe5
                    tong1 = (tong - 1) / 2

                    # Kiểm tra điều kiện thoát vòng lặp
                    if tong % 2 != 0 and tong1 % 2 == 0:
                        break   

                # Chọn giá trị k ngẫu nhiên
                lisk=[1,2,3,4]
                k = random.choice(lisk)

                x1=Rational(v+v+k,2)
                x2=Rational(v+k+v+2*k,2)
                x3=Rational(v+2*k+v+3*k,2)
                x4=Rational(v+3*k+v+4*k,2)
                x5=Rational(v+4*k+v+5*k,2)

                nhom=randint(1,5)
                listanso=[xe1,xe2,xe3,xe4,xe5]

                xtb=Rational(xe1*x1+xe2*x2+xe3*x3+xe4*x4+xe5*x5,tong)

                # Tạo danh sách số liệu gốc
                data = []
                data.extend([v] * xe1)
                data.extend([v + k] * xe2)
                data.extend([v + 2 * k] * xe3)
                data.extend([v + 3 * k] * xe4)
                data.extend([v + 4 * k] * xe5)

                # Sắp xếp danh sách
                data.sort()

                # Tính toán vị trí Q1
                n = len(data)
                Q1_index = (n + 1) / 4

                if Q1_index.is_integer():
                    Q1 = data[int(Q1_index) - 1]
                else:
                    lower_index = int(Q1_index) - 1
                    upper_index = lower_index + 1
                    Q1 = (data[lower_index] + data[upper_index]) / 2

                # Tính toán vị trí Q2 (Median)
                Q2_index = (n + 1) / 2

                if Q2_index.is_integer():
                    Q2 = data[int(Q2_index) - 1]
                else:
                    lower_index = int(Q2_index) - 1
                    upper_index = lower_index + 1
                    Q2 = (data[lower_index] + data[upper_index]) / 2

                # Tính toán vị trí Q3
                Q3_index = 3 * (n + 1) / 4

                if Q3_index.is_integer():
                    Q3 = data[int(Q3_index) - 1]
                else:
                    lower_index = int(Q3_index) - 1
                    upper_index = lower_index + 1
                    Q3 = (data[lower_index] + data[upper_index]) / 2

                # Tạo danh sách các khoảng và tần số tương ứng
                intervals = [(v, v + k), (v + k, v + 2 * k), (v + 2 * k, v + 3 * k), (v + 3 * k, v + 4 * k), (v + 4 * k, v + 5 * k)]
                frequencies = [xe1, xe2, xe3, xe4, xe5]

                # Tìm khoảng chứa Q1, Q2 và Q3
                Q1_interval, Q2_interval, Q3_interval = None, None, None
                Q1_interval_index, Q2_interval_index, Q3_interval_index = None, None, None

                for i, (start, end) in enumerate(intervals):
                    if start <= Q1 < end:
                        Q1_interval = (start, end)
                        Q1_interval_index = i
                    if start <= Q2 < end:
                        Q2_interval = (start, end)
                        Q2_interval_index = i
                    if start <= Q3 < end:
                        Q3_interval = (start, end)
                        Q3_interval_index = i

                # Tính tổng tần số đến trước khoảng chứa Q1, Q2 và Q3
                total_freq_before_Q1 = sum(frequencies[:Q1_interval_index]) if Q1_interval_index is not None else 0
                total_freq_before_Q2 = sum(frequencies[:Q2_interval_index]) if Q2_interval_index is not None else 0
                total_freq_before_Q3 = sum(frequencies[:Q3_interval_index]) if Q3_interval_index is not None else 0

                # Tìm tần số tương ứng với khoảng chứa Q1, Q2 và Q3
                Q1_interval_frequency = frequencies[Q1_interval_index] if Q1_interval_index is not None else 0
                Q2_interval_frequency = frequencies[Q2_interval_index] if Q2_interval_index is not None else 0
                Q3_interval_frequency = frequencies[Q3_interval_index] if Q3_interval_index is not None else 0

                # Tính toán kết quả Q1, Q2 và Q3
                kqQ1 = Q1_interval[0] + Rational(1 * n / 4 - total_freq_before_Q1, Q1_interval_frequency) * (Q1_interval[1] - Q1_interval[0])
                kqQ2 = Q2_interval[0] + Rational(2 * n / 4 - total_freq_before_Q2, Q2_interval_frequency) * (Q2_interval[1] - Q2_interval[0])
                kqQ3 = Q3_interval[0] + Rational(3 * n / 4 - total_freq_before_Q3, Q3_interval_frequency) * (Q3_interval[1] - Q3_interval[0])

                # Kết quả
                kq = kqQ3 - kqQ1

                # Giả sử max_value đã được xác định từ xe1, xe2, xe3, xe4, xe5
                max_xe = max(xe1, xe2, xe3, xe4, xe5)

                # Tìm khoảng chứa max_xe
                if max_xe == xe1:
                    kh1 = v  
                    kh2 = v+k
                elif max_xe == xe2:
                    kh1 = v+k
                    kh2 = v+2*k
                elif max_xe == xe3:
                    kh1 = v+2*k
                    kh2 = v+3*k
                elif max_xe == xe4:
                    kh1 = v+3*k
                    kh2 = v+4*k
                elif max_xe == xe5:
                    kh1 = v+4*k
                    kh2 = v+5*k 


                # Gán giá trị trước và sau max_xe cho m và n
                if max_xe == xe1:
                    m = 0  # Không có giá trị trước
                    n1 = xe2
                elif max_xe == xe2:
                    m = xe1
                    n1 = xe3
                elif max_xe == xe3:
                    m = xe2
                    n1 = xe4
                elif max_xe == xe4:
                    m = xe3
                    n1 = xe5
                elif max_xe == xe5:
                    m = xe4
                    n1 = 0 # Không có giá trị sau

                mo=kh1+Rational(max_xe-m,max_xe-m+max_xe-n1)*(kh2-kh1)

                # Nội dung câu hỏi
                noidungcauhoi = ('Chiều cao (đơn vị: centimet) của các học sinh lớp 11B được cho trong bảng sau \n'            
                                '\\begin{center} \n'
                                '\\begin{tabular}{|c|c|} \n'
                                '\\hline \n'
                                'Chiều cao (cm) & Số học sinh \\\\ \n'
                                '\\hline \n'
                                '$[%s; %s)$ & $%s$ \\\\ \n'
                                '\\hline \n'
                                '$[%s, %s)$ & $%s$ \\\\ \n'
                                '\\hline \n'
                                '$[%s; %s)$ & $%s$ \\\\ \n'
                                '\\hline \n'
                                '$[%s; %s)$ & $%s$ \\\\ \n'
                                '\\hline \n'
                                '$[%s; %s)$ & $%s$ \\\\ \n'
                                '\\hline \n'
                                '& $n=%s$ \\\\ \n'
                                '\\hline \n'
                                '\\end{tabular} \n'
                                '\\end{center} \n'
                                %(
                                latex(v),latex(v+k),latex(xe1),
                                latex(v+k),latex(v+2*k),latex(xe2),
                                latex(v+2*k),latex(v+3*k),latex(xe3),
                                latex(v+3*k),latex(v+4*k),latex(xe4),
                                latex(v+4*k),latex(v+5*k),latex(xe5),
                                latex(tong),
                                ))

                ######################################################################## Nhận biết ############################################
                # Các đáp án
                nb_da_1_d = '\\True Giá trị đại diện của nhóm $[%s;%s)$ là $%s$' %(latex(v+2*k),latex(v+3*k),latex(xe3))
                nb_da_1_s = 'Giá trị đại diện của nhóm $[%s;%s)$ là $%s$' %(latex(v+2*k),latex(v+3*k),latex(1+xe3))
                list_nb_da_1=[nb_da_1_d,nb_da_1_s]
                nb_da_1=random.choice(list_nb_da_1)

                nb_da_2_d = '\\True Cỡ mẫu là $n=%s$' %(latex(tong))
                nb_da_2_s = 'Cỡ mẫu là $n=%s$' %(latex(tong-1))
                list_nb_da_2=[nb_da_2_d,nb_da_2_s]
                nb_da_2=random.choice(list_nb_da_2)

                nb_da_3_d = '\\True Tần số của nhóm $[%s;%s)$ là $m=%s$'%(latex(v+2*k),latex(v+3*k),latex(xe3))
                nb_da_3_s = 'Tần số của nhóm $[%s;%s)$ là $m=%s$'%(latex(v+2*k),latex(v+3*k),latex(1+xe3))
                list_nb_da_3=[nb_da_3_d,nb_da_3_s]
                nb_da_3=random.choice(list_nb_da_3)

                nb_da_4_d = '\\True Độ dài của nhóm $[%s;%s)$ là $%s$'%(latex(v+2*k),latex(v+3*k),latex(k))
                nb_da_4_s = 'Độ dài của nhóm $[%s;%s)$ là $%s$'%(latex(v+2*k),latex(v+3*k),latex(1+k))
                list_nb_da_4=[nb_da_4_d,nb_da_4_s]
                nb_da_4=random.choice(list_nb_da_4)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_nb_1 = [nb_da_1, nb_da_2,nb_da_3,nb_da_4]

                # Nội dung lời giải
                loigiai_nb_1 = ('Áp dụng công thức $x_i=\\dfrac{a_i+a_{i+1}}{2}$ với $i=1,2,3,4,5$, ta có \\\\ \n'
                                'Giá trị đại diện của nhóm $[%s;%s)$ là $%s$.'
                                %(latex(v+2*k),latex(v+3*k),latex(xe3)
                                ))
                loigiai_nb_2 = ('Cỡ mẫu là \\\\ \n'
                                '\\hspace*{1cm} $n=%s+%s+%s+%s+%s=%s$.'
                                %(latex(xe1),latex(xe2),latex(xe3),latex(xe4),latex(xe5),latex(tong)
                                ))
                loigiai_nb_3 = ('Tần số của nhóm $[%s;%s)$ là $m=%s$.'
                                %(latex(v+2*k),latex(v+3*k),latex(xe3)
                                ))
                loigiai_nb_4 = ('Độ dài của nhóm $[%s;%s)$ là $%s$.'
                                %(latex(v+2*k),latex(v+3*k),latex(k)
                                ))

                # Đưa các lời giải vào danh sách lời giải
                list_nb_2 = [loigiai_nb_1, loigiai_nb_2,loigiai_nb_3,loigiai_nb_4]

                # Kết hợp các đáp án và lời giải vào cùng một danh sách
                combined_nb = list(zip(list_nb_1, list_nb_2))

                # Xáo trộn danh sách kết hợp
                random.shuffle(combined_nb)

                # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
                shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

                ######################################################################## Thông hiểu ############################################
                # Các đáp án
                th_da_1_d = '\\True Số trung bình của mẫu số liệu là $\\bar{x}=%s$' %(latex(xtb))
                th_da_1_s = 'Số trung bình của mẫu số liệu là $\\bar{x}=%s$' %(latex(xtb+1))
                list_th_da_1=[th_da_1_d,th_da_1_s]
                th_da_1=random.choice(list_th_da_1)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_th_1 = [th_da_1]

                # Nội dung lời giải
                loigiai_th_1 = ('Cỡ mẫu là $n=%s+%s+%s+%s+%s=%s$. \\\\ \n'
                                'Giá trị đại điện của các nhóm là \\\\ \n'
                                '\\hspace*{1cm} $x_1=%s, x_2=%s, x_3=%s, x_4=%s, x_5=%s$. \\\\ \n'
                                'Số trung bình của mẫu số liệu là \\\\ \n'
                                '\\hspace*{1cm} $\\bar{x}=\\dfrac{%s \\cdot %s+%s \\cdot %s+%s \\cdot %s+%s \\cdot %s+%s \\cdot %s}{%s}=%s$.'
                                %(latex(xe1),latex(xe2),latex(xe3),latex(xe4),latex(xe5),latex(tong),
                                    latex(x1),latex(x2),latex(x3),latex(x4),latex(x5),
                                latex(xe1),latex(x1),latex(xe2),latex(x2),latex(xe3),latex(x3),latex(xe4),latex(x4),latex(xe5),latex(x5),latex(tong),latex(xtb)               
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
                vd_da_1_d = '\\True Mốt của mẫu số liệu là $M_o=%s$' %(latex(mo))
                vd_da_1_s = 'Mốt của mẫu số liệu là $M_o=%s$' %(latex(mo+1))
                list_vd_da_1=[vd_da_1_d,vd_da_1_s]
                vd_da_1=random.choice(list_vd_da_1)


                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_vd_1 = [vd_da_1]

                # Nội dung lời giải
                loigiai_vd_1 = ('Tần số lớn nhất là $%s$ nên nhóm chứa mốt là nhóm $[%s; %s)$. \\\\ \n'
                                'Ta có \\\\ \n'
                                '\\hspace*{1cm} $M_o=%s+\\dfrac{%s-%s}{(%s-%s)+(%s-%s)} \\cdot (%s-%s)=%s$.'
                                %(latex(max_xe),latex(kh1),latex(kh2),
                                latex(kh1),latex(max_xe),latex(m),latex(max_xe),latex(m),latex(max_xe),latex(n1),latex(kh2),latex(kh1),latex(mo)              
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
                vdc_da_1_d = '\\True Trung vị của mẫu số liệu là $M_e=%s$' %(latex(kqQ2))
                vdc_da_1_s = 'Trung vị của mẫu số liệu là $M_e=%s$' %(latex(1+kqQ2))
                list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
                vdc_da_1=random.choice(list_vdc_da_1)

                vdc_da_2_d = '\\True Tứ phân vị thứ nhất của mẫu số liệu là $Q_1=%s$' %(latex(kqQ1))
                vdc_da_2_s = 'Tứ phân vị thứ nhất của mẫu số liệu là $Q_1=%s$' %(latex(1+kqQ1))
                list_vdc_da_2=[vdc_da_2_d,vdc_da_2_s]
                vdc_da_2=random.choice(list_vdc_da_2)

                vdc_da_3_d = '\\True Tứ phân vị thứ ba của mẫu số liệu là $Q_3=%s$' %(latex(kqQ3))
                vdc_da_3_s = 'Tứ phân vị thứ ba của mẫu số liệu là $Q_3=%s$' %(latex(1+kqQ3))
                list_vdc_da_3=[vdc_da_3_d,vdc_da_3_s]
                vdc_da_3=random.choice(list_vdc_da_3)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_vdc_1 = [vdc_da_1,vdc_da_2,vdc_da_3]

                # Nội dung lời giải
                loigiai_vdc_1 = ('Cỡ mẫu $n=%s$. Giả sử $x_1, x_2, ..., x_{%s}$ là $%s$ số liệu và giả sử dãy số liệu gốc này được sắp xếp theo thứ tự không giảm. \\\\ \n'            
                            'Vì $n=%s$ nên trung vị của mẫu số liệu là $M_e=x_{%s}$ thuộc nhóm $[%s;%s)$. \\\\ \n'
                            '\\hspace*{1cm} Do đó, trung vị là \\\\ \n'
                            '\\hspace*{1cm} $M_e=%s+\\dfrac{\\frac{%s}{2}-%s}{%s} \\cdot %s=%s$.'
                            %(latex(tong),latex(tong),latex(tong),
                            latex(n),latex((n+1)/2),latex(Q2_interval[0]),latex(Q2_interval[1]),
                            latex(Q2_interval[0]),latex(n),latex(total_freq_before_Q2),latex(Q2_interval_frequency),latex(Q2_interval[1]-Q2_interval[0]),latex(kqQ2),           
                            ))
                loigiai_vdc_2 = ('Cỡ mẫu $n=%s$. Giả sử $x_1, x_2, ..., x_{%s}$ là $%s$ số liệu và giả sử dãy số liệu gốc này được sắp xếp theo thứ tự không giảm. \\\\ \n'
                            'Vì $n=%s$ nên tứ phân vị thứ nhất của mẫu số liệu là $Q_1=\\dfrac{x_{%s}+x_{%s}}{2}$ thuộc nhóm $[%s;%s)$. \\\\ \n'
                            '\\hspace*{1cm} Do đó, tứ phân vị thứ nhất là \\\\ \n'
                            '\\hspace*{1cm} $Q_1=%s+\\dfrac{\\frac{%s}{4}-%s}{%s} \\cdot %s=%s$.'
                            %(latex(tong),latex(tong),latex(tong),               
                            latex(n),latex(n/4-1/4),latex(n/4-1/4+1),latex(Q1_interval[0]),latex(Q1_interval[1]),
                            latex(Q1_interval[0]),latex(n),latex(total_freq_before_Q1),latex(Q1_interval_frequency),latex(Q1_interval[1]-Q1_interval[0]),latex(kqQ1),
                            ))
                loigiai_vdc_3 = ('Cỡ mẫu $n=%s$. Giả sử $x_1, x_2, ..., x_{%s}$ là $%s$ số liệu và giả sử dãy số liệu gốc này được sắp xếp theo thứ tự không giảm. \\\\ \n'             
                            'Vì $n=%s$ nên tứ phân vị thứ ba của mẫu số liệu là $Q_3=\\dfrac{x_{%s}+x_{%s}}{2}$ thuộc nhóm $[%s;%s)$. \\\\ \n'
                            '\\hspace*{1cm} Do đó, tứ phân vị thứ ba là \\\\ \n'
                            '\\hspace*{1cm} $Q_3=%s+\\dfrac{\\frac{3 \\cdot %s}{4}-%s}{%s} \\cdot %s=%s$.'
                            %(latex(tong),latex(tong),latex(tong),                           
                            latex(n),latex(3*n/4+1/4),latex(3*n/4+1/4+1),latex(Q3_interval[0]),latex(Q3_interval[1]),
                            latex(Q3_interval[0]),latex(n),latex(total_freq_before_Q3),latex(Q3_interval_frequency),latex(Q3_interval[1]-Q3_interval[0]),latex(kqQ3),                          
                            ))

                # Đưa các lời giải vào danh sách lời giải
                list_vdc_2 = [loigiai_vdc_1,loigiai_vdc_2,loigiai_vdc_3]

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
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac','\\dfrac').replace('.0','')
            return content

