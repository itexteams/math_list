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


def bt_dang9_p2_b1_c3_hh10(self):
            # Khai báo biến
            # Khai báo biến
            t = symbols('t')

            # BƯỚC 1: NGẪU NHIÊN CÁC THÔNG SỐ
            # Tọa độ điểm xuất phát A(xA, yA)
            xA = random.randint(1, 8)
            yA = random.randint(1, 8)

            # Vectơ vận tốc v(u1, u2)
            u1 = random.randint(1, 4)
            u2 = random.randint(2, 5)
            if u1 == u2: u2 += 1

            # Thời điểm t để tính quãng đường
            t_val = random.choice([2, 3, 4, 5])

            # Tính toán các đại lượng
            # Phương trình: u2(x - xA) - u1(y - yA) = 0 <=> u2x - u1y + (u1*yA - u2*xA) = 0
            c_val = u1*yA - u2*xA
            v_mag_sq = u1**2 + u2**2
            quang_duong = t_val * sqrt(v_mag_sq)

            # Nội dung câu hỏi (Không dùng r)
            noidungcauhoi = ("Chuyển động của vật thể $M$ được thể hiện trên mặt phẳng toạ độ $Oxy$. Vật thể $M$ khởi hành từ điểm $A(%s;%s)$ và chuyển động thẳng đều với vectơ vận tốc là $\\vec{v}=(%s;%s)$." 
                             % (latex(xA), latex(yA), latex(u1), latex(u2)))

            ########################################################################
            # a) Nhận biết
            ########################################################################
            nb_da_1_d = '\\True Vectơ chỉ phương của đường thẳng biểu diễn chuyển động của vật thể là $\\vec{v}=(%s;%s)$' % (latex(u1), latex(u2))
            nb_da_1_s = 'Vectơ chỉ phương của đường thẳng biểu diễn chuyển động của vật thể là $\\vec{n}=(%s;%s)$' % (latex(u2), latex(-u1))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            loigiai_nb_1 = ("Vì vật thể $M$ chuyển động thẳng đều với vectơ vận tốc $\\vec{v}=(%s;%s)$ nên đường thẳng biểu diễn chuyển động nhận $\\vec{v}$ làm vecto chỉ phương." 
                            % (latex(u1), latex(u2)))

            ########################################################################
            # b) Thông hiểu
            ########################################################################
            th_da_1_d = '\\True Vật thể $M$ chuyển động trên đường thẳng $%sx %s y %s = 0$' % (latex(u2), latex(-u1) if -u1 < 0 else "+"+latex(-u1), latex(c_val) if c_val < 0 else "+"+latex(c_val))
            th_da_1_s = 'Vật thể $M$ chuyển động trên đường thẳng $%sx - %sy + %s = 0$' % (latex(u1), latex(u2), latex(c_val + 5))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            loigiai_th_1 = ("Đường thẳng quỹ đạo đi qua $A(%s;%s)$ và có vectơ chỉ phương $\\vec{v}=(%s;%s)$ nên có vectơ pháp tuyến là $\\vec{n}=(%s;%s)$. \\\\ Phương trình đường thẳng là: $%s(x - %s) %s (y - %s) = 0 \\Leftrightarrow %sx %s y %s = 0$." 
                            % (latex(xA), latex(yA), latex(u1), latex(u2), latex(u2), latex(-u1), latex(u2), latex(xA), latex(-u1) if -u1 < 0 else "+"+latex(-u1), latex(yA), latex(u2), latex(-u1) if -u1 < 0 else "+"+latex(-u1), latex(c_val) if c_val < 0 else "+"+latex(c_val)))

            ########################################################################
            # c) Vận dụng
            ########################################################################
            vd_da_1_d = '\\True Toạ độ của vật thể $M$ tại thời điểm $t(t > 0)$ tính từ khi khởi hành là $\\begin{cases} x = %s + %st \\\\ y = %s + %st \\end{cases}$' % (latex(xA), latex(u1), latex(yA), latex(u2))
            vd_da_1_s = 'Toạ độ của vật thể $M$ tại thời điểm $t(t > 0)$ tính từ khi khởi hành là $\\begin{cases} x = %s + %st \\\\ y = %s + %st \\end{cases}$' % (latex(u1), latex(xA), latex(u2), latex(yA))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            loigiai_vd_1 = ("Tại thời điểm $t$, tọa độ của vật thể $M(x;y)$ thỏa mãn hệ phương trình tham số: \\\\ $\\begin{cases} x = x_A + u_1 t \\\\ y = y_A + u_2 t \\end{cases} \\Rightarrow \\begin{cases} x = %s + %st \\\\ y = %s + %st \\end{cases}$." 
                            % (latex(xA), latex(u1), latex(yA), latex(u2)))

            ########################################################################
            # d) Vận dụng cao
            ########################################################################
            vdc_da_1_d = '\\True Khi $t = %s$ thì vật thể $M$ chuyển động được quãng đường dài bằng $%s$' % (latex(t_val), latex(quang_duong))
            vdc_da_1_s = 'Khi $t = %s$ thì vật thể $M$ chuyển động được quãng đường dài bằng %s' % (latex(t_val), latex(t_val * (u1 + u2)))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            loigiai_vdc_1 = ("Độ lớn vận tốc là $v = |\\vec{v}| = \\sqrt{%s^2 + %s^2} = \\sqrt{%s}$. \\\\ Khi $t = %s$, quãng đường vật thể đi được là: $s = v \\cdot t = \\sqrt{%s} \\cdot %s = %s$." 
                             % (latex(u1), latex(u2), latex(v_mag_sq), latex(t_val), latex(v_mag_sq), latex(t_val), latex(quang_duong)))

            # --- LOGIC KIỂM TRA SỐ CÂU ĐÚNG (1-3 CÂU) ---
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                ans_a = random.choice(list_nb_da_1)
                ans_b = random.choice(list_th_da_1)
                ans_c = random.choice(list_vd_da_1)
                ans_d = random.choice(list_vdc_da_1)
                if 1 <= count_true_answers([ans_a, ans_b, ans_c, ans_d]) <= 3:
                    break

            # Gán vào list để xuất
            shuffled_answers = [ans_a, ans_b, ans_c, ans_d]
            shuffled_solutions = [loigiai_nb_1, loigiai_th_1, loigiai_vd_1, loigiai_vdc_1]

            # XUẤT NỘI DUNG (Không dùng tiền tố r)
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + 
                str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
                '{' + str(shuffled_answers[0]) + '}\n'
                '{' + str(shuffled_answers[1]) + '}\n'
                '{' + str(shuffled_answers[2]) + '}\n'
                '{' + str(shuffled_answers[3]) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(shuffled_solutions[0]) + '\n'
                '\\item ' + str(shuffled_solutions[1]) + '\n'
                '\\item ' + str(shuffled_solutions[2]) + '\n'
                '\\item ' + str(shuffled_solutions[3]) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n'
                '\\end{minipage} \n\n')
            return content   

