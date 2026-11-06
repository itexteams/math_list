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


def bt_dang8_p2_b1_c3_hh10(self):
            # Khai báo biến
            # Khai báo biến ký hiệu
            x, y = symbols('x y')

            # --- BƯỚC 1: TẠO DỮ LIỆU NGẪU NHIÊN ---
            # Để bài toán có nghiệm đẹp hoặc phân số không quá phức tạp, ta có thể fix hoặc random nhẹ
            # Ở đây mình sẽ thiết lập các hệ số dựa trên bài gốc và thêm tính ngẫu nhiên
            def generate_data():
                while True:
                    # Tọa độ điểm A
                    xA, yA = 1, 2 # Có thể dùng randint(-5, 5) để random

                    # Đường trung tuyến d1: a1*x + b1*y + c1 = 0 (từ B)
                    # Đường trung tuyến d2: a2*x + b2*y + c2 = 0 (từ C)
                    a1, b1, c1 = 2, -1, 1
                    a2, b2, c2 = 1, 3, -3

                    # Kiểm tra A không thuộc d1 và d2
                    if a1*xA + b1*yA + c1 != 0 and a2*xA + b2*yA + c2 != 0:
                        return xA, yA, a1, b1, c1, a2, b2, c2

            xA, yA, a1, b1, c1, a2, b2, c2 = generate_data()

            # --- BƯỚC 2: GIẢI TOÁN BẰNG SYMPY ---
            # 1. Tìm tọa độ C: C nằm trên d2 và trung điểm M của AC nằm trên d1
            # Gọi C(xC, yC). M = ((xA+xC)/2, (yA+yC)/2)
            xC, yC = symbols('xC yC')
            eq_c1 = a2*xC + b2*yC + c2 # C thuộc d2
            eq_c2 = a1*(xA + xC)/2 + b1*(yA + yC)/2 + c1 # M thuộc d1
            sol_C = solve([eq_c1, eq_c2], [xC, yC])
            ptC = (sol_C[xC], sol_C[yC])

            # 2. Tìm tọa độ B: B nằm trên d1 và trung điểm N của AB nằm trên d2
            xB, yB = symbols('xB yB')
            eq_b1 = a1*xB + b1*yB + c1 # B thuộc d1
            eq_b2 = a2*(xA + xB)/2 + b2*(yA + yB)/2 + c2 # N thuộc d2
            sol_B = solve([eq_b1, eq_b2], [xB, yB])
            ptB = (sol_B[xB], sol_B[yB])

            # 3. Phương trình đường thẳng BC
            # Véc tơ pháp tuyến n_BC = (yB - yC, xC - xB)
            n_BC = (ptB[1] - ptC[1], ptC[0] - ptB[0])
            # Rút gọn n_BC (chia cho gcd nếu là số nguyên)
            c_BC = -(n_BC[0]*ptB[0] + n_BC[1]*ptB[1])
            dtBC = n_BC[0]*x + n_BC[1]*y + c_BC

            # 4. Phương trình đường thẳng AC
            n_AC = (yA - ptC[1], ptC[0] - xA)
            c_AC = -(n_AC[0]*xA + n_AC[1]*yA)
            dtAC = n_AC[0]*x + n_AC[1]*y + c_AC

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho tam giác $ABC$, biết $A(%s;%s)$ và phương trình hai đường trung tuyến là $%s = 0$ và $%s = 0$.''' 
                             % (xA, yA, latex(a1*x + b1*y + c1), latex(a2*x + b2*y + c2)))

            ########################################################################
            # Mệnh đề a: Tọa độ điểm C
            da_a_d = '\\True Điểm $C$ có tọa độ là $\\left( %s; %s \\right)$' % (latex(ptC[0]), latex(ptC[1]))
            da_a_s = 'Điểm $C$ có tọa độ là $\\left( %s; %s \\right)$' % (latex(ptC[1]), latex(ptC[0]))
            list_a = [da_a_d, da_a_s]
            nb_da_1 = random.choice(list_a)

            loigiai_a = ('''Vì $A$ không thuộc hai đường trung tuyến nên giả sử $d_1: %s = 0$ là đường trung tuyến kẻ từ $B$, $d_2: %s = 0$ là đường trung tuyến kẻ từ $C$. \\\\
            Gọi $C(x_C; y_C) \\in d_2 \\Rightarrow %s x_C + %s y_C + (%s) = 0$. \\\\
            Gọi $M$ là trung điểm $AC \\Rightarrow M\\left( \\frac{x_C+%s}{2}; \\frac{y_C+%s}{2} \\right)$. \\\\
            Vì $M \\in d_1 \\Rightarrow %s \\left( \\frac{x_C+%s}{2} \\right) + (%s) \\left( \\frac{y_C+%s}{2} \\right) + (%s) = 0$. \\\\
            Giải hệ phương trình ta được $C\\left( %s; %s \\right)$.''' 
                         % (latex(a1*x + b1*y + c1), latex(a2*x + b2*y + c2), a2, b2, c2, xA, yA, a1, xA, b1, yA, c1, latex(ptC[0]), latex(ptC[1])))

            ########################################################################
            # Mệnh đề b: Tọa độ điểm B
            da_b_d = '\\True Điểm $B$ có tọa độ là $\\left( %s; %s \\right)$' % (latex(ptB[0]), latex(ptB[1]))
            da_b_s = 'Điểm $B$ có tọa độ là $\\left( %s; %s \\right)$' % (latex(ptC[0]), latex(ptB[1]))
            list_b = [da_b_d, da_b_s]
            th_da_1 = random.choice(list_b)

            loigiai_b = ('''Tương tự, gọi $B(x_B; y_B) \\in d_1 \\Rightarrow %s x_B + %s y_B + (%s) = 0$. \\\\
            Gọi $N$ là trung điểm $AB \\Rightarrow N\\left( \\frac{x_B+%s}{2}; \\frac{y_B+%s}{2} \\right)$. \\\\
            Vì $N \\in d_2 \\Rightarrow %s \\left( \\frac{x_B+%s}{2} \\right) + (%s) \\left( \\frac{y_B+%s}{2} \\right) + (%s) = 0$. \\\\
            Giải hệ phương trình ta được $B\\left( %s; %s \\right)$.''' 
                         % (a1, b1, c1, xA, yA, a2, xA, b2, yA, c2, latex(ptB[0]), latex(ptB[1])))

            ########################################################################
            # Mệnh đề c: Phương trình BC
            da_c_d = '\\True Phương trình đường thẳng $BC$ là $%s = 0$' % (latex(sp.simplify(dtBC)))
            da_c_s = 'Phương trình đường thẳng $BC$ là $ %s = 0$' % (latex(sp.simplify(dtBC + x)))
            list_c = [da_c_d, da_c_s]
            vd_da_1 = random.choice(list_c)

            loigiai_c = ('''Đường thẳng $BC$ đi qua hai điểm $B\\left( %s; %s \\right)$ và $C\\left( %s; %s \\right)$. \\\\
            Véctơ chỉ phương $\\vec{BC} = \\left( %s; %s \\right)$. \\\\
            Phương trình đường thẳng $BC$ là: $%s = 0$.''' 
                         % (latex(ptB[0]), latex(ptB[1]), latex(ptC[0]), latex(ptC[1]), latex(ptC[0]-ptB[0]), latex(ptC[1]-ptB[1]), latex(sp.simplify(dtBC))))

            ########################################################################
            # Mệnh đề d: Phương trình AC
            da_d_d = '\\True Phương trình đường thẳng $AC$ là $%s = 0$' % (latex(sp.simplify(dtAC)))
            da_d_s = 'Phương trình đường thẳng $BC$ là $3x - 3y + 3 = 0$' # Giống phương án sai trong ảnh
            list_d = [da_d_d, da_d_s]
            vdc_da_1 = random.choice(list_d)

            loigiai_d = ('''Đường thẳng $AC$ đi qua hai điểm $A(%s; %s)$ và $C\\left( %s; %s \\right)$. \\\\
            Véctơ pháp tuyến $\\vec{n}_{AC} = \\left( %s; %s \\right)$. \\\\
            Phương trình đường thẳng $AC$ là: $%s = 0$.''' 
                         % (xA, yA, latex(ptC[0]), latex(ptC[1]), latex(n_AC[0]), latex(n_AC[1]), latex(sp.simplify(dtAC))))

            # --- PHẦN LOGIC XÁO TRỘN VÀ ĐIỀU KIỆN ĐÚNG/SAI ---
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                d_a = random.choice(list_a)
                d_b = random.choice(list_b)
                d_c = random.choice(list_c)
                d_d = random.choice(list_d)
                if 1 <= count_true_answers([d_a, d_b, d_c, d_d]) <= 3:
                    break

            shuffled_answers = [d_a, d_b, d_c, d_d]
            shuffled_solutions = [loigiai_a, loigiai_b, loigiai_c, loigiai_d]

            # --- XUẤT NỘI DUNG ---
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + 
                str(noidungcauhoi) + 
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
                '\\end{ex}\n \\end{minipage} \n\n').replace('+-','-').replace('+ -','-')
            return content   

