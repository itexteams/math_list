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


def bt_dang10_p1_b2_c6_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                n_max = random.choice([7, 9, 11, 13])

                tap_hop = list(range(1, n_max + 1))
                tap_chan = [i for i in tap_hop if i % 2 == 0]
                tap_le = [i for i in tap_hop if i % 2 != 0]

                n_chan = len(tap_chan)
                n_le = len(tap_le)

                # Sử dụng binomial thay cho comb
                n_omega = binomial(n_max, 2)
                n_a = binomial(n_chan, 2)

                p_a = Rational(n_a, n_omega)
                n_b = n_chan * n_le
                p_b = Rational(n_b, n_omega)

                n_c = n_a + n_b
                kq_phanso = Rational(n_c, n_omega)

                # --- Các bước còn lại giữ nguyên ---
                s_variants = [
                    Rational(n_le * (n_le - 1), 2 * n_omega),
                    Rational(n_a, n_omega),
                    Rational(n_b, n_omega),
                    Rational(1, 2),
                    Rational(2, 3)
                ]

                s_filtered = [v for v in s_variants if v != kq_phanso]
                random.shuffle(s_filtered)

                da = '$%s$' % (latex(kq_phanso))
                das1 = '$%s$' % (latex(s_filtered[0]))
                das2 = '$%s$' % (latex(s_filtered[1]))
                das3 = '$%s$' % (latex(s_filtered[2]))

                noidungcauhoi = ('''Một hộp đựng $%s$ tấm thẻ cùng loại được ghi số từ $1$ đến $%s$. Rút ngẫu nhiên đồng thời hai tấm thẻ từ trong hộp. Xác suất để "Tích hai số ghi trên hai tấm thẻ là một số chẵn" là'''
                                 % (latex(n_max), latex(n_max)))

                da_d = ('\\True ' + str(da))
                list_1 = [da_d, str(das1), str(das2), str(das3)]
                random.shuffle(list_1)

                str_tapchan = ';'.join(map(str, tap_chan))
                str_taple = ';'.join(map(str, tap_le))

                loigiai = ('''Không gian mẫu $\\Omega$ là tập hợp tất cả các tập con có hai phần tử của tập $\\left\\{ 1;2;...;%s \\right\\}$. \\\\
                             Do đó $n\\left( \\Omega \\right) = C_{%s}^2 = %s$. \\\\
                             - Xét biến cố $A$: "Hai số ghi trên $2$ thẻ rút được đều chẵn" thì số phần tử của $A$ là số tập con có hai phần tử của tập hợp $\\left\\{ %s \\right\\}$. Do đó $n\\left( A \\right) = C_{%s}^2 = %s$. Suy ra \\\\
                             $P\\left( A \\right) = \\frac{n\\left( A \\right)}{n\\left( \\Omega \\right)} = \\frac{%s}{%s}$. \\\\
                             - Xét biến cố $B$: "Hai số ghi trên $2$ thẻ rút được có $1$ thẻ ghi số lẻ và $1$ thẻ ghi số chẵn". Mỗi phần tử của $B$ được hình thành từ hai công đoạn: \\\\
                             Công đoạn 1: Chọn một số chẵn từ tập $\\left\\{ %s \\right\\}$. Có $%s$ cách chọn. \\\\
                             Công đoạn 2: Chọn một số lẻ từ tập $\\left\\{ %s \\right\\}$. Có $%s$ cách chọn. \\\\
                             Theo quy tắc nhân, tập $B$ có $%s \\cdot %s = %s$ (phần tử). \\\\
                             Do đó $n\\left( B \\right) = %s$. Suy ra $P\\left( B \\right) = \\frac{n\\left( B \\right)}{n\\left( \\Omega \\right)} = \\frac{%s}{%s}$. \\\\
                             Gọi $C$ là biến cố "Tích hai số ghi trên hai tấm thẻ là một số chẵn". Suy ra $C = A \\cup B$. \\\\
                             Do $A, B$ xung khắc nên $P\\left( C \\right) = P\\left( A \\right) + P\\left( B \\right) = \\frac{%s}{%s} + \\frac{%s}{%s} = \\frac{%s}{%s} = %s$.'''
                           % (latex(n_max), latex(n_max), latex(n_omega), 
                              str_tapchan, latex(n_chan), latex(n_a), 
                              latex(n_a), latex(n_omega),
                              str_tapchan, latex(n_chan),
                              str_taple, latex(n_le),
                              latex(n_chan), latex(n_le), latex(n_b),
                              latex(n_b), latex(n_b), latex(n_omega),
                              latex(n_a), latex(n_omega), latex(n_b), latex(n_omega), latex(n_a + n_b), latex(n_omega), latex(kq_phanso)
                              ))

            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\choice \n'
                       '{' + str(list_1[0]) + '}\n'
                       '{' + str(list_1[1]) + '}\n'
                       '{' + str(list_1[2]) + '}\n'
                       '{' + str(list_1[3]) + '}\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

