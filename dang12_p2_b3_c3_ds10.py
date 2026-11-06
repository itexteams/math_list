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


def bt_dang12_p2_b3_c3_ds10(self):
            # Khai báo biến
            # Khai báo hàm đếm số đáp án đúng
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Định dạng số phẩy của Việt Nam
            def format_num(num):
                res = f"{round(num, 3):g}"
                return res.replace('.', ',')

            ######################################################################## Xử lý Data Random ########################

            # Random trung bình số bàn thắng của 2 đội (để giống logic bài gốc là trung bình bằng nhau)
            mu = random.randint(2, 4)
            n = 12
            target_sum = n * mu

            def generate_data(target_sum, is_stable):
                # is_stable = True cho độ phân tán nhỏ (Việt Nam), False cho độ phân tán lớn (Thái Lan)
                if is_stable:
                    data = [random.randint(max(0, mu - 1), mu + 2) for _ in range(n)]
                else:
                    data = [random.randint(0, mu + 4) for _ in range(n)]

                # Cân bằng lại mảng để tổng đúng bằng target_sum
                current_sum = sum(data)
                while current_sum != target_sum:
                    idx = random.randint(0, n - 1)
                    if current_sum < target_sum:
                        data[idx] += 1
                        current_sum += 1
                    elif current_sum > target_sum and data[idx] > 0:
                        data[idx] -= 1
                        current_sum -= 1
                return data

            data_VN = generate_data(target_sum, True)
            data_TL = generate_data(target_sum, False)

            # Tính toán các đại lượng
            mean_VN = sum(data_VN) / n
            mean_TL = sum(data_TL) / n

            var_VN = sum((x - mean_VN)**2 for x in data_VN) / n
            var_TL = sum((x - mean_TL)**2 for x in data_TL) / n

            # Đảm bảo Việt Nam luôn ổn định hơn (var_VN < var_TL) để khớp với mạch logic
            if var_VN >= var_TL:
                data_VN, data_TL = data_TL, data_VN
                var_VN, var_TL = var_TL, var_VN

            std_VN = math.sqrt(var_VN)
            std_TL = math.sqrt(var_TL)

            # Format chuỗi hiển thị đề bài
            str_data_VN = " \\quad ".join(map(str, data_VN))
            str_data_TL = " \\quad ".join(map(str, data_TL))

            # Nội dung câu hỏi
            noidungcauhoi = f'''Mỗi mẫu số liệu sau ghi rõ số bàn thắng của hai đội tuyển Việt Nam và Thái Lan trong một năm dương lịch khi thi đấu với các đội bóng khác ở khu vực.
            \\\\Số bàn thắng đội tuyển Việt Nam: ${str_data_VN}$.
            \\\\Số bàn thắng đội tuyển Thái Lan: ${str_data_TL}$.'''

            ######################################################################## Nhận biết ############################################

            # Các đáp án (Logic: Trung bình luôn bằng nhau do cách ta setup random)
            nb_da_1_d = '\\True Số bàn thắng trung bình của đội tuyển Việt Nam và đội tuyển Thái Lan là bằng nhau'
            nb_da_1_s = 'Số bàn thắng trung bình của đội tuyển Việt Nam và đội tuyển Thái Lan là không bằng nhau'
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

            # Nội dung lời giải
            loigiai_nb_1 = (f"Số bàn thắng trung bình của đội tuyển Việt Nam và đội tuyển Thái Lan là bằng nhau và bằng ${mu}$ (bàn).")
            list_nb_2 = [loigiai_nb_1]

            ######################################################################## Thông hiểu ############################################

            # Đáp án sai ngẫu nhiên cho độ lệch chuẩn VN
            std_VN_fake = std_VN + random.choice([-0.25, 0.35, 0.45, -0.15])
            if std_VN_fake < 0: std_VN_fake += 0.5

            # Các đáp án
            th_da_1_d = f'\\True Xét mẫu số liệu về số bàn thắng của đội tuyển Việt Nam có độ lệch chuẩn là: $s_1 \\approx {format_num(std_VN)}$ (bàn)'
            th_da_1_s = f'Xét mẫu số liệu về số bàn thắng của đội tuyển Việt Nam có độ lệch chuẩn là: $s_1 \\approx {format_num(std_VN_fake)}$ (bàn)'
            list_th_da_1 = [th_da_1_d, th_da_1_s]

            # Nội dung lời giải
            loigiai_th_1 = (f"Xét mẫu số liệu về số bàn thắng của đội tuyển Việt Nam:\\\\"
                            f"Phương sai là: $s_1^2 \\approx {format_num(var_VN)}$; độ lệch chuẩn là: $s_1 = \\sqrt{{s_1^2}} \\approx {format_num(std_VN)}$ (bàn).")
            list_th_2 = [loigiai_th_1]

            ######################################################################## Vận dụng ############################################

            # Đáp án sai ngẫu nhiên cho phương sai TL
            var_TL_fake = var_TL + random.choice([-0.5, -0.8, 1.2, 0.6])
            if var_TL_fake < 0: var_TL_fake += 1.0

            # Các đáp án
            vd_da_1_d = f'\\True Xét mẫu số liệu về số bàn thắng của đội tuyển Thái Lan có phương sai là: $s_2^2 \\approx {format_num(var_TL)}$'
            vd_da_1_s = f'Xét mẫu số liệu về số bàn thắng của đội tuyển Thái Lan có phương sai là: $s_2^2 \\approx {format_num(var_TL_fake)}$'
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

            # Nội dung lời giải
            loigiai_vd_1 = (f"Xét mẫu số liệu về số bàn thắng của đội tuyển Thái Lan:\\\\"
                            f"Phương sai là: $s_2^2 \\approx {format_num(var_TL)}$; độ lệch chuẩn là: $s_2 = \\sqrt{{s_2^2}} \\approx {format_num(std_TL)}$ (bàn).")
            list_vd_2 = [loigiai_vd_1]

            ######################################################################## Vận dụng cao ########################################

            # Các đáp án (Vì var_VN < var_TL nên VN luôn ổn định hơn)
            vdc_da_1_d = '\\True Khả năng ghi bàn của đội tuyển Việt Nam có tính ổn định hơn so với đội tuyển Thái Lan'
            vdc_da_1_s = 'Khả năng ghi bàn của đội tuyển Thái Lan có tính ổn định hơn so với đội tuyển Việt Nam'
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

            # Nội dung lời giải
            loigiai_vdc_1 = (f"Vì số lượng bàn thắng trung bình của hai đội là ngang nhau mà $s_1 < s_2$ "
                             f"nên khả năng ghi bàn của đội tuyển Việt Nam có tính ổn định hơn so với đội tuyển Thái Lan.")
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

