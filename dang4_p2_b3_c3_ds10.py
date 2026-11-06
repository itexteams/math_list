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


def bt_dang4_p2_b3_c3_ds10(self):
            # Khai báo biến
            # Khai báo hàm đếm số đáp án đúng
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            ######################################################################## Xử lý Data Random ########################

            # Sinh ngẫu nhiên 15 số liệu (khối lượng từ 40 đến 75) và sắp xếp tăng dần
            data = sorted([random.randint(40, 75) for _ in range(15)])

            # Tính toán các đại lượng thống kê thực tế
            min_val = data[0]
            max_val = data[-1]
            R = max_val - min_val

            Q1 = data[3]   # Phần tử thứ 4 (index 3)
            Q2 = data[7]   # Phần tử thứ 8 (index 7)
            Q3 = data[11]  # Phần tử thứ 12 (index 11)

            delta_Q = Q3 - Q1

            # Chuỗi số liệu để in ra đề bài
            data_str_display = " \\quad ".join(map(str, data))

            # Nội dung câu hỏi
            noidungcauhoi = f"Mẫu số liệu sau cho biết khối lượng (kg) của 15 trẻ trong độ tuổi dậy thì:\\\\ {data_str_display}."

            ######################################################################## Nhận biết ############################################

            # Đáp án sai ngẫu nhiên cho R
            R_fake = R + random.choice([-5, -3, 2, 4])
            if R_fake == R: R_fake += 1

            # Các đáp án
            nb_da_1_d = f'\\True Khoảng biến thiên $R = {R}$'
            nb_da_1_s = f'Khoảng biến thiên $R = {R_fake}$'
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

            # Nội dung lời giải
            loigiai_nb_1 = (f"Giá trị lớn nhất và nhỏ nhất là $x_{{max}} = {max_val}, x_{{min}} = {min_val}$;\\\\"
                            f"Suy ra khoảng biến thiên $R = x_{{max}} - x_{{min}} = {R}$.")
            list_nb_2 = [loigiai_nb_1]

            ######################################################################## Thông hiểu ############################################

            # Đáp án sai ngẫu nhiên cho Q2
            Q2_fake = Q2 + random.choice([-2, -1, 1, 2])
            if Q2_fake == Q2: Q2_fake += 3

            # Các đáp án
            th_da_1_d = f'\\True Trung vị của mẫu là ${Q2}$'
            th_da_1_s = f'Trung vị của mẫu là ${Q2_fake}$'
            list_th_da_1 = [th_da_1_d, th_da_1_s]

            # Nội dung lời giải
            loigiai_th_1 = f"Tứ phân vị thứ hai của mẫu cũng là trung vị của mẫu: $Q_2 = {Q2}$."
            list_th_2 = [loigiai_th_1]

            ######################################################################## Vận dụng ############################################

            # Đáp án sai ngẫu nhiên cho Q1
            Q1_fake = Q1 + random.choice([-2, -1, 2, 3])
            if Q1_fake == Q1: Q1_fake -= 2

            # Các đáp án
            vd_da_1_d = f'\\True Tứ phân vị thứ nhất là $Q_1 = {Q1}$'
            vd_da_1_s = f'Tứ phân vị thứ nhất là $Q_1 = {Q1_fake}$'
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

            # Nội dung lời giải
            loigiai_vd_1 = f"Tứ phân vị thứ nhất là trung vị nửa mẫu bên trái (không kể $Q_2$): $Q_1 = {Q1}$."
            list_vd_2 = [loigiai_vd_1]

            ######################################################################## Vận dụng cao ########################################

            # Đáp án sai ngẫu nhiên cho delta_Q
            delta_Q_fake = delta_Q + random.choice([-3, -2, 2, 3])
            if delta_Q_fake == delta_Q: delta_Q_fake += 1

            vdc_da_1_d = f'\\True Khoảng tứ phân vị là $\\Delta_Q = {delta_Q}$'
            vdc_da_1_s = f'Khoảng tứ phân vị là $\\Delta_Q = {delta_Q_fake}$'
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

            # Nội dung lời giải
            loigiai_vdc_1 = (f"Tứ phân vị thứ ba là trung vị nửa mẫu bên phải (không kể $Q_2$): $Q_3 = {Q3}$.\\\\"
                             f"Do đó khoảng tứ phân vị là: $\\Delta_Q = Q_3 - Q_1 = {Q3} - {Q1} = {delta_Q}$.")
            list_vdc_2 = [loigiai_vdc_1]

            ######################################################################## Xáo trộn và in kết quả ###############################

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
                str(noidungcauhoi)+ '\n'
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
                '\\end{ex}\n'
                '\\end{minipage}\n\n')
            return content

