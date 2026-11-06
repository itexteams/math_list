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


def bt_dang15_p2_b3_c2_ds11(self):
            # Khai báo biến
            # Khai báo biến và sinh dữ liệu ngẫu nhiên
            u1_val = randint(2, 5)
            q_val = randint(3, 5)
            d_val = randint(1, 4)

            c_val = Rational(d_val, q_val - 1)
            v1_val = u1_val - c_val

            u_list = [u1_val]
            for _ in range(7):
                u_list.append(q_val * u_list[-1] - d_val)

            u2_val = u_list[1]
            u3_val = u_list[2]
            u4_val = u_list[3]
            u5_val = u_list[4]
            S8_val = sum(u_list)

            c_latex = latex(c_val)
            v1_latex = latex(v1_val)
            u5_latex = latex(u5_val)
            S8_latex = latex(S8_val)

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho dãy số $(u_n)$, biết $\\begin{cases} u_1 = %s \\\\ u_{n+1} = %s u_n - %s \\end{cases}$.'''
                             % (latex(u1_val), latex(q_val), latex(d_val)))

            ########################################################################
            # Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True Số hạng thứ năm của dãy số là $%s$' % (u5_latex)
            nb_da_1_s = 'Số hạng thứ năm của dãy số là $%s$' % (latex(u5_val + 2))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('''Ta có:\\\\
            $u_1 = %s$\\\\
            $u_2 = %s \\cdot %s - %s = %s$\\\\
            $u_3 = %s \\cdot %s - %s = %s$\\\\
            $u_4 = %s \\cdot %s - %s = %s$\\\\
            $u_5 = %s \\cdot %s - %s = %s$.\\\\
            Vậy số hạng thứ năm của dãy số là $%s$.'''
                            % (latex(u1_val),
                               latex(q_val), latex(u1_val), latex(d_val), latex(u2_val),
                               latex(q_val), latex(u2_val), latex(d_val), latex(u3_val),
                               latex(q_val), latex(u3_val), latex(d_val), latex(u4_val),
                               latex(q_val), latex(u4_val), latex(d_val), latex(u5_val),
                               latex(u5_val)))

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
            th_da_1_d = '\\True Đặt $v_n = u_n - %s$. Ta có $(v_n)$ là cấp số nhân' % (c_latex)
            th_da_1_s = 'Đặt $v_n = u_n - %s$. Ta có $(v_n)$ không phải là cấp số nhân' % (c_latex)
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('''Đặt $v_n = u_n - %s$, ta có:\\\\
            $v_{n+1} = u_{n+1} - %s = %s u_n - %s - %s = %s \\left( u_n - %s \\right) = %s v_n$.\\\\
            Do đó $(v_n)$ là một cấp số nhân với công bội $q = %s$.'''
                            % (c_latex, c_latex, latex(q_val), latex(d_val), c_latex, latex(q_val), c_latex, latex(q_val), latex(q_val)))

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
            vd_da_1_d = '\\True Số hạng tổng quát $u_n = %s \\cdot %s^{n-1} + %s$' % (v1_latex, latex(q_val), c_latex)
            vd_da_1_s = 'Số hạng tổng quát $u_n = %s \\cdot %s^{n-1} - %s$' % (v1_latex, latex(q_val), c_latex)
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('''Ta có $v_1 = u_1 - %s = %s - %s = %s$.\\\\
            Dãy số $(v_n)$ là cấp số nhân có số hạng đầu $v_1 = %s$ và công bội $q = %s$ nên có số hạng tổng quát là:\\\\
            $v_n = %s \\cdot %s^{n-1}$.\\\\
            Suy ra $u_n = v_n + %s = %s \\cdot %s^{n-1} + %s$.'''
                            % (c_latex, latex(u1_val), c_latex, v1_latex, v1_latex, latex(q_val), v1_latex, latex(q_val), c_latex, v1_latex, latex(q_val), c_latex))

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
            vdc_da_1_d = '\\True Ta có $S_8 = %s$' % (S8_latex)
            vdc_da_1_s = 'Ta có $S_8 = %s$' % (latex(S8_val + 100))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = ('''Tổng $8$ số hạng đầu tiên của dãy số $(u_n)$ là:\\\\
            $S_8 = u_1 + u_2 + \\dots + u_8 = \\sum_{k=1}^{8} \\left( %s \\cdot %s^{k-1} + %s \\right)\\\\
            = %s \\cdot \\frac{%s^8 - 1}{%s - 1} + 8 \\cdot %s = %s$.'''
                             % (v1_latex, latex(q_val), c_latex, v1_latex, latex(q_val), latex(q_val), c_latex, S8_latex))

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
                       '\\begin{ex}\n' +
                       str(noidungcauhoi) + 
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

