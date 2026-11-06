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


def bt_dang17_p2_b1_c3_hh10(self):
            # Khai báo biến
            # Khai báo biến
            x, y, t = symbols('x y t')

            # B1: Khởi tạo các giá trị ngẫu nhiên cho điểm A, B và M
            # Để đảm bảo số đẹp, ta chọn tọa độ nguyên nhỏ
            xA = random.randint(-5, 5)
            yA = random.randint(-5, 5)
            xB = xA + random.randint(1, 6) # Đảm bảo B khác A
            yB = yA + random.randint(1, 6)

            xM = random.randint(-5, 5)
            yM = random.randint(-5, 5)

            # Tính toán các thông số hình học
            # Vectơ chỉ phương AB = (u1, u2)
            u1 = xB - xA
            u2 = yB - yA

            # Vectơ pháp tuyến n = (u2, -u1)
            n1 = u2
            n2 = -u1

            # Phương trình tổng quát AB: n1(x - xA) + n2(y - yA) = 0 <=> n1*x + n2*y + C = 0
            C_val = -n1*xA - n2*yA
            pt_tong_quat = n1*x + n2*y + C_val

            # Nội dung câu hỏi
            noidungcauhoi = ('''Trong mặt phẳng tọa độ $Oxy$, cho hai điểm $A(%s; %s), B(%s; %s)$.''' 
                             %(latex(xA), latex(yA), latex(xB), latex(yB)))

            ########################################################################
            # a) Nhận biết: Vectơ chỉ phương
            ########################################################################
            nb_da_1_d = '\\True Đường thẳng $AB$ có vectơ chỉ phương là $\\vec{AB}=(%s;%s)$' %(latex(u1), latex(u2))
            nb_da_1_s = 'Đường thẳng $AB$ có vectơ chỉ phương là $\\vec{AB}=(%s;%s)$' %(latex(u2), latex(u1))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

            loigiai_nb_1 = ('''Ta có $\\vec{AB} = (x_B - x_A; y_B - y_A) = (%s - (%s); %s - (%s)) = (%s; %s)$.''' 
                            %(latex(xB), latex(xA), latex(yB), latex(yA), latex(u1), latex(u2)))

            ########################################################################
            # b) Thông hiểu: Vectơ pháp tuyến
            ########################################################################
            th_da_1_d = '\\True Đường thẳng $AB$ có vectơ pháp tuyến là $\\vec{n}=(%s;%s)$' %(latex(n1), latex(n2))
            th_da_1_s = 'Đường thẳng $AB$ có vectơ pháp tuyến là $\\vec{n}=(%s;%s)$' %(latex(u1), latex(u2))
            list_th_da_1 = [th_da_1_d, th_da_1_s]

            loigiai_th_1 = ('''Vì đường thẳng $AB$ có vectơ chỉ phương là $\\vec{AB} = (%s; %s)$ nên nó có một vectơ pháp tuyến là $\\vec{n} = (%s; %s)$.''' 
                            %(latex(u1), latex(u2), latex(n1), latex(n2)))

            ########################################################################
            # c) Vận dụng: Phương trình tổng quát
            ########################################################################
            vd_da_1_d = '\\True Phương trình tổng quát của đường thẳng $AB$ là $%s = 0$' %(latex(pt_tong_quat))
            vd_da_1_s = 'Phương trình tổng quát của đường thẳng $AB$ là $%s = 0$' %(latex(u1*x + u2*y - (u1*xA + u2*yA)))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

            loigiai_vd_1 = ('''Đường thẳng $AB$ đi qua điểm $A(%s; %s)$ và nhận $\\vec{n} = (%s; %s)$ làm vectơ pháp tuyến có phương trình là: \\\\
                            $%s(x - (%s)) %s(y - (%s)) = 0 \\Leftrightarrow %s = 0$.''' 
                            %(latex(xA), latex(yA), latex(n1), latex(n2), latex(n1), latex(xA), "+" if n2 >=0 else "", latex(yA), latex(pt_tong_quat)))

            ########################################################################
            # d) Vận dụng cao: Phương trình tham số đường thẳng song song
            ########################################################################
            # Đường thẳng qua M và song song AB nhận AB làm VTCP
            vdc_da_1_d = '\\True Phương trình tham số của đường thẳng đi qua $M(%s;%s)$ và song song với $AB$ là $\\begin{cases} x = %s + %st \\\\ y = %s + %st \\end{cases}$' %(latex(xM), latex(yM), latex(xM), latex(u1), latex(yM), latex(u2))
            vdc_da_1_s = 'Phương trình tham số của đường thẳng đi qua $M(%s;%s)$ và song song với $AB$ là $\\begin{cases} x = %s + %st \\\\ y = %s + %st \\end{cases}$' %(latex(xM), latex(yM), latex(xM), latex(u2), latex(yM), latex(u1))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

            loigiai_vdc_1 = ('''Đường thẳng song song với $AB$ nên nhận vectơ chỉ phương của $AB$ là $\\vec{AB} = (%s; %s)$ làm vectơ chỉ phương. \\\\
                            Phương trình tham số của đường thẳng đi qua $M(%s; %s)$ và có VTCP $(%s; %s)$ là: \\\\
                            $\\begin{cases} x = %s + %st \\\\ y = %s + %st \\end{cases}$.''' 
                            %(latex(u1), latex(u2), latex(xM), latex(yM), latex(u1), latex(u2), latex(xM), latex(u1), latex(yM), latex(u2)))

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Lặp đến khi có từ 1 đến 3 đáp án đúng
            while True:
                nb_da = random.choice(list_nb_da_1)
                th_da = random.choice(list_th_da_1)
                vd_da = random.choice(list_vd_da_1)
                vdc_da = random.choice(list_vdc_da_1)

                answers = [nb_da, th_da, vd_da, vdc_da]
                if 1 <= count_true_answers(answers) <= 3:
                    break

            # Xuất nội dung theo mẫu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
                '{' + str(nb_da) + '}\n'
                '{' + str(th_da) + '}\n'
                '{' + str(vd_da) + '}\n'
                '{' + str(vdc_da) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(loigiai_nb_1) + '\n'
                '\\item ' + str(loigiai_th_1) + '\n'
                '\\item ' + str(loigiai_vd_1) + '\n'
                '\\item ' + str(loigiai_vdc_1) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('- -', '+')
            return content   

