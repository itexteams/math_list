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


def bt_dang43_p2_b3_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # Random hóa bài toán: Giả sử bất phương trình x^2 - 2kx + m <= 0
            # Trong bài gốc: k = 2 (hệ số -4x)
            k = random.randint(2, 5)
            he_so_b = -2 * k
            tong_nghiem = 2 * k

            # Nội dung câu hỏi
            noidungcauhoi = (r'''Cho bất phương trình $x^2 %s x + m \leq 0$.''' 
                             % (latex(he_so_b)))

            ########################################################################
            # Nhận biết 
            ########################################################################
            nb_da_1_d = r'\True Bất phương trình đã cho không thể có tập nghiệm $\mathbb{R}$'
            nb_da_1_s = r'Bất phương trình đã cho luôn có tập nghiệm là $\mathbb{R}$ với mọi $m < 0$'
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            loigiai_nb_1 = (r'''Vì hệ số của $x^2$ là $1 > 0$, nên parabol $y = x^2 %s x + m$ luôn hướng bề lõm lên trên. Do đó, tập nghiệm của bất phương trình không thể là $\mathbb{R}$.''' 
                            % (latex(he_so_b)))

            list_nb_2 = [loigiai_nb_1]

            ########################################################################
            # Thông hiểu
            ########################################################################
            # Chọn m sao cho delta' > 0 để có độ dài cụ thể. Độ dài L = 2*sqrt(delta')
            do_dai = 2
            m_val = k**2 - (do_dai/2)**2
            th_da_1_d = r'\True Với $m = %s$ thì bất phương trình có tập nghiệm với độ dài bằng $%s$' % (latex(int(m_val)), latex(do_dai))
            th_da_1_s = r'Với $m = %s$ thì bất phương trình có tập nghiệm với độ dài bằng $%s$' % (latex(int(m_val)), latex(do_dai+1))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            loigiai_th_1 = (r'''Với $m = %s$, ta có $x^2 %s x + %s \leq 0$. Nghiệm của tam thức là $x = %s$ và $x = %s$. Tập nghiệm là $[%s; %s]$, độ dài bằng %s.''' 
                            % (latex(int(m_val)), latex(he_so_b), latex(int(m_val)), latex(k-1), latex(k+1), latex(k-1), latex(k+1), latex(do_dai)))

            list_th_2 = [loigiai_th_1]

            ########################################################################
            # Vận dụng
            ########################################################################
            vd_da_1_d = r'\True Nếu bất phương trình có tập nghiệm $S=[a;b]$ thì $a+b = %s, \forall m$' % (latex(tong_nghiem))
            vd_da_1_s = r'Nếu bất phương trình có tập nghiệm $S=[a;b]$ thì $a+b = m, \forall m$'
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            loigiai_vd_1 = (r'''Nếu bất phương trình có tập nghiệm $S=[a;b]$ thì $a, b$ là hai nghiệm của phương trình $x^2 %s x + m = 0$. Theo định lý Vi-ét, ta có $a+b = - \frac{-2k}{1} = %s$.''' 
                            % (latex(he_so_b), latex(tong_nghiem)))

            list_vd_2 = [loigiai_vd_1]

            ########################################################################
            # Vận dụng cao
            ########################################################################
            # Xét a^2 + b^2 <= Target. Ta có (a+b)^2 - 2ab = (2k)^2 - 2m
            target = tong_nghiem**2 - 2*(k**2 - 2) # Tạo ra khoảng 2 giá trị nguyên cho m
            vdc_da_1_d = r'\True Có đúng 2 số nguyên $m$ để bất phương trình có tập nghiệm $S=[a;b]$ thỏa mãn $a^2+b^2 \leq %s$' % (latex(target))
            vdc_da_1_s = r'Có đúng 4 số nguyên $m$ để bất phương trình có tập nghiệm $S=[a;b]$ thỏa mãn $a^2+b^2 \leq %s$' % (latex(target))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            loigiai_vdc_1 = (r'''Ta có $a^2+b^2 = (a+b)^2 - 2ab = %s - 2m$. Điều kiện bài toán: $%s - 2m \leq %s \Leftrightarrow 2m \geq %s \Leftrightarrow m \geq %s$. Để tồn tại tập nghiệm $[a;b]$ thì $\Delta' = %s - m \geq 0 \Leftrightarrow m \leq %s$. Vậy $m \in \{ %s; %s \}$.''' 
                             % (latex(tong_nghiem**2), latex(tong_nghiem**2), latex(target), latex(tong_nghiem**2 - target), latex(int((tong_nghiem**2 - target)/2)), latex(k**2), latex(k**2), latex(k**2-1), latex(k**2)))

            list_vdc_2 = [loigiai_vdc_1]

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                ans_nb = random.choice(list_nb_da_1)
                ans_th = random.choice(list_th_da_1)
                ans_vd = random.choice(list_vd_da_1)
                ans_vdc = random.choice(list_vdc_da_1)
                if 1 <= count_true_answers([ans_nb, ans_th, ans_vd, ans_vdc]) <= 3:
                    break

            # Xuất nội dung
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
                '{' + str(ans_nb) + '}\n'
                '{' + str(ans_th) + '}\n'
                '{' + str(ans_vd) + '}\n'
                '{' + str(ans_vdc) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(loigiai_nb_1) + '\n'
                '\\item ' + str(loigiai_th_1) + '\n'
                '\\item ' + str(loigiai_vd_1) + '\n'
                '\\item ' + str(loigiai_vdc_1) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

