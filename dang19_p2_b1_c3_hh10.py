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


def bt_dang19_p2_b1_c3_hh10(self):
            # Khai báo biến
            # Khai báo biến ký hiệu
            x, y = symbols('x y')

            # --- BƯỚC 1: SINH DỮ LIỆU NGẪU NHIÊN ---
            # Tọa độ điểm I(xI, yI)
            xI = random.randint(-3, 5)
            yI = random.randint(-3, 5)

            # Đường thẳng d1: a1*x + b1*y + c1 = 0
            a1 = random.choice([i for i in range(-10, 11) if i != 0])
            b1 = random.choice([i for i in range(-15, 16) if i != 0])
            c1 = random.randint(-20, 20)

            # Đường thẳng d2: a2*x + b2*y + c2 = 0 (Để giải M cho đẹp, ta chọn hệ số nhỏ)
            # Chọn d2 sao cho d2 đi qua một điểm nguyên nào đó gần I để IM=1 dễ có nghiệm đẹp
            a2 = 1
            b2 = 2
            # Giả sử chọn M(xI-1, yI) hoặc (xI+1, yI) thuộc d2 để IM=1
            # Ở đây ta lấy d2 đi qua (xI-1, yI) => 1*(xI-1) + 2*(yI) + c2 = 0 => c2 = -(xI - 1 + 2*yI)
            c2 = -(xI - 1 + 2*yI)

            # --- BƯỚC 2: TÍNH TOÁN CÁC THÀNH PHẦN ---

            # Câu a: Vectơ pháp tuyến d1
            n1 = (a1, b1)

            # Câu b: Kiểm tra điểm A(xA, yA) có thuộc d2 không
            xA = random.randint(-5, 5)
            yA = random.randint(-5, 5)
            check_A = a2 * xA + b2 * yA + c2
            is_A_on_d2 = (check_A == 0)

            # Câu c: Đường thẳng Delta qua I và song song d2
            # PT: a2(x - xI) + b2(y - yI) = 0 <=> a2*x + b2*y - (a2*xI + b2*yI) = 0
            c_delta = -(a2 * xI + b2 * yI)
            pt_delta = simplify(a2*x + b2*y + c_delta)

            # Câu d: Tìm M(a, b) thuộc d2 sao cho IM = 1
            # Hệ: a + 2b + c2 = 0 => a = -c2 - 2b
            # IM^2 = 1 => (a - xI)^2 + (b - yI)^2 = 1
            # Thay a: (-c2 - 2b - xI)^2 + (b - yI)^2 = 1
            b_sym = symbols('b')
            a_sym = -c2 - 2*b_sym
            eq_dist = (a_sym - xI)**2 + (b_sym - yI)**2 - 1
            roots_b = sp.solve(eq_dist, b_sym)
            # Lấy b lớn nhất (tương ứng b >= 1 trong đề bài mẫu)
            b_M = max(roots_b)
            a_M = -c2 - 2*b_M
            tong_ab = a_M + b_M

            # --- BƯỚC 3: NỘI DUNG CÂU HỎI ---
            noidungcauhoi = ('''Trong mặt phẳng tọa độ $Oxy$, cho điểm $I(%s;%s)$ và đường thẳng $d_1 : %s = 0; d_2 : %s = 0$.''' 
                             %(latex(xI), latex(yI), latex(a1*x + b1*y + c1), latex(a2*x + b2*y + c2)))

            ########################################################################
            # Nhận biết (Câu a)
            nb_da_1_d = '\\True Đường thẳng $d_1$ có một vectơ pháp tuyến là $\\vec{n}_1 = (%s; %s)$' %(latex(a1), latex(b1))
            nb_da_1_s = 'Đường thẳng $d_1$ có một vectơ chỉ phương là $\\vec{u}_1 = (%s; %s)$' %(latex(a1), latex(b1))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            loigiai_nb_1 = ('''Đường thẳng $d_1: %sx +%s y +%s = 0$ có các hệ số đứng trước $x, y$ lần lượt là $%s$ và $%s$. Do đó một vectơ pháp tuyến là $\\vec{n}_1 = (%s; %s)$.'''
                            %(latex(a1), '+' if b1>0 else '', latex(b1), latex(a1), latex(b1), latex(a1), latex(b1)))

            ########################################################################
            # Thông hiểu (Câu b)
            if is_A_on_d2:
                th_da_1_d = '\\True Đường thẳng $d_2$ đi qua điểm $A(%s;%s)$' %(latex(xA), latex(yA))
                th_da_1_s = 'Đường thẳng $d_2$ không đi qua điểm $A(%s;%s)$' %(latex(xA), latex(yA))
            else:
                th_da_1_d = '\\True Đường thẳng $d_2$ không đi qua điểm $A(%s;%s)$' %(latex(xA), latex(yA))
                th_da_1_s = 'Đường thẳng $d_2$ đi qua điểm $A(%s;%s)$' %(latex(xA), latex(yA))

            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            loigiai_th_1 = ('''Thay tọa độ điểm $A(%s;%s)$ vào phương trình $d_2$, ta có: $%s + 2(%s) %s = %s$. %s'''
                            %(latex(xA), latex(yA), latex(xA), latex(yA), '+' if c2>0 else latex(c2), latex(check_A), 
                              'Vậy $A \\in d_2$.' if is_A_on_d2 else 'Vậy $A \\notin d_2$.'))

            ########################################################################
            # Vận dụng (Câu c)
            vd_da_1_d = '\\True Phương trình tổng quát của đường thẳng $\\Delta$ đi qua $I$ và song song với đường thẳng $d_2$ là $%s = 0$' %(latex(pt_delta))
            vd_da_1_s = 'Phương trình tổng quát của đường thẳng $\\Delta$ đi qua $I$ và song song với đường thẳng $d_2$ là $%s = 0$' %(latex(simplify(pt_delta + random.randint(1,5))))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            loigiai_vd_1 = ('''Vì $\\Delta \\parallel d_2$ nên $\\Delta$ có dạng: $%s + 2y + m = 0$ ($m \\neq %s$). \\\\
                            Vì $I(%s;%s) \\in \\Delta$ nên: $%s + 2(%s) + m = 0 \\Leftrightarrow m = %s$. \\\\
                            Vậy phương trình đường thẳng $\\Delta$ là $%s = 0$.'''
                            %(latex(x), latex(c2), latex(xI), latex(yI), latex(xI), latex(yI), latex(c_delta), latex(pt_delta)))

            ########################################################################
            # Vận dụng cao (Câu d)
            val_check = float(tong_ab)
            vdc_da_1_d = '\\True Cho $b \\geq %s$. Điểm $M(a;b) \\in d_2$ sao cho $IM = 1$. Khi đó $a+b = %s$' %(latex(yI), latex(tong_ab))
            vdc_da_1_s = 'Cho $b \\geq %s$. Điểm $M(a;b) \\in d_2$ sao cho $IM = 1$. Khi đó $a+b = %s$' %(latex(yI), latex(tong_ab + 1))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            loigiai_vdc_1 = ('''Gọi $M(a;b)$. Vì $M \\in d_2$ nên $a + 2b %s = 0 \\Rightarrow a = %s - 2b$. \\\\
                            Ta có $IM^2 = 1 \\Leftrightarrow (a - %s)^2 + (b - %s)^2 = 1$. \\\\
                            Thay $a$ vào ta được: $(%s - 2b - %s)^2 + (b - %s)^2 = 1$. \\\\
                            Giải phương trình ta được $b = %s$ hoặc $b = %s$. \\\\
                            Với điều kiện $b \\geq %s$, ta nhận $b = %s \\Rightarrow a = %s$. \\\\
                            Vậy $a+b = %s$.'''
                            %(('+' if c2>0 else latex(c2)), latex(-c2), latex(xI), latex(yI), latex(-c2), latex(xI), latex(yI), 
                              latex(roots_b[0]), latex(roots_b[1]), latex(yI), latex(b_M), latex(a_M), latex(tong_ab)))

            # --- BƯỚC 4: XỬ LÝ ĐÁP ÁN VÀ XUẤT NỘI DUNG ---

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                ans_a = random.choice(list_nb_da_1)
                ans_b = random.choice(list_th_da_1)
                ans_c = random.choice(list_vd_da_1)
                ans_d = random.choice(list_vdc_da_1)

                if 1 <= count_true_answers([ans_a, ans_b, ans_c, ans_d]) <= 3:
                    break

            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
                '{' + str(ans_a) + '}\n'
                '{' + str(ans_b) + '}\n'
                '{' + str(ans_c) + '}\n'
                '{' + str(ans_d) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(loigiai_nb_1) + '\n'
                '\\item ' + str(loigiai_th_1) + '\n'
                '\\item ' + str(loigiai_vd_1) + '\n'
                '\\item ' + str(loigiai_vdc_1) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('++','+').replace('+ +','+').replace('+-','-').replace('+ -','-')
            return content   

