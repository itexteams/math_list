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


def bt_dang19_p2_b3_c4_ds10(self):
            # Khai báo biến
            # Khởi tạo các biến ký hiệu
            x = symbols('x')

            # B3: Logic Random - Chọn 2 nghiệm nguyên dương để giống đề bài gốc
            x1 = random.randint(1, 5)
            x2 = x1 + random.randint(3, 7) # Đảm bảo x2 > x1

            a_val = x1 + x2
            b_val = x1 * x2

            # Biểu thức f(x)
            f_x = x**2 - a_val*x + b_val

            # Nội dung câu hỏi
            noidungcauhoi = ('''Tam thức bậc hai $f(x)=x^2-ax+b$ có bảng xét dấu như hình vẽ.
            \\begin{center}
            \\begin{tikzpicture}
               \\tkzTabInit[lgt=1.2,espcl=2.5,deltacl=0.5]{$x$/1,$f(x)$/1}{$-\\infty$,$%s$,$%s$,$+\\infty$}
               \\tkzTabLine{,+,0,-,0,+,}
            \\end{tikzpicture}
            \\end{center}''' % (latex(x1), latex(x2)))

            ########################################################################
            # a) Nhận biết: Tập nghiệm f(x) < 0
            ########################################################################
            nb_da_1_d = '\\True $f(x) < 0 \\Leftrightarrow %s < x < %s$' % (latex(x1), latex(x2))
            nb_da_1_s = '$f(x) < 0 \\Leftrightarrow x < %s$ hoặc $x > %s$' % (latex(x1), latex(x2))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            loigiai_nb_1 = ('''Dựa vào bảng xét dấu, ta thấy $f(x) < 0$ khi $x$ nằm trong khoảng giữa hai nghiệm, tức là $x \\in (%s; %s)$.''' % (latex(x1), latex(x2)))

            ########################################################################
            # b) Thông hiểu: Tính a + b
            ########################################################################
            sum_ab = a_val + b_val
            th_da_1_d = '\\True $a + b = %s$' % (latex(sum_ab))
            th_da_1_s = '$a + b = %s$' % (latex(sum_ab + random.randint(1, 5)))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            loigiai_th_1 = ('''Theo định lý Vi-ét cho phương trình $x^2 - ax + b = 0$, ta có: \\\\
            $x_1 + x_2 = a \\Rightarrow a = %s + %s = %s$. \\\\
            $x_1 \\cdot x_2 = b \\Rightarrow b = %s \\cdot %s = %s$. \\\\
            Vậy $a + b = %s + %s = %s$.''' % (latex(x1), latex(x2), latex(a_val), latex(x1), latex(x2), latex(b_val), latex(a_val), latex(b_val), latex(sum_ab)))

            ########################################################################
            # c) Vận dụng: Bất phương trình f(x) < b
            ########################################################################
            # f(x) < b <=> x^2 - ax + b < b <=> x^2 - ax < 0 <=> x(x-a) < 0
            vd_da_1_d = '\\True Bất phương trình $f(x) < %s$ có tập nghiệm $(0; %s)$' % (latex(b_val), latex(a_val))
            vd_da_1_s = 'Bất phương trình $f(x) < %s$ có tập nghiệm $(%s; %s)$' % (latex(b_val), latex(x1), latex(x2))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            loigiai_vd_1 = ('''Bất phương trình $f(x) < %s \\Leftrightarrow x^2 - %s x + %s < %s \\\\
            \\Leftrightarrow x^2 - %s x < 0 \\Leftrightarrow x(x - %s) < 0$. \\\\
            Vì $a = %s > 0$ nên nghiệm của bất phương trình là $0 < x < %s$. Tập nghiệm là $(0; %s)$.''' 
            % (latex(b_val), latex(a_val), latex(b_val), latex(b_val), latex(a_val), latex(a_val), latex(a_val), latex(a_val), latex(a_val)))

            ########################################################################
            # d) Vận dụng cao: Hàm f(x+1)
            ########################################################################
            # f(x+1) = (x+1)^2 - a(x+1) + b = x^2 + (2-a)x + (1-a+b)
            m_val = a_val - 2
            n_val = 1 - a_val + b_val
            sum_mn = m_val + n_val

            vdc_da_1_d = '\\True $f(x+1) = x^2 - mx + n$ với $m + n = %s$' % (latex(sum_mn))
            vdc_da_1_s = '$f(x+1) = x^2 - mx + n$ với $m + n = %s$' % (latex(sum_mn + 2))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            loigiai_vdc_1 = ('''Ta có $f(x+1) = (x+1)^2 - %s(x+1) + %s$ \\\\
            $= x^2 + 2x + 1 - %sx - %s + %s = x^2 - %sx + %s$. \\\\
            Suy ra $m = %s$ và $n = %s$. Vậy $m + n = %s + %s = %s$.''' 
            % (latex(a_val), latex(b_val), latex(a_val), latex(a_val), latex(b_val), latex(m_val), latex(n_val), latex(m_val), latex(n_val), latex(m_val), latex(n_val), latex(sum_mn)))

            # --- Phần Logic trộn và xuất bản (Giống mẫu của bạn) ---

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
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

