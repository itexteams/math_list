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


def bt_dang19_p2_b1_c2_ds11(self):
            # Khai báo biến
            # Khai báo biến và chọn tham số ngẫu nhiên dưới dạng phân số
            B0_val = random.choice([100, 120, 150, 200])  # Khối lượng chất thải ban đầu (kg)
            p_val = random.choice([10, 20, 25])           # Tỷ lệ giảm mỗi tuần (%)
            C_val = random.choice([10, 12, 15, 20])       # Khối lượng bón thêm mỗi tuần (kg)

            B0 = Rational(B0_val, 1)
            C = Rational(C_val, 1)
            p_rat = Rational(p_val, 100)
            q_rat = Rational(100 - p_val, 100)            # Tỷ lệ còn lại (phân số)
            one_minus_q = Rational(p_val, 100)

            # Các giá trị tính toán theo phân số
            b1 = B0 * q_rat + C                           # b_1
            b1_wrong = b1 + Rational(5, 1)                 # Giá trị sai cho nhiễu
            b2 = b1 * q_rat + C                           # b_2
            b3 = b2 * q_rat + C                           # b_3
            b3_wrong = b3 + Rational(2, 1)                 # Giá trị sai cho VDC

            L_rat = C / one_minus_q                       # Giới hạn chặn dưới L = C / (1 - q)
            diff_b1_L = b1 - L_rat                        # b1 - L

            # Nội dung câu hỏi
            noidungcauhoi = ('''Để cải tạo đất, trang trại bón vào đất %s kg chất thải hữu cơ đã qua xử lý. Dưới tác động của vi sinh vật, mỗi tuần khối lượng chất thải còn lại trong đất giảm đi %s\\%% so với tuần trước, đồng thời vào cuối mỗi tuần trang trại lại bón thêm cố định %s kg chất thải hữu cơ mới. Gọi $b_n$ (đơn vị: kg) là khối lượng chất thải hữu cơ có trong đất ở cuối tuần thứ $n$ ($n \\ge 1$).'''
                             % (latex(B0), p_val, latex(C)))

            ########################################################################
            # Nhận biết ############################################
            nb_da_1_d = '\\True Công thức truy hồi biểu diễn $b_{n+1}$ theo $b_n$ là $b_{n+1} = %s b_n + %s$ với $b_1 = %s$ kg' % (latex(q_rat), latex(C), latex(b1))
            nb_da_1_s = 'Công thức truy hồi biểu diễn $b_{n+1}$ theo $b_n$ là $b_{n+1} = %s b_n + %s$ với $b_1 = %s$ kg' % (latex(q_rat), latex(C), latex(b1_wrong))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            list_nb_1 = [nb_da_1]

            loigiai_nb_1 = ('''Khối lượng chất thải hữu cơ ở cuối tuần thứ nhất là: \\\\
            $b_1 = %s \\cdot \\left(1 - %s\\right) + %s = %s \\cdot %s + %s = %s$ (kg). \\\\
            Ở cuối tuần thứ $n+1$, khối lượng chất thải còn lại từ tuần thứ $n$ là $\\left(1 - %s\\right) b_n = %s b_n$, sau đó bón thêm %s kg nên ta có công thức truy hồi: \\\\
            $b_{n+1} = %s b_n + %s$ với mọi $n \\ge 1$.'''
                            % (latex(B0), latex(p_rat), latex(C), latex(B0), latex(q_rat), latex(C), latex(b1), latex(p_rat), latex(q_rat), latex(C), latex(q_rat), latex(C)))

            list_nb_2 = [loigiai_nb_1]

            combined_nb = list(zip(list_nb_1, list_nb_2))
            random.shuffle(combined_nb)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ########################################################################
            # Thông hiểu ############################################
            th_da_1_d = '\\True Dãy số $(b_n)$ là một dãy số giảm'
            th_da_1_s = 'Dãy số $(b_n)$ là một dãy số tăng'
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            list_th_1 = [th_da_1]

            loigiai_th_1 = ('''Xét hiệu $b_{n+1} - b_n = \\left(%s b_n + %s\\right) - b_n = -%s b_n + %s = -%s\\left(b_n - %s\\right)$. \\\\
            Ta có công thức tổng quát $b_n = %s + %s \\cdot \\left(%s\\right)^{n-1}$. \\\\
            Vì $b_n > %s$ với mọi $n \\ge 1$ nên $b_{n+1} - b_n < 0$ với mọi $n \\ge 1$. \\\\
            Vậy $(b_n)$ là một dãy số giảm.'''
                            % (latex(q_rat), latex(C), latex(one_minus_q), latex(C), latex(one_minus_q), latex(L_rat), latex(L_rat), latex(diff_b1_L), latex(q_rat), latex(L_rat)))

            list_th_2 = [loigiai_th_1]

            combined_th = list(zip(list_th_1, list_th_2))
            random.shuffle(combined_th)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ########################################################################
            # Vận dụng ############################################
            vd_da_1_d = '\\True Dãy số $(b_n)$ là dãy số bị chặn, cụ thể $%s < b_n \\le %s$ với mọi $n \\ge 1$' % (latex(L_rat), latex(b1))
            vd_da_1_s = 'Dãy số $(b_n)$ là dãy số bị chặn, cụ thể $0 < b_n \\le %s$ với mọi $n \\ge 1$' % latex(b1)
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            list_vd_1 = [vd_da_1]

            loigiai_vd_1 = ('''Do $(b_n)$ là dãy số giảm nên $b_n \\le b_1 = %s$ với mọi $n \\ge 1$. \\\\
            Mặt khác, $b_n = %s + %s \\cdot \\left(%s\\right)^{n-1} > %s$ do $\\left(%s\\right)^{n-1} > 0$ với mọi $n \\ge 1$. \\\\
            Vậy $%s < b_n \\le %s$ với mọi $n \\ge 1$, tức là dãy số $(b_n)$ bị chặn.'''
                            % (latex(b1), latex(L_rat), latex(diff_b1_L), latex(q_rat), latex(L_rat), latex(q_rat), latex(L_rat), latex(b1)))

            list_vd_2 = [loigiai_vd_1]

            combined_vd = list(zip(list_vd_1, list_vd_2))
            random.shuffle(combined_vd)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ########################################################################
            # Vận dụng cao ############################################
            vdc_da_1_d = '\\True Khối lượng chất thải hữu cơ có trong đất ở cuối tuần thứ 3 là $%s$ kg' % latex(b3)
            vdc_da_1_s = 'Khối lượng chất thải hữu cơ có trong đất ở cuối tuần thứ 3 là $%s$ kg' % latex(b3_wrong)
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            list_vdc_1 = [vdc_da_1]

            loigiai_vdc_1 = ('''Sử dụng công thức truy hồi $b_{n+1} = %s b_n + %s$: \\\\
            Cuối tuần thứ nhất: $b_1 = %s$ (kg). \\\\
            Cuối tuần thứ hai: $b_2 = %s \\cdot %s + %s = %s$ (kg). \\\\
            Cuối tuần thứ ba: $b_3 = %s \\cdot %s + %s = %s$ (kg). \\\\
            Vậy khối lượng chất thải hữu cơ có trong đất ở cuối tuần thứ 3 là $%s$ kg.'''
                             % (latex(q_rat), latex(C), latex(b1), latex(q_rat), latex(b1), latex(C), latex(b2), latex(q_rat), latex(b2), latex(C), latex(b3), latex(b3)))

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
            str(noidungcauhoi)+ 
                '\n\\choiceTFn \n'
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
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

