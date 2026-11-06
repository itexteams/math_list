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


def bt_dang5_p2_b2_c5_ds10(self):
            # Khai báo biến
            # Khai báo biến ngẫu nhiên để tạo các bài toán tương tự
            n_nam = random.randint(4, 6) # Số nam từ 4 đến 6
            n_nu = 3 # Giữ cố định nữ là 3 hoặc random tùy ý
            tong = n_nam + n_nu

            # Các giá trị tính toán
            gt_tong = math.factorial(tong)
            gt_cung_gioi = math.factorial(n_nam) * math.factorial(n_nu) * 2
            gt_nu_canh_nhau = math.factorial(n_nu) * math.factorial(n_nam + 1)
            gt_vach_ngan = math.factorial(n_nam) * math.perm(n_nam + 1, n_nu)

            # Nội dung câu hỏi
            noidungcauhoi = ('''Có %s nam sinh và %s nữ sinh cần được xếp vào một hàng dọc.''' 
                             %(latex(n_nam), latex(n_nu)))

            ########################################################################
            # Nhận biết (Câu a)
            nb_da_1_d = '\\True Số cách xếp %s học sinh theo một hàng dọc là: %s (cách)' %(latex(tong), latex(gt_tong))
            nb_da_1_s = 'Số cách xếp %s học sinh theo một hàng dọc là: %s (cách)' %(latex(tong), latex(gt_tong + 100))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)
            loigiai_nb_1 = ('''Số cách xếp %s học sinh vào %s vị trí là một hoán vị của %s phần tử. \\\\ Ta có $%s! = %s$ (cách).'''
                            %(latex(tong), latex(tong), latex(tong), latex(tong), latex(gt_tong)))

            ########################################################################
            # Thông hiểu (Câu b)
            th_da_1_d = '\\True Số cách xếp học sinh cùng giới đứng cạnh nhau là: %s (cách)' %(latex(gt_cung_gioi))
            th_da_1_s = 'Số cách xếp học sinh cùng giới đứng cạnh nhau là: %s (cách)' %(latex(gt_cung_gioi // 2))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)
            loigiai_th_1 = ('''Buộc nhóm nam thành 1 khối có $%s!$ cách, nhóm nữ thành 1 khối có $%s!$ cách. \\\\ Xếp 2 khối này có $2!$ cách. \\\\ Vậy có $%s! \\cdot %s! \\cdot 2! = %s$ (cách).'''
                            %(latex(n_nam), latex(n_nu), latex(n_nam), latex(n_nu), latex(gt_cung_gioi)))

            ########################################################################
            # Vận dụng (Câu c)
            vd_da_1_d = '\\True Số cách xếp học sinh nữ luôn đứng cạnh nhau là: %s (cách)' %(latex(gt_nu_canh_nhau))
            vd_da_1_s = 'Số cách xếp học sinh nữ luôn đứng cạnh nhau là: %s (cách)' %(latex(gt_nu_canh_nhau + 120))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)
            loigiai_vd_1 = ('''Buộc %s học sinh nữ thành một nhóm $X$ (có $%s!$ cách hoán vị nội bộ). \\\\ Xếp $X$ cùng %s học sinh nam (tổng %s vị trí) có $%s!$ cách. \\\\ Vậy có $%s! \\cdot %s! = %s$ (cách).'''
                            %(latex(n_nu), latex(n_nu), latex(n_nam), latex(n_nam+1), latex(n_nam+1), latex(n_nu), latex(n_nam+1), latex(gt_nu_canh_nhau)))

            ########################################################################
            # Vận dụng cao (Câu d)
            vdc_da_1_d = '\\True Số cách xếp không có em nữ nào đứng cạnh nhau là: %s (cách)' %(latex(gt_vach_ngan))
            vdc_da_1_s = 'Số cách xếp không có em nữ nào đứng cạnh nhau là: 2400 (cách)'
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)
            loigiai_vdc_1 = ('''Đầu tiên xếp %s nam sinh có $%s!$ cách. \\\\ Giữa %s nam sinh có %s khoảng trống (tính cả 2 đầu). \\\\ Xếp %s nữ sinh vào %s khoảng trống đó có $A_{%s}^{%s}$ cách. \\\\ Vậy có $%s! \\cdot A_{%s}^{%s} = %s$ (cách).'''
                             %(latex(n_nam), latex(n_nam), latex(n_nam), latex(n_nam+1), latex(n_nu), latex(n_nam+1), latex(n_nam+1), latex(n_nu), latex(n_nam), latex(n_nam+1), latex(n_nu), latex(gt_vach_ngan)))

            # Kiểm soát số lượng câu Đúng từ 1 đến 3
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                d1 = random.choice(list_nb_da_1)
                d2 = random.choice(list_th_da_1)
                d3 = random.choice(list_vd_da_1)
                d4 = random.choice(list_vdc_da_1)
                if 1 <= count_true_answers([d1, d2, d3, d4]) <= 3:
                    shuffled_answers = [d1, d2, d3, d4]
                    shuffled_solutions = [loigiai_nb_1, loigiai_th_1, loigiai_vd_1, loigiai_vdc_1]
                    break

            # Xuất kết quả theo định dạng yêu cầu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+
                str(noidungcauhoi)+ 
                '\\choiceTFn \n'
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

