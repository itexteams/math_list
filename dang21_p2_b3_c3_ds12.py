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


def bt_dang21_p2_b3_c3_ds12(self):
            # Khai báo biến
            # Giao điểm tại x=0 và x=m. Khi đó p = k^2 * m^3
            k = random.randint(1, 3) 
            m = random.randint(1, 2)
            p = k**2 * m**3
            my = k * m**2 # Tung độ điểm M

            # Các biểu thức toán học
            f1 = k * x**2
            f2 = sqrt(p) * sqrt(x)

            # Tính toán kết quả
            S_val = Rational(k * m**3, 3)
            V_val_no_pi = Rational(3 * k**2 * m**5, 10)
            ratio = (V_val_no_pi / S_val) # V / (pi*S)
            a_frac = ratio.p
            b_frac = ratio.q
            bieu_thuc = 2 * a_frac - b_frac

            # Nội dung câu hỏi
            noidungcauhoi = (r'''Cho hình phẳng $(H)$ giới hạn bởi các đường $y = %s x^2 \, (C_1)$ và $y^2 = %s x \, (C_2)$.''' 
                             % (latex(k) if k != 1 else "", latex(p)))

            ########################################################################
            # Nhận biết 
            ########################################################################
            nb_da_1_d = r'\True Các đường $(C_1)$ và $(C_2)$ đều đi qua hai điểm $O(0;0)$ và $M(%s;%s)$' % (m, my)
            nb_da_1_s = r'Các đường $(C_1)$ và $(C_2)$ đều đi qua hai điểm $O(0;0)$ và $M(%s;%s)$' % (my, m)
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

            loigiai_nb_1 = r'''Phương trình hoành độ giao điểm: $y^2 = %s x \Rightarrow (%s x^2)^2 = %s x \Leftrightarrow %s x^4 - %s x = 0$. \\
            Giao điểm là $O(0;0)$ và $M(%s;%s)$.''' % (p, k, p, k**2, p, m, my)

            ########################################################################
            # Thông hiểu
            ########################################################################
            th_da_1_d = r'\True Diện tích của hình phẳng $(H)$ là $S = \int\limits_{0}^{%s} \left| %s x^2 - %s \sqrt{x} \right| \text{d}x$' % (m, k, latex(sqrt(p)))
            th_da_1_s = r'Diện tích của hình phẳng $(H)$ là $S = \int\limits_{0}^{%s} \left( %s x^2 + %s \sqrt{x} \right| \text{d}x$' % (m, k, latex(sqrt(p)))
            list_th_da_1 = [th_da_1_d, th_da_1_s]

            loigiai_th_1 = r'''Diện tích hình phẳng giới hạn bởi hai đồ thị là $S = \int\limits_{0}^{%s} |f_1(x) - f_2(x)| \text{d}x$.''' % m

            ########################################################################
            # Vận dụng
            ########################################################################
            vd_da_1_d = r'\True Thể tích vật thể tròn xoay khi quay $(H)$ quanh trục hoành là $V = \pi \int\limits_{0}^{%s} \left[ (%s x) - (%s x^2)^2 \right] \text{d}x$' % (m, p, k)
            vd_da_1_s = r'Thể tích vật thể tròn xoay khi quay $(H)$ quanh trục hoành là $V = \int\limits_{0}^{%s} \left[ %s x - (%s x^2)^2 \right] \text{d}x$' % (m, p, k)
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

            loigiai_vd_1 = r'''Công thức thể tích: $V = \pi \int\limits_{a}^{b} |f_1^2(x) - f_2^2(x)| \text{d}x$. Do đó $V = \pi \int\limits_{0}^{%s} \left( %s x - %s x^4 \right) \text{d}x$.''' % (m, p, k**2)

            ########################################################################
            # Vận dụng cao
            ########################################################################
            vdc_da_1_d = r'\True Giả sử $\frac{V}{S} = \frac{a\pi}{b}$ với $a, b \in \mathbb{N}$ và $\frac{a}{b}$ tối giản. Khi đó $2a - b = %s$' % bieu_thuc
            vdc_da_1_s = r'Giả sử $\frac{V}{S} = \frac{a\pi}{b}$ với $a, b \in \mathbb{N}$ và $\frac{a}{b}$ tối giản. Khi đó $2a - b = %s$' % (bieu_thuc + 2)
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

            loigiai_vdc_1 = r'''Ta có $S = %s$ và $V = %s \pi$. \\
            Suy ra $\frac{V}{S} = \frac{%s\pi}{%s} \Rightarrow a=%s, b=%s$. \\
            Vậy $2a - b = 2(%s) - %s = %s$.''' % (latex(S_val), latex(V_val_no_pi), a_frac, b_frac, a_frac, b_frac, a_frac, b_frac, bieu_thuc)

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                nb_sel = random.choice(list_nb_da_1)
                th_sel = random.choice(list_th_da_1)
                vd_sel = random.choice(list_vd_da_1)
                vdc_sel = random.choice(list_vdc_da_1)

                answers = [nb_sel, th_sel, vd_sel, vdc_sel]
                if 1 <= count_true_answers(answers) <= 3:
                    break

            solutions = [loigiai_nb_1, loigiai_th_1, loigiai_vd_1, loigiai_vdc_1]

            # Xuất kết quả
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
                '{' + nb_sel + '}\n'
                '{' + th_sel + '}\n'
                '{' + vd_sel + '}\n'
                '{' + vdc_sel + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + solutions[0] + '\n'
                '\\item ' + solutions[1] + '\n'
                '\\item ' + solutions[2] + '\n'
                '\\item ' + solutions[3] + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

