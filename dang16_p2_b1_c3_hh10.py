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


def bt_dang16_p2_b1_c3_hh10(self):
            # Khai báo biến
            # Khai báo các ký hiệu
            x, y, t = symbols('x y t')

            # B1: Nghiên cứu và khởi tạo các hệ số ngẫu nhiên cho bài toán
            # Delta 1: A1*x + B1*y + C1 = 0
            A1 = random.choice([i for i in range(-5, 6) if i != 0])
            B1 = random.choice([i for i in range(-5, 6) if i != 0])
            C1 = random.choice([1,2,3,4,5,6,7,8,9,-1,-2,-3,-4,-5,-6,-7,-8,-9])

            # Delta 2: x = x2 + ux*t; y = y2 + uy*t
            x2 = random.randint(-5, 5)
            y2 = random.randint(-5, 5)
            ux = random.choice([i for i in range(-5, 6) if i != 0])
            uy = random.choice([i for i in range(-5, 6) if i != 0])

            # Các đối tượng hình học
            # n1_dung = (A1, B1), n1_sai = (B1, A1) hoặc (A1, -B1)
            n1_dung = (A1, B1)
            n1_sai = (A1, -B1) if B1 != -B1 else (B1, A1+1)

            # n2_dung: tu u(ux, uy) -> n(uy, -ux)
            n2_dung = (uy, -ux)
            n2_sai = (ux, uy)

            # Tham số hóa Delta 1: x = t -> y = (-A1*t - C1)/B1
            # Để đẹp, ta chọn x = t. Khi đó B1*y = -A1*t - C1
            # Phương trình: x = t; y = (-A1/B1)t - C1/B1
            pt_ts_d1_dung = r"\begin{cases} x = t \\ y = %s + %s t \end{cases}" % (latex(Rational(-C1, B1)), latex(Rational(-A1, B1)))
            pt_ts_d1_sai = r"\begin{cases} x = t \\ y = %s - %s t \end{cases}" % (latex(Rational(-C1, B1)), latex(Rational(-A1, B1)))

            # Tổng quát hóa Delta 2: uy(x - x2) - ux(y - y2) = 0 <=> uy*x - ux*y + (ux*y2 - uy*x2) = 0
            C2 = ux*y2 - uy*x2
            pt_tq_d2_dung = "%s x %s y %s = 0" % (latex(uy) if uy != 1 else "", latex(-ux) if -ux < 0 else "+ " + latex(-ux), latex(C2) if C2 < 0 else "+ " + latex(C2))
            pt_tq_d2_sai = "%s x %s y %s = 0" % (latex(ux), latex(uy) if uy < 0 else "+ " + latex(uy), latex(-C2) if -C2 < 0 else "+ " + latex(-C2))

            # Nội dung câu hỏi gốc
            noidungcauhoi = ('''Cho hai đường thẳng $\\Delta_1 : %s x %s y %s = 0$ và $\\Delta_2 : \\begin{cases} x = %s %s t \\\\ y = %s %s t \\end{cases}$.''' 
                             % (latex(A1) if A1 != 1 else "", 
                                latex(B1) if B1 < 0 else "+ " + latex(B1), 
                                latex(C1) if C1 < 0 else "+ " + latex(C1),
                                latex(x2), latex(ux) if ux < 0 else "+ " + latex(ux),
                                latex(y2), latex(uy) if uy < 0 else "+ " + latex(uy)))

            ########################################################################
            # a) Nhận biết: Vectơ pháp tuyến Delta 1
            nb_da_1_d = r'\True Đường thẳng $\Delta_1$ có vectơ pháp tuyến $\vec{n}(%s; %s)$' % (A1, B1)
            nb_da_1_s = r'Đường thẳng $\Delta_1$ có vectơ pháp tuyến $\vec{n}(%s; %s)$' % (n1_sai[0], n1_sai[1])
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

            loigiai_nb_1 = (r'''Đường thẳng $\Delta_1$ có dạng tổng quát $Ax + By + C = 0$ nên có một vectơ pháp tuyến là $\vec{n} = (A; B) = (%s; %s)$.''' % (A1, B1))

            ########################################################################
            # b) Thông hiểu: Vectơ pháp tuyến Delta 2
            th_da_1_d = r'\True Đường thẳng $\Delta_2$ có vectơ pháp tuyến là $\vec{n}(%s; %s)$' % (n2_dung[0], n2_dung[1])
            th_da_1_s = r'Đường thẳng $\Delta_2$ có vectơ pháp tuyến là $\vec{n}(%s; %s)$' % (n2_sai[0], n2_sai[1])
            list_th_da_1 = [th_da_1_d, th_da_1_s]

            loigiai_th_1 = (r'''Đường thẳng $\Delta_2$ có vectơ chỉ phương là $\vec{u} = (%s; %s)$. Suy ra một vectơ pháp tuyến của $\Delta_2$ là $\vec{n} = (%s; %s)$.''' % (ux, uy, n2_dung[0], n2_dung[1]))

            ########################################################################
            # c) Vận dụng: Phương trình tham số Delta 1
            vd_da_1_d = r'\True Phương trình tham số của đường thẳng $\Delta_1$ là $%s$' % pt_ts_d1_dung
            vd_da_1_s = r'Phương trình tham số của đường thẳng $\Delta_1$ là $%s$' % pt_ts_d1_sai
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

            loigiai_vd_1 = (r'''Đặt $x = t$, thay vào phương trình $\Delta_1$ ta có: $%s t +%s y +%s = 0 \Leftrightarrow %s y = %s t +%s \Leftrightarrow y = %s + %s t$. Vậy phương trình tham số là $%s$.''' 
                            % (A1, B1, C1, B1, -A1, -C1, latex(Rational(-C1, B1)), latex(Rational(-A1, B1)), pt_ts_d1_dung))

            ########################################################################
            # d) Vận dụng cao: Phương trình tổng quát Delta 2
            vdc_da_1_d = r'\True Phương trình tổng quát của đường thẳng $\Delta_2$ là $%s$' % pt_tq_d2_dung
            vdc_da_1_s = r'Phương trình tổng quát của đường thẳng $\Delta_2$ là $%s$' % pt_tq_d2_sai
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

            loigiai_vdc_1 = (r'''Từ phương trình tham số của $\Delta_2$, ta có vectơ pháp tuyến là $\vec{n}(%s; %s)$ và đi qua điểm $M(%s; %s)$. Phương trình tổng quát: $%s(x - %s) %s(y - %s) = 0 \Leftrightarrow %s$.''' 
                             % (n2_dung[0], n2_dung[1], x2, y2, n2_dung[0], x2, "+" if n2_dung[1] > 0 else "-", abs(y2) if y2 < 0 else y2, pt_tq_d2_dung))

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Lặp đến khi đáp án có từ 1 đến 3 câu đúng
            while True:
                nb_da = random.choice(list_nb_da_1)
                th_da = random.choice(list_th_da_1)
                vd_da = random.choice(list_vd_da_1)
                vdc_da = random.choice(list_vdc_da_1)

                answers = [nb_da, th_da, vd_da, vdc_da]
                if 1 <= count_true_answers(answers) <= 3:
                    break

            # Gán lời giải tương ứng
            sol_nb = loigiai_nb_1
            sol_th = loigiai_th_1
            sol_vd = loigiai_vd_1
            sol_vdc = loigiai_vdc_1

            # Xuất câu hỏi
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + 
                str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
                '{' + str(nb_da) + '}\n'
                '{' + str(th_da) + '}\n'
                '{' + str(vd_da) + '}\n'
                '{' + str(vdc_da) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(sol_nb) + '\n'
                '\\item ' + str(sol_th) + '\n'
                '\\item ' + str(sol_vd) + '\n'
                '\\item ' + str(sol_vdc) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('+ -', '-').replace('+-', '-').replace('+ +', '+').replace('++', '+')
            return content   

