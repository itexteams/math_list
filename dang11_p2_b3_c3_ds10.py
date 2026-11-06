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


def bt_dang11_p2_b3_c3_ds10(self):
            # Khai báo biến
            # Khai báo hàm đếm số đáp án đúng
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            ######################################################################## Xử lý Data Random ########################

            # Random dữ liệu Hà Nội (Mẫu 1) - Rải đều
            R_target = random.randint(10, 15) # Khoảng biến thiên mục tiêu
            HN_min = random.randint(20, 25)
            HN_max = HN_min + R_target
            HN_mid = sorted([random.randint(HN_min + 2, HN_max - 2) for _ in range(5)])
            data_HN = [HN_min] + HN_mid + [HN_max]

            # Random dữ liệu Điện Biên (Mẫu 2) - Có giá trị ngoại lệ
            DB_range_tight = random.randint(3, 6) # Khoảng biến thiên nếu bỏ giá trị nhỏ nhất
            DB_2 = random.randint(22, 26) # Nhiệt độ của ngày thứ 2
            DB_max = DB_2 + DB_range_tight
            DB_min = DB_max - R_target # Ép R_DB = R_HN
            DB_mid = sorted([random.randint(DB_2, DB_max) for _ in range(4)])
            data_DB = [DB_min, DB_2] + DB_mid + [DB_max]
            data_DB = sorted(data_DB) # Đảm bảo sắp xếp tăng dần

            # Tính toán các đại lượng cho Hà Nội
            R_HN = data_HN[-1] - data_HN[0]
            Q1_HN = data_HN[1]
            Q2_HN = data_HN[3]
            Q3_HN = data_HN[5]
            IQR_HN = Q3_HN - Q1_HN

            # Tính toán các đại lượng cho Điện Biên
            R_DB = data_DB[-1] - data_DB[0]
            R_DB_new = data_DB[-1] - data_DB[1] # Khoảng biến thiên khi bỏ giá trị nhỏ nhất
            Q1_DB = data_DB[1]
            Q2_DB = data_DB[3]
            Q3_DB = data_DB[5]
            IQR_DB = Q3_DB - Q1_DB

            # Chuỗi số liệu để hiển thị
            str_HN = " \\quad ".join(map(str, data_HN))
            str_DB = " \\quad ".join(map(str, data_DB))

            # Nội dung câu hỏi
            noidungcauhoi = f'''Trong một tuần, nhiệt độ cao nhất trong ngày (đơn vị $^\\circ C$) tại hai thành phố Hà Nội và Điện Biên như sau:
            \\begin{{center}}
            \\begin{{tabular}}{{ll}}
            Hà Nội: & {str_HN} \\\\
            Điện Biên: & {str_DB}
            \\end{{tabular}}
            \\end{{center}}'''

            ######################################################################## Nhận biết ############################################

            # Các đáp án
            nb_da_1_d = '\\True Khoảng biến thiên nhiệt độ cao nhất trong ngày của Hà Nội và Điện Biên là giống nhau'
            nb_da_1_s = 'Khoảng biến thiên nhiệt độ cao nhất trong ngày của Hà Nội lớn hơn của Điện Biên'
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

            # Nội dung lời giải
            loigiai_nb_1 = (f"Khoảng biến thiên của hai mẫu số liệu:\\\\"
                            f"+ Hà Nội: $R_1 = {data_HN[-1]} - {data_HN[0]} = {R_HN}$\\\\"
                            f"+ Điện Biên: $R_2 = {data_DB[-1]} - {data_DB[0]} = {R_DB}$\\\\"
                            f"Khoảng biến thiên nhiệt độ cao nhất trong ngày của Hà Nội và Điện Biên là giống nhau.")
            list_nb_2 = [loigiai_nb_1]

            ######################################################################## Thông hiểu ############################################

            # Đáp án sai ngẫu nhiên
            R_DB_new_fake = R_DB_new + random.choice([-2, -1, 1, 2])

            # Các đáp án
            th_da_1_d = f'\\True Nếu bỏ đi giá trị ${data_DB[0]}$ thì khoảng biến thiên của Điện Biên chỉ bằng ${R_DB_new}$'
            th_da_1_s = f'Nếu bỏ đi giá trị ${data_DB[0]}$ thì khoảng biến thiên của Điện Biên bằng ${R_DB_new_fake}$'
            list_th_da_1 = [th_da_1_d, th_da_1_s]

            # Nội dung lời giải
            loigiai_th_1 = (f"Giá trị ${data_DB[0]}$ làm cho khoảng biến thiên của mẫu số liệu về nhiệt độ cao nhất trong ngày tại Điện Biên bị ảnh hưởng lớn.\\\\"
                            f"Nếu bỏ đi giá trị ${data_DB[0]}$ thì mẫu số liệu còn lại có GTLN là ${data_DB[-1]}$ và GTNN là ${data_DB[1]}$.\\\\"
                            f"Khoảng biến thiên mới của Điện Biên chỉ bằng $R'_2 = {data_DB[-1]} - {data_DB[1]} = {R_DB_new}$.")
            list_th_2 = [loigiai_th_1]

            ######################################################################## Vận dụng ############################################

            # Mẹo nhiễu: Tráo kết quả IQR của DB cho HN
            IQR_HN_fake = IQR_DB
            if IQR_HN_fake == IQR_HN:
                IQR_HN_fake = IQR_HN + 2

            # Các đáp án
            vd_da_1_d = f'\\True Khoảng tứ phân vị của mẫu Hà Nội là: $\\Delta_{{Q_{{HN}}}} = {IQR_HN}$'
            vd_da_1_s = f'Khoảng tứ phân vị của mẫu Hà Nội là: $\\Delta_{{Q_{{HN}}}} = {IQR_HN_fake}$'
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

            # Nội dung lời giải
            loigiai_vd_1 = (f"Hà Nội: {str_HN}. Mẫu đã sắp xếp tăng dần.\\\\"
                            f"Cỡ mẫu là $n=7$, là số lẻ nên giá trị tứ phân vị thứ hai là: $Q_2 = {Q2_HN}$.\\\\"
                            f"Tứ phân vị thứ nhất là trung vị của nửa mẫu trái: ${data_HN[0]}; {data_HN[1]}; {data_HN[2]}$. Do đó $Q_1 = {Q1_HN}$.\\\\"
                            f"Tứ phân vị thứ ba là trung vị của nửa mẫu phải: ${data_HN[4]}; {data_HN[5]}; {data_HN[6]}$. Do đó $Q_3 = {Q3_HN}$.\\\\"
                            f"Khoảng tứ phân vị của mẫu Hà Nội là: $\\Delta_{{Q_{{HN}}}} = Q_3 - Q_1 = {Q3_HN} - {Q1_HN} = {IQR_HN}$.")
            list_vd_2 = [loigiai_vd_1]

            ######################################################################## Vận dụng cao ########################################

            # Mẹo nhiễu: Tráo kết quả IQR của HN cho DB
            IQR_DB_fake = IQR_HN
            if IQR_DB_fake == IQR_DB:
                IQR_DB_fake = IQR_DB + 3

            vdc_da_1_d = f'\\True Khoảng tứ phân vị của mẫu Điện Biên là: $\\Delta_{{Q_{{DB}}}} = {IQR_DB}$'
            vdc_da_1_s = f'Khoảng tứ phân vị của mẫu Điện Biên là: $\\Delta_{{Q_{{DB}}}} = {IQR_DB_fake}$'
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

            # Nội dung lời giải
            loigiai_vdc_1 = (f"Điện Biên: {str_DB}. Mẫu đã sắp xếp tăng dần.\\\\"
                             f"Cỡ mẫu là $n=7$, là số lẻ nên giá trị tứ phân vị thứ hai là: $Q_2 = {Q2_DB}$.\\\\"
                             f"Tứ phân vị thứ nhất là trung vị của nửa mẫu trái: ${data_DB[0]}; {data_DB[1]}; {data_DB[2]}$. Do đó $Q_1 = {Q1_DB}$.\\\\"
                             f"Tứ phân vị thứ ba là trung vị của nửa mẫu phải: ${data_DB[4]}; {data_DB[5]}; {data_DB[6]}$. Do đó $Q_3 = {Q3_DB}$.\\\\"
                             f"Khoảng tứ phân vị của mẫu Điện Biên là: $\\Delta_{{Q_{{DB}}}} = Q_3 - Q_1 = {Q3_DB} - {Q1_DB} = {IQR_DB}$.\\\\"
                             f"Có thể dùng hiệu này để đo độ phân tán của mẫu số liệu (loại bỏ được ảnh hưởng của giá trị ngoại lệ ${data_DB[0]}$).")
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

