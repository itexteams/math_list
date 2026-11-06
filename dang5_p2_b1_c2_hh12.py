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


def bt_dang5_p2_b1_c2_hh12(self):
            # Khai báo biến
            def is_collinear(v1, v2):
                """Kiểm tra hai vectơ có cùng phương không."""
                v1_mat = Matrix(v1)
                v2_mat = Matrix(v2)
                # Cùng phương nếu cross product là vectơ zero, hoặc nếu một vectơ là bội số của vectơ kia.
                # Trong 3D, cách đơn giản là kiểm tra rank của ma trận chứa 2 vectơ là 1.
                if v1 == (0, 0, 0) or v2 == (0, 0, 0):
                    return True

                # Dùng cross product
                cross = v1_mat.cross(v2_mat)
                return cross == Matrix([0, 0, 0])

            def generate_points():
                """Tạo ngẫu nhiên các điểm A, B, C không thẳng hàng."""
                while True:
                    # Tọa độ điểm A
                    xA, yA, zA = randint(-3, 3), randint(-3, 3), randint(-3, 3)
                    # Tọa độ điểm B
                    xB, yB, zB = randint(-3, 3), randint(-3, 3), randint(-3, 3)
                    # Tọa độ điểm C
                    xC, yC, zC = randint(-3, 3), randint(-3, 3), randint(-3, 3)

                    # Tính vectơ AB và AC
                    vAB = (xB - xA, yB - yA, zB - zA)
                    vAC = (xC - xA, yC - yA, zC - zA)

                    # Kiểm tra điều kiện: A, B, C không thẳng hàng (vAB và vAC không cùng phương)
                    if not is_collinear(vAB, vAC) and vAB != (0, 0, 0) and vAC != (0, 0, 0):
                        break

                # Tính vectơ BC
                vBC = (xC - xB, yC - yB, zC - zB)

                # vectơ j (tương tự vectơ j=(0;1;0) hoặc k=(0;0;1) để đơn giản)
                # Đảm bảo vJ không cùng phương với vBC
                vJ = (0, 1, 0)
                if is_collinear(vJ, vBC):
                    vJ = (0, 0, 1) # Nếu cùng phương, đổi sang vectơ k

                return (xA, yA, zA), (xB, yB, zB), (xC, yC, zC), vAB, vAC, vBC, vJ

            # Thực hiện tạo điểm
            A_coords, B_coords, C_coords, vAB, vAC, vBC, vJ = generate_points()
            (xA, yA, zA) = A_coords
            (xB, yB, zB) = B_coords
            (xC, yC, zC) = C_coords

            # Biểu diễn tọa độ latex
            A_latex = '(%s; %s; %s)' % (latex(xA), latex(yA), latex(zA))
            B_latex = '(%s; %s; %s)' % (latex(xB), latex(yB), latex(zB))
            C_latex = '(%s; %s; %s)' % (latex(xC), latex(yC), latex(zC))

            # Biểu diễn vectơ latex
            vAB_latex = '(%s; %s; %s)' % (latex(vAB[0]), latex(vAB[1]), latex(vAB[2]))
            vAC_latex = '(%s; %s; %s)' % (latex(vAC[0]), latex(vAC[1]), latex(vAC[2]))
            vBC_latex = '(%s; %s; %s)' % (latex(vBC[0]), latex(vBC[1]), latex(vBC[2]))
            vJ_latex = '(%s; %s; %s)' % (latex(vJ[0]), latex(vJ[1]), latex(vJ[2]))

            # Tính vectơ Pháp tuyến n_ABC
            vAB_mat = Matrix(vAB)
            vAC_mat = Matrix(vAC)
            vN_ABC = vAB_mat.cross(vAC_mat)
            vN_ABC_latex = '(%s; %s; %s)' % (latex(vN_ABC[0]), latex(vN_ABC[1]), latex(vN_ABC[2]))

            # vectơ pháp tuyến rút gọn (chia cho ước chung lớn nhất)
            def get_simplified_normal_vectơ(v):
                v_abs = [abs(x) for x in v]
                gcd_val = math.gcd(v_abs[0], math.gcd(v_abs[1], v_abs[2]))
                if gcd_val != 0:
                    return (v[0] // gcd_val, v[1] // gcd_val, v[2] // gcd_val)
                return v

            vN_ABC_simple = get_simplified_normal_vectơ(vN_ABC)
            vN_ABC_simple_latex = '(%s; %s; %s)' % (latex(vN_ABC_simple[0]), latex(vN_ABC_simple[1]), latex(vN_ABC_simple[2]))

            # Tính vectơ Pháp tuyến n_alpha (chứa vJ và vBC)
            vJ_mat = Matrix(vJ)
            vBC_mat = Matrix(vBC)
            vN_alpha = vJ_mat.cross(vBC_mat)
            vN_alpha_latex = '(%s; %s; %s)' % (latex(vN_alpha[0]), latex(vN_alpha[1]), latex(vN_alpha[2]))

            # Nội dung câu hỏi
            noidungcauhoi = ('''Trong không gian $Oxyz$, cho các điểm $A%s$, $B%s$, $C%s$.''' 
                            %(A_latex, B_latex, C_latex))


            # a) Nhận biết: vectơ AB
            nb_da_1_d = '\\True $\\vec{AB} = %s$' % vAB_latex
            # Đáp án sai: dùng vectơ AC thay vì AB
            nb_da_1_s = '$\\vec{AB} = %s$' % vAC_latex
            list_nb_da_1=[nb_da_1_d, nb_da_1_s]
            nb_da_1=random.choice(list_nb_da_1)
            loigiai_nb_1 = ('''Ta có $\\vec{AB} = (x_B - x_A; y_B - y_A; z_B - z_A) = %s$.''' 
                            % vAB_latex)

            # b) Thông hiểu: Collinearity (A, B, C không thẳng hàng)
            th_da_1_d = '\\True Ba điểm $A, B, C$ không thẳng hàng'
            # Đáp án sai: Khẳng định thẳng hàng
            th_da_1_s = 'Ba điểm $A, B, C$ thẳng hàng'
            list_th_da_1=[th_da_1_d, th_da_1_s]
            th_da_1=random.choice(list_th_da_1)
            loigiai_th_1 = ('''Ta có $\\vec{AB} = %s$ và $\\vec{AC} = %s$. \\\\
                            Vì $\\vec{AB}$ và $\\vec{AC}$ không cùng phương nên ba điểm $A, B, C$ không thẳng hàng.'''
                            % (vAB_latex, vAC_latex))

            # c) Vận dụng: Normal vectơ of Plane (ABC)
            # Lấy vectơ pháp tuyến rút gọn
            vd_da_1_d = '\\True Mặt phẳng $(ABC)$ có một vectơ pháp tuyến là $\\vec{n}_1 = %s$' % vN_ABC_simple_latex
            # Đáp án sai: Lấy vectơ BC
            vd_da_1_s = 'Mặt phẳng $(ABC)$ có một vectơ pháp tuyến là $\\vec{n}_1 = %s$' % vBC_latex
            list_vd_da_1=[vd_da_1_d, vd_da_1_s]
            vd_da_1=random.choice(list_vd_da_1)
            loigiai_vd_1 = ('''Mặt phẳng $(ABC)$ có cặp vectơ chỉ phương $\\vec{AB} = %s$, $\\vec{AC} = %s$. \\\\
                            Một vectơ pháp tuyến là $\\vec{N} = \\left[\\vec{AB}, \\vec{AC} \\right] = %s$. \\\\
                            Vectơ $\\vec{n}_1 = %s$ cùng phương với $\\vec{N}$ nên cũng là một vectơ pháp tuyến.'''
                            % (vAB_latex, vAC_latex, vN_ABC_latex, vN_ABC_simple_latex))

            # d) Vận dụng cao: Normal vectơ of Plane (alpha)
            # Giả sử mặt phẳng (alpha) song song với $\vec{j}$ và $\vec{BC}$
            vdc_da_1_d = '\\True Mặt phẳng $(\\alpha)$ song song với giá của hai vectơ $\\vec{j} = %s$ và $\\vec{BC}$ có một vectơ pháp tuyến là $\\vec{n}_2 = %s$' % (vJ_latex, vN_alpha_latex)
            # Đáp án sai: Lấy vectơ AB
            vdc_da_1_s = 'Mặt phẳng $(\\alpha)$ song song với giá của hai vectơ $\\vec{j} = %s$ và $\\vec{BC}$ có một vectơ pháp tuyến là $\\vec{n}_2 = %s$' % (vJ_latex, vAB_latex)
            list_vdc_da_1=[vdc_da_1_d, vdc_da_1_s]
            vdc_da_1=random.choice(list_vdc_da_1)
            loigiai_vdc_1 = ('''Mặt phẳng $(\\alpha)$ có cặp vectơ chỉ phương $\\vec{j} = %s$ và $\\vec{BC} = %s$. \\\\
                            Một vectơ pháp tuyến là $\\vec{n}_2 = \\left[\\vec{j}, \\vec{BC}\\right] = %s$.'''
                            % (vJ_latex, vBC_latex, vN_alpha_latex))


            # --- Kết hợp và Xáo trộn ---
            list_nb_1 = [nb_da_1]
            list_th_1 = [th_da_1]
            list_vd_1 = [vd_da_1]
            list_vdc_1 = [vdc_da_1]

            list_nb_2 = [loigiai_nb_1]
            list_th_2 = [loigiai_th_1]
            list_vd_2 = [loigiai_vd_1]
            list_vdc_2 = [loigiai_vdc_1]

            # Đảm bảo số lượng đáp án True là 1, 2, hoặc 3
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                nb_da_1 = random.choice(list_nb_da_1)
                th_da_1 = random.choice(list_th_da_1)
                vd_da_1 = random.choice(list_vd_da_1)
                vdc_da_1 = random.choice(list_vdc_da_1)

                answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                true_count = count_true_answers(answers)

                # Lặp lại nếu True count không nằm trong [1, 3]
                if 1 <= true_count <= 3:
                    break

            # Gán lại vào list sau khi đã chọn ngẫu nhiên đáp án đúng/sai
            list_nb_1 = [nb_da_1]
            list_th_1 = [th_da_1]
            list_vd_1 = [vd_da_1]
            list_vdc_1 = [vdc_da_1]

            combined_nb = list(zip(list_nb_1, list_nb_2))
            combined_th = list(zip(list_th_1, list_th_2))
            combined_vd = list(zip(list_vd_1, list_vd_2))
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))

            # Xáo trộn từng cặp (đáp án, lời giải)
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
            str(noidungcauhoi)+ 
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
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

