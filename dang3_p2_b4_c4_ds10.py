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


def bt_dang3_p2_b4_c4_ds10(self):
            # Khai báo biến
            # Để x1, x2 không là nghiệm, ta cần x1, x2 > -e (vì điều kiện là -x + e >= 0 <=> x <= e)

            k = random.randint(4, 6) # k tương ứng với số 5 trong -x-5
            e_val = -k
            b_val = random.choice([1, -1, 3, -3])

            # Tìm x1, x2 sao cho x1+x2 = -(b+2e) và x1, x2 đều > e
            # Gọi S_sum = -(b_val + 2*e_val)
            s_sum = -(b_val + 2*e_val)
            x1 = random.randint(k + 2, k + 7)
            x2 = s_sum - x1

            # Tính c để phương trình x^2 + (b+2e)x + (c-e^2) = 0 có nghiệm x1, x2
            # c - e^2 = x1 * x2 => c = e^2 + x1*x2
            c_val = e_val**2 + x1*x2

            # Phương trình gốc và phương trình hệ quả
            f_left = 2*x**2 + b_val*x + c_val
            f_right = -x + e_val
            quad_eq = x**2 + (b_val - 2*e_val)*x + (c_val - e_val**2)

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho phương trình $\\sqrt{%s} = %s \\quad (*)$.''' 
                             %(latex(f_left), latex(f_right)))

            ########################################################################
            # Nhận biết: Bước bình phương
            nb_da_1_d = '\\True Bình phương hai vế của phương trình ta được $%s = 0$' %(latex(quad_eq))
            nb_da_1_s = 'Bình phương hai vế của phương trình ta được $%s = 0$' %(latex(quad_eq + random.randint(1,5)))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            loigiai_nb_1 = ('''Bình phương hai vế của phương trình (*), ta có: \\\\
                            $2x^2 + %sx + %s = (-x %s)^2 \\\\
                            \\Leftrightarrow 2x^2 + %sx + %s = x^2 %s x + %s \\\\
                            \\Leftrightarrow %s = 0$.''' 
                            %(latex(b_val), latex(c_val), latex(e_val), 
                              latex(b_val), latex(c_val), latex(-2*e_val), latex(e_val**2),
                              latex(quad_eq)))

            ########################################################################
            # Thông hiểu: So sánh tập nghiệm
            th_da_1_d = '\\True Phương trình $\\sqrt{%s} = %s$ và phương trình $%s = 0$ không có chung tập nghiệm' %(latex(f_left), latex(f_right), latex(quad_eq))
            th_da_1_s = 'Phương trình $\\sqrt{%s} = %s$ và phương trình $%s = 0$ có chung tập nghiệm' %(latex(f_left), latex(f_right), latex(quad_eq))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            loigiai_th_1 = ('''Điều kiện của phương trình (*) là $%s \\ge 0 \\Leftrightarrow x \\le %s$. \\\\
                            Phương trình $%s = 0$ có hai nghiệm là $x = %s$ và $x = %s$. \\\\
                            Cả hai nghiệm này đều không thỏa mãn điều kiện $x \\le %s$, do đó hai phương trình không có chung tập nghiệm.''' 
                            %(latex(f_right), latex(e_val), latex(quad_eq), latex(x1), latex(x2), latex(e_val)))

            ########################################################################
            # Vận dụng: Kiểm tra nghiệm cụ thể
            vd_da_1_d = '\\True $x = %s; x = %s$ không là nghiệm của phương trình (*)' %(latex(x1), latex(x2))
            vd_da_1_s = '$x = %s; x = %s$ là nghiệm của phương trình (*)' %(latex(x1), latex(x2))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            loigiai_vd_1 = ('''Thay $x = %s$ vào vế phải ta được $%s < 0$. \\\\
                            Thay $x = %s$ vào vế phải ta được $%s < 0$. \\\\
                            Vì vế trái của (*) luôn không âm, nên $x = %s$ và $x = %s$ đều không là nghiệm.''' 
                            %(latex(x1), latex(-x1 + e_val), latex(x2), latex(-x2 + e_val), latex(x1), latex(x2)))

            ########################################################################
            # Vận dụng cao: Kết luận tập nghiệm
            vdc_da_1_d = '\\True Tập nghiệm của phương trình (*) là $S = \\varnothing$'
            vdc_da_1_s = 'Tập nghiệm của phương trình (*) là $S = \\{%s; %s\\}$' %(latex(x1), latex(x2))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            loigiai_vdc_1 = ('''Dựa trên các bước phân tích trên, phương trình hệ quả có nghiệm nhưng không nghiệm nào thỏa mãn điều kiện xác định của phương trình ban đầu. \\\\
                             Vậy tập nghiệm của phương trình là $S = \\varnothing$.''')

            # --- Phần xử lý xuất bản (Giữ nguyên cấu trúc mẫu) ---

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                nb_sel = random.choice(list_nb_da_1)
                th_sel = random.choice(list_th_da_1)
                vd_sel = random.choice(list_vd_da_1)
                vdc_sel = random.choice(list_vdc_da_1)
                if 1 <= count_true_answers([nb_sel, th_sel, vd_sel, vdc_sel]) <= 3:
                    break

            # Đóng gói để xáo trộn (ở đây demo theo thứ tự a, b, c, d tương ứng nb, th, vd, vdc)
            ans_list = [nb_sel, th_sel, vd_sel, vdc_sel]
            sol_list = [loigiai_nb_1, loigiai_th_1, loigiai_vd_1, loigiai_vdc_1]

            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+
                str(noidungcauhoi)+ 
                '\\choiceTFn \n'
                '{'+str(ans_list[0])+'}\n'
                '{'+str(ans_list[1])+'}\n'
                '{'+str(ans_list[2])+'}\n'
                '{'+str(ans_list[3])+'}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item '+str(sol_list[0])+'\n'
                '\\item '+str(sol_list[1])+'\n'
                '\\item '+str(sol_list[2])+'\n'
                '\\item '+str(sol_list[3])+'\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

