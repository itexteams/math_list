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


def bt_dang30_p2_b2_c4_ds12(self):
            # Khai báo biến
            # Hàm bổ trợ để chuyển số thập phân sang định dạng Việt Nam (dấu phẩy)
            def f_vn(val, precision=3):
                if isinstance(val, (int, float)):
                    # Làm tròn theo độ chính xác yêu cầu
                    s = "{:.{}f}".format(val, precision).rstrip('0').rstrip('.')
                    if '.' not in s: # Nếu là số nguyên
                        return s
                    return s.replace('.', ',')
                return str(val).replace('.', ',')

            # --- Khởi tạo giá trị ngẫu nhiên cho bài toán ---
            # p_lao: Tỉ lệ lao phổi (ví dụ 10% - 20%)
            p_lao_val = random.randint(120, 180) / 1000 
            # p_co_trieu_chung_khi_lao: P(B|A) (ví dụ 85% - 95%)
            p_B_A_val = random.randint(880, 960) / 1000
            # p_khong_trieu_chung_khi_khong_lao: P(not B | not A) (ví dụ 30% - 45%)
            p_notB_notA_val = random.randint(320, 420) / 1000

            # Các giá trị tính toán
            p_notA_val = 1 - p_lao_val
            p_B_notA_val = 1 - p_notB_notA_val
            p_B_val = p_B_A_val * p_lao_val + p_B_notA_val * p_notA_val
            p_A_B_val = (p_B_A_val * p_lao_val) / p_B_val

            # Chuyển sang phần trăm làm tròn đến hàng đơn vị cho câu c và d
            perc_B = round(p_B_val * 100)
            perc_A_B = round(p_A_B_val * 100)

            # Nội dung câu hỏi gốc
            noidungcauhoi = ('''Một nghiên cứu đã chỉ ra rằng tỉ lệ người lao phổi trong nhóm X những người mắc phải hội chứng suy giảm miễn dịch $H$ là $%s\\%%$. Kết quả nghiên cứu về một số triệu chứng lâm sàng như có ho trong vòng bốn tuần, hoặc có bị sốt trong vòng bốn tuần, hoặc ra mồ hôi ban đêm từ ba tuần trở lên của nhóm X cho thấy: trong số những người mắc bệnh lao phổi, có $%s\\%%$ trường hợp có ít nhất một triệu chứng; trong số những người không mắc bệnh lao phổi, có $%s\\%%$ trường hợp không có triệu chứng nào.''' 
                             %(f_vn(p_lao_val*100, 1), f_vn(p_B_A_val*100, 1), f_vn(p_notB_notA_val*100, 1)))

            ########################################################################
            # Nhận biết ############################################
            nb_da_1_d = '\\True Gặp ngẫu nhiên một bệnh nhân thuộc nhóm X, xác suất bệnh nhân bị lao phổi là %s' % f_vn(p_lao_val, 3)
            nb_da_1_s = 'Gặp ngẫu nhiên một bệnh nhân thuộc nhóm X, xác suất bệnh nhân bị lao phổi là %s' % f_vn(p_lao_val + 0.05, 3)
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)
            loigiai_nb_1 = ('''Gọi $A$ là biến cố: "gặp được người bị lao phổi". Theo giả thiết $P(A) = %s\\%% = %s$.''' % (f_vn(p_lao_val*100, 1), f_vn(p_lao_val, 3)))

            ########################################################################
            # Thông hiểu ############################################
            th_da_1_d = '\\True Gặp được bệnh nhân không mắc bệnh lao phổi, xác suất bệnh nhân đó có ít nhất một triệu chứng trên là %s' % f_vn(p_B_notA_val, 3)
            th_da_1_s = 'Gặp được bệnh nhân không mắc bệnh lao phổi, xác suất bệnh nhân đó có ít nhất một triệu chứng trên là %s' % f_vn(p_notB_notA_val, 3)
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)
            loigiai_th_1 = ('''Gọi $B$ là biến cố: "gặp được người có ít nhất một triệu chứng". Ta có \\\\ $P(B|\\bar{A}) = 1 - P(\\bar{B}|\\bar{A}) = 1 - %s = %s$.''' % (f_vn(p_notB_notA_val, 3), f_vn(p_B_notA_val, 3)))

            ########################################################################
            # Vận dụng ############################################
            vd_da_1_d = '\\True Có %s\\%% bệnh nhân thuộc nhóm X có ít nhất một triệu chứng trên (kết quả tính theo phần trăm được làm tròn đến hàng đơn vị)' % perc_B
            vd_da_1_s = 'Có %s\\%% bệnh nhân thuộc nhóm X có ít nhất một triệu chứng trên (kết quả tính theo phần trăm được làm tròn đến hàng đơn vị)' % (perc_B + 5)
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)
            loigiai_vd_1 = ('''Áp dụng công thức xác suất đầy đủ: \\\\ $P(B) = P(B|A).P(A) + P(B|\\bar{A}).P(\\bar{A}) = %s.%s + %s.%s = %s$. \\\\ Suy ra có khoảng %s\\%% bệnh nhân có ít nhất một triệu chứng.''' 
                            % (f_vn(p_B_A_val, 3), f_vn(p_lao_val, 3), f_vn(p_B_notA_val, 3), f_vn(p_notA_val, 3), f_vn(p_B_val, 5), perc_B))

            ########################################################################
            # Vận dụng cao ############################################
            vdc_da_1_d = '\\True Trong số những bệnh nhân có ít nhất một triệu chứng trên, có %s\\%% người mắc bệnh lao phổi (kết quả tính theo phần trăm được làm tròn đến hàng đơn vị)' % perc_A_B
            vdc_da_1_s = 'Trong số những bệnh nhân có ít nhất một triệu chứng trên, có %s\\%% người mắc bệnh lao phổi (kết quả tính theo phần trăm được làm tròn đến hàng đơn vị)' % (perc_A_B - 4)
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)
            loigiai_vdc_1 = ('''Áp dụng công thức Bayes: \\\\ $P(A|B) = \\frac{P(B|A).P(A)}{P(B)} = \\frac{%s.%s}{%s} \\approx %s$. \\\\ Suy ra trong số những người có triệu chứng, có khoảng %s\\%% người thực sự mắc bệnh lao phổi.''' 
                             % (f_vn(p_B_A_val, 3), f_vn(p_lao_val, 3), f_vn(p_B_val, 5), f_vn(p_A_B_val, 4), perc_A_B))

            # --- Phần Logic Shuffling và Content (Giữ nguyên cấu trúc mẫu) ---

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                nb_sel = random.choice(list_nb_da_1)
                th_sel = random.choice(list_th_da_1)
                vd_sel = random.choice(list_vd_da_1)
                vdc_sel = random.choice(list_vdc_da_1)
                if 1 <= count_true_answers([nb_sel, th_sel, vd_sel, vdc_sel]) <= 3:
                    break

            # Gán lời giải tương ứng (do bài này lời giải đi kèm cố định với câu hỏi a,b,c,d)
            # Ở đây ta mặc định thứ tự a->nb, b->th, c->vd, d->vdc như trong ảnh
            shuffled_answers = [nb_sel, th_sel, vd_sel, vdc_sel]
            shuffled_solutions = [loigiai_nb_1, loigiai_th_1, loigiai_vd_1, loigiai_vdc_1]

            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+
                str(noidungcauhoi)+ 
                '\n\\choiceTFn \n'
                '{'+str(shuffled_answers[0])+'}\n'
                '{'+str(shuffled_answers[1])+'}\n'
                '{'+str(shuffled_answers[2])+'}\n'
                '{'+str(shuffled_answers[3])+'}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item '+str(shuffled_solutions[0])+'\n'
                '\\item '+str(shuffled_solutions[1])+'\n'
                '\\item '+str(shuffled_solutions[2])+'\n'
                '\\item '+str(shuffled_solutions[3])+'\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

