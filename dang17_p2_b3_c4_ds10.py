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


def bt_dang17_p2_b3_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')
            m = symbols('m')

            # Ngẫu nhiên hóa m cho một số trường hợp cụ thể nếu cần, 
            # nhưng bài toán gốc là xét biểu thức tổng quát theo m.
            # Ở đây ta sẽ giữ nguyên tham số m để giải các khẳng định.

            # Biểu thức gốc: f(x) = m*x^2 + 2*(m-1)*x + m - 1
            f_x = m*x**2 + 2*(m-1)*x + m - 1

            # Nội dung câu hỏi
            noidungcauhoi = "Cho biểu thức $f(x) = " + latex(f_x) + "$."

            ########################################################################
            # Câu a) Xét m = 0
            ########################################################################
            # f(x) khi m = 0: 2(0-1)x + 0 - 1 = -2x - 1
            f_m0 = f_x.subs(m, 0)
            val_2024 = f_m0.subs(x, 2024)
            val_2023 = f_m0.subs(x, 2023)

            is_a_true = val_2024 > val_2023
            prefix_a = "\\True " if is_a_true else ""
            nb_da_1 = prefix_a + "Nếu $m = 0$ thì $f(2024) > f(2023)$"

            loigiai_nb_1 = "Với $m=0$, ta có $f(x) = " + latex(f_m0) + "$. Đây là hàm số bậc nhất có hệ số $a = -2 < 0$, nên hàm số nghịch biến trên $\\mathbb{R}$. " \
                           "Vì $2024 > 2023$ nên $f(2024) < f(2023)$. Do đó khẳng định này là Sai."
            if is_a_true: # Trường hợp nếu m dương (logic dự phòng)
                loigiai_nb_1 = "Với $m=0$, ta có $f(x) = -2x-1$. Vì $-2 < 0$ nên hàm số nghịch biến, suy ra $f(2024) < f(2023)$."

            ########################################################################
            # Câu b) Nếu m > 1 thì f(x) > 0 với mọi x thuộc R
            ########################################################################
            # Xét Delta' = (m-1)^2 - m(m-1) = (m-1)(m-1-m) = -(m-1)
            delta_prime = (m-1)**2 - m*(m-1)
            # Với m > 1 thì a = m > 0 và Delta' = -(m-1) < 0
            is_b_true = True # Theo lý thuyết tam thức bậc hai
            prefix_b = "\\True " if is_b_true else ""
            th_da_1 = prefix_b + "Nếu $m > 1$ thì $f(x) > 0, \\forall x \\in \\mathbb{R}$"

            loigiai_th_1 = "Xét $m > 1$, ta có hệ số $a = m > 0$. Biệt thức $\\Delta' = (m-1)^2 - m(m-1) = -(m-1)$. " \
                           "Vì $m > 1$ nên $\\Delta' < 0$. Tam thức bậc hai có $a > 0$ và $\\Delta' < 0$ thì $f(x) > 0, \\forall x \\in \\mathbb{R}$. " \
                           "Vậy khẳng định này là Đúng."

            ########################################################################
            # Câu c) f(x+1)
            ########################################################################
            f_x_plus_1 = sp.expand(f_x.subs(x, x + 1))
            # f(x+1) = m(x+1)^2 + 2(m-1)(x+1) + m-1 = mx^2 + (4m-2)x + 4m-3
            is_c_true = True 
            prefix_c = "\\True " if is_c_true else ""
            vd_da_1 = prefix_c + "$f(x+1) = " + latex(f_x_plus_1) + "$"

            loigiai_vd_1 = "Ta có $f(x+1) = m(x+1)^2 + 2(m-1)(x+1) + m-1$. \\\\ " \
                           "Khai triển: $f(x+1) = m(x^2+2x+1) + (2m-2)x + 2m-2 + m-1$ \\\\ " \
                           "$= mx^2 + 2mx + m + 2mx - 2x + 3m - 3 = " + latex(f_x_plus_1) + "$. " \
                           "Vậy khẳng định này là Đúng."

            ########################################################################
            # Câu d) Khi 0 < m < 1 thì f(x) <= m-1
            ########################################################################
            # f(x) <= m-1 <=> mx^2 + 2(m-1)x + m-1 <= m-1 <=> mx^2 + 2(m-1)x <= 0
            # <=> x[mx + 2(m-1)] <= 0. Nghiệm là 0 và -2(m-1)/m = (2-2m)/m
            # Vì 0 < m < 1 nên (2-2m)/m > 0. Vậy tập nghiệm là [0, (2-2m)/m]
            is_d_true = True
            prefix_d = "\\True " if is_d_true else ""
            vdc_da_1 = prefix_d + "Khi $0 < m < 1$ thì bất phương trình $f(x) \\le m-1$ có tập nghiệm $S = \\left[ 0; \\frac{2-2m}{m} \\right]$"

            loigiai_vdc_1 = "Bất phương trình $f(x) \\le m-1 \\Leftrightarrow mx^2 + 2(m-1)x + m-1 \\le m-1 \\Leftrightarrow mx^2 + 2(m-1)x \\le 0$. \\\\ " \
                            "Xét phương trình $mx^2 + 2(m-1)x = 0 \\Leftrightarrow x[mx + 2(m-1)] = 0 \\Leftrightarrow x = 0$ hoặc $x = \\frac{2-2m}{m}$. \\\\ " \
                            "Vì $0 < m < 1$ nên $m > 0$ và $2-2m > 0$, suy ra $\\frac{2-2m}{m} > 0$. \\\\ " \
                            "Do $a = m > 0$, tập nghiệm của bất phương trình là đoạn giữa hai nghiệm: $S = \\left[ 0; \\frac{2-2m}{m} \\right]$."

            # Tổng hợp và xuất bản (giữ nguyên cấu trúc mẫu)
            shuffled_answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
            shuffled_solutions = [loigiai_nb_1, loigiai_th_1, loigiai_vd_1, loigiai_vdc_1]

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
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

