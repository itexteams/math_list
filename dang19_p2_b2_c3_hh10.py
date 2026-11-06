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


def bt_dang19_p2_b2_c3_hh10(self):
            # Khai báo biến
            # Khai báo biến
            x, y = symbols('x y')

            # --- Bước 1: Tạo dữ liệu ngẫu nhiên cho đường thẳng d: x + by + c = 0 ---
            a_d = 1
            b_d = 2 # Giữ nguyên hệ số giống ảnh mẫu hoặc random.choice([2, 3])
            c_d = -1 

            line_d_expr = a_d*x + b_d*y + c_d

            # Nội dung câu hỏi
            noidungcauhoi = ('''Trong mặt phẳng tọa độ $(Oxy)$, cho đường thẳng $d: %s = 0$.''' 
                            % (latex(line_d_expr)))

            ########################################################################
            # a) Nhận biết ########################################################
            a_delta = 1
            b_delta = -2
            c_delta = 2
            line_delta = a_delta*x + b_delta*y + c_delta

            nb_da_1_d = '\\True Đường thẳng $d$ cắt đường thẳng $\\Delta : %s = 0$' % (latex(line_delta))
            nb_da_1_s = 'Đường thẳng $d$ song song với đường thẳng $\\Delta : %s = 0$' % (latex(line_delta))

            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)
            list_nb_1 = [nb_da_1]

            loigiai_nb_1 = ('''Đường thẳng $d$ có vectơ pháp tuyến $\\vec{n}_d = (1; %s)$, đường thẳng $\\Delta$ có vectơ pháp tuyến $\\vec{n}_{\\Delta} = (1; %s)$. \\\\
            Vì $\\frac{1}{1} \\neq \\frac{%s}{%s}$ nên hai đường thẳng $d$ và $\\Delta$ cắt nhau.''' 
                            % (b_d, b_delta, b_d, b_delta))
            list_nb_2 = [loigiai_nb_1]

            ########################################################################
            # b) Thông hiểu #######################################################
            k_b = 2
            line_delta1_true = k_b*a_d*x + k_b*b_d*y + k_b*c_d

            th_da_1_d = '\\True $d$ trùng với $\\Delta_1 : %s = 0$' % (latex(line_delta1_true))
            th_da_1_s = '$d$ song song với $\\Delta_1 : %s = 0$' % (latex(line_delta1_true))

            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)
            list_th_1 = [th_da_1]

            loigiai_th_1 = ('''Đường thẳng $d$ có phương trình $%s = 0$. Nhân cả hai vế của phương trình với $%s$, ta được $%s = 0$. Phương trình này trùng với phương trình của đường thẳng $\\Delta_1$. Vậy $d$ trùng với $\\Delta_1$.''' 
                            % (latex(line_d_expr), k_b, latex(line_delta1_true)))
            list_th_2 = [loigiai_th_1]

            ########################################################################
            # c) Vận dụng #########################################################
            xA, yA = -3, 4
            # Delta2 vuông góc d: b_d*x - a_d*y + m = 0
            m_c = -(b_d*xA - a_d*yA)
            line_delta2 = b_d*x - a_d*y + m_c

            vd_da_1_d = '\\True Đường thẳng $\\Delta_2$ đi qua điểm $A\\left( %s; %s \\right)$ và vuông góc với đường thẳng $d$ là $\\Delta_2 : %s = 0$' % (xA, yA, latex(line_delta2))
            vd_da_1_s = 'Đường thẳng $\\Delta_2$ đi qua điểm $A\\left( %s; %s \\right)$ và vuông góc với đường thẳng $d$ là $\\Delta_2 : %s = 0$' % (xA, yA, latex(line_d_expr))

            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)
            list_vd_1 = [vd_da_1]

            loigiai_vd_1 = ('''Đường thẳng $d$ có vectơ pháp tuyến $\\vec{n}_d = \\left( 1; %s \\right)$. Vì $\\Delta_2 \\perp d$ nên $\\Delta_2$ nhận vectơ $\\vec{n}_{\\Delta_2} = \\left( %s; -1 \\right)$ làm vectơ pháp tuyến. \\\\
            Phương trình đường thẳng $\\Delta_2$ đi qua $A\\left( %s; %s \\right)$ là: \\\\
            $%s\\left( x - \\left( %s \\right) \\right) - 1\\left( y - %s \\right) = 0 \\Leftrightarrow %s = 0$.''' 
                            % (b_d, b_d, xA, yA, b_d, xA, yA, latex(line_delta2)))
            list_vd_2 = [loigiai_vd_1]

            ########################################################################
            # d) Vận dụng cao #####################################################
            yM_target = 1
            xM_target = solve(line_d_expr.subs(y, yM_target), x)[0]
            # Đường thẳng Delta qua M vuông góc d
            m_d = -(b_d*xM_target - a_d*yM_target)
            line_delta_vdc = b_d*x - a_d*y + m_d

            # Giao điểm Ox, Oy
            xP = solve(line_delta_vdc.subs(y, 0), x)[0]
            yQ = solve(line_delta_vdc.subs(x, 0), y)[0]
            S_val = abs(Rational(1, 2) * xP * yQ)
            S_str = str(latex(S_val)).replace('.', ',')

            vdc_da_1_d = '\\True Gọi $M$ là điểm có hoành độ dương thuộc đường thẳng $d$ sao cho đường thẳng $\\Delta$ đi qua điểm $M$ và vuông góc với đường thẳng $d$ hợp với các trục tọa độ một tam giác có diện tích bằng $%s$. Khi đó, tung độ điểm $M$ bằng $%s$' % (S_str, yM_target)
            vdc_da_1_s = 'Khi đó, tung độ điểm $M$ bằng $%s$' % (yM_target + 2)

            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)
            list_vdc_1 = [vdc_da_1]

            loigiai_vdc_1 = ('''Gọi $M\\left( x_0; y_0 \\right) \\in d \\Rightarrow x_0 = 1 - 2y_0$. \\\\
            Đường thẳng $\\Delta$ đi qua $M$ và vuông góc với $d$ có phương trình: $2\\left( x - x_0 \\right) - \\left( y - y_0 \\right) = 0 \\Leftrightarrow 2x - y + y_0 - 2x_0 = 0$. \\\\
            Thay $x_0 = 1 - 2y_0$ vào ta được: $2x - y + 5y_0 - 2 = 0$. \\\\
            Giao điểm của $\\Delta$ với $Ox$ là $P\\left( \\frac{2 - 5y_0}{2}; 0 \\right)$, với $Oy$ là $Q\\left( 0; 2 - 5y_0 \\right)$. \\\\
            Diện tích tam giác $OPQ$ là $S = \\frac{1}{2} |x_P| \\cdot |y_Q| = \\frac{1}{2} \\cdot \\left| \\frac{2 - 5y_0}{2} \\right| \\cdot |2 - 5y_0| = \\frac{\\left( 2 - 5y_0 \\right)^2}{4}$. \\\\
            Theo đề bài $S = %s \\Leftrightarrow \\frac{\\left( 2 - 5y_0 \\right)^2}{4} = %s \\Leftrightarrow \\left( 2 - 5y_0 \\right)^2 = %s$. \\\\
            Giải phương trình và kết hợp điều kiện hoành độ $x_0 > 0$, ta chọn được $y_0 = %s$.''' 
                             % (S_str, S_str, latex(4*S_val), yM_target))
            list_vdc_2 = [loigiai_vdc_1]

            # --- Trộn đáp án ---
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                ans_nb = random.choice(list_nb_da_1)
                ans_th = random.choice(list_th_da_1)
                ans_vd = random.choice(list_vd_da_1)
                ans_vdc = random.choice(list_vdc_da_1)
                if 1 <= count_true_answers([ans_nb, ans_th, ans_vd, ans_vdc]) <= 3:
                    break

            # --- Xuất nội dung ---
            content = ('\\begin{minipage}{\\textwidth} \n' +
                '\\begin{ex}\n' +
                str(noidungcauhoi) + ' \n' +
                '\\choiceTFn \n' +
                '{' + str(ans_nb) + '}\n' +
                '{' + str(ans_th) + '}\n' +
                '{' + str(ans_vd) + '}\n' +
                '{' + str(ans_vdc) + '}\n' +
                '\\loigiai{ \n' +
                '\\begin{enumEX}[a)]{1} \n' +
                '\\item ' + str(loigiai_nb_1) + '\n' +
                '\\item ' + str(loigiai_th_1) + '\n' +
                '\\item ' + str(loigiai_vd_1) + '\n' +
                '\\item ' + str(loigiai_vdc_1) + '\n' +
                '\\end{enumEX}} \n' +
                '\\end{ex}\n' +
                '\\end{minipage}\n\n')
            return content   

